.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Pytype
======

Pytype ist ein statisches Analysewerkzeug, das Typen aus eurem Python-Code
ableitet ohne dass Typanmerkungen notwendig sind. Es kann jedoch auch im Code
stehende `Type Annotations <https://peps.python.org/pep-0484/>`_ erzwingen.
Obwohl Annotationen für Pytype optional sind, werden sie geprüft und angewendet,
sofern sie vorhanden sind. Die von Pytype erzeugten Typ-Annotationen werden in
eigenständigen ``.pyi``-Dateien gespeichert, die mit `merge-pyi
<https://github.com/google/pytype/tree/main/pytype/tools/merge_pyi>`_ wieder
in den Python-Code eingebunden werden können. Schließlich markiert es häufige
Fehler wie falsch geschriebene Attributnamen oder Funktionsaufrufe und vieles
mehr, auch über Dateigrenzen hinweg.

.. seealso::
   * `Home <https://google.github.io/pytype/>`_
   * `GitHub <https://github.com/google/pytype>`_
   * `PyPI <https://pypi.org/project/pytype/>`_
   * `User guide <https://google.github.io/pytype/user_guide.html>`_
   * `FAQ <https://google.github.io/pytype/faq.html>`_

Anforderungen
-------------

* Alle gängigen Linux-Distributionen werden unterstützt
* macOS ≥ 10.7 und Xcode ≥ 8
* Windows mit `WSL <https://learn.microsoft.com/en-us/windows/wsl/faq>`_.
  Zusätzlich müssen folgende Bibliotheken installiert werden:

  .. code-block:: console

    $ sudo apt install build-essential python3-dev libpython3-dev

Installation
------------

Pytype kann einfach installiert werden mit

.. code-block:: console

    $ pipenv install pytype

Anschließend kann die Installation überprüft werden mit

.. code-block:: console

    $ pipenv run pytype file_or_directory

Konfiguration
-------------

Für ein Python-Paket könnt ihr Pytype einrichten indem ihr eine
``pytype.cfg``-Datei anlegt mit

.. code-block:: console

    $ pipenv run pytype --generate-config pytype.cfg

Diese beginnt dann :abbr:`z.B. (zum Beispiel)` mit

.. code-block:: ini

    # NOTE: All relative paths are relative to the location of this file.

    [pytype]

    # Space-separated list of files or directories to exclude.
    exclude =
        **/*_test.py
        **/test_*.py

    # Space-separated list of files or directories to process.
    inputs =
        .

Nun könnt ihr die Konfigurationsdatei euren Anforderungen entsprechend ampassen.

Zusätzliche Skripte
-------------------

``annotate-ast``
    in-progress Type-Annotator für ASTs
``merge-pyi``
    Zusammenführen von Typinformationen aus einer ``.pyi``- in eine Python-Datei
``pytd-tool``
    Parser für ``.pyi``-Dateien
``pytype-single``
    Debugging-Tool für Pytype-Entwickler, das eine einzelne Python-Datei unter
    der Annahme analysiert, dass für alle Abhängigkeiten bereits
    ``.pyi``-Dateien generiert wurden
``pyxref``
    cross-References-Generator
