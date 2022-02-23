pganalyze
=========

`pganalyze <https://pganalyze.com/>`_ analysiert die Abfagepläne (Query Plans)
von PostgreSQL. Aktuell sammelt er Informationen über

* Schema mit Tabellen (Spalten, Constraints, Trigger-Definitionen) und Indizees
* Statistiken zu Tabellen Indizees, Datenbanken und Anfragen (Queries)
* Betriebssystem (OS, RAM, Storage)

   .. seealso::
   * `GitHub <https://github.com/pganalyze/collector>`_
   * `Dokumentation <https://pganalyze.com/docs>`_

Installation
------------

#. Erstellen eines Monitoring-User für pganalyze:

   .. code-block:: postgresql

    CREATE USER pganalyze WITH PASSWORD '…' CONNECTION LIMIT 5;
    GRANT pg_monitor TO pganalyze;
    CREATE SCHEMA pganalyze;
    GRANT USAGE ON SCHEMA pganalyze TO pganalyze;
    REVOKE ALL ON SCHEMA public FROM pganalyze;
    CREATE OR REPLACE FUNCTION pganalyze.get_stat_replication() RETURNS SETOF pg_stat_replication AS
    $$ /* pganalyze-collector */ SELECT * FROM pg_catalog.pg_stat_replication;
    $$ LANGUAGE sql VOLATILE SECURITY DEFINER;

#. Überprüfen der Verbindung:

   .. code-block:: postgresql

    PGPASSWORD=…  psql -h localhost -d mydb -U pganalyze

#. Aktivieren der ``pg_stat_statements``:

   .. code-block:: postgresql

    ALTER SYSTEM SET shared_preload_libraries = 'pg_stat_statements';

#. Neustart des PostgreSQL-Daemon:

   .. code-block:: console

    $ sudo service postgresql restart

#. Überprüfen von ``pg_stat_statements``:

   .. code-block:: postgresql

    CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
    SELECT calls, query FROM pg_stat_statements LIMIT 1;
     calls | query
    -------+-------
         8 | SELECT * FROM t WHERE field = ?
    (1 row)

#. Installieren des *Collector*:

   .. code-block:: console

    $ curl -L https://packages.pganalyze.com/pganalyze_signing_key.asc | sudo apt-key add -
    $ echo "deb [arch=amd64] https://packages.pganalyze.com/ubuntu/bionic/ stable main" | sudo tee /etc/apt/sources.list.d/pganalyze_collector.list
    $ sudo apt-get update
    $ sudo apt-get install pganalyze-collector

#. Erstellen des API-Schlüssel

   Für den nächsten Schritt benötigt ihr den pganalyze ``api_key``. Diesen könnt
   ihr erstellen auf unter der Site https://app.pganalyze.com/

#. Konfigurieren des  *Collector*:

   .. code-block:: ini

    [pganalyze]
    api_key: …

    [server]
    db_host: 127.0.0.1
    db_port: 5432
    db_name: postgres, *
    db_username: pganalyze
    db_password: …

#. Testen der *Collector*-Konfiguration:

   .. code-block:: console

    $ sudo pganalyze-collector --test --reload

.. seealso::
   * `Installation Guide <https://pganalyze.com/docs/install/self_managed/01_create_monitoring_user>`_

Log-Analyse
-----------

Um die lokalen Log-Dateien kontinuierlich zu überwachen, zu klassifizieren und
statistisch auszuwerten, muss ``db_log_location`` in
``pganalyze-collector.conf`` angegeben werden. ``pganalyze-collector`` bietet
eine Hilfe zum Auffinden der Log-Dateien:

.. code-block:: console

    $ pganalyze-collector --discover-log-location

Die Ausgabe kann dann z.B. so aussehen:

.. code-block:: console

    db_log_location = /var/log/postgresql/postgresql-12-main.log

Nachdem dieses Ergebnis in der ``pganalyze-collector.conf``-Konfigurationsdatei
eingetragen wurde, könnt ihr diese testen mit:

.. code-block:: console

    $ pganalyze-collector --test

Das Ergebnis kann dann z.B. so aussehen:

.. code-block:: console

    2021/02/06 06:40:06 I [server1] Testing statistics collection...
    2021/02/06 06:40:07 I [server1] Test submission successful (15.8 KB received)
    2021/02/06 06:40:07 I [server1] Testing local log tailing...
    2021/02/06 06:40:13 I [server1] Log test successful
    2021/02/06 06:40:13 I Re-running log test with reduced privileges of "pganalyze" user (uid = 107, gid = 113)
    2021/02/06 06:40:13 I [server1] Testing local log tailing...
    2021/02/06 06:40:19 I [server1] Log test successful

Wenn der Test erfolgreich verlief, muss der *Collector* neu gestartet werden
damit die Konfiugration wirksam wird:

.. code-block:: console

    $ systemctl restart pganalyze-collector

