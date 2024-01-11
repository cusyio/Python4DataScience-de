.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

``log`` und ``reflog``
======================

``log``
-------

.. seealso::
   * `Git’s Database Internals III: File History Queries
     <https://github.blog/2022-08-31-gits-database-internals-iii-file-history-queries/>`_

Filtern und sortieren
~~~~~~~~~~~~~~~~~~~~~

.. glossary::

   :samp:`git log [-n {COUNT}]`
       auflisten der Commit-Historie des aktuellen Zweiges.

       ``-n``
           beschränkt die Anzahl der Commits auf die angegebene Zahl.

   :samp:`git log [--after="{YYYY-MM-DD}"] [--before="{YYYY-MM-DD}"]`
       Commit-Historie gefiltert nach Datum.

       Auch relative Angaben wie ``1 week ago`` oder ``yesterday`` sind
       zulässig.

   :samp:`git log --author="{VEIT}"`
       filtert die Commit-Historie nach Autor*innen.

       Es kann auch nach mehreren Autor*innen gleichzeitig gesucht werden,
       :abbr:`z.B. (zum Beispiel)`:

       :samp:`git log --author="{VEIT\|VSC}"`

   :samp:`git log --grep = "{TERM}" [-i]`
       filtert die Commit-Historie nach regulären Ausdrücken in der
       Commit-Nachricht.

       ``-i``
           ignoriert Groß- und Kleinschreibung.

   :samp:`git log -S"{FOO}" [-i]`
       filtert Commits nach bestimmten Zeilen im Quellcode.

       ``-i``
           ignoriert Groß- und Kleinschreibung.

   :samp:`git log -G"{BA*}"`
       filtert Commits nach regulären Ausdrücken im Quellcode.

   :samp:`git log -- {PATH/TO/FOO.PY}`
       filtert die Commit-Historie nach bestimmten Dateien.

   :samp:`git log {MAIN}..{FEATURE}`
       filtert nach unterschiedlichen Commits in verschiedenen Zweigen
       (Branches), in unserem Fall zwischen den Branches :samp:`MAIN` und
       :samp:`FEATURE`.

       Dies ist jedoch nicht dasselbe wie :samp:`git log {FEATURE}..{MAIN}`.
       Nehmen wir folgendes Beispiel.

       .. code-block::

          A - B main
           \
            C - D feature

       :samp:`git log {MAIN}..{FEATURE}`
           zeigt Änderungen in :samp:`{FEATURE}` an, die nicht in :samp:`{MAIN}`
           enthalten sind, also die Commits ``C`` und ``D``.
       :samp:`git log {FEATURE}..{MAIN}`
           zeigt Änderungen in :samp:`{MAIN}` an, die nicht in :samp:`{FEATURE}`
           enthalten sind, also den Commit ``B``.
       :samp:`git log {MAIN}...{FEATURE}`
           zeigt die Änderungen auf beiden Seiten an, also die Commits ``B``,
           ``C`` und ``D``.

   :samp:`$git log --follow {PATH/TO/FOO.PY}`
       Dies sorgt dafür, dass das Log Änderungen an einer einzelnen Datei
       anzeigt, auch wenn diese umbenannt oder verschoben wurde.

       Ihr könnt ``--follow`` für einzelne Dateiaufrufe standardmäßig
       aktivieren, indem ihr die Option ``log.follow`` in eurer globalen
       Konfiguration aktiviert:

       .. code-block:: console

          git config --global log.follow true

       Dann müsst ihr nicht mehr ``--follow`` angeben, sondern nur noch den
       Dateinamen.

   :samp:`git log -L {LINE_START_INT|LINE_START_REGEX},{LINE_END_INT|LINE_END_REGEX}:{PATH/TO/FOO.PY}`
   :samp:`git log -L :{FUNCNAME_REGEX}:{PATH/TO/FOO.PY}`
       Mit der Option `-L
       <https://git-scm.com/docs/git-log#Documentation/git-log.txt--Lltstartgtltendgtltfilegt>`_
       könnt ihr eine verfeinerte Suche durchführen, indem ihr das Log nur eines
       Teils einer Datei überprüft. Mit dieser Funktion könnt ihr die Historie
       einer einzelnen Funktion, einer Klasse oder eines anderen Code-Blocks
       gründlich durchforsten. Sie ist ideal, um herauszufinden, wann etwas
       erstellt und wie es geändert wurde, so dass ihr es getrost korrigieren,
       refaktorisieren oder löschen könnt.

       Für umfassendere Untersuchungen könnt ihr auch mehrere Blöcke verfolgen.
       Hierfür könnt ihr mehrere ``-L``-Optionen auf einmal verwenden.

   :samp:`git log --reverse`
       Üblicherweise zeigt das Protokoll den neuesten Commit zuerst an. Ihr
       könnt dies mit ``--reverse`` umkehren. Dies ist besonders nützlich, wenn
       ihr mit den bereits erwähnten Optionen ``-S`` und ``-G`` untersucht.
       Indem ihr die Reihenfolge der Commits umkehrt, könnt ihr schnell den
       ersten Commit finden, der eine bestimmte Zeichenfolge zur Codebasis
       hinzugefügt hat.

Ansicht
~~~~~~~

.. glossary::

   :samp:`git log --stat --patch|-p`
       ``--stat``
           Den üblichen Metadaten wird noch eine eine Zusammenfassung der Anzahl
           der geänderten Zeilen pro Datei hinzugefügt.
       ``--patch|-p``
           ergänzt die Ausgabe um den vollständigen Commit-Diff.

   :samp:`git log --oneline --decorate --graph --all|{FEATURE}`
       anzeigen des Verlaufsdiagramms mit Referenzen, ein Commit pro Zeile.

       ``--oneline``
           Ein Commit pro Zeile.
       ``--decorate``
           Die Präfixe ``refs/heads/``, ``refs/tags/`` und  ``refs/remotes/``
           werden nicht ausgegeben.
       ``--graph``
           Üblicherweise *glättet* das Log historische Zweige und zeigt Commits
           nacheinander an. Damit wird die parallele Struktur der Historie beim
           Zusammenführen von Zweigen verborgen. ``--graph`` stellt den Verlauf
           der Zweige in ASCII-Art dar.
       :samp:`--all|{FEATURE}`
           ``--all`` zeigt das Log für alle Zweige; :samp:`{FEATURE}` zeigt nur
           die Commits dieses Zweiges an.

``reflog``
----------

Mit `git reflog <https://git-scm.com/docs/git-reflog>`_ wird euer Git-Repository
nicht ein zweites Mal überprüft. Stattdessen zeigt es das Reference-Log an, eine
Aufzeichnung aller vorgenommenen Commits. Das Reflog verfolgt nicht nur
Änderungen an einem Zweig, es zeichnet auch Änderungen am *aktuellen* Commit,
den Wechsel des Zweiges, Rebasing, :abbr:`etc. (et cetera)` auf. Ihr könnt es
benutzen, um alle unerreichbaren Commits zu finden, sogar solche auf gelöschten
Zweigen. Damit könnt ihr viele, ansonsten destruktive Aktionen wieder rückgängig
machen.

Schauen wir uns die Grundlagen der Verwendung von Reflog und einige typische
Anwendungsfälle an.

Das Reflog für ``HEAD`` anzeigen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. glossary::

   :samp:`git reflog`
       Wenn keine Optionen angegeben sind, zeigt der Befehl standardmäßig das
       Reflog für ``HEAD`` an. Es ist die Abkürzung für ``git reflog show
       HEAD``. git reflog hat weitere Unterbefehle zur Verwaltung des Logs, aber
       ``show`` ist der Standardbefehl, wenn kein Unterbefehl übergeben wird.

.. code-block:: console
   :linenos:

   $ git reflog
   12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{0}: merge my-feature-branch: Fast-forward
   900844a HEAD@{1}: checkout: moving from my-feature-branch to main
   12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{2}: commit (amend): Add my feature and more
   982d93a HEAD@{3}: commit: Add my feature
   900844a HEAD@{4}: checkout: moving from main to my-feature-branch
   900844a HEAD@{5}: commit (initial): Initial commit

* Die Ausgabe ist ziemlich dicht.
* Jede Zeile ist ein Reflog-Eintrag, der neueste zuerst.
* Die Zeilen beginnen mit dem abgekürzten SHA des entsprechenden Commits,
  :abbr:`z.B. (zum Beispiel)` ``12bc4d4``.
* Der erste Eintrag ist das, worauf ``HEAD`` derzeit verweist: ``(HEAD -> main,
  my-feature)``.
* Die Namen ``HEAD@\{N}`` sind alternative Referenzen für die angegebenen
  Commits. ``N`` ist die Anzahl der zurückgehenden reflog-Einträge.
* Der restliche Text beschreibt die Änderung. Oben könnt ihr mehrere Arten von
  Einträgen sehen:

  * :samp:`commit: {MESSAGE}` für Commits
  * :samp:`commit (amend): {MESSAGE}` für eine Commit-Änderung
  * :samp:`checkout: moving from {SRC} TO {DST}` für einen Zweigwechsel

Es gibt viele weitere mögliche Arten von Einträgen. Der Text sollte so
beschreibend sein, dass ihr den Vorgang auch ohne Nachschlagen in der
Dokumentation nachvollziehen könnt. In den meisten Fällen werdet ihr solche
Reflog-Einträge durchsehen wollen, um den entsprechenden Commit SHA zu finden.

Das Reflog für einen Zweig anzeigen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ihr könnt euch auf Einträge für einen einzelnen Zweig fokussieren, indem ihr den
expliziten Unterbefehl ``show`` und dem Zweignamen verwendet:

.. code-block:: console

   $ git reflog show my-feature-branch
   12bc4d4 (HEAD -> main, my-feature-branch) my-feature-branch@{0}: commit (amend): Add my feature and more
   982d93a my-feature-branch@{1}: commit: Add my feature
   900844a my-feature-branch@{2}: branch: Created from HEAD

Zeitstempel der Einträge anzeigen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wenn ihr zwischen ähnlich betitelten Änderungen unterscheiden müsst, können die
Zeitstempel helfen. Für relative Zeitstempel könnt ihr ``--date=relative``
verwenden:

.. code-block:: console

   $ git reflog --date=relative
   12bc4d4 (HEAD -> main, my-feature) HEAD@{vor 37 Minuten}: merge my-feature-branch: Fast-forward
   900844a HEAD@{vor 37 Minuten}: checkout: moving from my-feature-branch to main
   12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{vor 37 Minuten}: commit (amend): Add my feature and more
   982d93a HEAD@{vor 38 Minuten}: commit: Add my feature
   900844a HEAD@{vor 39 Minuten}: checkout: moving from main to my-feature-branch
   900844a HEAD@{vor 40 Minuten}: commit (initial): Initial commit

Und für absolute Zeitstempel könnt ihr auch ``--date=iso`` verwenden:

.. code-block:: console

    $ git reflog --date=iso
    12bc4d4 (HEAD -> main, my-feature) HEAD@{2024-01-11 15:26:53 +0100}: merge my-feature-branch: Fast-forward
    900844a HEAD@{2024-01-11 15:26:47 +0100}: checkout: moving from my-feature-branch to main
    12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{2024-01-11 15:26:11 +0100}: commit (amend): Add my feature and more
    982d93a HEAD@{2024-01-11 15:25:38 +0100}: commit: Add my feature
    900844a HEAD@{2024-01-11 15:24:37 +0100}: checkout: moving from main to my-feature-branch
    900844a HEAD@{2024-01-11 15:23:56 +0100}: commit (initial): Initial commit

Übergebt alle Optionen, die ``git log`` unterstützt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``git reflog show`` hat die gleichen Optionen wie ``git log``. So könnt ihr
beispielsweise mit ``--grep`` nach Commit-Meldungen suchen, in denen :samp:`{my
feature}` erwähnt wird, ohne die Groß- und Kleinschreibung zu berücksichtigen:

.. code-block:: console

    $ git reflog -i --grep 'my feature'
    12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{0}: merge my-feature: Fast-forward
    12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{2}: commit (amend): Add my feature and more
    982d93a HEAD@{3}: commit: Add my feature

Wiederherstellen eines gelöschten Zweigs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Angenommen, ihr habt versehentlich einen nicht zusammengefügten Zweig gelöscht,
so könnt ihr den Zweig mit dem zugehörigen SHA neu erstellen:

.. code-block:: console

   $ git branch -D new-feature
   Branch new-feature entfernt (war d53e431).

Die Ausgabe enthält den SHA-Commit, auf den der Zweig zeigte. Ihr könnt den
Zweig mit diesem SHA neu erstellen:

.. code-block:: console

   $ git branch new-feature d53e431

Was aber, wenn ihr die Verzweigung gelöscht haben und der entsprechende
Terminalverlauf verloren gegangen ist? Um die SHA wiederzufinden, könnt ihr die
Reflog-Ausgabe an ``grep`` übergeben:

.. code-block:: console

   $ git reflog | grep -A 1 new-feature
   12bc4d4 HEAD@{0}: checkout: moving from new-feature to main
   d53e431 HEAD@{1}: commit: Add new feature
   12bc4d4 HEAD@{2}: checkout: moving from main to new-feature
   12bc4d4 HEAD@{3}: merge my-feature: Fast-forward

``-A 1`` zeigt nach nach jedem Treffer eine zusätzliche Zeile an. Die Ausgabe
zeigt mehrere reflog-Einträge, die sich auf den Zweig beziehen. Der erste
Eintrag zeigt einen Wechsel von ``new-feature`` zu ``main``, mit dem Commit-SHA
auf ``main``. Der Eintrag davor ist die letzte Änderung an ``new-feature`` mit
dem SHA zum Wiederherstellen:

.. code-block:: console

   $ git branch triceratops-enclosure 43f66f9

Standardmäßig könnt ihr einen solchen Zweig innerhalb von 30 Tagen nach dem
Löschen des Zweigs speichern, da ``gc.reflogExpireUnreachable`` üblicherweise
so eingestellt ist.

Rückgängigmachen einer Commit-Änderung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kehren wir zum einleitenden Beispiel zurück. Stellt euch vor, ihr hättet einen
Commit gemacht und ihn später geändert. Dann stellt ihr fest, dass die Änderung rückgängig gemacht werden sollte. Wie könnt ihr vorgehen? Wenn ihr die
ursprüngliche Git-Commit-Ausgabe noch in Ihrem Terminalverlauf seht, könnt ihr
die SHA von dort abrufen und die Änderung rückgängig machen. Aber wenn das nicht
mehr möglich ist, ist es Zeit für das Reflog. Prüft das Reflog für den Zweig:

.. code-block:: console

   $ git reflog my-feature-branch
   12bc4d4 (HEAD -> main, my-feature-branch) my-feature-branch@{0}: commit (amend): Add my feature and more
   982d93a my-feature-branch@{1}: commit: Add my feature
   900844a my-feature-branch@{2}: branch: Created from HEAD

Der erste Eintrag, ``commit (amend)``, zeigt die Erstellung des geänderten
Commits an. Der zweite Eintrag zeigt den ursprünglichen Commit, zu der wir nun
wiederum mit einem Hard Reset zurückkehren wollen:

.. code-block:: console

   $ git reset --hard 982d93a

Vielleicht möchtet ihr dann den Inhalt des geänderten Commits wiederherstellen,
um ihn zu korrigieren und erneut zu ändern. Tut dies mit git ``restore`` aus dem
geänderten Commit SHA, der oben in der vorherigen ``reflog``-Ausgabe steht:

.. code-block:: console

   $ git restore -s 12bc4d4

Rückgängig machen eines fehlerhaften Rebase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stellt euch vor, ihr arbeitet an einem Zweig ``new-feature`` mit drei Commits,
wovon ihr den mittleren rückgängig machen wollt:

.. code-block:: console

   $ git rebase -i main

.. code-block:: diff

    pick d53e431 Add new feature
   -pick 329271a More performant implementation for the new feature
   -pick 1d6c477 Add API docs

Versehentlich habt ihr jetzt jedoch auch den letzten Commit gelöscht. Falls ihr
den SHA-Wert nicht mehr im Terminalverlauf sehen könnt, könnt ihr wieder die
``reflog``-Ausgabe an ``grep`` übergeben:

.. code-block:: console

   $ git reflog| grep 'API docs'
   1d6c477 HEAD@{2}: commit: Add API docs

Mit dieser SHA kann der Commit nun mit :doc:`advanced/cherry-pick`
wiederhergestellt werden:

.. code-block:: console

   $ git cherry-pick 1d6c477

Beachtet den Verfall von Einträgen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reflog-Einträge verfallen nach einer gewissen Zeit, wenn Git den automatischen
:abbr:`gc (engl.: Garbage Collection)`-Prozess für euer Repository ausführt.
Diese Verfallszeit wird durch zwei ``gc.*``-Optionen gesteuert:

``gc.reflogExpire``
    Die allgemeine Verfallszeit, die standardmäßig auf 90 Tage eingestellt ist.
``gc.reflogExpireUnreachable``
    Die Verfallszeit für Einträge, die sich auf nicht mehr erreichbare Commits
    beziehen, ist standardmäßig auf 30 Tage eingestellt.

Ihr könnt diese Optionen auf einen längeren Zeitrahmen erhöhen, was allerdings
nur selten sinnvoll sein dürfte.

.. warning::
   Das Reflog ist nur Teil eures lokalen Repository. Wenn ihr ein Projektarchiv
   löscht und neu klont, wird der neue Klon ein frisches, leeres Reflog haben.
