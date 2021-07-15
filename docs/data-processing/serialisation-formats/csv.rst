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
|                       |       | Semikolon etc.).                                      |
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
|                       |       | Excel-Dateien direkt einlesen, z.B. mit pandas        |
|                       |       | `read_excel`_.                                        |
+-----------------------+-------+-------------------------------------------------------+
| Menschliche Lesbarkeit| +-    | CSV ist speziell bei Ganz- oder Dezimalzahlen mit     |
|                       |       | gleicher Zeichenlänge gut lesbar. In allen anderen    |
|                       |       | Fällen kann es schwierig werden, die entsprechenden   |
|                       |       | Spalten zu identifizieren.                            |
+-----------------------+-------+-------------------------------------------------------+
| Geschwindigkeit       | \+    | CSV kann sehr schnell serialisiert und deserialisiert |
|                       |       | werden.                                               |
+-----------------------+-------+-------------------------------------------------------+
| Dateigröße            | ++    | Nur :doc:`protobuf` sollte kompakter sein.            |
+-----------------------+-------+-------------------------------------------------------+

Beispiel
--------

`iris.csv`_

.. code-block:: csv

    5.1,0.222222222,3.5,0.625,1.4,0.06779661,0.2,0.041666667,setosa
    4.9,0.166666667,3,0.416666667,1.4,0.06779661,0.2,0.041666667,setosa
    4.7,0.111111111,3.2,0.5,1.3,0.050847458,0.2,0.041666667,setosa
    4.6,0.083333333,3.1,0.458333333,1.5,0.084745763,0.2,0.041666667,setosa
    5,0.194444444,3.6,0.666666667,1.4,0.06779661,0.2,0.041666667,setosa
    ...

.. seealso::

    * `RFC 4180 <https://tools.ietf.org/html/rfc4180>`_

.. _`csv`: https://docs.python.org/3/library/csv.html
.. _`pandas`: https://pandas.pydata.org/
.. _`read_excel`: https://pandas.pydata.org/docs/user_guide/io.html#io-excel-reader
.. _`iris.csv`: https://sourceforge.net/projects/irisdss/files/IRIS.csv
