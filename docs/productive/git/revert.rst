Änderungen zurücknehmen
=======================

:samp:`$ git reset [--hard|--soft] [{TARGET-REFERENCE}]`
    setzt die Historie auf einen früheren Commit zurück, :abbr:`z.B. (zum
    Beispiel)`:

    .. code-block:: console

        $ git reset HEAD~1

    ``--HEAD~1``
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

    ``--soft``
        nimmt den oder die Commits zurück, lässt jedoch Bühnen- und
        Arbeitsbereich unverändert.

    .. warning::
        Das Risiko bei ``reset`` ist, dass Arbeit verloren gehen kann. Zwar
        werden Commits nicht unmittelbar gelöscht, allerdings können sie
        verwaisen, so dass es keinen direkten Pfad mehr zu ihnen gibt. Sie
        müssen dann zeitnah mit ``git reflog`` gefunden und wiederhergestellt
        werden da Git üblicherweise alle verwaisten Commits nach 30 Tagen
        löscht.

:samp:`$ git revert [{COMMIT SHA}]`
    erstellt einen neuen Commit und nimmt die Änderungen des angegebenen Commits
    zurück, sodass die Änderungen invertiert werden.
:samp:`$ git fetch [{REMOTE}]`
    übernimmt die Änderungen von Remote, aktualisiert jedoch nicht die Zweige.
:samp:`$ git fetch --prune [{REMOTE}]`
    Remote-Refs werden entfernt wenn sie im Remote-Repository entfernt wurden.
:samp:`$ git commit --amend`
    aktualisiert und ersetzt den letzten Commit durch einen neuen Commit, der
    alle bereitgestellten Änderungen mit dem Inhalt des vorherigen Commits
    kombiniert. Wenn nichts bereitgestellt ist, wird nur die vorherige
    Commit-Nachricht neu geschrieben.
:samp:`$ git restore [{FILE}]`
    ändert Dateien im Arbeitsverzeichnis in einen Zustand, der Git zuvor bekannt
    war. Standardmäßig checkt Git ``HEAD`` den letzten Commit des aktuellen
    Zweigs aus.

    .. note::

        In Git < 2.23 steht euch ``git restore`` noch nicht zur Verfügung. In
        diesem Fall müsst ihr noch ``git checkout`` verwenden:

       :samp:`$ git checkout [{FILE}]`

:samp:`$ git pull [{REMOTE}]`
    ruft Änderungen aus dem Remote-Repository ab und führt den aktuellen Zweig
    mit dem Upstream zusammen.
:samp:`$ git push [--tags] [{REMOTE}]`
    überträgt lokale Änderungen nach Remote.

    Mit ``--tags`` können gleichzeitig Tags übertragen werden.

:samp:``$ git push -u [{REMOTE}] [{BRANCH}]``
    überträgt den lokalen Zweig in das Remote-Repository wobei die Kopie als
    Upstream festgelegt wird.
