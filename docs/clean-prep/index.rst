Daten bereinigen und validieren
===============================

Im Folgenden wollen wir euch einen praktischen Überblick über verschiedene
Bibliotheken und Methoden zur `Datenbereinigung
<https://de.wikipedia.org/wiki/Datenbereinigung>`_ und -validierung mit Python
geben. Dabei verwenden wir neben bekannten Bibliotheken wie NumPy und Pandas
auch mehrere kleine, spezialisierte Bibliotheken wie
:doc:`dedupe <deduplicate>`, :doc:`fuzzywuzzy <string-matching>`,
:doc:`voluptuous <voluptuous>`, :doc:`bulwark <bulwark>`, :doc:`tdda <tdda>` und
:doc:`hypothesis <hypothesis>`. Wir bevorzugen diese leichtgewichtigeren
Lösungen gegenüber großen, universellen Systemen wie `Great Expectations
<https://greatexpectations.io/>`_.

.. seealso::
   * `pandera <https://pandera.readthedocs.io/en/stable/>`_
   * `pandas-validation <https://pandas-validation.readthedocs.io/en/latest/>`_
   * `PandasSchema <https://multimeric.github.io/PandasSchema/>`_
   * `Opulent-Pandas <https://github.com/danielvdende/opulent-pandas>`_
   * `signpost <https://github.com/ilsedippenaar/signpost>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    nulls.ipynb
    outliers.ipynb
    string-matching.ipynb
    deduplicate.ipynb
    engarde.ipynb
    bulwark.ipynb
    hypothesis.ipynb
    tdda.ipynb
    voluptuous.ipynb
    scikit-learn-reprocessing.ipynb
    dask-pipeline.ipynb
