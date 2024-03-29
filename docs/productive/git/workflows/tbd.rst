Trunk-Based Development
=======================

`Trunk Based Development <https://trunkbaseddevelopment.com>`_ empfiehlt
kurzlebige Themenzweige, die zu einem einzigen ``main``-Zweig zusammengeführt
werden. :abbr:`TBD (Trunk-Based Development)` führt zu einem leicht zu
verwaltenden linearen Verlauf.

Trunk Based Development eignet sich hervorragend für ein-Personen-Projekte.
Verzweigungen sind nicht notwendig, das Verwenden einer Versionskontrolle zahlt sich
aber auch für einen selbst schnell aus.

In kleineren Entwicklungsteams übertragen wir
kleine Commits direkt in den Trunk (oder den ``main``-Branch), wobei vor der
Integration zunächst der Build erfolgreich ausgeführt sein muss.

Trunk Based Development in großem Maßstab wird am besten mit kurzlebigen
Feature-Zweigen durchgeführt, wobei eine Person maximal über ein paar Tage
entwickelt und die Änderungen anschließend mit Pull- oder Merge-Requests,
Code-Review und Build-Automatisierung in den Trunk (oder ``main``) integriert
werden.
