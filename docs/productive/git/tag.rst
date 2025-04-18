.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git-Tags
========

Git-Tags sind Referenzen, die auf bestimmte Commits in der Git-Historie
verweisen. So können bestimmte Punkte in der Historie für eine bestimmte Version
markiert werden, :abbr:`z.B. (zum Beispiel)` :samp:`v3.9.16`. Tags sind wie
:doc:`branch`, die sich nicht ändern, also keine weitere Historie von Commits
haben.

:samp:`$ git tag {TAGNAME}`
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
        Beispiel)` anzeigen lassen mit :samp:`git show {v3.9.16}`.

    Leichtgewichtige Tags
        Leichtgewichtige Tags können :abbr:`z.B. (zum Beispiel)` mit :samp:`git
        tag {v3.9.16}` ohne die Optionen :samp:`-a`, :samp:`-s` oder :samp:`-m`
        erstellt werden. Sie erstellen eine Tag-Prüfsumme, die im
        :file:`.git/`-Verzeichnis eures Repos gespeichert werden.

``git tag``
-----------

:samp:`$ git tag`
    listet die Tags eures Repos auf, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: console

       0.1.0
       0.1.1
       0.1.10
       0.1.11
       0.1.12
       0.1.2
       …

    .. _tag-sort:

    .. tip::
       Die Reiehnfolge der Tags entspricht jedoch nicht derjenigen, die wir
       eigentlich erwarten würden: Nach ``0.1.1`` erwarten wir ``0.1.2`` und
       nicht ``0.1.10``. Um dies zu erreichen, können wir Git folgendermaßen
       konfigurieren:

       .. code-block:: console

          git config --global tag.sort version:refname

    :samp:`$ git tag -l '{REGEX}'`
        listet nur Tags auf, die zu einem regulären Ausdruck passen.

:samp:`$ git tag -a {TAGNAME} {COMMIT-SHA}`
    erstellt einen Tag für einen früheren Commit.

    Die vorangegangenen Beispiele erstellen Tags für implizite Commits, die auf
    ``HEAD`` verweisen. Alternativ kann :samp:`git tag` auch die Referenz auf
    einen bestimmten Commit übergeben werden, die ihr mit :doc:`review`
    erhaltet.

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

:samp:`$ git push origin {TAGNAME}`
    Das Teilen von Tags ist ähnlich wie der Push von Zweigen: standardmäßig
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

    Um Tags an den Server zu übermitteln, könnt ihr die :samp:`--tags`-Option
    für den Befehl :samp:`git push` verwenden. Andere erhalten die Tags bei
    :samp:`git clone`, :samp:`git pull` oder :samp:`git fetch` des Repos.

    Mit ``git push --follow-tags`` könnt ihr mit einem Commit auch gleichzeitig
    die zugehörigen annotierten Tags teilen.

    .. note::
       ``--follow-tags`` funktioniert  nur für annotierte Tags, nicht für die
       leichtgewichtigen Tags.

    Wenn ihr für alle zukünftigen Pushes ``--follow-tags`` verwenden wollt,
    könnt ihr dies konfigurieren mit

    .. code-block:: console

       $ git config --global push.followTags true

    .. seealso::
       * `git push --follow-tags
         <https://git-scm.com/docs/git-push#Documentation/git-push.txt---follow-tags>`_
       * `git config push.followTags
         <https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushfollowTags>`_

:samp:`$ git checkout {TAGNAME}`
    wechselt in den Zustand des Repository mit diesem Tag und trennt ``HEAD`` ab.
    :abbr:`D.h. (Das heißt)`, dass alle Änderungen, die nun vorgenommen werden,
    das Tag nicht aktualisieren, sondern in einem losgelösten Commit landen, der
    nicht Teil eines Zweiges sein kann und nur direkt über den SHA-Hash des
    Commits erreichbar sein wird. Daher wird meist ein neuer Zweig erstellt,
    wenn solche Änderungen vorgenommen werden sollen, :abbr:`z.B. (zum
    Beispiel)` mit :samp:`git checkout -b v3.9.17 v3.9.16`.

:samp:`$ git tag -d {TAGNAME}`
    löscht einen Tag, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: console

        $ git tag -d v3.9.16
        $ git push origin --delete v3.9.16

    .. _prune-tags:

    Wenn Tags, die auf dem Server gelöscht wurden, auch bei euch lokal
    gelöscht werden sollen, könnt ihr :samp:`git fetch --prune-tags`
    verwenden. Alternativ könnt ihr auch die globale Konfiguration anpassen
    mit:

    .. code-block:: console

       $ git config --global fetch.pruneTags true

``git describe``
----------------

Der :samp:`git describe {SH}`-Befehl findet das neueste Tag, das von einem
Commit aus erreicht werden kann. Wenn das Tag auf den Commit verweist, wird nur
das Tag angezeigt, andernfalls wird die Anzahl der weiteren Commits an den
Tagnamen angehängt. Das Ergebnis ist ein Objektname, der von anderen
Git-Befehlen verwendet werden kann, um den Commit zu identifizieren. Angenommen,
ihr habt einen Commit-SHA und möchtet wissen, in welcher Version er zuerst
veröffentlicht wurde, könnt ihr den folgenden Befehl verwenden:

.. code-block:: console

   $ git describe --contains 39ff38d | sed -E 's/[~^][0-9]*//g'
   24.1.0
