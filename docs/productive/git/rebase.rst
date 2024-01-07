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
   :doc:`git bisect <advanced/bisect>` weiter. Dabei hilft ``git bisect`` die
   saubere Git-Historie bei der Suche nach der Regression.

.. warning::
    Die veröffentlichte Historie sollte nur in sehr seltenen Ausnahmefällen
    geändert werden, da die alten Commits durch neue ersetzt und es so aussehen
    würde, als wäre dieser Teil der Projektgeschichte plötzlich verschwunden.

.. seealso::
   `git rebase: what can go wrong?
   <https://jvns.ca/blog/2023/11/06/rebasing-what-can-go-wrong-/#undoing-a-rebase-is-hard>`_

.. note::
   ``git rebase`` wird auch kurz in :doc:`advanced/jupyter-notebooks`
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


Commits mit ``git rebase`` löschen
----------------------------------

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

Ändern einer Commit-Nachricht mit ``git rebase``
------------------------------------------------

Dies lässt sich ebenfalls einfach mit ``git rebase`` realisieren wobei ihr in
eurem Editor nicht die Zeile löschen sondern in der Zeile ``pick`` durch ``r``
(*reword*) ersetzen müsst.

``rebase`` als Standard-``git pull``-Strategie
----------------------------------------------

Normalerweise holt und führt ``git pull`` neue Remote-Commits ohne Probleme
zusammen. Meistens werden nur neue Commits aus dem entfernten Zweig hinzugefügt,
ein :abbr:`sog. (sogenannter)` Fast-Forward-Merge. Wenn aber sowohl der lokale
als auch der entfernte Zweig neue Commits haben, weichen die Zweige voneinander
ab. Ihr müsst dann die verschiedenen Historien irgendwie in Einklang bringen.
Standardmäßig führt ab Git 2.33.1 jede Abweichung dazu, dass ``git pull`` anhält
und die folgende Meldung ausgibt:

.. code-block:: console

   $ git pull
   Hinweis: Sie haben abweichende Branches und müssen angeben, wie mit diesen
   Hinweis: umgegangen werden soll.
   Hinweis: Sie können dies tun, indem Sie einen der folgenden Befehle vor dem
   Hinweis: nächsten Pull ausführen:
   Hinweis:
   Hinweis:   git config pull.rebase false  # Merge
   Hinweis:   git config pull.rebase true   # Rebase
   Hinweis:   git config pull.ff only       # ausschließlich Vorspulen
   Hinweis:
   Hinweis: Sie können statt "git config" auch "git config --global" nutzen, um
   Hinweis: einen Standard für alle Repositories festzulegen. Sie können auch die
   Hinweis: Option --rebase, --no-rebase oder --ff-only auf der Kommandozeile nutzen,
   Hinweis: um das konfigurierte Standardverhalten pro Aufruf zu überschreiben.
   Schwerwiegend: Es muss angegeben werden, wie mit abweichenden Branches umgegangen werden sollen.

Die Hinweise erlauben drei Optionen:

``git config pull.rebase false``
    führt die lokalen und entfernten Commits zusammen. Vor Git 2.33.1 verwendete
    Git immer diese Zusammenführung.
``git config pull.rebase true``
    Die lokalen Commits werden auf die Remote-Commits übernommen.
``git config pull.ff only``
    führt bei divergierenden Zweigen immer zu einen Fehler. Ihr könnt dann von
    Fall zu Fall mit ``--no-rebase`` (was ``merge`` bedeutet) oder ``--rebase``
    entscheiden, ob ihr mergen oder rebasen wollt.

.. tip::
   Ich empfehle ``git config pull.rebase true``, da Merging verwirrend sein
   kann. Das Rebasen der lokalen Commits auf die entfernten macht die Geschichte
   linear, was verständlicher ist.

Macht ``rebase`` zu eurer Standardstrategie mit:

.. code-block:: console

   $ git config --global pull.rebase interactive

Wenn ``git pull`` dann auf abweichende lokale und entfernte Zweige stößt, wird
es ein ``rebase`` durchgeführt:

.. code-block:: console

   $ git pull
   automatischer Merge von README.md
   KONFLIKT (Inhalt): Merge-Konflikt in README.md
   Fehler: Konnte e50dfe5... nicht anwenden
   Hinweis: Resolve all conflicts manually, mark them as resolved with
   Hinweis: "git add/rm <conflicted_files>", then run "git rebase --continue".
   Hinweis: You can instead skip this commit: run "git rebase --skip".
   Hinweis: To abort and get back to the state before "git rebase", run "git rebase --abort".
   Konnte e50dfe5... nicht anwenden
