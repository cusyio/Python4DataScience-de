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

* :doc:`/data-processing/serialisation-formats/excel` zu ersetzen
* einen `ETL-Prozess <https://de.wikipedia.org/wiki/ETL-Prozess>`_ zu
  realisieren
* :doc:`/data-processing/serialisation-formats/csv/index`- oder
  :doc:`/data-processing/serialisation-formats/json/index`-Daten zu
  verarbeiten
* maschinelles Lernen vorzubereiten

.. seealso::
    * `Home
      <https://pandas.pydata.org/>`_
    * `User guide
      <https://pandas.pydata.org/docs/user_guide/index.html>`_
    * `API reference
      <https://pandas.pydata.org/docs/reference/index.html>`_
    * `GitHub
      <https://github.com/pandas-dev/pandas/>`_

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
