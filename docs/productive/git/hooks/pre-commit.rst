pre-commit-Framework
====================

`pre-commit <https://pre-commit.com/>`_ ist ein Framework zum Verwalten und
Pflegen mehrsprachiger Commit-Hooks.

Eine wesentliche Aufgabe ist es, dem gesamten Entwicklungsteam dieselben Skripte
zur Verfügung zu stellen. `pre-commit <https://pre-commit.com/>`_ von yelp
verwaltet solche Hooks und verteilt sie auf verschiedene Projekte und
Entwickler.

Git Hooks werden meist verwendet um vor Code Reviews automatisch auf Probleme im
Code hinzuweisen, :abbr:`z.B. (zum Beispiel)` um die Formatierung zu überprüfen
oder Debug-Anweisungen zu finden. pre-commit vereinfacht das
projektübergreifende Teilen vom Hooks. Dabei ist auch die Sprache, in der
:abbr:`z.B. (zum Beispiel)` ein Linter geschrieben wurde, wegabstrahiert –
so ist ``scss-lint`` in Ruby geschrieben, ihr könnt ihn jedoch mit pre-commit
verwenden ohne eurem Projekt ein Gemfile hinzufügen zu müssen.

Installation
------------

Bevor ihr die Hooks ausführen könnt, muss das pre-commit Framework installiert
werden:

.. tab:: Windows

   Bevor das pre-commit Framework mit Pipenv installiert werden kann, müssen
   zunächst noch die `Microsoft Build Tools für C++
   <https://visualstudio.microsoft.com/de/visual-cpp-build-tools/>`_
   heruntergeladen und ausgeführt werden damit anschließend die
   *Desktopentwicklung mit C++* ausgewählt und mit den Standardoptionen
   installiert werden kann.

   Erst dann kann das pre-commit Framework installiert werden mit:

   .. code-block:: console

      $ pipenv install pre-commit

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ apt install pre-commit

.. tab:: macOS

   .. code-block:: console

      $ brew install pre-commit

.. tab:: Andere

   .. code-block:: console

      $ pipenv install pre-commit

Überprüfen der Installation :abbr:`z.B. (zum Beispiel)` mit

.. code-block:: console

    $ pipenv run pre-commit -V
    pre-commit 2.21.0

Konfiguration
-------------

Nachdem Pre-Commit installiert ist, können mit der
``.pre-commit-config.yaml``-Datei im Root-Verzeichnis eures Projekts Plugins für
dieses Projekt konfiguriert werden.

.. code-block:: yaml

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files

Ihr könnt euch eine solche initiale ``.pre-commit-config.yaml``-Datei auch
generieren lassen mit

.. code-block:: console

    $ pipenv run pre-commit sample-config > .pre-commit-config.yaml

Wenn ihr ``check-json`` auf eure Jupyter Notebooks anwenden möchtet, müsst ihr
zunächst konfigurieren, dass die Überprüfung auch für den Datei-Suffix
``.ipynb`` verwendet werden soll:

.. code-block:: yaml
   :emphasize-lines: 7-8

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
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

    $ pre-commit install
    pre-commit installed at .git/hooks/pre-commit

Wollt ihr die Git-Hook-Skripte wieder deinstallieren, könnt ihr dies mit
``pre-commit uninstall``.

Ausführen
---------

:samp:`pre-commit run --all-files`
    führt alle pre-commit-Hooks unabhängig von ``git commit`` aus:

    .. code-block:: console

        $ pipenv run pre-commit run --all-files
        Trim Trailing Whitespace.................................................Passed
        Fix End of Files.........................................................Passed
        Check Yaml...............................................................Passed
        Check for added large files..............................................Passed

:samp:`pre-commit run {HOOK}`
    führt einzelne pre-commit-Hooks aus, :abbr:`z.B. (zum Beispiel)`
    :samp:`pre-commit run trailing-whitespace`

.. note::
    Beim ersten Aufruf eines pre-commit-Hooks wird dieser zunächst
    heruntergeladen und anschließend installiert. Dies kann einige Zeit
    benötigen, :abbr:`z.B. (zum Beispiel)` wenn eine Kopie von ``node`` erstellt
    werden muss.

:samp:`pre-commit autoupdate`
    aktualisiert die Hooks automatisch:

    .. seealso::

        * `pre-commit autoupdate [options]
          <https://pre-commit.com/#pre-commit-autoupdate>`_.

Die vom pre-commit-Framework verwalteten Hooks jedoch nicht darauf beschränkt,
vor Commits ausgeführt zu werden; sie können auch für andere Git-Hooks verwendet
werden, siehe :doc:`advanced`.
