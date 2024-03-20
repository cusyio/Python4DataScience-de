.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git Best Practices
==================

Macht früh Commits
------------------

Macht euren ersten Commit nachdem ihr die initiale Installation fertiggestellt
habt und noch bevor ihr erste Änderungen vornehmt.

Verwendet ihr ein Cookiecutter-Template, committet unmittelbar nach den
folgenden Schritten:

.. code-block:: console

  $ pipenv run cookiecutter https://github.com/veit/cookiecutter-namespace-template.git
  full_name [Veit Schiele]:
  email [veit@cusy.io]:
  github_username [veit]:
  project_name [cusy.example]:
  …

Anschließend könnt ihr die initialen Änderungen in ein neu erstelltes, leeres
Repository auf GitHub einchecken:

  .. code-block:: console

    $ cd cusy.example
    $ git init
    $ git add *
    $ git commit -m 'Initial commit'
    $ git remote add origin ssh://git@github.com:veit/cusy.example.git
    $ git push -u origin main

Schließt unerwünschte Dateien aus
---------------------------------

Temporäre Dateien, Jupyter Checkpoints und builds haben in einem Repository
nichts zu suchen. Passwörter erst recht nicht. Die :file:`.gitignore`-Datei
enthält eine Liste von Dateipfaden, die git nicht hinzufügt, außer ihr wünscht
das explizit.

Eine Vorlage mit :file:`.gitignore`-Einträgen für Python-Projekte findet ihr im
Repository `dotfiles <https://github.com/veit/dotfiles>`_. Auf der Website
`gitignore.io <https://gitignore.io/>`_ könnt ihr euch
:file:`.gitignore`-Vorlagen für euer Projekt generieren lassen.  Auch die
:file:`.gitignore`-Datei gehört in das Repository eingecheckt:

.. code-block:: console

  $ git add .gitignore
  $ git commit -m 'Add .gitignore file'

Falls ihr versehentlich schon entsprechende Dateien in euer Git-Repository
eingecheckt habt, beispielsweise einen :file:`.ipynb_checkpoints`-Ordner, könnt
ihr diese wieder entfernen mit:

.. code-block:: console

  $ git rm -r .ipynb_checkpoints/


Schreibt eine :file:`README`-Datei
----------------------------------

Auch eine :file:`README`-Datei sollte in jedem Repository vorhanden sein, in
der das Deployment und der grundsätzliche Aufbau des Codes beschrieben wird.

Macht oft Commits
-----------------

Nach jeder abgeschlossenen Aufgabe und Teilaufgabe sollte ein Commit erfolgen.
Auch nicht abgeschlossene Aufgaben können auf git gesichert werden. Als
Faustregel gilt: Committe mindestens einmal pro Tag, nämlich kurz vor
Feierabend. In Stoßzeiten kann es auch vorkommen, dass ihr alle 10 Minuten
committet.

Häufige Commits erleichtern euch:

* das Eingrenzen von Fehlern
* das Verständnis für den Code
* die zukünftige Wartung und Pflege.

Falls ihr doch einmal mehrere Änderungen an einer Datei durchgeführt habt, könnt
ihr diese auch später noch in mehrere Commits aufteilen mit:

.. code-block:: console

  $ git add -p my-changed-file.py

Ändert die veröffentlichte Historie nicht
-----------------------------------------

Auch wenn ihr zu einem späteren Zeitpunkt herausfindet, dass ein Commit, der mit
``git push`` bereits veröffentlicht wurde, einen oder mehrere Fehler enthält, so
solltet ihr dennoch niemals versuchen, diesen Commit ungeschehen zu machen.
Vielmehr solltet ihr durch weitere Commits den oder die aufgetretenen Fehler zu
beheben.

.. warning::

   Die große Ausnahme zu dieser Regel sind Workflows mit ``git-rebase`` wie in
   :doc:`workflows/feature-branches`.

Wählt einen Git-Workflow
------------------------

Wählt einen Workflow, der am besten zu eurem Projekt passt. Projekte sind
keineswegs identisch und ein Workflow, der zu einem Projekt passt, muss nicht
zwingend auch in einem anderen Projekt passen. Auch kann sich initial ein
anderer Workflow empfehlen als im weiteren Fortschritt des Projekts.

Schreibt aussagekräftige Commit-Nachrichten
-------------------------------------------
Aufschlussreiche und beschreibende Commit-Nachrichten erleichtern euch die
Arbeit im Team ungemein. Sie ermöglichen anderen und euch selbst, eure
Änderungen zu verstehen. Auch sind sie zu einem späteren Zeitpunkt hilfreich um
nachvollziehen zu können, welches Ziel mit dem Code erreicht werden sollte.

Üblicherweise sollten kurze, 50–72 Zeichen lange Nachrichten angegeben werden,
die in einer Zeile ausgegeben werden, `z.B. (zum Beispiel)` mit ``git log
--oneline``.

Mit ``git blame`` könnt ihr euch auch später noch für jede Zeile angeben lassen,
in welcher Revision und von welchem Autor sie kam. Weitere Informationen hierzu
findet ihr in der Git-Dokumentation: `git-blame
<https://git-scm.com/docs/git-blame>`_.

.. note::
  * `A Note About Git Commit Messages
    <https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_

Gitmojis
~~~~~~~~

Wenn ihr Gitmojis in euren Commit-Nachrichten verwendet, könnt ihr später leicht
die Absicht des Commits erkennen.

.. note::

  * `gitmoji.dev <https://gitmoji.dev/>`_
  * `github.com/carloscuesta/gitmoji
    <https://github.com/carloscuesta/gitmoji>`_
  * `github.com/carloscuesta/gitmoji-cli
    <https://github.com/carloscuesta/gitmoji-cli>`_
  * `Visual Studio Code Extension
    <https://marketplace.visualstudio.com/items?itemName=seatonjiang.gitmoji-vscode>`_

GitLab
~~~~~~

GitLab interpretiert bestimmte Commit-Nachrichten auch als Links, :abbr:`z.B.
(zum Beispiel)`:

.. code-block:: console

  $ git commit -m "Expand section on meaningful commit messages (#21: Add
  multi-line commit messages and close group/project#22)"

* zu Issues: :samp:`#{NUMBER}`

  * auch in anderen Projekten: :samp:`{GROUP/PROJECT}#{NUMBER}`

* zu Merge Requests: :samp:`!{NUMBER}`
* zu Snippets::samp:`${NUMBER}`

Dabei sollte es zu jedem Commit mindestens ein Ticket geben, das ausführlichere
Hinweise zu den Änderungen geben sollte. Alternativ könnt ihr auch mehrzeilige
Commit-Nachrichten schreiben, die diese Informationen enthalten, :abbr:`z.B.
+(zum Beispiel)` mit:

.. code-block:: console

   $ git commit -m 'Expand section on meaningful commit messages' -m 'Fix the serious problem'

Oder, wenn ihr nur :samp:`git commit` eingebt, öffnet sich euer Editor,
:abbr:`z.B. (zum Beispiel)` mit folgendem Text:

.. code-block:: ini

   # Bitte geben Sie eine Commit-Beschreibung für Ihre Änderungen ein. Zeilen,
   # die mit '#' beginnen, werden ignoriert, und eine leere Beschreibung
   # bricht den Commit ab.
   #
   # Auf Branch main

Git erwartet, dass ihr eure Commit-Nachricht am Anfang der Datei einfügt.
Nachdem ihr die Bearbeitung der Datei abgeschlossen habt, liest Git ihren Inhalt
und fährt fort. Es *bereinigt* die Datei, indem es mit ``#`` kommentierte Zeilen
und nachfolgende Leerzeilen entfernt. Wenn die Nachricht nach dem Aufräumen leer
ist, bricht Git den Commit ab – das ist praktisch, wenn ihr merkt, dass ihr
etwas vergessen habt. Andernfalls wird der Commit mit dem verbleibenden Inhalt
erstellt. GitLab verwendet ``#`` jedoch als Präfix für die Nummer eines Items.
Diese doppelte Bedeutung von ``#`` kann zu einer Verwechslung führen, wenn ihr
eine Commit-Nachricht schreibt, die sich auf ein Item bezieht:

.. code-block:: ini

   Expand section on meaningful commit messages

   #21: Add multi-line commit messages

   # Bitte geben Sie eine Commit-Beschreibung für Ihre Änderungen ein. Zeilen,
   # die mit '#' beginnen, werden ignoriert, und eine leere Beschreibung
   # bricht den Commit ab.
   #
   # Auf Branch main
   # Ihr Branch ist auf demselben Stand wie 'origin/main'.
   #
   # Zum Commit vorgemerkte Änderungen:
   #       geändert:       productive/git/best-practices.rst
   #

Üblicherweise entfernt Git die Zeile, die mit #21 beginnt, so dass die Nachricht
wie folgt aussieht:

.. code-block:: ini

   Expand section on meaningful commit messages

Vermeidet dieses Missgeschick, indem ihr einen alternativen Bereinigungsmodus
namens *Scissors* verwendet. Ihr könnt ihn global aktivieren mit:

.. code-block:: console

   $ git config --global commit.cleanup scissors

Dann beginnt Git jede neue Commit-Nachricht mit der *Scissors*-Zeile:

.. code-block:: ini

   # ------------------------ >8 ------------------------
   # Ändern oder entfernen Sie nicht die obige Zeile.
   # Alles unterhalb von ihr wird ignoriert.
   #
   # Auf Branch main
   # Ihr Branch ist auf demselben Stand wie 'origin/main'.
   #
   # ...
   #

Co-Autoren angeben
~~~~~~~~~~~~~~~~~~

Wenn ihr mit einem Teammitglied an einem Commit arbeiten, ist es gut, dessen
Beitrag mit dem ``co-authored-by``-Trailer anzuerkennen. Trailer sind
zusätzliche Metadaten am Ende der Commit-Nachricht, die eine :samp:`{KEY}:
{VALUE}`-Syntax verwenden und wiederholt werden kann, um mehrere Werte
aufzulisten:

.. code-block:: ini

   Expand section on meaningful commit messages

   #21: Add multi-line commit messages

   co-authored-by: Kristian Rother <kristian.rother@cusy.io>
   co-authored-by: Frank Hofmann <frank.hofmann@cusy.io>

GitLab analysiert die ``co-authored-by``-Zeilen, um alle Avatare des Commits
anzuzeigen und auch die Profilstatistiken der Co-Autoren zu aktualisieren
:abbr:`usw (und so weiter)`.

Wartet euer Repository regelmäßig
---------------------------------

Folgende Wartungsarbeiten solltet ihr regelmäßig durchführen:

Validiert das Repo
~~~~~~~~~~~~~~~~~~

Der Befehl ``git fsck`` prüft, ob alle Objekte in der internen Datenstruktur von
Git noch miteinander verknüpft sind.

Komprimiert das Repo
~~~~~~~~~~~~~~~~~~~~

Spart Speicherplatz mit den Befehlen ``git gc`` bzw. ``git gc --aggressive``.

.. seealso::
   * `git gc <https://git-scm.com/docs/git-gc>`_
   * `Git Interna - Wartung und Datenwiederherstellung
     <https://git-scm.com/book/de/v2/Git-Interna-Wartung-und-Datenwiederherstellung>`_

Bereinigt Remote Tracking Branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nicht genutzte Zweige auf einem entfernten Server lassen sich mit ``git remote
update --prune`` löschen. Noch besser ist, wenn ihr die Standardeinstellung so
ändert, dass entfernt gelöschte Zweige auch bei ``git fetch`` und ``git pull``
bei euch lokal gelöscht werden. Dies erreicht ihr mit:

.. code-block:: console

   $ git config --global fetch.prune true

Überprüft vergessene Arbeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit ``git stash list`` seht ihr eine List von gespeicherten stashes. Diese könnt
ihr mit ``git stash drop`` entfernen.

Überprüft eure Repositories auf unerwünschte Dateien
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit `Gitleaks <https://github.com/zricethezav/gitleaks>`_ könnt ihr eure
Repositories regelmäßig auf ungewollt gespeicherte Zugangsdaten überprüfen.

Ihr könnt Gitleaks auch automatisch als GitLab-Action ausführen. Hierzu müsst
ihr die `Secret-Detection.gitlab-ci.yml
<https://gitlab.com/gitlab-org/gitlab/-/blob/master/lib/gitlab/ci/templates/Jobs/Secret-Detection.gitlab-ci.yml>`_-Vorlage
:abbr:`z.B. (zum Beispiel)` in eine Stufe namens ``secrets-detection`` in
eurer ``.gitlab-ci.yml``-Datei einbinden:

.. code-block:: yaml

   include:
   - template: Security/Secret-Detection.gitlab-ci.yml

Die Vorlage erstellt *Secret Detection*-Aufträge in eurer CI/CD-Pipeline und
durchsucht den Quellcode eures Projekts nach *Secrets*. Die Ergebnisse werden
als `Secret Detection Report Artefakt
<https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportssecret_detection>`_
gespeichert, den ihr später herunterladen und analysieren könnt.

.. seealso::

   * `GitLab Secret Detection
     <https://docs.gitlab.com/ee/user/application_security/secret_detection/>`_

Mit :ref:`git-filter-repo` könnt ihr unerwünschte Dateien oder Zugangsdaten aus
eurer Git-Historie entfernen.
