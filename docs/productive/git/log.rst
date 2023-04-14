Git Log
=======

:samp:`$ git log [-n {COUNT}]`
    auflisten der Commit-Historie des aktuellen Zweiges.

    ``-n``
        beschränkt die Anzahl der Commits auf die angegebene Zahl.

:samp:`$ git log [--after="{YYYY-MM-DD}"] [--before="{YYYY-MM-DD}"]`
    Commit-Historie gefiltert nach Datum.

    Auch relative Angaben wie ``1 week ago`` oder ``yesterday`` sind zulässig.

:samp:`$ git log --author="{VEIT}"`
    filtert die Commit-Historie nach Autor*innen.

    Es kann auch nach mehreren Autor*innen gleichzeitig gesucht werden,
    :abbr:`z.B. (zum Beispiel)`:

    :samp:`$ git log --author="{VEIT\|VSC}"`

:samp:`$ git log --grep = "{TERM}"`
    filtert die Commit-Historie nach regulären Ausdrücken in der
    Commit-Nachricht.

:samp:`$ git log -S"{FOO}"`
    filtert Commits nach bestimmten Zeilen im Quellcode.

:samp:`$ git log -G"{BA*}"`
    filtert Commits nach regulären Ausdrücken im Quellcode.

:samp:`$ git log -- {PATH/TO/FOO.PY}`
    filtert die Commit-Historie nach bestimmten Dateien.

:samp:`$ git log {MAIN}..{FEATURE}`
    filtert nach unterschiedlichen Commits in verschiedenen Zweigen (Branches),
    in unserem Fall zwischen den Branches :samp:`MAIN` und :samp:`FEATURE`.

:samp:`$ git log --oneline --graph --decorate`
    anzeigen des Verlaufsdiagramms mit Referenzen, ein Commit pro Zeile.

:samp:`$ git log {REF}..`
    Commits auflisten, die im aktuellen Zweig vorhanden sind und nicht in
    :samp:`{REF}` zusammengeführt werden. :samp:`{REF}` kann dabei der Name
    eines Zweigs oder eines Tag sein.

:samp:`$ git log ..{REF}`
    Commits auflisten, die in :samp:`{REF}` vorhanden sind und nicht mit dem
    aktuellen Zweig zusammengeführt werden.

:samp:`$ git reflog`
    Vorgänge (:abbr:`z.B. (zum Beispiel)` ``switch`` oder ``commit``) auflisten,
    die im lokalen Repository ausgeführt wurden.

.. seealso::
   * `Git’s Database Internals III: File History Queries
     <https://github.blog/2022-08-31-gits-database-internals-iii-file-history-queries/>`_
