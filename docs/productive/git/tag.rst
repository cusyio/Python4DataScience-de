Git-Tags
========

Git-Tags sind Referenzen, die auf bestimmte Commits in der Git-Historie
verweisen. So können bestimmte Punkte in der Historie für eine bestimmte Version
markiert werden, :abbr:`z.B. (zum Beispiel)` :samp:`v3.9.16`. Tags sind wie
:doc:`branch`, die sich nicht ändern, also keine weitere Historie von Commits
haben.

:samp:`git tag {TAGNAME}`
    erstellt einen Tag, wobei :samp:`{TAGNAME}` eine semantische Bezeichnung für
    den aktuellen Zustand des Git-Repositories ist. Dabei unterscheidet Git zwei
    verschiedene Arten von Tags: annotierte und leichtgewichtige Tags. Sie
    unterscheiden sich in der Menge der zugehörigen Metadaten.

    Annotierte Tags
        Sie speichern nicht nur den :samp:`{TAGNAME}`, sondern auch zusätzliche
        Metadaten wie Namen und E-Mail-Adresse derjenigen Person, die den Tag
        erstellt hat sowie das Datum. Zudem haben annotierte Tags, ähnlich wie
        Commits Nachrichten. Ihr könnt solche Tags erstellen, :abbr:`z.B. (zum
        Beispiel)` mit :samp:`git tag -a {v3.9.16} -m '{Python 3.9.16}'`.
        Anshließend könnt ihr euch diese zusätzlichen Metadaten :abbr:`z.B. (zum
        Beispiel)` anzeigen lassen mit :samp:`git show {v3.9.16}'.

    Leichtgewichtige Tags
        Leichtgewichtige Tags können :abbr:`z.B. (zum Beispiel)` mit :samp:`git
        tag {v3.9.16}` ohne die Optionen :samp:`-a`, :samp:`-s` oder :samp:`-m`
        erstellt werden. Sie erstellen eine Tag-Prüfsumme, die im
        :file:`.git/`-Verzeichnis eures Repos gespeichert werden.

:samp:`git tag`
    listet die Tags eures Repos auf, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: console

        v0.9.9
        v1.0.1
        v1.0.2
        v1.1
        ...

    :samp:`git tag -l '{REGEX}'`
        listet nur Tags auf, die zu einem regulären Ausdruck passen.

:samp:`git tag -a {TAGNAME} {COMMIT-SHA}`
    erstellt einen Tag für einen früheren Commit.

    Die vorangegangenen Beispiele erstellen Tags für implizite Commits, die auf
    ``HEAD`` verweisen. Alternativ kann :samp:`git tag` auch die Referenz auf
    einen bestimmten Commit übergeben werden, die ihr mit :doc:`log` erhaltet.

    Wenn ihr jedoch versucht, ein Tag mit dem gleichen Bezeichner wie ein
    bestehendes Tag zu erstellen, gibt Git eine Fehlermeldung aus, :abbr:`z.B.
    (zum Beispiel)` :samp:`Schwerwiegend: Tag '{v3.9.16}' existiert bereits`.
    Wenn ihr versucht, einen älteren Commit mit einem bestehenden Tag zu
    markieren, gibt Git denselben Fehler aus.

    Für den Fall, dass ihr einen bestehendes Tag aktualisieren müsst, könnt ihr
    die Option ``-f`` verwenden, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: console

        $ git tag -af v3.9.16 595f9ccb0c059f2fb5bf13643bfc0cdd5b55a422 -m 'Python 3.9.16'
        Tag 'v3.9.16' aktualisiert (war 4f5c5473ea)

:samp:`git push origin {TAGNAME}`
    Die Teilen von Tags ist ähnlich wie der Push von Zweigen: standardmäßig
    werden mit :samp:`git push` keine Tags freigegeben, sondern sie müssen
    explizit an :samp:`git push` übergeben werden :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: console

        $ git tag -af v3.9.16 -m 'Python 3.9.16'
        $ git push origin v3.9.16
        Counting objects: 1, done.
        Writing objects: 100% (1/1), 161 bytes, done.
        Total 1 (delta 0), reused 0 (delta 0)
        To git@github.com:python/cpython.git
         * [new tag]         v3.9.16 -> v3.9.16

    Um mehrere Tags gleichzeitig zu pushen, übergebt die Option :samp:`--tags`
    an den Befehl :samp:`git push`. Andere erhalten die Tags bei :samp:`git
    clone` oder :samp:`git pull` des Repos.

:samp:`git checkout {TAGNAME}`
    wechselt in den Zustand des Repos mit diesem Tag und trennt ``HEAD`` ab.
    :abbr:`D.h. (Das heißt)`, dass alle Änderungen, die nun vorgenommen werden,
    das Tag nicht aktualisieren, sondern in einem losgelösten Commit landen, der
    nicht Teil eines Zweiges sein kann und nur direkt über den SHA-Hash des
    Commits erreichbar sein wird. Daher wird meist ein neuer Zweig erstellt,
    wenn solche Änderungen vorgenommen werden sollen, :abbr:`z.B. (zum
    Beispiel)` mit :samp:`git checkout -b v3.9.17 v3.9.16`

:samp:`git tag -d {TAGNAME}`
    löscht einen Tag, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: console

        $ git tag -d v3.9.16
        $ git push origin --delete v3.9.16
