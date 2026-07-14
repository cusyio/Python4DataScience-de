.. SPDX-FileCopyrightText: 2023 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

prek
====

`prek <https://prek.j178.dev>`_ ist eine in Rust geschriebene Variante von
`pre-commit <https://pre-commit.com/>`_ zum Verwalten und Pflegen mehrsprachiger
Commit-Hooks.

Eine wesentliche Aufgabe ist es, dem gesamten Entwicklungsteam dieselben Skripte
zur Verfügung zu stellen. pre-commit von yelp verwaltet solche Hooks und
verteilt sie auf verschiedene Projekte und Entwickler.

Git Hooks werden meist verwendet um vor Code Reviews automatisch auf Probleme im
Code hinzuweisen, :abbr:`z. B. (zum Beispiel)` um die Formatierung zu überprüfen
oder Debug-Anweisungen zu finden. pre-commit vereinfacht das
projektübergreifende Teilen vom Hooks. Dabei ist auch die Sprache, in der
:abbr:`z. B. (zum Beispiel)` ein Linter geschrieben wurde, wegabstrahiert –
so ist ``scss-lint`` in Ruby geschrieben, ihr könnt ihn jedoch mit pre-commit
verwenden ohne eurem Projekt ein Gemfile hinzufügen zu müssen.

Installation
------------

Bevor ihr die Hooks ausführen könnt, muss prek installiert werden:

.. tab:: Windows

   .. code-block:: console

      > powershell -ExecutionPolicy ByPass -c "irm https://github.com/j178/prek/releases/download/v0.4.9/prek-installer.ps1 | iex"

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ curl --proto '=https' --tlsv1.2 -LsSf https://github.com/j178/prek/releases/download/v0.4.9/prek-installer.sh | sh

.. tab:: macOS

   .. code-block:: console

      $ brew install prek

.. tab:: Andere

   .. code-block:: console

      $ uv add --group dev prek

Überprüfen der Installation :abbr:`z.B. (zum Beispiel)` mit

.. code-block:: console

    $ uv run prek -V
    prek 0.4.9 (42b79a57f 2026-07-11)

Konfiguration
-------------

Nachdem Pre-Commit installiert ist, können mit der
``.pre-commit-config.yaml``-Datei im Root-Verzeichnis eures Projekts Plugins für
dieses Projekt konfiguriert werden.

.. code-block:: yaml

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: 3e8a8703264a2f4a69428a0aa4dcb512790b2c8c # v6.0.0
        hooks:
        - id: trailing-whitespace
        - id: end-of-file-fixer
        - id: check-yaml
        - id: check-added-large-files

Ihr könnt euch eine solche initiale ``.pre-commit-config.yaml``-Datei auch
generieren lassen mit

.. code-block:: console

    $ uv run prek sample-config > .pre-commit-config.yaml

Wenn ihr ``check-json`` auf eure Jupyter Notebooks anwenden möchtet, müsst ihr
zunächst konfigurieren, dass die Überprüfung auch für den Datei-Suffix
``.ipynb`` verwendet werden soll:

.. code-block:: yaml
   :emphasize-lines: 7-8

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: 3e8a8703264a2f4a69428a0aa4dcb512790b2c8c # v6.0.0
        hooks:
        …
        - id: check-json
          types: [file]
          files: \.(json|ipynb)$

.. seealso::

    Eine vollständige Liste der Konfigurationsoptionen erhaltet ihr in `Adding
    pre-commit plugins to your project
    <https://pre-commit.com/#adding-pre-commit-plugins-to-your-project>`_.

    Ihr könnt auch eigene Hooks schreiben, siehe `Creating new hooks
    <https://pre-commit.com/#creating-new-hooks>`_.

Installieren der Git-Hook-Skripte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit Pre-Commit auch vor jedem Commit zuverlässig ausgeführt wird, wird das
Skript in unserem Projekt installiert:

.. code-block:: console

    $ prek install
    prek installed at .git/hooks/pre-commit

Wollt ihr die Git-Hook-Skripte wieder deinstallieren, könnt ihr dies mit
``prek uninstall``.

Ausführen
---------

:samp:`uv run prek run --all-files`
    führt alle prek-Checks unabhängig von ``git commit`` aus:

    .. code-block:: console

        $ uv run prek run --all-files
        Trim Trailing Whitespace.................................................Passed
        Fix End of Files.........................................................Passed
        Check Yaml...............................................................Passed
        Check for added large files..............................................Passed

:samp:`uv run prek run {HOOK}`
    führt einzelne prek-Checks aus, :abbr:`z. B. (zum Beispiel)` :samp:`prek run
    trailing-whitespace`

.. note::
   Beim ersten Aufruf eines prek-Checks wird dieser zunächst heruntergeladen und
   anschließend installiert. Dies kann einige Zeit benötigen, :abbr:`z. B. (zum
   Beispiel)` wenn eine Kopie von ``node`` erstellt  werden muss.

:samp:`prek update [OPTIONS]`
    aktualisiert die Hooks automatisch, :abbr:`z. B. (zum Beispiel)`:

    .. code-block:: console

       $ uv run prek update --freeze --cooldown-days 7
       https://github.com/pre-commit/pre-commit-hooks
         updating rev `v6.0.0` -> `3e8a8703264a2f4a69428a0aa4dcb512790b2c8c` (frozen: v6.0.0)

Die von prek verwalteten Hooks sind jedoch nicht darauf beschränkt, vor Commits
ausgeführt zu werden; sie können auch für andere Git-Hooks verwendet werden,
siehe :doc:`hooks`.
