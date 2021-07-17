tox
===

`tox <https://tox.readthedocs.io/>`_ ist ein Tool zur Automatisierung des
``virtualenv``-Environment-Management und zum Testen mit mehreren
Interpreter-Konfigurationen.

Mit ``tox`` könnt ihr komplexe Multiparameter-Testmatrizen über eine einfache
Konfigurationsdatei im ``INI``-Stil konfigurieren.

Beispiel
--------

Erstellt eine ``tox.ini``-Datei:

.. code-block:: ini

    [tox]
    envlist = py27,py36

    [testenv]
    deps = pytest
    commands =
        pytest

Beim Aufrufen von ``pipenv run tox`` werden dann die folgenden Schritte
durchlaufen:

#. Optional erstellen eines Python-Package mit

   .. code-block:: console

        $ pipenv run python setup.py sdist

#. Erstellen der in ``envlist`` angegebenen Umgebungen

   In jeder dieser Umgebungen werden dann

   #. die Abhängigkeiten und Pakete installiert
   #. die Befehle aus ``commands`` ausgeführt

#. Erstellen eines Reports mit den Ergebnissen aus jeder der Umgebungen, z.B.:

   .. code-block:: text

        ____________________ summary ____________________
        py27: commands succeeded
        ERROR:   py36: commands failed

.. seealso::

   * `Beispiele <https://tox.readthedocs.io/en/latest/examples.html>`_

Installation
------------

.. code-block:: console

    $ pipenv install tox

.. note::
   Falls ihr pipenv noch nicht installiert habt, findet ihr eine Anleitung
   hierzu unter :doc:`/first-steps/install`.

.. seealso::
   * `tox plugins <https://tox.readthedocs.io/en/latest/plugins.html>`_

GitHub-Actions
--------------

Wenn euer Projekt auf `GitHub <https://github.com/>`_ gehostet ist, könnt ihr
GitHub-Actions verwenden um automatisiert eure Tests in verschiedenen Umgebungen
ausführen zu können. Dabei sind eine ganze Reihe von Umgebungen für die
GitHub-Actions verfügbar: `github.com/actions/virtual-environments
<https://github.com/actions/virtual-environments/#readme>`_.

#. Um eine GitHub-Action in eurem Projekt zu erstellen, klickt auf
   :menuselection:`Actions --> set up a workflow yourself`. Dies erstellt
   üblicherweise eine Datei :file:`.github/workflows/main.yml`.
#. Gebt dieser Datei einen aussagekräftigeren Namen. Wir verwenden hierfür
   üblicherweise :file:`ci.yml`, wobei ``ci`` für *Continuous Integration*,
   (Englisch: `Kontinuierliche Integration
   <https://de.wikipedia.org/wiki/Kontinuierliche_Integration>`_) steht.
#.  Die vorausgefüllte YAML-Datei ist für unsere Zwecke wenig hilfreich. Ihr
    könnt den Text ersetzen, :abbr:`z.B. (zum Beispiel)` mit:

   .. code-block:: yaml

    name: CI

    on:
      push:
        branches: ["main"]
      pull_request:
        branches: ["main"]
      workflow_dispatch:

    jobs:
      tests:
        name: "Python ${{ matrix.python-version }}"
        runs-on: "ubuntu-latest"
        env:
          USING_COVERAGE: '3.6,3.8'

        strategy:
          matrix:
            python-version: ["3.6", "3.7, "3.8"]

        steps:
          - uses: "actions/checkout@v2"
          - uses: "actions/setup-python@v2"
            with:
              python-version: "${{ matrix.python-version }}"
          - name: "Install dependencies"
            run: |
              set -xe
              python -VV
              python -m site
              python -m pip install --upgrade pip setuptools wheel
              python -m pip install --upgrade coverage[toml] virtualenv tox tox-gh-actions

          - name: "Run tox targets for ${{ matrix.python-version }}"
            run: "python -m tox"

   .. note::
      Passt :abbr:`ggf. (gegebenenfalls)` die Python-Versionen in
      :envvar:`python-version` an; ihr müsst jedoch nicht auch die
      Umgebungsvariable in ``USING_COVERAGE`` ändern, da dies durch das
      tox-Plugin ``tox-gh-actions`` (siehe unten) erfolgt.

#. Anschließend könnt ihr auf :guilabel:`Start commit` klicken. Da wir noch
   weitere Änderungen vornehmen wollen bevor die Tests automatisiert ausgeführt
   werden sollen, wählen wir :guilabel:`Create a new branch for this commit and
   start a pull request` und als Name für den neuen :term:`Branch <branch>`
   ``github-actions``. Schließlich könnt ihr auf :guilabel:`Create pull request`
   klicken.
#. Um nun in den neuen Branch zu wechseln, gehen wir zu :menuselection:`Code -->
   main --> github-actions`.
#. `tox-gh-actions <https://pypi.org/project/tox-gh-actions/>`_ vereinfacht das
   Ausführen von tox in GitHub-Actions indem es als Umgebung für die Tests
   diejenige bereitstellt, die auch tox selbst verwendet. Hierfür müssen wir
   jedoch noch unsere :file:`tox.ini`-Datei anpassen, :abbr:`z.B. (zumr
   Beispiel)`:

   .. code-block:: ini

    [gh-actions]
    python =
        3.6: py36
        3.7: py37, docs
        3.8: py38, lint, typing, changelog

   Dies ordnet GitHub-Actions tox-Umgebungen zu.

   .. note::
      * Es müssen nicht alle Varianten eurer Umgebung angegeben werden. Dies
        unterscheidet ``tox-gh-actions`` von ``tox -e py``.
      * Stellt sicher, dass die Versionen im ``[gh-actions]``-Abschnitt mit den
        verfügbaren Python-Versionen und :abbr:`ggf. (gegebenenfalls)` mit denen
        in den :ref:`GitHub-Actions für Git pre-commit Hooks
        <gh-action-pre-commit-example>` übereinstimmen.
      * Da alle Tests für eine spezifische Python-Version nacheinander in einem
        Container ausgeführt werden, gehen hierbei die Vorteile der parallelen
        Ausführung verloren.

#. Nun könnt ihr in eurer :file:`README.rst`-Datei noch ein Badge hinzufügen,
   :abbr:`z.B. (zum Beispiel)` mit:

   .. code-block::

    .. image:: https://github.com/YOU/YOUR_PROJECT/workflows/CI/badge.svg?branch=main
         :target: https://github.com/YOU/YOUR_PROJECT/actions?workflow=CI
         :alt: CI Status

#. Die Code-Abdeckung könnt ihr auf `Codecov <https://about.codecov.io/>`_
   veröffentlichen, indem ihr in eurer :file:`ci.yml`-Datei :abbr:`z.B. (zum
   Beispiel)` folgendes hinzufügen:

   .. code-block:: yaml

    - name: "Convert coverage"
      run: "python -m coverage xml"
    - name: "Upload coverage to Codecov"
      uses: "codecov/codecov-action@v1"
      with:
        fail_ci_if_error: true

#. Schließlich könnt ihr auch noch ein Badge für die Code-Abdeckung in eurer
   :file:`README.rst`-Datei anzeigen, :abbr:`z.B. (zum Beispiel)` mit:

   .. code-block::

    .. image:: https://codecov.io/gh/YOU/YOUR_PROJECT/branch/main/graph/badge.svg
       :target: https://codecov.io/gh/YOU/YOUR_PROJECT
       :alt: Code Coverage Status (Codecov)

.. seealso::
   * `Build & test Python
     <https://docs.github.com/en/actions/guides/building-and-testing-python>`_
   * `Workflow syntax
     <https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions>`_
