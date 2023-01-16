Repos aufteilen
===============

Hier beschreibe ich, wie ihr ein Git-Repository aufteilen könnt, ohne die
jeweils zugehörige Historie zu verlieren. 

Szenario und Ziele
------------------

Wir wollen aus dem Jupyter-Tutorial-Repository denjenigen Teil herauslösen, der
sich mit der Visualisierung der Daten befasst: ``docs/viz/``. Die
Herausforderung besteht darin, dass die Historie für das
``docs/viz/``-Verzeichnis mit anderen Änderungen vermischt ist. Daher klonen wir
zunächst zweimal dasselbe Repository:

.. code-block:: console

    $ git clone git@github.com:veit/jupyter-tutorial.git
    Klone nach 'jupyter-tutorial' …
    $ git clone git@github.com:veit/jupyter-tutorial.git pyviz-tutorial
    Klone nach 'pyviz-tutorial' …

Der nächste Schritt besteht darin, die unerwünschten Historien aus jedem der
beiden Repos herauszufiltern. Hierzu müssen wir uns jedoch nicht für jeden
Commit den Verzeichnispfad anschauen, sondern können die
``filter-branch``-Option ``-subdirectory-filter`` verwenden um die Historie
umzuschreiben und diejenigen Commits zu behalten, die tatsächlich den Inhalt
eines bestimmten Unterordners betreffen:

.. note::
   ``-subdirectory-filter`` betrachtet das Unterverzeichnis auch als Wurzel des
   gesamten Repo.

Der aktuelle Zweig, in diesem Fall ``main``, wird umgeschrieben und nur die
Historie des gewünschten Ordners extrahiert:

.. code-block:: console

    $ git filter-branch --subdirectory-filter docs/viz/ -- main
    …
    Proceeding with filter-branch...
    Ref 'refs/heads/main' was rewritten

.. warning::
   ``git-filter-branch`` kann die Historie jedoch auch fehlerhaft umschreiben. 
   Stattdessen sollte besser `git filter-repo
   <https://github.com/newren/git-filter-repo/>`_ verwendet werden, :abbr:`s.a.
   (siehe auch)` `filter-branch <https://git-scm.com/docs/git-filter-branch>`_.

Anstatt nur einen Zweig, in diesem Fall ``main``, zu überschreiben, könnt ihr
auch mehrere Zweige und sogar Tags überschreiben. Natürlich kann nicht jeder
Tag in der neuen Historie erfolgreich umgeschrieben werden: der getaggte Commit
muss innerhalb der umgeschriebenen Commits liegen, damit der Tag wieder
angewendet werden kann.

Wie ihr euch vielleicht vorstellen könnt, kann dieser Vorgang schädlich sein.
Aus diesem Grund erstellt ``filter-branch`` eine Sicherungskopie von jedem
``ref``, den es verändert, als ``original/refs/*``. Git hat zwar die Commits
umgeschrieben und eine Kopie davon erstellt, die alten Commits bleiben jedoch
durch die ursprünglichen Referenzen erhalten. Um also eine Referenz
wiederherzustellen, könnt ihr sie auf das Original zurückführen mit

.. code-block::

    $ git reset --hard original/refs/heads/main

Wenn ihr die alte Historie sofort loswerden wollt, müsst ihr alle Verweise
darauf löschen und ein Verfallsdatum für diese toten Objekte aus dem Reflog
erzwingen, da das Reflog verhindern könnte, dass diese Objekte tatsächlich
gelöscht werden. Sobald ihr alle Verweise gelöscht habt, könnt ihr eine
Garbage-Collection für das Reflog starten, um diese alten Objekte endgültig zu
entfernen.

Das Einzige, was jetzt noch zu tun ist, ist die Anpassung de Remotes des neuen
Repos, da es die lokale Kopie des Jupyter-Tutorial-Repos als ihre
Ursprungs-Remote haben werden.

Für unser Jupyter-Tutorial-Repository können wir einen anderen Ansatz wählen, da
wir die gesamte Historie, die zum ``docs/viz/``-Verzeichnis gehört, löschen
wollen:

.. code-block::

   $ git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch opt/viz' --prune-empty
    …
    Proceeding with filter-branch...
    Ref 'refs/heads/main' was rewritten

Dies wird bei einem großen Projektarchiv eine Weile dauern: Git muss jeden
Commit durchgehen und alle Vorkommen von ``docs/viz`` aus dem Diff löschen.

``git rm -r -cached -ignore-unmatch docs/viz``
    wird auf den Index jeder Übertragung angewendet, wodurch ``docs/viz`` aus
    dem Index gelöscht wird, der Arbeitsbaum jedoch unverändert bleibt.

``-prune-empty``
    entfernt mögliche leere Commits, die von der Operation herrühren könnten.
