Git Cherry-Pick
===============

``git cherry-pick`` ermöglicht euch, beliebige Git-Commits anhand ihres
Hash-Wertes dem aktuellen ``HEAD`` anzuhängen. Beim Cherry-Picking wird ein
Commit aus einem Branch ausgewählt und auf einen anderen angewendet, :abbr:`z.B.
(zum Beispiel)`:

.. code-block:: console

   $ git checkout 3.10
   $ git cherry-pick 61de025
   [3.10 b600967] Fix bug #17
    Date: Thu Sep 15 11:17:35 2022 +0200
    1 file changed, 9 insertions(+)

Dabei kann ``git cherry-pick`` mit verschiedenen Optionen eingesetzt werden:

``--edit``, ``-e``
    übernimmt nicht die bestehende Commit-Nachricht sondern ermöglicht euch,
    eine eigene Commit-Nachricht für diesen Cherry-Pick zu erstellen.
``--no-commit``, ``-n``
    erstellt keinen neuen Commit sondern verschiebt die Inhalte des Commits in
    das Arbeitsverzeichnis.
``--signoff``, ``-s``
    fügt am Ende der Commit-Nachricht eine Signaturzeile mit ``Signed-off-by``
    hinzu.

``git cherry-pick`` kann hilfreich sein, um Änderungen rückgängig zu machen,
wenn beispielsweise ein Commit versehentlich für den falschen Branch
durchgeführt wurde, könnt ihr zu dem Branch wechseln, in dem die Änderung
eigentlich vorgenommen weerden sollte, und den Commit dann per Cherry-Pick auf
diesen Branch übertragen.

Beim Cherry-Picking entstehen jedoch üblicherweise doppelte Commits, und in
vielen Fällen bevorzugen wir daher eher Git Merges. Dennoch kann sich ``git
cherry-pick`` für einige Szenarien sehr gut eignen, :abbr:`z.B. (zum Beispiel)`
für :ref:`release-branches`-Workflows.
