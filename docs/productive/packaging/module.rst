Module
======

Notebooks sind gut geeignet um schnell voranzukommen, doch bei umfangreicher
werdendem Code empfiehlt sich, stabilen Code in einzelne Dateien auszulagern.
Solche Dateien werden :doc:`Module <python:tutorial/modules>` genannt. Wenn ihr
z.B. in eurem Notebook geschrieben habt:

.. code-block:: python

    filename = 'example.csv'
    df = pd.read_csv(filename)

so könnt ihr dies in ein Modul auslagern. Dabei wird für den Dateinamen der
Modulname ``dataprep`` um den Suffix ``.py`` ergänzt.

Innerhalb dieser Datei könnt ihr nun die Methode ``load_data``
definieren:

.. literalinclude:: dataprep.py
   :language: python
   :linenos:

Das Modul kann dann wieder in das Notebook importiert werden:

.. code-block:: python

    import dataprep

Anschließend könnt ihr die Methode ``load_data`` verwenden um z.B. die CSV-Datei
``example.csv`` zu lesen:

.. code-block:: python

    dataprep.load_data(filename)

Wenn ihr das Modul ändert, kann die aktualiserte Variante automatisch
übernommen werden mit :mod:`IPython.extensions.autoreload`:

   .. code-block:: python

    %load_ext autoreload
    %autoreload
