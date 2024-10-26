.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Arbeitsbereiche
===============

.. figure:: git-workspaces.svg
   :alt: Git Arbeitsbereiche

Git verwaltet mehrere Speicherorte oder **Workspaces**, in denen Dateien
gespeichert werden:

local working copy
    enthält Dateien und Verzeichnisse, die normal bearbeitet werden.
staging area
    enthält Änderungen an Dateien, die in die Versionsgeschichte geschrieben
    werden sollen.
local repository
    enthält die gesamte Historie aller Dateien im Projekt.
remote repository
    enthält ebenfalls die gesamte Historie, ist aber auf einem entfernten Server
    gespeichert.
stash
    enthält Änderungen, die vorübergehend an einem anderen Ort gespeichert
    werden, um sie aus dem aus dem Weg zu schaffen.

Basic Git commands
------------------

The following basic Git commands move changes between these workspaces.

``git add``
    fügt Dateien aus dem Arbeitsverzeichnis dem Bühnenbereich (:abbr:`engl.
    (englisch)`: *staging area*) hinzu.
``git reset HEAD``
    stellt eine Datei im Arbeitsbereich aus dem Bühnenbereich wieder her.
``git stash``
    verschiebt Dateien aus dem Arbeitsbereich in ein Versteck (:abbr:`engl.
    (englisch)`: *stash*).
``git stash pop``
    holt Dateien aus dem Versteck in den Arbeitsbereich.
``git commit``
    schreibt Änderungen im Bühnenbereich in das lokale Repository.
``git pull``
    kopiert Änderungen aus dem entfernten in das lokale Repository und aktualisiert das Arbeitsverzeichnis.
``git push``
    kopiert Änderungen aus dem lokalen Repository in das entfernte (:abbr:`engl.
    (englisch)`: *remote*) Repository.

    :samp:`git push -u {UPSTREAM} {BRANCHNAME}`
        ``-u`` (Langform ``--set-upstream``)
            erlaubt die Angabe eines entfernten Repository und des darin
            enthaltenen Zweiges.

        :samp:`{UPSTREAM}`
            ist der Name des entfernten Repository, üblicherweise ``origin``.

        :samp:`{BRANCHNAME}`
            ist der Name des Zweiges im entfernten Repository, üblicherweise
            derselbe Name wie im lokalen Repository.
