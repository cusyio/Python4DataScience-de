Wily
====

Wily ist ein Kommandozeilenwerkzeug zum Überprüfen der Komplexität von
Python-Code in Tests und Anwendungen. Auch Python code in ``.ipynb``-Dateien
wird automatisch erkannt.

.. seealso::

   * `Docs <https://wily.readthedocs.io/en/latest/>`_
   * `GitHub <https://github.com/tonybaloney/wily>`_
   * `PyPI <https://pypi.org/project/wily/>`_

Installation
------------

Wily kann einfach installiert werden mit

.. code-block:: console

    $ pipenv install wily

Anschließend könnt Ihr die Installation überprüfen mit

.. code-block:: console

    $ pipenv run wily --help
    Usage: wily [OPTIONS] COMMAND [ARGS]...
      Version: 1.19.0
      🦊 Inspect and search through the complexity of your source code. To get
      started, run setup:
        $ wily setup …

Konfiguration
-------------

Im Projektverzeichnis kann eine ``wily.cfg``-Datei angelegt werden mit der Liste
der verfügbaren Operatoren:

.. code-block:: ini

    [wily]
    # list of operators, choose from cyclomatic, maintainability, mccabe and raw
    operators = cyclomatic,raw
    # archiver to use, defaults to git
    archiver = git
    # path to analyse, defaults to .
    path = /path/to/target
    # max revisions to archive, defaults to 50
    max_revisions = 20

Für Jupyter Notebooks könnt Ihr ggf. angeben, dass diese nicht analysiert werden
sollen mit

.. code-block:: python

    ipynb_support = false

oder für einzelne Zellen mit

.. code-block:: python

    ipynb_cells = false

Verwendung
----------

… als Kommandozeilenwerkzeug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Aufbau eines Caches mit den Statistiken des Projekts

   .. note::
      Wily geht davon aus, dass Euer Projektordner ein :doc:`Git
      <../../productive/git/index>`-Repository ist. Wily erstellt jedoch keinen
      Cache, wenn das Arbeitsverzeichnis verschmutzt ist.

   .. code-block:: console

        $ pipenv run wily build

#. Metrik anzeigen

   .. code-block:: console

        $ pipenv run wily report

    Dies gibt sowohl die Metrik wie auch das Delta zur vorherigen Revision aus.

#. Rangfolge anzeigen

   .. code-block:: console

        $ pipenv run wily rank

   Dies zeigt die Rangfolge aller Dateien in einem Verzeichnis oder einer
   einzelnen Datei an basierend auf der angegebenen Metrik, sofern diese in
   ``.wily/`` vorhanden ist.

#. Diagramm anzeigen

   .. code-block:: console

        $ pipenv run wily graph

   Dies zeigt ein Diagramm im Standard-Browser an.

#. Informationen zum Build-Verzeichnis anzeigen

   .. code-block:: console

        $ pipenv run wily index

#. Auflisten der in den Wily-Operatoren verfügbaren Metriken

   .. code-block:: console

        $ pipenv run wily list-metrics

… als pre-commit Hook
~~~~~~~~~~~~~~~~~~~~~

Ihr könnt Wily auch als :doc:`pre-commit Hook
<../../productive/git/pre-commit>` verwenden. Hierzu müsstet Ihr in der
``pre-commit-config.yaml``-Konfigurationsdatei z.B. folgendes hinzufügen:

.. code-block:: yaml

    repos:
    -   repo: local
        hooks:
        -   id: wily
            name: wily
            entry: wily diff
            verbose: true
            language: python
            additional_dependencies: [wily]

… in einer CI/CD-Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~

Üblicherweise vergelicht Wily die Komplexität mit der vorherigen Revision. Ihr
könnt jedoch auch andere Referenzen angeben, z.B. ``HEAD^1`` mit

.. code-block:: console

    $ pipenv run wily build src/
    $ pipenv run wily diff src/ -r HEAD^1
