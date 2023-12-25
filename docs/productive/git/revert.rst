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

       :samp:`$ git checkout {FILE}`

    :samp:`git restore [-S|--staged] {FILE}`
        nimmt das Hinzufügen von Dateien zurück. Die Änderungen bleiben in eurem
        Arbeitsbereich erhalten, so dass ihr sie bei Bedarf ändern und wieder
        hinzufügen könnt.

        Der Befehl entspricht :samp:`git reset {PATH}`.

    :samp:`git restore [-SW] {FILE}`
        nimmt das Hinzufügen und Änderungen im Arbeitsbereich zurück.
    :samp:`git restore [-s|--source] {BRANCH} {FILE}`
        setzt eine Änderung auf die Version im Zweig :samp:`{BRANCH}` zurück.
    :samp:`git restore [-s|--source] @~ {FILE}`
        setzt eine Änderung auf den vorherigen Commit zurück.
    :samp:`git restore [-p|--patch]`
        lässt euch die rückgängig zu machenden Änderungen einzeln auswählen.

:samp:`$ git reset [--hard | --mixed | --soft | --keep] {TARGET_REFERENCE}`
    setzt die Historie auf einen früheren Commit zurück.

    .. warning::
        Das Risiko bei ``reset`` ist, dass Arbeit verloren gehen kann. Zwar
        werden Commits nicht unmittelbar gelöscht, allerdings können sie
        verwaisen, so dass es keinen direkten Pfad mehr zu ihnen gibt. Sie
        müssen dann zeitnah mit ``git reflog`` gefunden und wiederhergestellt
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

:samp:`$ git revert {COMMIT SHA}`
    erstellt einen neuen Commit und nimmt die Änderungen des angegebenen Commits
    zurück, sodass die Änderungen invertiert werden.
:samp:`$ git fetch --prune {REMOTE}`
    Remote-Refs werden entfernt wenn sie im Remote-Repository entfernt wurden.
:samp:`$ git commit --amend`
    aktualisiert und ersetzt den letzten Commit durch einen neuen Commit, der
    alle bereitgestellten Änderungen mit dem Inhalt des vorherigen Commits
    kombiniert. Wenn nichts bereitgestellt ist, wird nur die vorherige
    Commit-Nachricht neu geschrieben.

Commit im falschen Zweig zurücknehmen
-------------------------------------

Wenn ihr versehentlich einen Commit in einem bestehenden Zweig gemacht habt,
anstatt zunächst einen neuen Zweig zu erstellen, könnt ihr das in den folgenden
drei Schritten ändern:

#. Erstellt einen neuen Zweig mit :samp:`$ git branch {NEW_BRANCH}`
#. Nehmt den letzten Commit in eurem aktiven Branch zurück mit :samp:`$ git
   reset HEAD~ --hard`
#. Übernehmt die Änderungen in den neuen Zweig mit :samp:`$ git switch
   {NEW_BRANCH}`

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
