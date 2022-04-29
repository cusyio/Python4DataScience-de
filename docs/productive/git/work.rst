Mit Git arbeiten
================

Die Arbeit an einem Projekt beginnen
------------------------------------

Ein eigenes Projekt starten
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ git init [my_project]``
    erstellt ein neues, lokales Git-Repository

    ``[my_project]``
        wenn der Projektname angegeben wird, erzeugt Git ein neues Verzeichnis
        und initialisiert es

        Wird kein Projektname angegeben, wird das aktuelle Verzeichnis
        initialisiert

An einem Projekt mitarbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ git clone [project_url]``
    lädt ein Projekt mit allen Zweigen (engl.: branches) und der gesamten
    Historie vom entfernten Repository herunter

    ``--depth``
        gibt die Anzahl der Commits an, die heruntergeladen werden sollen

    ``-b``
        gibt den Namen des entfernten Zweigs an, der heruntergeladen werden soll

An einem Projekt arbeiten
-------------------------

``$ git status``
    zeigt den Status des aktuellen Zweiges im Arbeitsverzeichnisses an mit
    neuen, geänderten und bereits zum Commit vorgemerkten Dateien.
``$ git add [file]``
    fügt eine Datei dem Bühnenbereich hinzu.

    ``-p``
        fügt Teile einer Datei dem Bühnenbereich hinzu.
    ``-e``
        die zu übernehmenden Änderungen können im Standardeditor bearbeitet
        werden.

``$ git diff [file]``
    zeigt Unterschiede zwischen Arbeits- und Bühnenbereich.

    ``--staged``
        zeigt Unterschiede zwischen Bühnenbereich und Repository an.
    ``--word-diff``
        zeigt die geänderten Wörter an.

``$ git checkout -- [file]``
    unwiderruflich Änderungen im Arbeitsbereich verwerfen.
``$ git commit``
    einen neuen Commit mit den hinzugefügten Änderungen machen.

    ``-m 'Commit message'``
        direkt in der Kommandozeile eine Commit-Message schreiben.
    ``--dry-run --short``
        zeigt, was committet werden würde mit dem Status im Kurzformat.

``$ git reset [file]``
    zurückkehren zur aktuellen Datei aus dem Bühnenbereich.
``$ git rm [file]``
    entfernen einer Datei aus dem Arbeits- und Bühnenbereich.
``$ git stash``
    verschieben der aktuellen Änderungen aus dem Arbeitsbereich in das Versteck
    (engl.: *stash*).

    Um eure versteckten Änderungen möglichst gut unterscheiden zu können,
    empfehlen sich die folgenden beiden Optionen:

    ``-p``
        erlaubt euch, Änderungen partiell zu verstecken.

        ``-p`` oder ``--patch``
            zeigt die Unterschiede detailliert an, :abbr:`z.B. (zum Beispiel)`:

            .. code-block:: console

                $ git show -p
                diff --git a/docs/productive/git/work.rst b/docs/productive/git/work.rst
                index cff338e..1988ab2 100644
                --- a/docs/productive/git/work.rst
                +++ b/docs/productive/git/work.rst
                @@ -83,7 +83,16 @@ An einem Projekt arbeiten
                     ``list``
                         listet die versteckten Änderungen auf.
                     ``show``
                -        zeigt die Änderungen in den versteckten Dateien an.
                +        zeigt die Änderungen in den versteckten Dateien an, :abbr:`z.B. (zum
                +        Beispiel)`
                +
                +        .. code-block:: console
                +
                +            $ git show
                +             index.rst | 1 +
                +             work.rst | 3 +++
                +             2 files changed, 4 insertions(+)
                +
                     ``pop``
                         übernimmt Änderungen aus dem Versteck in den Arbeitsbereich und leert
                         das Versteck, :abbr:`z.B. (zum Beispiel)`
                (1/1) Stash this hunk [y,n,q,a,d,e,?]? y

        Mit ``?`` erhaltet ihr eine vollständige Liste der Optionen. Die
        gebräuchlichsten sind:

        +---------------+-----------------------------------------------+
        | Befehl        | Beschreibung                                  |
        +===============+===============================================+
        | ``/``         | sucht nach einer Änderung mit einem regulären |
        |               | Ausdruck                                      |
        +---------------+-----------------------------------------------+
        | ``?``         | Hilfe                                         |
        +---------------+-----------------------------------------------+
        | ``n``         | Diese Änderung nicht übernehmen               |
        +---------------+-----------------------------------------------+
        | ``q``         | Alle bereits ausgewählten Änderungen werden   |
        |               | gespeichert                                   |
        +---------------+-----------------------------------------------+
        | ``s``         | Diese Änderungen aufteilen                    |
        +---------------+-----------------------------------------------+
        | ``y``         | Diese Änderung verstecken                     |
        +---------------+-----------------------------------------------+

    ``branch``
        erstellt aus versteckten Dateien einen Zweig, :abbr:`z.B. (zum
        Beispiel)`:

        .. code-block:: console

            $ git stash branch stash-example stash@{0}
            Auf Branch stash-example
            Zum Commit vorgemerkte Änderungen:
              (benutzen Sie "git restore --staged <Datei>..." zum Entfernen aus der Staging-Area)
                neue Datei:     docs/productive/git/work.rst

            Änderungen, die nicht zum Commit vorgemerkt sind:
              (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
              (benutzen Sie "git restore <Datei>...", um die Änderungen im Arbeitsverzeichnis zu verwerfen)
                geändert:       docs/productive/git/index.rst

            stash@{0} (6565fdd1cc7dff9e0e6a575e3e20402e3881a82e) gelöscht

    ``save MESSAGE``
        fügt den Änderungen eine Nachricht hinzu.
    ``-u UNTRACKED_FILE``
        versteckt unversionierte Dateien.
    ``list``
        listet die versteckten Änderungen auf.
    ``show``
        zeigt die Änderungen in den versteckten Dateien an.
    ``pop``
        übernimmt Änderungen aus dem Versteck in den Arbeitsbereich und leert
        das Versteck, :abbr:`z.B. (zum Beispiel)`

        .. code-block:: console

            $ git stash pop stash@{2}

    ``drop``
        leeren eines spezifischen Verstecks, :abbr:`z.B. (zum Beispiel)`:

        .. code-block:: console

            $ git stash drop stash@{0}
            stash@{0} (defcf56541b74a1ccfc59bc0a821adf0b39eaaba) gelöscht
