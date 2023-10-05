.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git rebase
==========

Die Befehle ``git rebase`` und ``git merge`` ermöglichen das Zusammenführen von
:doc:`branch`. Während ``git merge`` immer ein sich vorwärtsbewegender
Änderungsansatz ist, verfügt ``git rebase`` über leistungsfähige Funktionen zum
Umschreiben der Historie.
Hier wollen wir die Konfiguration, Anwendungsfälle und Fallstricke
genauer betrachten.

Dabei verschiebt ``git rebase`` eine Folge von Commits zu einem neuen
Basis-Commit und kann so für :doc:`workflows/feature-branches`-Workflows
nützlich sein. Intern erreicht Git dies, indem es neue Commits erstellt und
diese auf die angegebene Basis anwendet; die gleichaussehenden Commits von
Zweigen sind also völlig neue Commits.

Der Hauptgrund für ``git rebase`` ist, einen linearen Projektverlauf
aufrechtzuerhalten. Wenn sich der Hauptzweig weiterentwickelt hat, seit ihr mit
der Arbeit an einem Funktionszweig begonnen habt, wollt ihr vielleicht die
letzten Aktualisierungen des Hauptzweigs in eurem Funktionszweig erhalten, aber
die Historie eures Zweigs sauber halten. Dies hätte den Vorteil, dass ihr
später ein sauberes ``git merge`` eures Funktionszweiges in den Hauptzweig
durchführen könntet. Diese *saubere Historie* erleichtert euch auch, eine
Regression mit :doc:`advanced/bisect` zu finden. Ein realistischeres Szenario wäre
folgendes:

#. Im Hauptzweig wird ein Fehler in einer Funktion festgestellt, die früher
   einmal fehlerfrei funktionierte.
#. Durch die *saubere Historie* des Hauptzweigs sollte :doc:`log` schnell
   Rückschlüsse ermöglichen.
#. Sollte :doc:`log` nicht zum gewünschten Ergebnis führen, hilft vermutlich
   :doc:`git bisect <advanced/bisect>` weiter. Dabei hilft ``git bisect`` die saubere
   Git-Historie bei der Suche nach der Regression.

.. warning::
    Die veröffentlichte Historie sollte nur in sehr seltenen Ausnahmefällen
    geändert werden, da die alten Commits durch neue ersetzt und es so aussehen
    würde, als wäre dieser Teil der Projektgeschichte plötzlich verschwunden.

.. note::

   ``git rebase`` wird auch kurz in :doc:`advanced/jupyter-config`
   und :doc:`workflows/feature-branches` behandelt

Rebase abhängiger Zweige mit ``–update-refs``
---------------------------------------------

Wenn ihr an einem großen Feature arbeitet, ist es oft hilfreich, die Arbeit auf
mehrere Zweige zu verteilen, die aufeinander aufbauen.

Diese Zweige können jedoch umständlich zu verwalten sein, wenn ihr den Verlauf
in einem früheren Zweig überschreiben müsst. Da jeder Zweig von den vorherigen
Zweigen abhängt, führt das Umschreiben von Commits in einem Zweig dazu, dass die
nachfolgenden Zweige nicht mehr mit der Historie verbunden sind.

Git 2.38 wird mit einer neuen ``--update-refs``-Option für ``git rebase``
ausgeliefert, die solche Aktualisierungen für euch durchführt , ohne dass ihr
jeden einzelnen Zweig manuell aktualisieren müsst und ohne dass die
nachfolgenden Zweige ihre Historie verlieren.

Wenn ihr diese Option bei jedem Rebase verwenden möchtet, könnt ihr ``git config
--global rebase.updateRefs true`` ausführen, damit sich Git so verhält, als ob
die Option ``--update-refs`` immer angegeben ist.

.. seealso::
   `rebase: add --update-refs option
   <https://lore.kernel.org/git/3ec2cc922f971af4e4a558188cf139cc0c0150d6.1657631226.git.gitgitgadget@gmail.com/>`_


Commits mit rebase löschen
--------------------------

.. code-block:: console

  $ git rebase -i SHA origin/main

``-i``
interaktiver Modus, in dem euer Standardeditor geöffnet wird und eine
Liste aller Commits nach dem zu entfernenden Commit mit dem Hash-Wert
:samp:`{SHA}` angezeigt wird, :abbr:`z.B. (zum Beispiel)`:

.. code-block:: console

   pick d82199e Update readme
   pick 410266e Change import for the interface
   …

Wenn ihr nun eine Zeile entfernt, so wird dieser Commit nach dem
Speichern und Schließen des Editors gelöscht. Anschließend kann das
entfernte Repository aktualisiert werden mit:

.. code-block:: console

    $ git push origin HEAD:main -f

rebase zum Ändern einer Commit-Nachricht
----------------------------------------

Dies lässt sich ebenfalls einfach mit ``rebase`` realisieren wobei ihr in
eurem Editor nicht die Zeile löschen sondern in der Zeile ``pick`` durch
``r`` (*reword*) ersetzen müsst.
