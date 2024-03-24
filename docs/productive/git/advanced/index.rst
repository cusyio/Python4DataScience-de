.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Fortgeschrittenes Git
=====================

:doc:`git cherry-pick <cherry-pick>`
    ermöglicht euch, beliebige Git-Commits anhand ihres Hash-Wertes dem
    aktuellen ``HEAD`` anzuhängen.
:doc:`git bisect <bisect>`
    ermöglicht euch, einen Git-Commit, der eine Regression eingeführt hat,
    schnell zu finden.
:doc:`git notes <notes>`
    fügt Textnotizen zu Commits, Tags und anderen Objekten hinzu.
:doc:`hooks/index`
    sind Skripte, die bei bestimmten Ereignissen in einem Git-Repository
    automatisch ausgeführt werden.
:doc:`Jupyter Notebooks <jupyter-notebooks>`
    können zu Problemen führen bei der Verwaltung mit Git.
:doc:`Binärdateien <binary-files>`
    können in Git so konfiguriert werden, dass sinnvolle Diffs angezeigt werden.
:doc:`vs-code/index`
    kann eine bereits vorhandene Git-Installation nutzen um die entsprechenden
    Funktionalitäten zur Verfügung zu stellen.
:doc:`gitlab/index`
    ist eine Webanwendung zur Versionsverwaltung auf Basis von Git.
:doc:`git-big-picture`
    visualisiert Git-Repositories als :abbr:`DAGs (gerichteter azyklischer
    Graph, engl.: directed acyclic graph)`.
:doc:`etckeeper`
    ist eine Sammlung von Werkzeugen, mit denen das :file:`/etc`-Verzeichnis in
    einem Git-Repository verwaltet werden kann.
:doc:`internals`
    verweist auf Artikel zu Git’s Datenbank-Interna.

.. toctree::
   :hidden:

   cherry-pick
   bisect
   notes
   hooks/index
   jupyter-notebooks
   binary-files
   vs-code/index
   gitlab/index
   git-big-picture
   etckeeper
   internals
