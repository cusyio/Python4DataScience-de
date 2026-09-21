.. SPDX-FileCopyrightText: 2021 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

CSV
===

Überblick
---------

+-----------------------+-------+-------------------------------------------------------+
| Unterstützung von     | -\-   | CSV wird zum Speichern von Tabellendaten verwendet,   |
| Datenstrukturen       |       | ist aber im Gegensatz zu anderen hier besprochenen    |
|                       |       | Serialisierungsformaten nicht für verschachtelte      |
|                       |       | Daten geeignet.                                       |
+-----------------------+-------+-------------------------------------------------------+
| Standardisierung      | -\-   | CSV ist nicht gut standardisiert: weder das Encoding  |
|                       |       | noch die Trennung der Zelleninhalte (Komma,           |
|                       |       | Semikolon :abbr:`etc. (et cetera)`).                  |
+-----------------------+-------+-------------------------------------------------------+
| Schema IDL            | -\-   | Nein                                                  |
+-----------------------+-------+-------------------------------------------------------+
| Sprachunterstützung   | ++    | Das CSV-Format wird in fast jeder Programmiersprache  |
|                       |       | gut unterstützt. Ein `csv`_-Modul ist in der          |
|                       |       | Python-Standardbibliothek enthalten und `pandas`_     |
|                       |       | läd eine CSV-Datei direkt als ``Dataframe``.          |
|                       |       |                                                       |
|                       |       | Auch wenn CSV das einzige hier besprochene Format ist,|
|                       |       | das gut von Tabellenkalkulationen wie Excel           |
|                       |       | unterstützt wird, solltet ihr strukturiertere         |
|                       |       | Excel-Dateien direkt einlesen, :abbr:`z.B. (zum       |
|                       |       | Beispiel)` mit pandas `read_excel`_.                  |
+-----------------------+-------+-------------------------------------------------------+
| Menschliche Lesbarkeit| +-    | CSV ist speziell bei Ganz- oder Dezimalzahlen mit     |
|                       |       | gleicher Zeichenlänge gut lesbar. In allen anderen    |
|                       |       | Fällen kann es schwierig werden, die entsprechenden   |
|                       |       | Spalten zu identifizieren.                            |
+-----------------------+-------+-------------------------------------------------------+
| Geschwindigkeit       | \+    | CSV kann sehr schnell serialisiert und deserialisiert |
|                       |       | werden.                                               |
+-----------------------+-------+-------------------------------------------------------+
| Dateigröße            | ++    | Nur :doc:`../protobuf` sollte kompakter sein.         |
+-----------------------+-------+-------------------------------------------------------+

Beispiel
--------

.. code-block::
   :caption: iris.csv

   5.1,0.222222222,3.5,0.625,1.4,0.06779661,0.2,0.041666667,setosa
   4.9,0.166666667,3,0.416666667,1.4,0.06779661,0.2,0.041666667,setosa
   4.7,0.111111111,3.2,0.5,1.3,0.050847458,0.2,0.041666667,setosa
   4.6,0.083333333,3.1,0.458333333,1.5,0.084745763,0.2,0.041666667,setosa
   5,0.194444444,3.6,0.666666667,1.4,0.06779661,0.2,0.041666667,setosa
   ...

.. seealso::

   * `iris.csv`_
   * :rfc:`4180`
   * `xan <https://github.com/medialab/xan>`_

CSVW
----

`CSVW <https://csvw.org>`_ ist ein W3C-Standard *„zur Beschreibung und Verdeutlichung des
Inhalts von CSV-Tabellen“* im Web und ermöglicht die bestimmte Einschränkungen für
CSV-Daten. Nachfolgend die ersten Zeilen einer Beispiel-CSV-Datei, :file:`grit_bins.csv`
von der CSVW-Website:

.. code-block::
   :caption: grit_bins.csv
   :linenos:

   42, 425584, 439562
   43, 425301, 439519
   44, 425379, 439596
   45, 425024, 439663
   46, 424915, 439697
   48, 425157, 440347
   49, 424784, 439681
   50, 424708, 439759
   51, 424913, 440642
   52, 425342, 440376
   ... ... ...

----

… und hier ist die zugehörige CSVW-Metadatendatei :file:`grit_bins.json`:

.. code-block:: javascript
   :caption: grit_bins.json
   :linenos:

   {
     "@context": ["http://www.w3.org/ns/csvw", {"@language": "en"}],
     "tables": [{
       "url": "http://opendata.leeds.gov.uk/downloads/gritting/grit_bins.csv",
       "tableSchema": {
         "columns": [
         {
           "name": "location",
           "datatype": "integer"
         },
         {
           "name": "easting",
           "datatype": "decimal",
           "propertyUrl": "http://data.ordnancesurvey.co.uk/ontology/spatialrelations/easting"
         },
         {
           "name": "northing",
           "datatype": "decimal",
           "propertyUrl": "http://data.ordnancesurvey.co.uk/ontology/spatialrelations/northing"
         }
         ],
         "aboutUrl": "#{location}"
       }
     }],
     "dialect": {
       "header": false
     }
   }

Zeile 2
    Das ``@context``-Element gibt an, dass es sich um eine CSVW-Spezifikation in
    englischer Sprache handelt.
Zeilen 3–24
    CSVW unterstützt mehrere Tabellen oder CSV-Dateien innerhalb einer Datei.
Zeile 4
    CSVW verweist mithilfe einer URL auf die Daten, die es beschreibt.
Zeilen 5–23
    CSVW ermöglicht die Angabe des Namens und des Datentyps jeder Spalte.
Zeilen 14, 19
    Die letzten beiden Spalten verfügen zudem über eine ``propertyURL``, die als
    Schlüssel dient, sofern die Daten in JSON oder RDF umgewandelt werden. In diesem Fall
    würde bei einer solchen Umwandlung in JSON beispielsweise die Werte ``easting`` und
    ``northing`` der ersten Zeile der CSV-Datei zugeordnet werden:

    .. code-block:: javascript

       "http://data.ordnancesurvey.co.uk/ontology/spatialrelations/easting": 425584
       "http://data.ordnancesurvey.co.uk/ontology/spatialrelations/northing": 439562

Zeile 22
    ``aboutURL`` gibt den Speicherort der Informationen zu dem in der jeweiligen Zeile
    beschriebenen Element an. In unerem Beispiel ist der Speicherort

    .. code-block::

       http://opendata.leeds.gov.uk/downloads/gritting/42

Zeilen 25–27
    Im ``dialect``-Feld werden einige Formatangaben zur Datei angegeben – in diesem Fall
    das Fehlen von Kopfzeilen. Meist sollten hier jedoch auch das Encoding und das Trennzeichen angegeben werden, :abbr:`z. B. (zum Beispiel)`

    .. code-block:: javascript

       "dialect": {
         "header": false,
         "encoding": "utf-8",
         "delimiter": ","
       }

    Auch andere Aspekte wie Anführungszeichen, Escape-Zeichen und Null-Indikatoren können
    in diesem Abschnitt angegeben werden.

Zusätzlich zu den im Beispiel gezeigten Elementen bietet CSVW auch die Möglichkeit,
verschiedene Arten von Einschränkungen für die Daten in einer CSV-Datei festzulegen,
darunter zulässige Bereiche für Spalten mit Minimal- und Maximalwerten, Formate für
numerische Daten und Anforderungen an die Eindeutigkeit.

Die CSVW-Website verfügt über einen Bereich `Tools <https://csvw.org/tools.html>`_,
darunter `CSV Lint <https://github.com/Data-Liberation-Front/csvlint.rb>`_, mit dem ihr
überprüfen könnt, ob eure CSV-Datei wohlgeformt ist, und sie anhand eines CSV-Dialekts,
eines JSON-Tabellenschemas oder einer CSVW-Annotation testen könnt. Mit `csvw
<https://github.com/cldf/csvw>`_ könnt ihr csv-Daten validieren und in JSON konvertieren.

.. seealso::
   * `Model for Tabular Data and Metadata on the Web
     <https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/>`_
   * `Metadata Vocabulary for Tabular Data
     <https://www.w3.org/TR/2015/REC-tabular-metadata-20151217/>`_

CSVW und ``tdda.serial``
~~~~~~~~~~~~~~~~~~~~~~~~

Die :doc:`tdda </clean-prep/libs-methods/tdda>`-Bibliothek stellt nicht nur eine API zum
Lesen und Schreiben von Daten und Metadaten bereit, sie ermöglicht die Verwendung von
Metadatendateien. ``tdda serial`` kann zwischen verschiedenen Metadatenformaten
konvertieren und Python-Code zum Lesen von Dateien generieren, wie in einer
Metadatendatei festgelegt:

:samp:`tdda serial {EXAMPLE_METADATA}.json {EXAMPLE}.serial`
    konvertiert CSVW- in :file:`tdda.serial`-Dateien
:samp:`tdda serial --to csvw {EXAMPLE}.serial {EXAMPLE}.json`
    konvertiert :file:`tdda.serial`- in CSVW-Dateien
:samp:`tdda serial --to pd.[r|w] {EXAMPLE}.serial {EXAMPLE}.serial`
    konvertiert eine :file:`tdda.serial`-Datei entweder mit pandas ``read_csv`` oder
    ``to_csv``

.. seealso::
   * `tdda.serial: Metadata and Tools for Flat (“CSV”) Files
     <https://tdda.readthedocs.io/en/latest/serialformat.html>`_
   * `TDDA Serial API <https://tdda.readthedocs.io/en/latest/serial-api.html>`_
   * `Test-Driven Data Analysis
     <https://www.tdda.info/tddaserial-metadata-for-flat-files-csv-files>`_

.. _`csv`: https://docs.python.org/3/library/csv.html
.. _`pandas`: https://pandas.pydata.org/
.. _`read_excel`: https://pandas.pydata.org/docs/user_guide/io.html#io-excel-reader
.. _`iris.csv`: https://sourceforge.net/projects/irisdss/files/IRIS.csv/download

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   example.ipynb
