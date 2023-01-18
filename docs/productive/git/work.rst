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
    lädt ein Projekt mit allen Zweigen (engl.: *branches*) und der gesamten
    Historie vom entfernten Repository herunter

    ``--depth``
        gibt die Anzahl der Commits an, die heruntergeladen werden sollen

    ``-b`` (Langform: ``--branch``)
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
    zeigt Unterschiede zwischen Arbeits- und Bühnenbereich, :abbr:`z.B. (zum
    Beispiel)`.

    .. code-block:: console

        $ git diff docs/productive/git/work.rst
        diff --git a/docs/productive/git/work.rst b/docs/productive/git/work.rst
        index e2a5ea6..fd84434 100644
        --- a/docs/productive/git/work.rst
        +++ b/docs/productive/git/work.rst
        @@ -46,7 +46,7 @@

         :samp:`$ git diff {FILE}`
        -    zeigt Unterschiede zwischen Arbeits- und Bühnenbereich.
        +    zeigt Unterschiede zwischen Arbeits- und Bühnenbereich, :abbr:`z.B. (zum Beispiel)`.

    ``index e2a5ea6..fd84434 100644`` zeigt einige interne Git-Metadaten an, die
    ihr vermutlich nie benötigen werdet. Die Zahlen entsprechen den
    Hash-Kennungen der Git-Objektversionen.

    Die übrige Ausgabe ist eine Liste von :abbr:`sog. (sogenannten)` *diff
    chunks*, deren Header von ``@@``-Symbolen eingeschlossen ist. Er gibt eine
    Zusammenfassung der in der Datei vorgenommenen Änderungen. In unserem
    Beispiel wurden 7 Zeilen ab Zeile 46 extrahiert und 7 Zeilen ab Zeile 46
    hinzugefügt.

    Standardmäßig führt ``git diff`` den Vergleich gegen ``HEAD`` aus. Wenn ihr
    im obigen Beispiel ``git diff HEAD docs/productive/git/work.rst`` verwendet,
    hat das denselben Effekt.

    Mit ``git diff`` können Git-Referenzen auf Commits an ``diff`` übergeben
    werden. Neben ``HEAD`` sind einige weitere Beispiele für Referenzen Tags und
    Zweignamen, :abbr:`z.B. (zum Beispiel)` :samp:`git
    diff {MAIN}..{FEATURE_BRANCH}`. Der Punkt-Operator in diesem Beispiel zeigt
    an, dass die ``diff``-Eingabe die Spitzen der beiden Zweige sind. Der
    gleiche Effekt tritt ein, wenn die Punkte weggelassen werden und ein
    Leerzeichen zwischen den Zweigen verwendet wird. Zusätzlich gibt es einen
    Operator mit drei Punkten: :samp:`git diff {MAIN}...{FEATURE_BRANCH}`, der
    ein Diff initiiert, bei dem der erste Eingabeparammeter :samp:`{MAIN}` so
    geändert wird, dass die Referenz der gemeinsame Vorfahre von :samp:`MAIN`
    und :samp:`FEATURE` ist.

    Jeder Commit in Git hat eine Commit-ID, die ihr erhalten könnt, wenn ihr
    ``git log`` ausführt. Anschließend könnt ihr diese Commit-ID auch an ``git
    diff`` übergeben:

    .. code-block:: console

        $ git log --pretty=oneline 
        af1a395a08221ffa83b46f562b6823cf044a108c (HEAD -> main, origin/main, origin/HEAD) :memo: Add some git diff examples
        d650de52306b63b93e92bba4f15be95eddfea425 :memo: Add „Debug .gitignore files“ to git docs
        …
        $ git diff af1a395a08221ffa83b46f562b6823cf044a108c d650de52306b63b93e92bba4f15be95eddfea425

    ``--staged``, ``--cached``
        zeigt Unterschiede zwischen Bühnenbereich und Repository an.
    ``--word-diff``
        zeigt die geänderten Wörter an.

:samp:`$ git restore {FILE}`
    ändert Dateien im Arbeitsverzeichnis in einen Zustand, der Git zuvor bekannt
    war. Standardmäßig checkt Git ``HEAD``, den letzten Commit des aktuellen
    Zweigs, aus.

    .. note::

        In Git < 2.23 steht euch ``git restore`` noch nicht zur Verfügung. In
        diesem Fall müsst ihr noch ``git checkout`` verwenden:

        :samp:`$ git checkout {FILE}`

``$ git commit``
    einen neuen Commit mit den hinzugefügten Änderungen machen.

    :samp:`-m '{COMMIT_MESSAGE}'`
        direkt in der Kommandozeile eine Commit-Message schreiben.
    ``--dry-run --short``
        zeigt, was committet werden würde mit dem Status im Kurzformat.

``$ git reset [--hard|--soft] [target-reference]``
    setzt die Historie auf einen früheren Commit zurück.
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
        | ``y``         | Diese Änderung verstecken                     |
        +---------------+-----------------------------------------------+
        | ``n``         | Diese Änderung nicht in das Versteck          |
        |               | übernehmen                                    |
        +---------------+-----------------------------------------------+
        | ``q``         | Nur die bereits ausgewählten Änderungen werden|
        |               | in das Versteck übernommen                    |
        +---------------+-----------------------------------------------+
        | ``a``         | Diese und alle folgenden Änderungen übernehmen|
        +---------------+-----------------------------------------------+
        | ``e``         | Diese Änderung manuell editieren              |
        +---------------+-----------------------------------------------+
        | ``?``         | Hilfe                                         |
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
