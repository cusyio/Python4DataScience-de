Git-Verzweigungen
=================

Verzweigen ist eine Funktion, die in den meisten modernen
Versionskontrollsystemen verfügbar ist. In anderen VCS-Systemen kann das
Verzweigen eine teure Operation sein, die sowohl Zeit als auch Speicherplatz
kostet; in Git sind Verzweigungen jedoch Verweise auf einen Schnappschuss eurer
Änderungen. Wenn ihr eine neue Funktion hinzufügen oder einen Fehler beheben
wollt, legt ihr einen neuen Zweig an, um eure Änderungen darin zu kapseln.
Dadurch könnt ihr euch auf diese Aufgabe konzentrieren ohne zunächst
gleichzeitige Änderungen im Hauptzweig berücksichtigen zu müssen. Umgekehrt hält
es auch den Hauptzweig frei von fragwürdigem Code. Git-Zweige wurden daher ein
fester Bestandteil des täglichen Arbeitsablaufs.

Ihr könnt euch Verzweigungen auch als ein neues Arbeitsverzeichnis mit neuen
Staging-Bereich und Projektverlauf vorstellen wobei eure Commits zunächst in der
Historie für den aktuellen Zweig aufgezeichnet  werden.

.. seealso::
    * `Git Branching - Branches auf einen Blick
      <https://git-scm.com/book/de/v2/Git-Branching-Branches-auf-einen-Blick>`_

Gebräuchliche Befehle
---------------------

:samp:`$ git branch [-a]`
    zeigt alle lokalen Verzweigungen in einem Repository an.

    ``-a``
        zeigt auch alle entfernten Verzweigungen an.

:samp:`$ git branch [{BRANCH_NAME}]`
    erstellt auf Basis des aktuellen ``HEAD`` einen neuen Zweig.

:samp:`$ git switch [-c] [{BRANCH_NAME}]`
    wechselt zwischen Zweigen.

    ``-c``
        erstellt einen neuen Zweig.

    .. note::

        In Git < 2.23 steht euch ``git switch`` noch nicht zur Verfügung. In
        diesem Fall müsst ihr noch ``git checkout`` verwenden:

        :samp:`$ git checkout [-b] [{BRANCH_NAME}]`
            ändert das Arbeitsverzeichnis in den angegebenen Zweig.

            ``-b``
                erstellt den angegebenen Zweig, wenn dieser nicht schon besteht.

:samp:`$ git merge [{FROM_BRANCH_NAME}]`
    verbindet den angegebenen mit dem aktuellen Zweig, in dem ihr euch gerade
    befindet, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: console

        $ git switch main
        $ git merge hotfix
        Updating f42c576..3a0874c
        Fast forward
         setup.py |    1 -
         1 files changed, 0 insertions(+), 1 deletions(-)

    ``Fast forward``
        besagt, dass der neue Commit direkt auf den ursprünglichen Commit folgte
        und somit der Zeiger (*branch pointer*) nur weitergeführt werden musste.

    In anderen Fällen kann die Ausgabe :abbr:`z.B. (zum Beispiel)` so
    aussehen:

    .. code-block:: console

        $ git switch main
        $ git merge '#42'
        Merge made by recursive.
         setup.py |    1 +
         1 files changed, 1 insertions(+), 0 deletions(-)

    ``recursive``
        ist eine Merge-Strategie, die verwendet wird, sofern die Zusammenführung
        nur zu ``HEAD`` erfolgt.

.. _merge-conflicts:

Merge-Konflikte
---------------

Gelegentlich stößt Git beim Zusammenführen jedoch auf Probleme, :abbr:`z.B.
(zum Beispiel)`:

.. code-block:: console

    $ git merge '#17'
    automatischer Merge von setup.py
    KONFLIKT (Inhalt): Merge-Konflikt in setup.py
    Automatischer Merge fehlgeschlagen; beheben Sie die Konflikte und committen Sie dann das Ergebnis.

Die Historie kann dann :abbr:`z.B. (zum Beispiel)` so aussehen:

.. code-block:: console

    *   49770a2 (HEAD -> main) Fix merge conflict with #17
    |\
    | * 9412467 (#17) Feature #17
    * | 46ab1a2 Hotfix directly in main
    |/
    * 0c65f04 Initial commit

.. seealso::

    * `Git Branching - Einfaches Branching und Merging
      <https://git-scm.com/book/de/v2/Git-Branching-Einfaches-Branching-und-Merging>`_
    * `Git Tools - Fortgeschrittenes Merging
      <https://git-scm.com/book/de/v2/Git-Tools-Fortgeschrittenes-Merging>`_

Zweige löschen
--------------

:samp:`$ git branch -d [{BRANCH_NAME}]`
    löscht den ausgewählten Zweig, wenn er bereits in einen anderen überführt
    wurde.

    ``-D`` statt ``-d`` erzwingt die Löschung.

Entfernte Zweige
----------------

Bisher haben diese Beispiele alle lokale Verzweigungen gezeigt. Der Befehl ``git
branch`` funktioniert jedoch auch mit entfernten Zweigen. Um mit entfernten
Zweigen arbeiten zu können, muss zunächst ein entferntes Repository konfiguriert
und zur lokalen Repository-Konfiguration hinzugefügt werden:

:samp:`$ git remote add origin https://ce.cusy.io/veit/{NEWREPO}.git`

Nun kann der Zweig auch im entfernten Repository hinzugefügt werden:

:samp:`$ git push origin [{BRANCH_NAME}]`

Mit ``git branch -d`` löscht ihr die Zweige nur lokal. Um sie auch auf dem
entfernten Server zu löschen, könnt ihr folgendes eingeben:

:samp:`$ git push origin --delete [{BRANCH_NAME}]`

Zweige umbenennen
-----------------

Ihr könnt Zweige umbenennen, :abbr:`z.B. (zum Beispiel)` mit

.. code-block:: console

   $ git branch --move master main

Dies ändert euren lokalen ``master``-Zweig in ``main``. Damit andere den neuen
Zweig sehen können, müsst ihr ihn auf den entfernten Server pushen. Dadurch wird
der ``main``-Zweig auch auf dem entfernten Server verfügbar:

.. code-block:: console

   $ git push origin main

Der aktuelle Zustand eures Repository kann nun :abbr:`z.B. (zum Beispiel)` so
aussehen:

.. code-block:: console

   $ git branch -a
   * main
     remotes/origin/HEAD -> origin/master
     remotes/origin/main
     remotes/origin/master

* Euer lokaler ``master``-Zweig ist verschwunden, da er durch den ``main``-Zweig
  ersetzt wurde.
* Der ``main``-Zweig ist auch auf dem entfernten Rechner vorhanden.
* Auch der ``master``-Zweig ist jedoch auch noch auf dem entfernten Server
  vorhanden. Vermutlich werden also andere weiterhin den ``master``-Zweig für
  ihre Arbeit verwenden, bis ihr die folgenden Änderungen vorgenommen habt:

  * Für alle Projekte, die von diesem Projekt abhängen, muss der Code und/oder
    die Konfiguration aktualisiert werden.
  * Die Konfigurationsdateien des test-runner müssen :abbr:`ggf.
    (gegebenenfalls)` aktualisiert werden.
  * Build- und Release-Skripte müssen angepasst werden.
  * Die Einstellungen auf eurem Repository-Server wie der Standardzweig des
    Repository, Zusammenführungsregeln und anderes müssen angepasst werden.
  * Verweise auf den alten Zweig in der Dokumentation müssen aktualisiert
    werden.
  * Alle Pull- oder Merge-Requests, die auf den ``master``-Zweig abzielen,
    sollten geschlossen werden.

Nachdem ihr all diese Aufgaben erledigt habt und sicher seid, dass der
``main``-Zweig genauso funktioniert wie der ``master``-Zweig, könnt ihr den
``master``-Zweig löschen:

.. code-block:: console

   $ git push origin --delete master

Team-Mitgliedeer können ihre lokal noch vorhandenen Referenzen auf den
``master``-Zweig löschen mit

.. code-block:: console

   $ git fetch origin --prune
