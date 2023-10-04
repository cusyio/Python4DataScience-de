.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Arbeitsbereiche
===============

.. figure:: git-workspaces.png
   :alt: Git Arbeitsbereiche

``git add``
    fügt Dateien aus dem Arbeitsverzeichnis dem Bühnenbereich (engl.: *staging
    area*) hinzu.
``git reset HEAD``
    stellt eine Datei im Arbeitsbereich aus dem Bühnenbereich wieder her.
``git stash``
    verschiebt Dateien aus dem Arbeitsbereich in ein Versteck (engl.: *stash*).
``git stash pop``
    holt Dateien aus dem Versteck in den Arbeitsbereich.
``git push``
    verschiebt Dateien aus dem Bühnenbereich in das Repository.

    :samp:`git push -u {origin} {main}`
        ``-u`` legt die Upstream-Referenz für jeden Zweig fest, deren Argumente
        anschließend in ``git pull`` o.ä. nicht mehr explizit festgelegt werden
        müssen. In unserem Beispiel wird ``main`` im entfernten Repository
        referenziert.

        Hierbei bedeuten die einzelnen Parameter:

        ``-u`` (Langform ``--set-upstream``)
            Lege die Upstream-Referenz für jeden Zweig fest.

        ``origin``
            Benutze als Herkunftszweig ``origin``.

        ``main``
            Benutze den Zweig ``main`` im entfernten Repository.
