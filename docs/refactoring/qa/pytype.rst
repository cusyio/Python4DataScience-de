Pytype
======

Pytype ist ein statisches Analysewerkzeug, das Typen aus Eurem Python-Code
ableitet ohne dass Typanmerkungen notwendig sind. Es kann jedoch auch im Code
stehende `Type Annotations <https://www.python.org/dev/peps/pep-0484>`_
erzwingen. Obwohl Annotationen für Pytype optional sind, werden sie geprüft und
angewendet, sofern sie vorhanden sind. Die von Pytype erzeugten Typ-Annotationen
werden in eigenständigen ``.pyi``-Dateien gespeichert, die mit `merge-pyi
<https://github.com/google/pytype/tree/master/pytype/tools/merge_pyi>`_ wieder
in den Python eingebunden werden können. Schließlich markiert es häufige Fehler
wie falsch geschriebene Attributnamen oder Funktionsaufrufe und vieles mehr,
auch über Dateigrenzen hinweg.

.. seealso::
   * `Home <https://google.github.io/pytype/>`_
   * `GitHub <https://github.com/google/pytype>`_
   * `PyPI <https://pypi.org/project/pytype/>`_
   * `User guide <https://google.github.io/pytype/user_guide.html>`_
   * `FAQ <https://google.github.io/pytype/faq.html>`_

Anforderungen
-------------

* Alle gängigen Linux-Distributionen werden unterstützt
* MacOS ≥ 10.7 und Xcode ≥ 8
* Windows mit `WSL <https://docs.microsoft.com/en-us/windows/wsl/faq>`_.
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

Für ein Python-Paket könnt Ihr Pytype einrichten indem Ihr eine
``pytype.cfg``-Datei anlegt mit

.. code-block:: console

    $ pipenv run pytype --generate-config pytype.cfg

Diese beginnt dann z.B. mit

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

Nun könnt Ihr die Konfigurationsdatei Euren Anforderungen entsprechend ampassen.

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
