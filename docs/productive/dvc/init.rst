.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Projekt erstellen
=================

DVC lässt sich einfach initialisieren mit:

.. code-block:: console

    $ uv init --package dvc-example
    $ cd dvc-example
    $ git init
    $ git add --all
    $ git commit -m ':tada: Initial commit'
    $ uv add dvc
    $ uv run dvc init
    $ git add pyproject.toml .dvc .dvcignore
    $ git commit -m ":heavy_plus_sign: Add and initialise DVC"

``uv run dvc init``
    erstellt ein Verzeichnis :file:`.dvc/` mit :file:`config`,
    :file:`.gitignore` und :file:`cache`-Verzeichnis.

    Beim ersten Aufruf von ``dvc init`` werdet ihr darüber informiert, dass DVC
    anonymisierte Nutzungsstatistiken erfasst und überträgt. Wenn ihr dies
    deaktivieren möchtet, könnt ihr dies mit dem Befehl ``dvc config`` machen:

    .. code-block:: console

       $ uv run dvc config core.analytics false

    Dadurch wird es für das Projekt deaktiviert. Alternativ könnt ihr die
    Optionen ``--global`` oder ``--system`` von ``dvc config`` verwenden, um die
    Analyse für den aktiven Account :abbr:`bzw. (beziehungsweise)` für alle
    Accounts im System zu deaktivieren.

``git add pyproject.toml .dvc .dvcignore``
    stellt :file:`.dvc/config`, :file:`.dvc/.gitignore` und die aktualisierte
    :file:`pyproject.toml` unter Git-Versionsverwaltung.

Remote Storages konfigurieren
-----------------------------

.. _dvc-remote:

Bevor DVC verwendet wird, sollte noch ein entfernter Speicherplatz (*remote
storage*) eingerichtet werden. Dieser sollte für alle zugänglich sein, die auf
die Daten oder das Modell zugreifen sollen. Es ähnelt der Verwendung eines
Git-Server. Häufig ist das jedoch auch ein NFS-Mount, der :abbr:`z. B. (zum
Beispiel)` folgendermaßen eingebunden werden kann:

.. code-block:: console

    $ mkdir ~/dvc-storage
    $ uv run dvc remote add -d local ~/dvc-storage
    Setting 'local' as a default remote.
    $ git commit .dvc/config -m ":wrench: Configure local remote"
    [main 3e0c8fb] :wrench: Configure local remote
     1 file changed, 4 insertions(+)

``-d``, ``--default``
    Standardwert für den entfernten Speicherplatz
``local``
    Name des entfernten Speicherplatzes
:file:`~/dvc-storage`
    URL des entfernten Speicherplatzes

    Daneben werden noch weitere Protokolle unterstützt, die dem Pfad
    vorangestellt werden, u.a. ``ssh:``, ``hdfs:``, ``https:``.

Es kann also einfach noch ein weiterer entfernter Datenspeicher hinzugefügt
werden, :abbr:`z. B. (zum Beispiel)` mit:

.. code-block:: console

    $ uv run dvc remote add webserver https://dvc.cusy.io/dvc-example

Die zugehörige Konfigurationsdatei :file:`.dvc/config` sieht dann so aus:

.. code-block:: ini

   [core]
       remote = local
   ['remote "local"']
       url = /Users/veit/dvc-storage
   ['remote "webserver"']
       url = https://dvc.cusy.io/dvc-example

.. seealso::
   `Remote Storage
   <https://dvc.org/doc/user-guide/data-management/remote-storage>`_

pre-commit konfigurieren
------------------------

Ihr könnt vor jedem ``git commit`` und ``git push`` sowie nach jedem ``git
checkout`` die von DVC verwalteten Daten mit dem
:doc:`../git/advanced/hooks/pre-commit` überprüfen. Mit ``dvc config
--use-pre-commit-tool`` erhält die :file:`.pre-commit-config.yaml`-Datei
folgende Checks:

.. code-block:: yaml

    - repo: https://github.com/iterative/dvc
      rev: 3.63.0
      hooks:
      - id: dvc-pre-commit
        additional_dependencies:
        - .[all]
        language_version: python3
        stages:
        - pre-commit
      - id: dvc-pre-push
        additional_dependencies:
        - .[all]
        language_version: python3
        stages:
        - pre-push
      - id: dvc-post-checkout
        additional_dependencies:
        - .[all]
        language_version: python3
        stages:
        - post-checkout
        always_run: true

Damit nicht nur der ``pre-commit``-Hook verwendet wird, müsst ihr auch die
``pre-push``- und ``post-checkout``-Hooks aktivieren:

.. code-block:: console

   $ pre-commit install --hook-type pre-commit --hook-type pre-push --hook-type post-checkout
   pre-commit installed at .git/hooks/pre-commit
   pre-commit installed at .git/hooks/pre-push
   pre-commit installed at .git/hooks/post-checkout
