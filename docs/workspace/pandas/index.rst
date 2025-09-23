.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

pandas
======

`pandas <https://pandas.pydata.org/>`_ ist eine Python-Bibliothek zur
Datenanalyse, die in den letzten Jahren sehr populär geworden ist. Auf der
Website wird pandas so beschrieben:

    »pandas ist ein schnelles, leistungsfähiges, flexibles und einfach zu
    bedienendes Open-Source-Tool zur Datenanalyse und -manipulation, das auf der
    Programmiersprache Python aufbaut.«

Genauer ist pandas ein In-Memory-Analysewerkzeug, das SQL-ähnliche Konstrukte,
sowie statistische und analytische Werkzeuge bietet. Dabei baut pandas auf
`Cython <https://cython.org/>`_ und :doc:`../numpy/index` auf, wodurch es
weniger speicherintensiv und schneller ist als reiner Python-Code. Meist wird
pandas genutzt, um

* :doc:`/data-processing/serialisation-formats/excel` und `Power BI
  <https://www.microsoft.com/de-de/power-platform/products/power-bi/>`_ zu
  ersetzen
* einen `ETL-Prozess <https://de.wikipedia.org/wiki/ETL-Prozess>`_ zu
  realisieren
* :doc:`/data-processing/serialisation-formats/csv/index`- oder
  :doc:`/data-processing/serialisation-formats/json/index`-Daten zu
  verarbeiten
* maschinelles Lernen vorzubereiten

.. tip::
   `cusy Seminar: Daten analysieren mit pandas
   <https://cusy.io/de/our-training-courses/analysing-data-with-pandas.html>`_

.. seealso::
    * `Home
      <https://pandas.pydata.org/>`_
    * `User guide
      <https://pandas.pydata.org/docs/user_guide/index.html>`_
    * `API reference
      <https://pandas.pydata.org/docs/reference/index.html>`_
    * `GitHub
      <https://github.com/pandas-dev/pandas/>`_

pandas vs. Polars vs. Dask und DuckDB
-------------------------------------

Die Wahl zwischen pandas, `Polars <https://pola.rs>`_, :doc:`/performance/dask`
und `DuckDB <https://duckdb.org>`_ hängt von der Art der Arbeitslast ab:

pandas
    ist die kanonische Python-DataFrame-Bibliothek für Analysen auf einem
    einzelnen Rechner.
Polars
    ist in Rust geschrieben und erlaubt leistungsfähige Analysen auf einem
    einzigen Knoten oder wenn `Lazy
    Evaluation <https://de.wikipedia.org/wiki/Lazy_Evaluation>`_ und
    `Expressions-API
    <https://docs.pola.rs/api/python/stable/reference/expressions/index.html>`_
    wichtig sind.
Dask
    ist eine Python-Bibliothek für paralleles Rechnen, die bekannte APIs,
    :abbr:`u.a. (unter anderem)` von pandas und `Scikit-Learn
    <https://scikit-learn.org/stable/>`_ auf Cluster skaliert.
DuckDB
    ist eine In-Process `OLAP
    <https://de.wikipedia.org/wiki/Online_Analytical_Processing>`_-Datenbank
    für Analysen und SQL über **lokale** Dateien, die häufig pandas DataFrames
    ergänzt, da es sich hervorragend für In-Process-Analysen und SQL-Aufgaben
    eignet.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    data-structures.ipynb
    python-data-structures.ipynb
    indexing.ipynb
    date-time.ipynb
    select-filter.ipynb
    transforming.ipynb
    string-manipulation.ipynb
    arithmetic.ipynb
    descriptive-statistics.ipynb
    sorting-ranking.ipynb
    discretisation.ipynb
    combining-merging.ipynb
    group-operations.ipynb
    aggregation.ipynb
    apply.ipynb
    pivoting-crosstab.ipynb
    convert-dtypes.ipynb
