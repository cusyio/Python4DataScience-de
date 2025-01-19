.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

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
    * :doc:`workflows/merge-strategies`

Gebräuchliche Befehle
---------------------

:samp:`$ git branch [-a] [-l "{GLOB_PATTERN}"]`
    zeigt alle lokalen Verzweigungen in einem Repository an.

    ``-a``
        zeigt auch alle entfernten Verzweigungen an.
    ``-l``
        beschränkt die Zweige auf diejenigen, die einem bestimmten Muster
        entsprechen.

:samp:`$ git branch --sort=-committerdate`
    sortiert die Zweige nach dem Commit-Datum.

    Mit :samp:`git config --global branch.sort -committerdate` könnt ihr diese
    Einstellung auch zu eurer Standardeinstellung machen.

:samp:`$ git branch {BRANCH_NAME}`
    erstellt auf Basis des aktuellen ``HEAD`` einen neuen Zweig.

:samp:`$ git switch [-c] {BRANCH_NAME}`
    wechselt zum Zweig.

    ``-c``
        erstellt einen neuen Zweig.

:samp:`$ git switch -`
    wechselt zu dem zuvor zuvor ausgecheckten Zweig. Das hin und her springen
    zwischen zwei Zweigen wird damit deutlich vereinfacht.

    .. note::

       In Git < 2.23 steht euch ``git switch`` noch nicht zur Verfügung. In
       diesem Fall müsst ihr noch ``git checkout`` verwenden:

       :samp:`$ git checkout [-b] [{BRANCH_NAME}]`
           ändert das Arbeitsverzeichnis in den angegebenen Zweig.

           ``-b``
               erstellt den angegebenen Zweig, wenn dieser nicht schon besteht.

:samp:`$ git merge {FROM_BRANCH_NAME}`
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
       $ git merge 'my-feature'
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

   $ git merge 'my-feature'
   automatischer Merge von setup.py
   KONFLIKT (Inhalt): Merge-Konflikt in setup.py
   Automatischer Merge fehlgeschlagen; beheben Sie die Konflikte und committen Sie dann das Ergebnis.

Die Historie kann dann :abbr:`z.B. (zum Beispiel)` so aussehen:

.. code-block:: console

   *   49770a2 (HEAD -> main) Fix merge conflict with my-feature
   |\
   | * 9412467 (my-feature) My feature
   * | 46ab1a2 Hotfix directly in main
   |/
   * 0c65f04 Initial commit

.. seealso::

   * `Git Branching - Einfaches Branching und Merging
     <https://git-scm.com/book/de/v2/Git-Branching-Einfaches-Branching-und-Merging>`_
   * `Git Tools - Fortgeschrittenes Merging
     <https://git-scm.com/book/de/v2/Git-Tools-Fortgeschrittenes-Merging>`_

Verbesserte Konfliktanzeige mit zdiff3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normalerweise stellt Git Zusammenführungskonflikte folgendermaßen dar:

.. code-block:: console

   <<<<<<< HEAD
   This line has been changed by feature one.
   This line has also been changed by feature one.
   This line will be changed by feature two.
   =======
   This line is changed by feature one.
   This line has been changed by feature two.
   This line has also been changed by feature two.
   >>>>>>> feature_two

Zwischen den Markierungen ``<<<<<<<`` und ``=======`` befinden sich die Zeilen
des Merge-Ziels. Die Zeilen zwischen den Markierungen ``=======`` und
``>>>>>>>`` sind die Zeilen der Merge-Quelle. Die Beschriftungen nach den
Pfeilmarkierungen benennen die Commit-Referenzen, die zusammengeführt werden.

Dies ist oft ausreichend, um einen Konflikt lösen zu können. Aber es kann auch
unnötig herausfordernd sein, weil die ursprünglichen Zeilen, von denen beide
Seiten ausgingen, fehlen. Die gemeinsame Basis, von der beide Seiten ausgegangen
sind, schaffen Klarheit über den Kontext, in dem beide Änderungen entstanden.

Wenn iht `merge.conflictStyle
<https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeconflictStyle>`_
auf ``zdiff3`` setzt, könnt ihr euch auch die gemeinsame Basis anzeigen lassen:

.. code-block:: console

   $ git config --global merge.conflictStyle zdiff3

Hier ist der gleiche Merge mit diesem Stil:

.. code-block:: console

   <<<<<<< HEAD
   This line has been changed by feature one.
   This line has also been changed by feature one.
   This line will be changed by feature two.
   ||||||| 45d92bd
   This line is changed by feature one.
   This line will be changed by feature one and feature two.
   This line will be changed by feature two.
   =======
   This line is changed by feature one.
   This line has been changed by feature two.
   This line has also been changed by feature two.

Die gemeinsame Basis wird nun zwischen den Markierungen ``|||||||`` und
``=======`` angezeigt mit dem SHA-Wert der gemeinsamen Basis. Dieser zusätzliche
Kontext ist oft nützlich, um einen Konflikt auflösen zu können.

``rerere``, um aufgezeichnete Konfliktlösungen wiederzuverwenden
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:abbr:`rerere (engl.: reuse recorded resolutions)` erleichtert euch, immer
wieder dieselben Merge-Konflikte lösen zu müssen. Dies kann :abbr:`z.B. (zum
Beispiel)` passieren, wenn ihr einen Commit in mehrere Zweige zusammenführen
oder wenn ihr einen Zweig wiederholt rebasen müsst. Das Beheben von
Merge-Konflikten erfordert Konzentration und Energie, und es ist Verschwendung,
denselben Konflikt immer wieder neu zu lösen. `git rerere
<https://git-scm.com/docs/git-rerere>`_ wird jedoch nur selten direkt
aufgerufen, sondern meist global aktiviert. Dann wird er automatisch von ``git
merge``, ``git rebase`` und ``git commit`` verwendet. Seine wichtigste
Auswirkung besteht darin, dass er der Ausgabe dieser Befehle einige Meldungen
hinzufügt. Ihr könnt ihn aktivieren mit:

.. code-block:: console

   $ git config --global rerere.enabled true

Schauen wir uns ein Beispiel für ``git rerere`` in Aktion an. Angenommen, ihr
versucht eine Zusammenführung und stoßt auf Konflikte:

.. code-block:: console

   % git merge rerere-example
   automatischer Merge von README.md
   KONFLIKT (Inhalt): Merge-Konflikt in README.md
   Preimage für 'README.md' aufgezeichnet.
   Automatischer Merge fehlgeschlagen; beheben Sie die Konflikte und committen Sie dann das Ergebnis.

``git rerere`` schrieb die dritte Zeile, ``Preimage für 'README.md'
aufgezeichnet.``, :abbr:`d.h. (das bedeutet)`, dass der Konflikt aufgezeichnet
wurde, bevor wir ihn beheben. Wenn wir den Konflikt nun beheben, können wir mit
der Zusammenführung fortfahren, in unserem Beispiel mit:

.. code-block:: console

   $ git add README.md
   $ git merge --continue
   Konfliktauflösung für 'README.md' aufgezeichnet.
   [main 5935d00] Merge branch 'rerere-example'

``git rerere`` meldet nun ``Konfliktauflösung für 'README.md' aufgezeichnet.``,
:abbr:`d.h. (das heißt)`, dass es gespeichert hat, wie wir die Konflikte in
dieser Datei aufgelöst haben.

Angenommen, ihr macht diese Zusammenführung rückgängig, weil ihr
feststellgestellt habt, dass sie nicht fertig war:

.. code-block:: console

   $ git reset --keep @~

Später wiederholt ihr die Zusammenführung:

.. code-block:: console

   $ git merge rerere-example
   Auto-merging README.md
   CONFLICT (content): Merge conflict in README.md
   Resolved 'README.md' using previous resolution.
   Automatic merge failed; fix conflicts and then commit the result.
   When finished, apply stashed changes with `git stash pop`

``git rerere`` löste den Konflikt unter Verwendung der früheren Lösung,
:abbr:`d.h. (das heißt)`, es hat eure vorherige Zusammenführung wiederverwendet.
Prüft nun, ob die Datei korrekt ist, und fahrt dann fort:

.. code-block:: console

   $ git add README.md
   $ git merge --continue
   [main c922b21] Merge branch 'rerere-example'

``git rerere`` speichert seine Daten innerhalb des :file:`.git`-Verzeichnisses
eures Git-Repositorys in einem :file:`rr-cache`-Verzeichnis. Dabei solltet ihr
zweierlei beachten:

#. Der Rerere-Cache ist lokal. Er wird nicht geteilt, wenn ihr ``git push``
   durchführt, so dass eure Teamkollegen die von euch durchgeführten Merges
   nicht wiederverwenden können.
#. Git’s automatische Garbage-Collection löscht Einträge aus dem
   :file:`rr-cache`. Sie wird durch zwei Konfigurationsoptionen gesteuert:

   `gc.rerereResolved <https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcrerereResolved>`_
       bestimmt, wie lange Einträge für gelöste Konflikte aufbewahrt werden. Der
       Standardwert ist 60 Tage. Und mit ``git config gc.rerereResolved`` könnt
       ihr die Standardwerte für euer Projekt ändern.

   `gc.rerereUnresolved <https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcrerereUnresolved>`_
       bestimmt, wie lange Einträge für ungelöste Konflikte aufbewahrt werden.
       Der Standardwert ist 15 Tage.

Zweige löschen
--------------

:samp:`$ git branch -d [{BRANCH_NAME}]`
    löscht den ausgewählten Zweig, wenn er bereits in einen anderen überführt
    wurde.

    ``-D`` statt ``-d`` erzwingt die Löschung.

Entfernte Zweige
----------------

Bisher haben diese Beispiele alle lokalen Verzweigungen gezeigt. Der Befehl
``git branch`` funktioniert jedoch auch mit entfernten Zweigen. Um mit
entfernten Zweigen arbeiten zu können, muss zunächst ein entferntes Repository
konfiguriert und zur lokalen Repository-Konfiguration hinzugefügt werden:

:samp:`$ git remote add origin https://ce.cusy.io/veit/{NEWREPO}.git`

Entfernte Zweige hinzufügen
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nun kann der Zweig auch im entfernten Repository hinzugefügt werden:

:samp:`$ git push --set-upstream origin [{BRANCH_NAME}]`

Wollt ihr alle Zweige eines lokalen Repositories dem entfernten Repo hinzufügen,
könnt ihr dies mit:

:samp:`$ git push --set-upstream origin --all`

Damit dies für Zweige ohne Tracking-Upstream automatisch geschieht, könnt ihr
folgendes konfigurieren:

.. code-block:: console

   $ git config --global push.autoSetupRemote true

Entfernte Zweige löschen
~~~~~~~~~~~~~~~~~~~~~~~~

Mit ``git branch -d`` löscht ihr die Zweige nur lokal. Um sie auch auf dem
entfernten Server zu löschen, könnt ihr folgendes eingeben:

:samp:`$ git push origin --delete [{BRANCH_NAME}]`

Um entfernte Zweige auch bei euch lokal zu entfernen, könnt ihr ``git fetch``
mit der Option ``--prune`` oder ``-p`` ausführen. Ihr könnt dieses Verhalten
auch zur Standardeinstellung machen, indem ihr ``fetch.prune`` aktiviert:

.. code-block:: console

   $ git config --global fetch.prune true

.. seealso::
   `PRUNING <https://git-scm.com/docs/git-fetch#_pruning>`_

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
