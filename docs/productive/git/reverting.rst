Änderungen zurücknehmen
=======================

``$ git reset [--hard] [target reference]``
   wechselt vom aktuellen Zweig zur Zielreferenz und hinterlässt den Unterschied
   als nicht festgeschriebene Änderung, z.B.:

   .. code-block:: console

        $ git reset HEAD setup.py

   ``--hard`` verwirft alle Änderungen.

``$ git revert [commit sha]``
    erstellt einen neuen Commit und nimmt die Änderungen des angegebenen Commits
    zurück. Die Änderungen werden invertiert.
``$ git fetch [remote]``
    übernimmt die Änderungen von Remote, aktualisiert jedoch nicht die Zweige.
``$ git fetch --prune [remote]``
    Remote-Refs werden entfernt wenn sie im Remote-Repository entfernt wurden.
``$ git commit --amend``
    aktualisiert und ersetzt den letzten Commit durch einen neuen Commit, der
    alle bereitgestellten Änderungen mit dem Inhalt des vorherigen Commits
    kombiniert. Wenn nichts bereitgestellt ist, wird nur die vorherige
    Commit-Nachricht neu geschrieben.
``$ git restore [file]``
    ändert Dateien im Arbeitsverzeichnis in einen Zustand, der Git zuvor bekannt
    war. Standardmäßig checkt Git ``HEAD``, den letzten Commit des aktuell
    ausgecheckten Zweigs, aus. Alternativ könnt ihr auch einen bestimmte Zweig
    oder SHA auswählen.

    .. note::

        In Git < 2.23 steht euch ``git restore`` noch nicht zur Verfügung. In
        diesem Fall müsst ihr noch ``git checkout`` verwenden:

        ``$ git checkout [file]``

``$ git pull [remote]``
    ruft Änderungen aus dem Remote-Repository ab und führt den aktuellen Zweig
    mit dem Upstream zusammen.
``$ git push [--tags] [remote]``
    überträgt lokale Änderungen nach Remote.

    Mit ``--tags`` können gleichzeitig Tags übertragen werden.
``$ git push -u [remote] [branch]``
    überträgt den lokalen Zweig in das Remote-Repository wobei die Kopie als
    Upstream festgelegt wird.
