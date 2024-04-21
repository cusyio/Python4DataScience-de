.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Änderungen zurücknehmen
=======================

Mit Git 2.23 kam ``git restore`` zum Rückgängigmachen von Datei-Änderungen
hinzu. Vorher übernahm ``git reset`` diese Aufgabe, das aber auch noch andere
Aufgaben hat:

:samp:`$ git restore`
    ändert Dateien im Arbeitsverzeichnis in einen Zustand, der Git zuvor bekannt
    war. Standardmäßig checkt Git ``HEAD`` den letzten Commit des aktuellen
    Zweigs aus.

    .. note::

        In Git < 2.23 steht euch ``git restore`` noch nicht zur Verfügung. In
        diesem Fall müsst ihr noch ``git checkout`` verwenden:

       :samp:`$ git checkout {PATH/TO/FILE}`

    :samp:`$ git restore [-S|--staged] {PATH/TO/FILE}`
        nimmt das Hinzufügen von Dateien zurück. Die Änderungen bleiben in eurem
        Arbeitsbereich erhalten, so dass ihr sie bei Bedarf ändern und wieder
        hinzufügen könnt.

        Der Befehl entspricht :samp:`git reset {PATH/TO/PATH}`.

    :samp:`$ git restore [-SW] {PATH/TO/FILE}`
        nimmt das Hinzufügen und Änderungen im Arbeitsbereich zurück.
    :samp:`$ git restore [-s|--source] {BRANCH} {PATH/TO/FILE}`
        setzt eine Änderung auf die Version im Zweig :samp:`{BRANCH}` zurück.
    :samp:`$ git restore [-s|--source] @~ {PATH/TO/FILE}`
        setzt eine Änderung auf den vorherigen Commit zurück.
    :samp:`$ git restore [-p|--patch]`
        lässt euch die rückgängig zu machenden Änderungen einzeln auswählen.

:samp:`$ git reset [--hard | --mixed | --soft | --keep] {TARGET_REFERENCE}`
    setzt die Historie auf einen früheren Commit zurück.

    .. warning::
        Das Risiko bei ``reset`` ist, dass Arbeit verloren gehen kann. Zwar
        werden Commits nicht unmittelbar gelöscht, allerdings können sie
        verwaisen, so dass es keinen direkten Pfad mehr zu ihnen gibt. Sie
        müssen dann zeitnah mit :ref:`reflog` gefunden und wiederhergestellt
        werden da Git üblicherweise alle verwaisten Commits nach 30 Tagen
        löscht.

    .. code-block:: console

        $ git reset @~

    ``@~``
        nimmt den letzten Commit zurück wobei dessen Änderungen nun wieder in
        den Bühnenbereich übernommen werden.

        Sind Änderungen im Bühnenbereich vorhanden, so werden diese in den
        Arbeitsbereich verschoben, :abbr:`z.B. (zum Beispiel)`:

        .. code-block:: console

            $ echo 'My first repo' > README.rst
            $ git add README.rst
            $ git status
            Auf Branch main
            Zum Commit vorgemerkte Änderungen:
              (benutzen Sie "git rm --cached <Datei>..." zum Entfernen aus der Staging-Area)
                neue Datei:     README.rst
            $ git reset
            $ git status
            Auf Branch main
            Unversionierte Dateien:
              (benutzen Sie "git add <Datei>...", um die Änderungen zum Commit vorzumerken)
                README.rst

    ``@~3``
        nimmt den letzten drei Commits zurück.
    ``'@{u}'``
        nimmt die entfernte Version (*Upstream*) des aktuellen Zweigs.

    ``--hard``
        verwirft die Änderungen auch im Staging- und Arbeitsbereich.

        .. code-block:: console

            $ git status
            Auf Branch main
            Zum Commit vorgemerkte Änderungen:
              (benutzen Sie "git rm --cached <Datei>..." zum Entfernen aus der Staging-Area)
                neue Datei:     README.rst
            $ git reset --hard
            $ git status
            Auf Branch main
            nichts zu committen (erstellen/kopieren Sie Dateien und benutzen
            Sie "git add" zum Versionieren)

    ``--mixed``
        setzt den Bühnen-, aber nicht den Arbeitsbereich zurück, :abbr:`d.h.
        (das heißt)`, die geänderten Dateien bleiben erhalten, werden aber nicht
        für den Commit markiert.

        .. tip::
           Ich bevorzuge meist ``--soft`` gegenüber ``--mixed``: es hält die
           rückgängig gemachten Änderungen getrennt, so dass alle zusätzlichen
           Änderungen explizit sind. Dies ist Besonders nützlich, wenn ihr
           im Bühnen- und Arbeitsbereich Änderungen an der gleichen Datei habt.

    ``--soft``
        nimmt den oder die Commits zurück, lässt jedoch Bühnen- und
        Arbeitsbereich unverändert.
    ``--keep``
        setzt den Bühnenbereich zurück und aktualisiert die Dateien im
        Arbeitsbereich, die sich zwischen :samp:`COMMIT` und ``HEAD``
        unterscheiden, behält aber diejenigen bei, die sich zwischen Bühnen- und
        Arbeitsbereich unterscheiden, :abbr:`d.h. (das heißt)`, die Änderungen
        haben, aber noch nicht hinzugefügt wurden. Wenn eine Datei, die sich
        zwischen :samp:`COMMIT` und Bühnenbereich unterscheidet, nicht
        hinzugefügte Änderungen aufweist, wird ``reset`` abgebrochen.

        Ihr könnt euch dann mit euren nicht im Commit enthaltenen Änderungen
        befassen, sie vielleicht mit ``git restore`` rückgängig macht oder mit
        ``git stash`` versteckt, bevor ihr es erneut versucht.

        .. tip::
           Viele andere Anleitungen empfehlen ``--hard`` für diese Aufgabe,
           wahrscheinlich weil es diesen Modus schon länger gibt. Dieser Modus
           ist jedoch riskanter, da er die nicht im Commit enthaltenen
           Änderungen unwiderruflich verwirft ohne Fragen zu stellen.  Ich
           verwende jedoch ``--keep`` und wenn ich alle nicht zum Commit
           vorgesehenen Änderungen vor dem ``reset`` verwerfen will, verwende
           ich ``git restore -SW``.

:samp:`$ git revert {COMMIT_SHA}`
    erstellt einen neuen Commit und nimmt die Änderungen des angegebenen Commits
    zurück, sodass die Änderungen invertiert werden.
:samp:`$ git fetch --prune {REMOTE}`
    Remote-Refs werden entfernt wenn sie im Remote-Repository entfernt wurden.
:samp:`$ git commit --amend`
    aktualisiert und ersetzt den letzten Commit durch einen neuen Commit, der
    alle bereitgestellten Änderungen mit dem Inhalt des vorherigen Commits
    kombiniert. Wenn nichts bereitgestellt ist, wird nur die vorherige
    Commit-Nachricht neu geschrieben.

Referenz für häufige Befehle zum Zurücksetzen
---------------------------------------------

Alle lokalen Änderungen an einem Zweig rückgängig machen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ git reset --keep '@{u}'

Alle Commits im aktuellen Zweig rückgängig machen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`git merge-base <https://git-scm.com/docs/git-merge-base>`_ wählt den Commit
aus, bei dem sich zwei Zweige getrennt haben. Übergebt ``@`` und ``main``, um
den Commit auszuwählen, bei dem der aktuelle Zweig von ``main`` abgezweigt ist.
Setzt ihn zurück, um alle Commits auf dem lokalen Zweig rückgängig zu machen
mit:

.. code-block:: console

    $ git reset --soft $(git merge-base @ main)

Alle Änderungen im aktuellen Zweig rückgängig machen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ git reset --keep main

Commit im falschen Zweig zurücknehmen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wenn ihr versehentlich einen Commit in einem bestehenden Zweig gemacht habt,
anstatt zunächst einen neuen Zweig zu erstellen, könnt ihr das in den folgenden
drei Schritten ändern:

#. Erstellt einen neuen Zweig mit :samp:`$ git branch {NEW_BRANCH}`
#. Nehmt den letzten Commit in eurem aktiven Branch zurück mit :samp:`$ git
   reset --keep @~`
#. Übernehmt die Änderungen in den neuen Zweig mit :samp:`$ git switch
   {NEW_BRANCH}`

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
:ref:`reflog`-Ausgabe an ``grep`` übergeben:

.. code-block:: console

   $ git reflog | grep -A 1 new-feature
   12bc4d4 HEAD@{0}: checkout: moving from new-feature to main
   d53e431 HEAD@{1}: commit: Add new feature
   12bc4d4 HEAD@{2}: checkout: moving from main to new-feature
   12bc4d4 HEAD@{3}: merge my-feature: Fast-forward

``-A 1`` zeigt nach nach jedem Treffer eine zusätzliche Zeile an. Die Ausgabe
zeigt mehrere :ref:`reflog`-Einträge, die sich auf den Zweig beziehen. Der erste
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
geänderten Commit SHA, der oben in der vorherigen :ref:`reflog`-Ausgabe steht:

.. code-block:: console

   $ git restore -s 12bc4d4

Rückgängig machen eines fehlerhaften Rebase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stellt euch vor, ihr arbeitet an einem Zweig ``new-feature`` mit drei Commits,
wovon ihr den mittleren mit :doc:`rebase` rückgängig machen wollt:

.. code-block:: console

   $ git rebase -i main

.. code-block:: diff

    pick d53e431 Add new feature
   -pick 329271a More performant implementation for the new feature
   -pick 1d6c477 Add API docs

Versehentlich habt ihr jetzt jedoch auch den letzten Commit gelöscht. Falls ihr
den SHA-Wert nicht mehr im Terminalverlauf sehen könnt, könnt ihr wieder die
:ref:`reflog`-Ausgabe an ``grep`` übergeben:

.. code-block:: console

   $ git reflog| grep 'API docs'
   1d6c477 HEAD@{2}: commit: Add API docs

Mit dieser SHA kann der Commit nun mit :doc:`advanced/cherry-pick`
wiederhergestellt werden:

.. code-block:: console

   $ git cherry-pick 1d6c477

.. _git-filter-repo:

Entfernen einer Datei aus der Historie
--------------------------------------

Eine Datei kann vollständig aus Git-Historie des aktuellen Branches entfernt
werden.
Das ist nötig, wenn ihr beispielsweise aus Versehen Passwörter oder eine sehr große Datei zum Repository hinzugefügt habt.

.. code-block:: console

    $ git filter-repo --invert-paths --path path/somefile
    $ git push --no-verify --mirror

.. note::
    Informiert die Team-Mitglieder, dass sie erneut einen Klon des Repository
    erstellen sollten.

Entfernen einer Zeichenkette aus der Historie
---------------------------------------------

Das Entfernen funktioniert auch mit einzelnen Wörtern oder Zeichenketten:

.. code-block:: console

    $ git filter-repo --message-callback 'return re.sub(b"^git-svn-id:.*\n", b"", message, flags=re.MULTILINE)'

.. seealso::
  * `git-filter-repo — Man Page <https://www.mankier.com/1/git-filter-repo>`_
  * `git-reflog <https://git-scm.com/docs/git-reflog>`_
  * `git-gc <https://git-scm.com/docs/git-gc>`_
