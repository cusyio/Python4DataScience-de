Wily
====

Das *Zen of Python* [#]_ betont in vielfältiger Weise die Komplexitätsreduktion:

    Einfach ist besser als komplex.

    Komplex ist besser als kompliziert.

    Flach ist besser als verschachtelt.

Wily ist ein Kommandozeilenwerkzeug zum Überprüfen der Komplexität von
Python-Code in Tests und Anwendungen. Hierfür verwendet Wily folgende Metriken:

`McCabe-Metrik <https://de.wikipedia.org/wiki/McCabe-Metrik>`_
    auch zyklomatische Komplexität genannt, misst die Komplexität von Code durch
    die Anzahl linear unabhängiger Pfade im Kontrollflussgraphen.

    Das Software Engineering Institute der Carnegie Mellon University
    unterscheidet die folgenden vier Risikostufen [#]_:

    +--------------------------------+--------------------------------+
    | Zyklomatische Komplexität      | Risikobewertung                |
    +================================+================================+
    |  1–10                          | einfaches Programm ohne großes |
    |                                | Risiko                         |
    +--------------------------------+--------------------------------+
    | 11–20                          | mäßiges Risiko                 |
    +--------------------------------+--------------------------------+
    | 21–50                          | komplexes, hochriskantes       |
    |                                | Programm                       |
    +--------------------------------+--------------------------------+
    | > 50                           | untestbares Programm mit sehr  |
    |                                | hohem Risiko                   |
    +--------------------------------+--------------------------------+

`Halstead-Metrik <https://de.wikipedia.org/wiki/Halstead-Metrik>`_
    statisch analysierendes Verfahren, das aus der Anzahl der Operatoren und
    Operanden die Schwierigkeit des Programms, den Aufwand und die
    Implementierungszeit berechnet.
Wartbarkeitsindex (engl. Maintainability Index)
    basiert auf den McCabe- und Halstead-Metriken sowie der Anzahl der
    Codezeilen [#]_:

    +--------------------------------+--------------------------------+
    | Index                          | Wartbarkeit                    |
    +================================+================================+
    |  0–25                          | unwartbar                      |
    +--------------------------------+--------------------------------+
    | 25–50                          | besorgniserregend              |
    +--------------------------------+--------------------------------+
    | 50–75                          | verbesserungsbedürftig         |
    +--------------------------------+--------------------------------+
    | 75–100                         | Superhelden-Code               |
    +--------------------------------+--------------------------------+

.. seealso::

   * `Docs <https://wily.readthedocs.io/en/latest/>`_
   * `GitHub <https://github.com/tonybaloney/wily>`_
   * `PyPI <https://pypi.org/project/wily/>`_
   * `wily-pycharm <https://github.com/tonybaloney/wily-pycharm>`_

Installation
------------

Wily kann einfach installiert werden mit

.. code-block:: console

    $ pipenv install wily

Anschließend könnt ihr die Installation überprüfen mit

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

Auch Python code in ``.ipynb``-Dateien wird üblicherweise automatisch erkannt.
Ihr könnt dies jedoch ggf. unterbinden für ein Jupyter Notebooks mit

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
      Wily geht davon aus, dass euer Projektordner ein :doc:`Git
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
<../../productive/git/pre-commit>` verwenden. Hierzu müsstet ihr in der
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

----

.. [#] `PEP 20 – The Zen of Python <https://www.python.org/dev/peps/pep-0020/>`_
.. [#] `C4 Software Technology Reference Guide, S. 147
       <https://resources.sei.cmu.edu/asset_files/Handbook/1997_002_001_16523.pdf>`_
.. [#] `Using Metrics to Evaluate Software Svstem Maintainability
       <https://www.ecs.csun.edu/~rlingard/comp589/ColemanPaper.pdf>`_
