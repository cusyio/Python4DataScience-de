Git Hooks
=========

Git-Hooks sind Skripte, die bei bestimmten Ereignissen in einem Git-Repository
automatisch ausgeführt werden. Sie können sich entweder in lokalen oder
serverseitigen Repositories befinden. So können Git-Repositories individuell
angepasst und benutzerdefinierte Aktionen ausgelöst werden.

Git Hooks befinden sich im Verzeichnis :file:`.git/hooks/`. Beim Anlegen eines
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
.git/{PREPARE-COMMIT-MSG}`.

Die integrierten Skripte sind Shell- und Perl-Skripte, es können jedoch
beliebige Skriptsprachen verwenden werden. Dabei bestimmt die Shebang-Zeile
(:samp:`#!/bin/sh`), wie die Datei interpretiert werden soll.

Die Skripte können jedoch nicht in das serverseitige Repository kopiert werden.

.. toctree::
    :hidden:

    pre-commit
    hooks
    advanced
    template
    ci
