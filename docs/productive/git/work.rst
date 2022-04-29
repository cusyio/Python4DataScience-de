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
        das Versteck.
    ``drop``
        leeren eines spezifischen Verstecks.
