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

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    deduplicate.ipynb
    string-matching.ipynb
    nulls.ipynb
    scikit-learn-reprocessing.ipynb
    dask-pipeline.ipynb
    voluptuous.ipynb
    engarde.ipynb
    bulwark.ipynb
    tdda.ipynb
    hypothesis.ipynb
