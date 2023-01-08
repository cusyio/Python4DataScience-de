Git Hooks
=========

Git-Hooks sind Skripte, die bei bestimmten Ereignissen in einem Git-Repository
automatisch ausgeführt werden. Sie können sich entweder in lokalen oder
serverseitigen Repositories befinden. So können Git-Repositories individuell
angepasst und benutzerdefinierte Aktionen ausgelöst werden.

Git_Hooks befinden sich im Verzeichnis :file:`.git/hooks/`. Beim Anlegen eines
Repository werden dort auch bereits einige Beispielskripte angelegt:

.. code-block:: console

    .git/hooks/
    ├── applypatch-msg.sample
    ├── commit-msg.sample
    ├── fsmonitor-watchman.sample
    ├── post-update.sample
    ├── pre-applypatch.sample
    ├── pre-commit.sample
    ├── pre-merge-commit.sample
    ├── prepare-commit-msg.sample
    ├── pre-push.sample
    ├── pre-rebase.sample
    ├── pre-receive.sample
    └── update.sample

Damit die Skripte ausgeführt werden, muss lediglich der Suffix ``.sample``
entfernt werden und :abbr:`ggf. (gegebenenfalls)` die Dateiberechtigung
ausführbar sein, :abbr:`z.B. (zum Beispiel)` mit :samp:`chmod +x
.git/{prepare-commit-msg}`.

Die integrierten Skripte sind Shell- und Perl-Skripte, es können jedoch
beliebige Skriptsprachen verwenden werden. Die Shebang-Zeile (:samp:`#!/bin/sh`)
bestimmt, wie die Datei interpretiert werden soll.

Sie können jedoch nicht nicht in das serverseitige Repository kopiert werden.

.. _pre-commit-framework:

pre-commit-Framework
--------------------

`pre-commit <https://pre-commit.com/>`_ ist ein Framework zum Verwalten und
Pflegen mehrsprachiger pre-commit-Hooks.

Eine wesentliche Aufgabe ist es, dem gesamten Entwicklungsteam dieselben Skripte
zur Verfügung zu stellen. `pre-commit <https://pre-commit.com/>`_ von yelp
verwaltet solche pre-commit-Hooks und verteilt sie auf verschiedene Projekte und
Entwickler.

Git pre-commit Hooks werden meist verwendet um vor Code Reviews automatisch auf
Probleme im Code hinzuweisen, :abbr:`z.B. (zum Beispiel)` um die Formattierung
zu überprüfen oder Debug-Anweisungen zu finden. Pre-Commit vereinfacht das
projektübergreifende Teilen vom Pre-Commit-Hooks. Dabei ist auch die Sprache, in
der :abbr:`z.B. (zum Beispiel)` ein Linter geschrieben wurde, wegabstrahiert –
so ist ``scss-lint`` in Ruby geschrieben, ihr könnt ihn jedoch mit Pre-Commit
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

.. tab:: macOS

   .. code-block:: console

      $ brew install pre-commit

.. tab:: Python

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
        -   id: check-json
            types: [file]  # override `types: [json]`
            files: \.(json|ipynb)$

Ihr könnt Euch eine initiale ``.pre-commit-config.yaml``-Datei auch generieren
lassen mit

.. code-block:: console

    $ pipenv run pre-commit sample-config
    # See https://pre-commit.com for more information
    # See https://pre-commit.com/hooks.html for more hooks
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.2.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files

:samp:`pre-commit install`
    installiert die pre-commit-Hooks, sodass sie vor jedem ``git commit``
    ausgeführt werden
:samp:`pre-commit run --all-files`
    führt alle pre-commit-Hooks unabhängig von ``git commit`` aus
:samp:`pre-commit run {HOOK}`
    führt einzelne pre-commit-Hooks aus, :abbr:`z.B. (zum Beispiel)`
    :samp:`pre-commit run trailing-whitespace`

.. note::
    Beim ersten Aufruf eines pre-commit-Hooks wird dieser zunächst
    heruntergeladen und anschließend installiert. Dies kann einige Zeit
    benötigen, :abbr:`z.B. (zum Beispiel)` wenn eine Kopie von ``node`` erstellt
    werden muss.

.. code-block:: console

    $ pipenv run pre-commit run --all-files
    Trim Trailing Whitespace.................................................Passed
    Fix End of Files.........................................................Passed
    Check Yaml...............................................................Passed
    Check for added large files..............................................Passed

Eine vollständige Liste der Konfigurationsoptionen erhaltet ihr in `Adding pre-commit
plugins to your project
<https://pre-commit.com/#adding-pre-commit-plugins-to-your-project>`_.

Ihr könnt auch eigene Hooks schreiben, siehe `Creating new hooks
<https://pre-commit.com/#creating-new-hooks>`_.

Ihr könnt die Hooks auch automatisch aktualisieren mit:

.. code-block:: console

    $ pipenv run pre-commit autoupdate

Weitere Optionen findet ihr unter `pre-commit autoupdate [options]
<https://pre-commit.com/#pre-commit-autoupdate>`_.

Installieren der Git-Hook-Skripte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Damit Pre-Commit auch vor jedem Commit zuverlässig ausgeführt wird, werden die
Skripte in unserem Projekt installiert:

.. code-block:: console

    $ pre-commit install
    pre-commit installed at .git/hooks/pre-commit

Verwenden für CI
----------------

Pre-Commit kann auch für kontinuierliche Integration (:abbr:`CI (Continuous
Integration)`) verwendet werden.

.. _gh-action-pre-commit-example:

Beispiele für GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pre-commit ci <https://pre-commit.ci>`_
    Service, der eurem GitHub-Repository die *pre-commit ci*-App in eurem
    Repository unter
    :samp:`https://github.com/{PROFILE}/{REPOSITORY}/installations` hinzufügt.

    Neben der automatischen Änderung von Pull-Requests führt die App auch
    `autoupdate <https://pre-commit.com/#pre-commit-autoupdate>`_ aus, um eure
    Konfiguration aktuell zu halten.

    Weitere Installationen könnt ihr hinzufügen unter `Install pre-commit ci
    <https://github.com/apps/pre-commit-ci/installations/new>`_.

:samp:`.github/workflows/ci.yml`
    Alternative Konfiguration als GitHub-Workflow, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: yaml

        - uses: actions/cache@v3
          with:
            path: ~/.cache/pre-commit
            key: pre-commit|${{ env.pythonLocation }}|${{ hashFiles('.pre-commit-config.yaml') }}

    .. seealso::

        * `pre-commit/action <https://github.com/pre-commit/action>`_

Beispiel für GitLab Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    my_job:
      variables:
        PRE_COMMIT_HOME: ${CI_PROJECT_DIR}/.cache/pre-commit
      cache:
        paths:
          - ${PRE_COMMIT_HOME}

.. seealso::

    Weitere Informationen zur Feinabstimmung des Caching findet ihr in `Good
    caching practices
    <https://docs.gitlab.com/ee/ci/caching/#good-caching-practices>`_.
