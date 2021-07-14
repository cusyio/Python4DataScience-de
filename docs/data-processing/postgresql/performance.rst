PostgreSQL-Performance
======================

Ihr solltet nicht mit :term:`MVCC – Multiversion Concurrency Control` beginnen,
wenn Ihr Eure PostgreSQL-Datenbank optimieren wollt: viele Verbesserungen können
sehr viel einfacher vorgenommen werden da weder Transaktionslogs noch große
Linux Kernel Page Sizes verantwortlich sein dürften. Üblicherweise beginnen wir
mit zwei Metriken, die sehr gut die Performance Eurer Datenbanken anzeigen
können:

Cache- und Index-Trefferquote
-----------------------------

Cache-Trefferquote (engl.: *cache hit ratio*)
    Prozentsatz der Zeit, in der die Daten aus dem Arbeitsspeicher statt aus dem
    Festplattenspeicher bereitgestellt werden können. Für eine Web-Anweundung
    mit vielen kleinen Anfragen empfehle ich ca. 99%.

    .. code-block:: postgresql

        SELECT
          'index hit rate' AS name,
          (sum(idx_blks_hit)) / nullif(sum(idx_blks_hit + idx_blks_read),0) AS ratio
        FROM pg_statio_user_indexes
        UNION ALL
        SELECT
         'table hit rate' AS name,
          sum(heap_blks_hit) / nullif(sum(heap_blks_hit) + sum(heap_blks_read),0) AS ratio
        FROM pg_statio_user_tables;

    Falls die Cache-Trefferquote zu gering sein sollte, könnt Ihr einfach den
    Arbeitsspeicher erhöhen.

Index-Trefferquote (engl.: *index hit ratio*)
    Häufigkeit der Verwendung der Indizes.

    .. code-block:: postgresql

         SELECT relname,
           CASE idx_scan
             WHEN 0 THEN 'Insufficient data'
             ELSE (100 * idx_scan / (seq_scan + idx_scan))::text
           END percent_of_times_index_used,
           n_live_tup rows_in_table
         FROM
           pg_stat_user_tables
         ORDER BY
           n_live_tup DESC;
                relname        | percent_of_times_index_used | rows_in_table
        -----------------------+-----------------------------+---------------
         account               | 11                          |          5409
         activity              | 69                          |         58276
         application           | 93                          |          5345
         …

    Üblicherweise sollten bei uns nicht mehr als 10.000 Datensätze in einer
    Tabelle und der Prozentsatz des verwendeten Index größer als 90% sein.

    In unserem Beispiel sehen wir, dass der ``account``-Tabelle relevante
    Indizes fehlen, da nur in 11% der Anfragen ein Index genutzt wird. Auch der
    ``activity``-Tabelle fehlen einige passende Indizes, sie hat jedoch auch
    sehr viele Datensätze, sodass es sinnvoll sein dürfte, sie in mehrere
    Tabellen aufzuteilen.

Nicht-verwendete Indizes bereinigen
-----------------------------------

Nicht-verwendete Indizes führen beim Schreiben der Datensätze zu einem
langsameren Durchsatz ohne dass dadurch Abfragen schneller würden.

.. code-block:: postgresql

    SELECT
      schemaname || '.' || relname AS table,
      indexrelname AS index,
      pg_size_pretty(pg_relation_size(i.indexrelid)) AS index_size,
      idx_scan as index_scans
    FROM pg_stat_user_indexes ui
    JOIN pg_index i ON ui.indexrelid = i.indexrelid
    WHERE NOT indisunique AND idx_scan < 50 AND pg_relation_size(relid) > 5 * 8192
    ORDER BY pg_relation_size(i.indexrelid) / nullif(idx_scan, 0) DESC NULLS FIRST,
    pg_relation_size(i.indexrelid) DESC;

Indizes ohne Verwendung können einfach entfernt werden. Schwieriger wird die
Entscheidung hingegen bei Indizes, die nur sehr selten verwendet werden: hier
muss eine Abwägung zwischen der Schreib- und Abfragegeschwindigkeit getroffen
werden.

Nicht-verwendete Daten bereinigen
---------------------------------

Auch wenn PostgreSQL sehr vielfältige Daten aufnehmen kann, ist das jedoch nicht
immer sinnvoll. Tabellen wie ``messages``, ``logs`` und ``events`` haben eine
gute Chance, den Großteil des Speichers zu beanspruchen ohne dass die
Datenbankanwendung unmittelbar davon profitiert: wenn diese Daten vielmehr der
Fehleranalyse dienen, sollten sie außerhalb der Datenbank gespeichert und
regelmäßig rotiert werden.

Abfrageleistung mit ``pg_stat_statements`` analysieren
------------------------------------------------------

`pg_stat_statements
<https://www.postgresql.org/docs/current/pgstatstatements.html>`_ zeichnet
Abfragen auf und führt eine Reihe von Statistiken dazu. So lassen wir uns in
regelmäßigen Abständen anzeigen, welche Abfragen im Durchschnitt am langsamsten
sind und welche das System am stärksten belasten:

.. code-block:: postgresql

    SELECT
      (total_time / 1000 / 60) as total_minutes,
      (total_time/calls) as average_time,
      query
    FROM pg_stat_statements
    ORDER BY 1 DESC
    LIMIT 50;
    total_time        |     avg_time      |                           query
    ------------------+-------------------+------------------------------------------------------------
     295.761165833319 | 10.1374053278061  | SELECT id FROM account WHERE email LIKE ?
     219.138564283326 | 80.24530822355305 | SELECT * FROM account WHERE user_id = ? AND current = True
    …

Üblich sollten Antwortzeiten von ~1ms und in wenigen Fällen ~4–5ms sein. Um mit
der Performance-Optimierung zu beginnen, wägen wir meist zwischen der Gesamtzeit
und der Durchschnittszeit ab, sodass wir in obigem Beispiel vermutlich mit der
zweiten Zeile beginnen würden da wir hier die größeren Einsparmöglichkeiten
sehen. Um eine genauere Vorstellung von der Abfrage zu erhalten, analysieren wir
sie genauer mit:

.. code-block:: postgresql

    EXPLAIN ANALYZE
    SELECT *
    FROM account
    WHERE user_id = 123
      AND current = True
                                                                       QUERY PLAN
    --------------------------------------------------------------------------------------------------------------------------------------------------------
     Aggregate  (cost=4690.88..4690.88 rows=1 width=0) (actual time=519.288..519.289 rows=1 loops=1)
       ->  Nested Loop  (cost=0.00..4690.66 rows=433 width=0) (actual time=15.302..519.076 rows=213 loops=1)
             ->  Index Scan using idx_account_userid on account  (cost=0.00..232.52 rows=23 width=4) (actual time=10.143..62.822 rows=1 loops=8)
                   Index Cond: (user_id = 123)
                   Filter: current
                   Rows Removed by Filter: 14
     Total runtime: 219.428 ms
    (1 rows)

Wir sehen also, dass zwar ein Index verwendet wird, jedoch werden 15
verschiedene Zeilen daraus abgerufen von denen dann 14 wieder verworfen werden.
Um dies zu optimieren, würden wir einen bedingten oder zusammengesetzten Index
erstellen. Im ersten Fall müsste ``current = true`` erfüllt sein, im zweiten
Fall würde ein Composite-Index mit beiden Werten erstellt werden. Ein bedingter
Index ist in der Regel sinnvoller bei einem kleinen Satz von Werten, während der
Composite-Index bei größeren Sätzen von Werten vorteilhafter ist. In unserem
Beispiel dürfte klar ein bedingter Index sinnvoller sein. Diesen können wir
erstellen mit:

.. code-block:: postgresql

    CREATE INDEX CONCURRENTLY idx_account_userid_current ON account(user_id) WHERE current = True;

Nun müsste sich auch der Query-Plan verbessern:

.. code-block:: postgresql

    EXPLAIN ANALYZE
    SELECT *
    FROM account
    WHERE user_id = 123
      AND current = True

                                                                       QUERY PLAN
    ------------------------------------------------------------------------------------------------------------------------------------------------
     Aggregate  (cost=4690.88..4690.88 rows=1 width=0) (actual time=519.288..519.289 rows=1 loops=1)
         ->  Index Scan using idx_account_userid_current on account  (cost=0.00..232.52 rows=23 width=4) (actual time=10.143..62.822 rows=1 loops=8)
               Index Cond: ((user_id = 123) AND (current = True))
     Total runtime: .728 ms
    (1 rows)
