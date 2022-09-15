Git Cherry-Pick
===============

``git cherry-pick`` ermöglicht euch, beliebige Git-Commits anhand ihres
Hash-Wertes dem aktuellen ``HEAD`` anzuhängen. Beim Cherry-Picking wird ein
Commit aus einem Branch ausgewählt und auf einen anderen angewendet.

``git cherry-pick`` kann auch hilfreich sein, um Änderungen rückgängig zu
machen, wenn beispielsweise ein Commit versehentlich für den falschen Branch
durchgeführt wurde, könnt ihr zu dem Branch wechseln, in dem die Änderung
eigentlich vorgenommen weerden sollte, und den Commit dann per Cherry-Pick auf
diesen Branch übertragen.

Beim Cherry-Picking entstehen jedoch üblicherweise doppelte Commits, und in
vielen Fällen bevorzugen wir daher eher Git Merges. Dennoch kann sich ``git
cherry-pick`` für einige Szenarien sehr gut eignen, :abbr:`z.B. (zum Beispiel)`
für :ref:`release-branches`-Workflows.
