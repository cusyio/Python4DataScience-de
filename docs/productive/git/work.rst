.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Mit Git arbeiten
================

Die Arbeit an einem Projekt beginnen
------------------------------------

.. _git-init:

Ein eigenes Projekt starten
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:samp:`$ git init {PROJECT}`
    erstellt ein neues, lokales Git-Repository.

    :samp:`{PROJECT}`
        wenn der Projektname angegeben wird, erzeugt Git ein neues Verzeichnis
        und initialisiert es.

        Wird kein Projektname angegeben, wird das aktuelle Verzeichnis
        initialisiert.

    .. tip::
       Der Standardzweig in Git ist ``master``. Da dieser Begriff jedoch
       `für manche Menschen verletzend ist
       <https://sfconservancy.org/news/2020/jun/23/gitbranchname/>`_, lässt sich
       in Git ≥ 2.28 der Standard-Zweigname konfigurieren:

       .. code-block:: console

          $ git config --global init.defaultBranch main

    Die meisten Git-Hosts verwenden ebenfalls *main* als Standard für neue
    Repositories.

An einem Projekt mitarbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:samp:`$ git clone {SOURCE}`
    lädt ein Projekt mit allen Zweigen (engl.: *branches*) und der gesamten
    Historie vom entfernten Repository herunter, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: console

       $ git clone https://github.com/cusyio/Python4DataScience.git

    oder

    .. code-block:: console

       $ git clone git@github.com:cusyio/Python4DataScience.git

    ``git clone --depth``
        gibt die Anzahl der Commits an, die heruntergeladen werden sollen.

    ``git clone -b|--branch``
        gibt den Namen des entfernten Zweigs an, der heruntergeladen werden
        soll.

An einem Projekt arbeiten
-------------------------

``$ git status``
    zeigt den Status des aktuellen Zweiges im Arbeitsverzeichnisses an mit
    neuen, geänderten und bereits zum Commit vorgemerkten Dateien.

    ``git status -v``
        zeigt die Änderungen im Bühnenbereich als Diff an.
    ``git status -vv``
        zeigt auch die Änderungen im Arbeitsverzeichnis als zweites Diff an.

    .. seealso::
       `git status -v
       <https://git-scm.com/docs/git-status#Documentation/git-status.txt--v>`_

    ``git status -s|--short``
        zeigt den Status im Kurzformat an, :abbr:`z.B. (zum Beispiel)`:

        .. code-block:: console

           $ git status -s
            M docs/productive/git/work.rst
           ?? Python4DataScience.txt

        Die vorangestellten Buchstaben geben den Zustand der Datei an.

    ``git status`` gibt viele Ratschläge, was mit den Dateien in den einzelnen
    Zuständen geschehen soll:

    .. code-block:: console

       $ git status
       Auf Branch main
       Ihr Branch und 'origin/main' sind divergiert,
       und haben jeweils 1 und 1 unterschiedliche Commits.
         (verwenden Sie "git pull", wenn Sie den Remote-Branch in Ihren integrieren wollen)

       Änderungen, die nicht zum Commit vorgemerkt sind:
         (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
         (benutzen Sie "git restore <Datei>...", um die Änderungen im Arbeitsverzeichnis zu verwerfen)
           geändert:       docs/productive/git/work.rst

       Unversionierte Dateien:
         (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
           Python4DataScience.txt

       keine Änderungen zum Commit vorgemerkt (benutzen Sie "git add" und/oder "git commit -a")

    .. _git-statushints:

    Wenn ihr mit Git vertraut seid, werdet ihr diese Hinweise vielleicht als
    unnötig empfinden. Dann könnt ihr diese Meldungen mit der Option
    ``advice.statusHints`` deaktivieren:

    .. code-block:: console

       $ git config --global advice.statusHints false

    Von nun an zeigt der Aufruf von ``git status`` keine Hinweise mehr an:

    .. code-block:: console

       $ git status
       Auf Branch main
       Ihr Branch und 'origin/main' sind divergiert,
       und haben jeweils 1 und 1 unterschiedliche Commits.

       Änderungen, die nicht zum Commit vorgemerkt sind:
           geändert:       docs/productive/git/work.rst

       Unversionierte Dateien:
           Python4DataScience.txt

       keine Änderungen zum Commit vorgemerkt

    Auch beim Aufruf von ``git-switch``  und ``git-checkout`` sowie beim
    Schreiben von Commit-Nachrichten werden nun keine Hinweise mehr angezeigt.

    .. tip::
       Es gibt zwar noch viele andere `advice.*
       <https://git-scm.com/docs/git-config#Documentation/git-config.txt-advice>`_-Optionen,
       die meisten davon sind jedoch ziemlich unbedeutend, so dass sie erst
       ausgeschlossen werden sollten, wenn sie anfangen zu stören.

:samp:`$ git add {PATH}`
    fügt eine oder mehrere Dateien dem Bühnenbereich hinzu.

    ``git add -p``
        fügt Teile einer oder mehrerer Dateien dem Bühnenbereich hinzu.
    ``git add -e``
        die zu übernehmenden Änderungen können im Standardeditor bearbeitet
        werden.

:samp:`$ git diff {PATH}`
    zeigt Unterschiede zwischen Arbeits- und Bühnenbereich, :abbr:`z.B. (zum
    Beispiel)`:

    .. code-block:: console

       $ git diff docs/productive/git/work.rst
       diff --git a/docs/productive/git/work.rst b/docs/productive/git/work.rst
       index e2a5ea6..fd84434 100644
       --- a/docs/productive/git/work.rst
       +++ b/docs/productive/git/work.rst
       @@ -46,7 +46,7 @@

        :samp:`$ git diff {PATH}`
       -    zeigt Unterschiede zwischen Arbeits- und Bühnenbereich.
       +    zeigt Unterschiede zwischen Arbeits- und Bühnenbereich, :abbr:`z.B. (zum Beispiel)`.

    Git erweitert das Diff-Format standardmäßig um die Präfixe ``a/`` und ``b/``
    vor den Dateipfaden.

    .. tip::
       Diese Präfixe sollen dazu dienen, die Pfade als *alt* und *neu* zu
       kennzeichnen, aber die verhindern, dass die Dateipfade einfach kopiert
       werden können – manche Terminals erlauben auch, Dateipfade anzuklicken,
       um sie zu öffnen – aber die Präfixe verhindern dies. Mit einer neuen
       Funktion in Git 2.45 könnt ihr dies ändern:

       .. code-block:: console

          $ git config --global diff.srcPrefix './'
          $ git config --global diff.dstPrefix './'

    ``index e2a5ea6..fd84434 100644`` zeigt einige interne Git-Metadaten an, die
    ihr vermutlich nie benötigen werdet. Die Zahlen entsprechen den
    Hash-Kennungen der Git-Objektversionen.

    Die übrige Ausgabe ist eine Liste von :abbr:`sog. (sogenannten)` *diff
    chunks*, deren Header von ``@@``-Symbolen eingeschlossen ist. Jeder *diff
    chunk* zeigt in einer Datei vorgenommene Änderungen. In unserem Beispiel
    wurden 7 Zeilen ab Zeile 46 extrahiert und 7 Zeilen ab Zeile 46 hinzugefügt.

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
    geändert wird, dass die Referenz der gemeinsame Vorfahre von :samp:`{MAIN}`
    und :samp:`{FEATURE}` ist.

    Jeder Commit in Git hat eine Commit-ID, die ihr mittels ``git log`` erhaltet.
    Anschließend könnt ihr diese Commit-ID auch an ``git diff`` übergeben:

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

    .. seealso::
       * :ref:`git-name-only`

:samp:`$ git restore {FILE}`
    ändert Dateien im Arbeitsverzeichnis in einen Zustand, der Git zuvor bekannt
    war. Standardmäßig checkt Git ``HEAD``, den letzten Commit des aktuellen
    Zweigs, aus.

    .. note::

        In Git < 2.23 steht euch ``git restore`` noch nicht zur Verfügung. In
        diesem Fall müsst ihr noch ``git checkout`` verwenden:

        :samp:`$ git checkout {FILE}`

``$ git commit``
    macht einen neuen Commit mit den hinzugefügten Änderungen.

    :samp:`git commit -m '{COMMIT_MESSAGE}'`
        schreibt direkt in der Kommandozeile eine Commit-Message.
    ``--dry-run --short``
        zeigt, was committet werden würde mit dem Status im Kurzformat.
    :samp:`git commit -m '{FILE}'`
        übergibt Dateinamen oder `Globbing
        <https://de.wikipedia.org/wiki/Wildcard_(Informatik)>`_-Muster an ``git
        commit``, um Änderungen an diesen Dateien zu übertragen, wobei alle
        Änderungen übersprungen werden, die mit ``git add`` bereits in der
        Staging-Area vorhanden sind.

:samp:`$ git reset [--hard|--soft] [{TARGET_REFERENCE}]`
    setzt die Historie auf einen früheren Commit zurück.
:samp:`$ git rm {PATH}`
    entfernt eine Datei namens :samp:`{PATH}` aus dem Arbeits- und
    Bühnenbereich.

.. _git-stash:

``$ git stash``
    verschiebt die aktuellen Änderungen aus dem Arbeitsbereich in das Versteck
    (:abbr:`engl. (englisch)`: *stash*).

    .. _git-autostash:

    Ihr könnt auch automatisch Stash für Merge und Rebase anwenden:

    .. code-block:: console

       $ git config --global merge.autoStash true
       $ git config --global rebase.autoStash true

    Um eure versteckten Änderungen möglichst gut unterscheiden zu können,
    empfehlen sich die folgenden beiden Optionen:

    ``git stash -p|--patch``
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

        .. _git-singlekey:

        .. tip::
           Normalerweise müsst ihr nach jedem Befehl, der einen Buchstaben
           enthält, die Taste ︎:kbd:`↩︎` drücken. Ihr könnt diesen Overhead jedoch
           abschalten:

           .. code-block:: console

              $ git config --global interactive.singleKey true

    :samp:`git stash save {MESSAGE}`
        fügt den Änderungen eine Nachricht hinzu.

    ``git stash pop``
        entfernt den obersten Stash-Eintrag und übernimmt die Änderungen in den
        Arbeitsbereich.
    :samp:`git stash pop {n}`
        entfernt den :samp:`{n}+1`-ten Stash-Eintrag und übernimmt die
        Änderungen in den Arbeitsbereich.
    ``git stash show``
        zeigt den Inhalt eines Stash-Eintrags an.
    :samp:`git stash show {n}`
        zeigt den :samp:`{n}+1`-ten Stash-Eintrag an.

        .. _showpatch:

        .. tip::
           Üblicherweise zeigt die Ausgabe nur die hinzugefügten oder entfernten
           Zeilen pro Datei an. Um die Ausgabe informativer zu machen, könnt ihr
           die Option ``-p`` hinzufügen, um auch das Diff des Stash-Eintrags
           auszugeben. Noch besser ist jedoch, dieses Verhalten zur
           Voreinstellung zu machen mit

           .. code-block:: console

              $ git config --global stash.showPatch true

    :samp:`git stash branch {BRANCHNAME} [{n}]`
        erstellt aus versteckten Dateien einen Zweig, :abbr:`z.B. (zum
        Beispiel)`:

        .. code-block:: console

            $ git stash branch stash-example 1
            Auf Branch stash-example
            Zum Commit vorgemerkte Änderungen:
              (benutzen Sie "git restore --staged <Datei>..." zum Entfernen aus der Staging-Area)
                neue Datei:     docs/productive/git/work.rst

            Änderungen, die nicht zum Commit vorgemerkt sind:
              (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
              (benutzen Sie "git restore <Datei>...", um die Änderungen im Arbeitsverzeichnis zu verwerfen)
                geändert:       docs/productive/git/index.rst

            stash@{1} (6565fdd1cc7dff9e0e6a575e3e20402e3881a82e) gelöscht

    :samp:`git stash -u {UNTRACKED_FILE}`
        versteckt unversionierte Dateien.
    ``git stash list``
        listet die Verstecke auf.

        :samp:`git stash list --date=relative|default`
            zeigt zusätzlich das relative oder absolute datum an.

    ``git stash pop``
        übernimmt Änderungen aus einem Versteck in den Arbeitsbereich und leert
        das Versteck, :abbr:`z.B. (zum Beispiel)`:

        .. code-block:: console

           $ git stash pop 2

    ``git stash drop``
        leert ein spezifisches Versteck, :abbr:`z.B. (zum Beispiel)`:

        .. code-block:: console

            $ git stash drop 1
            stash@{1} (defcf56541b74a1ccfc59bc0a821adf0b39eaaba) gelöscht

    ``git stash clear``
        löscht alle eure Verstecke.
