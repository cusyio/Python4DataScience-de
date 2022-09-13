Git rebase
==========

Zwar wird ``git rebase`` auch kurz in :doc:`jupyter-config`,
:doc:`best-practices` und :doc:`workflows/feature-branches` behandelt, hier
wollen wir nun jedoch genauer die Konfiguration, Anwendungsfälle und Fallstricke
betrachten.

Dabei ermöglicht ``git rebase`` neben ``git merge`` das Zusammenführen von
:doc:`branch`. Während ``git merge`` immer ein sich vorwärtsbewegender
Änderungsansatz ist, verfügt ``git rebase`` über leistungsfähige Funktionen zum
Umschreiben der Historie.

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
Regression mit :doc:`bisect` zu finden. Ein realistischeres Szenario wäre
folgendes:

#. Im Hauptzweig wird ein Fehler in einer Funktion festgestellt, die früher
   einmal fehlerfrei funktionierte.
#. Durch die *saubere Historie* des Hauptzweigs sollte :doc:`log` schnell
   Rückschlüsse ermöglichen.
#. Sollte :doc:`log` nicht zum gewünschten Ergebnis führen, hilft vermutlich
   :doc:`git bisect <bisect>` weiter. Dabei hilft ``git bisect`` die saubere
   Git-Historie bei der Suche nach der Regression.

.. warning::
    Die veröffentlichte Historie sollte nur in sehr seltenen Ausnahmefällen
    geändert werden, da die alten Commits durch neue ersetzt und es so aussehen
    würde, als wäre dieser Teil der Projektgeschichte plötzlich verschwunden.
