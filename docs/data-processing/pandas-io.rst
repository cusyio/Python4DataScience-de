pandas IO tools
===============

pandas verfügt über eine Reihe von Funktionen zum Lesen von Tabellendaten als
DataFrame-Objekt, darunter

+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Funktion                                           | Beschreibung                                                                                     |
+====================================================+==================================================================================================+
| :doc:`pandas:reference/api/pandas.read_csv`        | lädt :doc:`serialisation-formats/csv/index`-Daten aus                                            |
|                                                    | einer Datei, einer URL oder einem dateiähnlichen Objekt;                                         |
|                                                    | üblicherweise wird ein Komma als Trennzeichen verwendet                                          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_fwf`        | liest :abbr:`fwf (fixed-width files)`, also Daten im                                             |
|                                                    | Spaltenformat mit fester Breite                                                                  |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_clipboard`  | liest Daten aus der Zwischenablage und übergibt sie an                                           |
|                                                    | ``read_csv``; :abbr:`u.a. (unter anderem)` nützlich für                                          |
|                                                    | die Konvertierung von Tabellen aus Webseiten                                                     |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_excel`      | liest Tabellendaten aus einer                                                                    |
|                                                    | :doc:`serialisation-formats/excel` XLS- oder XLSX-Datei                                          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_hdf`        | liest :abbr:`HDF5 (Hierarchical Data Format)`-Dateien                                            |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_html`       | liest alle Tabellen aus dem angegebenen                                                          |
|                                                    | :ref:`/data-processing/serialisation-formats/xml-html/xml-html-examples.ipynb#html`-Dokument     |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_json`       | liest Daten aus einer                                                                            |
|                                                    | :doc:`serialisation-formats/json/index`-Datei                                                    |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_feather`    | liest das                                                                                        |
|                                                    | `Feather <https://arrow.apache.org/docs/python/feather.html>`_-Binärdateiformat                  |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_orc`        | liest Apache :abbr:`ORC (Optimized Row Columnar)`-Binärdaten                                     |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_parquet`    | liest das `Apache                                                                                |
|                                                    | Parquet <https://parquet.apache.org>`_-Binärdateiformat                                          |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_pickle`     | liest ein beliebiges Objekt, das im                                                              |
|                                                    | Python-:doc:`serialisation-formats/pickle/index`-Format                                          |
|                                                    | gespeichert ist                                                                                  |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_sas`        | liest einen                                                                                      |
|                                                    | :abbr:`SAS (Statistical Analysis System)`-Datensatz                                              |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_spss`       | liest eine von `SPSS                                                                             |
|                                                    | <https://de.wikipedia.org/wiki/SPSS>`_ erstellte                                                 |
|                                                    | Datendatei                                                                                       |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_sql`        | liest die Ergebnisse einer SQL-Abfrage (mit                                                      |
|                                                    | :doc:`postgresql/sqlalchemy`) als pandas DataFrame                                               |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_sql_table`  | liest eine ganze SQL-Tabelle (mit                                                                |
|                                                    | :doc:`postgresql/sqlalchemy`) als pandas DataFrame                                               |
|                                                    | (entspricht einer Abfrage, die alles in dieser Tabelle                                           |
|                                                    | mit ``read_sql`` auswählt)                                                                       |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+
| :doc:`pandas:reference/api/pandas.read_stata`      | liest einen Datensatz aus dem                                                                    |
|                                                    | `Stata <https://www.stata.com>`_-Dateiformat                                                     |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. seealso::
    `pandas I/O API <https://pandas.pydata.org/docs/user_guide/io.html>`_
        Die pandas I/O API ist eine Sammlung von ``reader``-Funktionen, die ein
        pandas-Objekt zurückgeben. Meist stehen auch entsprechende
        ``write``-Methoden zur Verfügung.

Zunächst werde ich einen Überblick über einige dieser Funktionen geben, die dazu
gedacht sind, Text- und Exceldaten in einen pandas-DataFrame zu konvertieren:
:doc:`CSV <serialisation-formats/csv/example>`,
:doc:`JSON <serialisation-formats/json/example>` und
:doc:`serialisation-formats/excel`. Dabei lassen sich die optionalen Argumente für
diese Funktionen in folgende Kategorien einteilen:

Indizierung
    Können eine oder mehrere Spalten den zurückgegebenen DataFrame erschließen,
    und ob die Spaltennamen aus der Datei, den von euch angegebenen Argumenten
    oder gar nicht abgerufen werden sollen.
Typinferenz und Datenkonvertierung
    Dazu gehören die benutzerdefinierten Wertkonvertierungen und die
    benutzerdefinierte Liste der Markierungen für fehlende Werte.
Parsen von Datum und Uhrzeit
    Dies umfasst die Kombinationsfähigkeit, einschließlich der Kombination von
    Datums- und Zeitinformationen, die über mehrere Spalten verteilt sind, in
    einer einzigen Spalte im Ergebnis.
Iteration
    Unterstützung für die Iteration über Teile von sehr großen Dateien.
Probleme mit unsauberen Daten
    Überspringen von Zeilen oder Fußzeilen, Kommentaren oder anderen
    Kleinigkeiten wie numerischen Daten mit durch Kommas getrennte Tausender.

Da Daten in der realen Welt sehr unübersichtlich sein können, haben einige der
Datenladefunktionen (insbesondere ``read_csv``) im Laufe der Zeit eine lange
Liste optionaler Argumente angehäuft. Die Online-Dokumentation von pandas
enthält viele Beispiele für die einzelnen Funktionen.

Einige dieser Funktionen, wie ``pandas.read_csv``, führen eine Typinferenz
durch, da die Datentypen der Spalten nicht Teil des Datenformats sind. Das
bedeutet, dass ihr nicht unbedingt angeben müsst, welche Spalten numerisch,
integer, boolesch oder string sind. Bei anderen Datenformaten wie HDF5, ORC und
Parquet sind die Datentypinformationen hingegen bereits in das Format
eingebettet.
