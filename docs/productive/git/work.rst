Mit Git arbeiten
================

Die Arbeit an einem Projekt beginnen
------------------------------------

Ein eigenes Projekt starten
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:samp:`$ git init {MY_PROJECT}`
    erstellt ein neues, lokales Git-Repository

    :samp:`{MY_PROJECT}`
        wenn der Projektname angegeben wird, erzeugt Git ein neues Verzeichnis
        und initialisiert es

        Wird kein Projektname angegeben, wird das aktuelle Verzeichnis
        initialisiert

An einem Projekt mitarbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:samp:`$ git clone {PROJECT_URL}`
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
:samp:`$ git add {FILE}`
    fügt eine Datei dem Bühnenbereich hinzu.

    ``-p``
        fügt Teile einer Datei dem Bühnenbereich hinzu.
    ``-e``
        die zu übernehmenden Änderungen können im Standardeditor bearbeitet
        werden.

:samp:`$ git diff {FILE}`
    zeigt Unterschiede zwischen Arbeits- und Bühnenbereich.

    ``--staged``
        zeigt Unterschiede zwischen Bühnenbereich und Repository an.
    ``--word-diff``
        zeigt die geänderten Wörter an.

:samp:`$ git checkout -- {FILE}`
    unwiderruflich Änderungen im Arbeitsbereich verwerfen.
``$ git commit``
    einen neuen Commit mit den hinzugefügten Änderungen machen.

    :samp:`-m '{COMMIT_MESSAGE}'`
        direkt in der Kommandozeile eine Commit-Message schreiben.
    ``--dry-run --short``
        zeigt, was committet werden würde mit dem Status im Kurzformat.

:samp:`$ git reset {FILE}`
    zurückkehren zur aktuellen Datei aus dem Bühnenbereich.
:samp:`$ git rm {FILE}`
    entfernen einer Datei aus dem Arbeits- und Bühnenbereich.
``$ git stash``
    verschieben der aktuellen Änderungen aus dem Arbeitsbereich in das Versteck
    (engl.: *stash*).

    Um eure versteckten Änderungen möglichst gut unterscheiden zu können,
    empfehlen sich die folgenden beiden Optionen:

    ``-p`` oder ``--patch``
        erlaubt euch, Änderungen partiell zu verstecken, :abbr:`z.B. (zum
        Beispiel)`:

        .. code-block:: console

            $ git stash -p
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
            …
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

    :samp:`save {MESSAGE}`
        fügt den Änderungen eine Nachricht hinzu.
    :samp:`-u {UNTRACKED_FILE}`
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

    ``clear``
        löscht alle eure Verstecke.
