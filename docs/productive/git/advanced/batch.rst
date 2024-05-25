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

:samp:`$ git ls-files -z -- "*.py" | xargs -0 git update-index --chmod=+x`
    ändert für alle Dateien mit dem Suffix ``.py`` ggf. die Berechtigungen von
    ``100644`` zu ``100755``, sodass sie ausführbar werden.

Alle im Arbeits- oder Bühnenbereich geänderten Dateien
------------------------------------------------------

:samp:`git diff --name-only`
    gibt diejenigen Dateien aus, die von Git verwaltet werden und im
    Arbeitsbereich geändert wurden.
:samp:`git diff --staged --name-only`
    gibt die dem Bühnenbereich hinzugefügten Dateien aus.
:samp:`git diff --staged --name-only "*.{SUFFIX}"`
    filtert darüberhinaus noch nach einer bestimmten Dateiendung.

Beispiel
~~~~~~~~

:samp:`pytest $(git diff --staged --name-only "tests/test_*.py")`
    ruft :doc:`python-basics:test/pytest/index` auf, um anschließend nur
    diejenigen Testmodule auszuführen, die im Arbeitsverzeichnis geändert
    wurden.
