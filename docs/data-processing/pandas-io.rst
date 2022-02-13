pandas IO tools
===============

pandas verfügt über eine Reihe von Funktionen zum Lesen von Tabellendaten als
DataFrame-Objekt, darunter

+--------------------+----------------------------------------------------------+
| Funktion           | Beschreibung                                             |
+====================+==========================================================+
| ``read_csv``       | Laden von durch Trennzeichen getrennte Daten aus einer   |
|                    | Datei, einer URL oder einem dateiähnlichen Objekt;       |
|                    | standardmäßig wird ein Komma als Trennzeichen verwendet  |
+--------------------+----------------------------------------------------------+
| ``read_fwf``       | Lesen von Daten im Spaltenformat mit fester Breite (d.h. | 
|                    | ohne Begrenzungszeichen)                                 |
+--------------------+----------------------------------------------------------+
| ``read_clipboard`` | Version von ``read_csv``, die Daten aus der              |
|                    | Zwischenablage liest; nützlich für die Konvertierung von |
|                    | Tabellen aus Webseiten                                   |
+--------------------+----------------------------------------------------------+
| ``read_excel``     | Einlesen von Tabellendaten aus einer Excel XLS- oder     |
|                    | XLSX-Datei                                               |
+--------------------+----------------------------------------------------------+
| ``read_hdf``       | Lesen von HDF5-Dateien, die von Pandas geschrieben wurden|
+--------------------+----------------------------------------------------------+
| ``read_html``      | Liest alle Tabellen aus dem angegebenen HTML-Dokument    |
+--------------------+----------------------------------------------------------+
| ``read_json``      | Lesen von Daten aus einer JSON (JavaScript Object        |
|                    | Notation) String-Darstellung                             |
+--------------------+----------------------------------------------------------+
| ``read_feather``   | Lesen des Feather-Binärdateiformats                      |
+--------------------+----------------------------------------------------------+
| ``read_orc``       | Einlesen des Apache ORC-Binärdateiformats                |
+--------------------+----------------------------------------------------------+
| ``read_parquet``   | Lesen des Apache Parquet-Binärdateiformats               |
+--------------------+----------------------------------------------------------+
| ``read_pickle``    | Lesen eines beliebigen Objekts, das im                   |
|                    | Python-Pickle-Format gespeichert ist                     |
+--------------------+----------------------------------------------------------+
| ``read_sas``       | Lesen eines SAS-Datensatzes, der in einem der            |
|                    | benutzerdefinierten Speicherformate des SAS-Systems      |
|                    | gespeichert ist                                          |
+--------------------+----------------------------------------------------------+
| ``read_spss``      | Liest eine von SPSS erstellte Datendatei                 |
+--------------------+----------------------------------------------------------+
| ``read_sql``       | Lesen der Ergebnisse einer SQL-Abfrage (mit SQLAlchemy)  |
|                    | als pandas DataFrame                                     |
+--------------------+----------------------------------------------------------+
| ``read_sql_table`` | Lesen einer ganzen SQL-Tabelle (mit SQLAlchemy) als      |
|                    | pandas DataFrame (entspricht einer Abfrage, die alles in |
|                    | dieser Tabelle mit ``read_sql`` auswählt)                |
+--------------------+----------------------------------------------------------+
| ``read_stata``     | Lesen eines Datensatzes aus dem Stata-Dateiformat        |
+--------------------+----------------------------------------------------------+

.. seealso::
    `pandas I/O API <https://pandas.pydata.org/docs/user_guide/io.html>`_
        Die pandas I/O API ist eine Sammlung von ``reader``-Funktionen, die ein
        pandas-Objekt zurückgeben. Meist stehen auch entsprechende
        ``write``-Methoden zur Verfügung.

Zunächst werde ich einen Überblick über diese Funktionen geben, die dazu gedacht
sind, Textdaten in einen DataFrame zu konvertieren. Dabei lassen sich die
optionalen Argumente für diese Funktionen in folgende Kategorien einteilen:

Indizierung
    Kann eine oder mehrere Spalten als den zurückgegebenen DataFrame behandeln,
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

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    json-example.ipynb
    excel-example.ipynb
