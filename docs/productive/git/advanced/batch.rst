Stapelverarbeitung
==================

Alle Dateien in einem Repository
--------------------------------

Gelegentlich kommt es vor, dass alle Dateien in eurem Repository oder
diejenigen, die einem Muster entsprechen, geändert werden sollen. Dies ist durch
die Kombination von `git ls-files <https://git-scm.com/docs/git-ls-files>`_ und
`xargs <https://linux.die.net/man/1/xargs>`_ möglich:

:samp:`$ git ls-files -z | xargs -0 {COMMAND}`
    änder alle Dateien in einem Repository.
:samp:`$ git ls-files -z -- "*.{SUFFIX}" | xargs -0 {COMMAND}`
    ändert nur die Dateien mit einer bestimmten Dateiendung.

    ``-z``, ``-0``
        verwendet das Null-Byte-Trennzeichen.

Beispiel
~~~~~~~~

To execute commands for the changed file list, you can use the shell `Command
Substitution
<https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html>`_:

:samp:`$ uv run codespell $(git list-changed '*.py')`
    Die Shell führt das ``git list-changed`` in Klammern aus und fügt dessen
    Ausgabe in den äußeren Befehl ein. ``codespell`` erhält also die Liste der
    geänderten Textdateien als Argument.
:samp:`uv run pytest $(git diff --staged --name-only "tests/*test_*.py")`
    ändert für alle Dateien mit dem Suffix ``.py`` ggf. die Berechtigungen von
    ``100644`` zu ``100755``, sodass sie ausführbar werden.

.. _git-name-only:

Alle im Arbeits- oder Bühnenbereich geänderten Dateien
------------------------------------------------------

:samp:`git diff --name-only`
    gibt diejenigen Dateien aus, die von Git verwaltet werden und im
    Arbeitsbereich geändert wurden.
:samp:`git diff --staged --name-only`
    gibt die dem Bühnenbereich hinzugefügten Dateien aus.
:samp:`git diff --staged --name-only "*.{SUFFIX}"`
    filtert darüberhinaus noch nach einer bestimmten Dateiendung.

.. _list-changed:

:samp:`git diff --name-only --diff-filter d`
    schließt gelöschte Dateien aus.

    Dies ist bei mir der häufigste Fall, weswegen ich mir hierfür einen Alias
    ``list-changed`` angelegt habe: ``git config --global alias.list-changed
    'diff --name-only --diff-filter d'``.

Beispiel
~~~~~~~~

Um Befehle für die geänderte Dateiliste auszuführen, könnt ihr die
Shell-`Command Substitution
<https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html>`_
verwenden:

:samp:`$ uv run codespell $(git list-changed '*.py')`
    Die Shell führt das in Klammern gesetzte ``git list-changed`` aus und fügt
    dessen Ausgabe in den äußeren Befehl ein. ``codespell`` erhält also die
    Liste der geänderten Textdateien als Argument.
:samp:`uv run pytest $(git diff --staged --name-only "tests/*test_*.py")`
    ruft :doc:`python-basics:test/pytest/index` auf, um anschließend nur
    diejenigen Testmodule auszuführen, die im Arbeitsverzeichnis geändert
    wurden.
