Weitere pre-commit-Hooks
========================

Die vom pre-commit-Framework verwalteten Hooks beschränken sich nicht darauf,
vor Commits ausgeführt zu werden; sie können auch für andere Git-Hooks verwendet
werden:

``post-commit``
    Ab Version 2.4.0 kann das Framework auch `post-commit
    <https://git-scm.com/docs/githooks#_post_commit>`_-Hooks ausführen mit:

    .. code-block:: console

        $ pipenv run pre-commit install --hook-type post-commit
        pre-commit installed at .git/hooks/post-commit

    Da ``post-commit`` jedoch nicht auf Dateien wirkt, müssen all diese Hooks
    ``always_run`` setzen:

    .. code-block:: yaml

        - repo: local
          hooks:
          - id: post-commit-local
            name: post commit
            always_run: true
            stages: [post-commit]
            # …

``pre-merge``
    Ab Git 2.24 gibt es den `pre-merge-commit
    <https://git-scm.com/docs/githooks#_pre_merge_commit>`_-Hook, der ausgelöst
    wird, ausgelöst, nachdem eine Zusammenführung erfolgreich war, aber bevor
    der Merge-Commit erstellt wird. Ihr könnt ihn mit dem pre-commit-Framework
    nutzen mit:

    .. code-block:: console

        $ pre-commit install --hook-type pre-merge-commit
        pre-commit installed at .git/hooks/pre-merge-commit

``post-merge``
    Ab Version 2.11.0 kann das Framework auch Skripte für den `post-merge
    <https://git-scm.com/docs/githooks#_post_merge>`_-Hook ausführen:

    .. code-block:: console

        $ pipenv run pre-commit install --hook-type post-merge
        pre-commit installed at .git/hooks/post-merge

    Mit ``$PRE_COMMIT_IS_SQUASH_MERGE`` könnt ihr herausfinden, ob es sich um
    einen Squash-Merge handelte.

``pre-push``
    Um den `pre-push <https://git-scm.com/docs/githooks#_pre_push>`_-Hook mit
    dem pre-commit-Framework verwenden zu können, gebt folgendes ein:

    .. code-block:: console

        $ pre-commit install --hook-type pre-push
        pre-commit installed at .git/hooks/pre-push

    Hierfür werden die folgenden Umgebungsvariablen bereitgestellt:

    ``$PRE_COMMIT_FROM_REF``
        Die entfernte Revision, zu der gepusht wurde
    ``$PRE_COMMIT_TO_REF``
        Die lokale Revision, die an die entfernte Revision gepusht wurde
    ``$PRE_COMMIT_REMOTE_NAME``
        Die lokale Revision, die an die entfernte Revision gepusht wurde,
        :abbr:`z.B. (zum Beispiel)` :samp:`origin`
    ``$PRE_COMMIT_REMOTE_URL``
        Die URL des entfernten Repository, zu dem gepusht wurde,
        :abbr:`z.B. (zum Beispiel)`
        :samp:`git@github.com:veit/jupyter-tutorial`
    ``$PRE_COMMIT_REMOTE_BRANCH``
        Der Name des entfernten Zweigs, zu dem gepusht wurde, :abbr:`z.B. (zum
        Beispiel)` :samp:`refs/heads/{TARGET-BRANCH}`
    ``$PRE_COMMIT_LOCAL_BRANCH``
        Der Name des lokalen Zweigs, der in den entfernten Zweig verschoben
        wurde, :abbr:`z.B. (zum Beispiel)` :samp:`{HEAD}`

``commit-msg``
    `commit-msg <https://git-scm.com/docs/githooks#_commit_msg>`_ kann verwendet
    werden mit:

    .. code-block:: console

        $ pre-commit install --hook-type commit-msg
        pre-commit installed at .git/hooks/commit-msg

    Der ``commit-msg``-Hook kann mit ``stages: [commit-msg]`` konfiguriert
    werden, wobei der Name einer Datei übergeben wird, die den aktuellen Inhalt
    der Commit-Nachricht enthält, der überprüft werden kann.

``prepare-commit-msg``
    `prepare-commit-msg
    <https://git-scm.com/docs/githooks#_prepare_commit_msg>`_ kann mit
    pre-commit verwendet werden mit:

    .. code-block:: console

        $ pre-commit install --hook-type prepare-commit-msg
        pre-commit installed at .git/hooks/prepare-commit-msg

    Der ``prepare-commit-msg``-Hook wird mit ``stages: [prepare-commit-msg]``
    konfiguriert, wobei der Name einer Datei übergeben wird, die die anfängliche
    Commit-Nachricht enthält, :abbr:`z.B. (zum Beispiel)` von :samp:`git commit
    -m "{COMMIT-MESSAGE}"` um daraus eine dynamische Vorlage zu erstellen, die
    im Editor angezeigt wird. Schließlich sollte der Hook noch überprüfen, ob
    kein Editor gestartet wird mit ``GIT_EDITOR=:``.

``post-checkout``
    Der `post-checkout <https://git-scm.com/docs/githooks#_post_checkout>`_-Hook
    wird aufgerufen, wenn ``git checkout`` oder ``git switch`` ausgeführt wird.

    Der ``post-checkout``-Hook kann :abbr:`z.B. (zum Beispiel)` verwendet
    werden für

    * die Überprüfung von Repositories
    * die Ansicht der Unterschiede zum vorherigen ``HEAD``
    * das Ändern der Metadaten des Arbeitsverzeichnisses.

    In pre-commit kann kann er verwendet werden mit:

    .. code-block:: console

        $ pre-commit install --hook-type post-checkout
        pre-commit installed at .git/hooks/post-checkout

    Da ``post-checkout`` nicht auf Dateien wirkt, muss für alle
    ``post-checkout``-Skripte ``always_run`` gesetzt werden, :abbr:`z.B. (zum
    Beispiel)`:

    .. code-block:: yaml

        - repo: local
          hooks:
          - id: post-checkout-local
            name: Post checkout
            always_run: true
            stages: [post-checkout]
            # …

    Dabei gibt es drei Umgebungsvariablen, die den drei Arguementen von
    ``post-checkout`` entsprechen:

    ``$PRE_COMMIT_FROM_REF``
        gibt die Referenz des vorherigen ``HEAD`` aus
    ``$PRE_COMMIT_TO_REF``
        gibt die Referenz des neuen ``HEAD`` aus,  der sich geändert haben kann
        oder auch nicht
    ``$PRE_COMMIT_CHECKOUT_TYPE``
        gibt ``Flag=1`` aus, wenn es ein Branch-Checkout war und ``Flag=0``,
        wenn es ein File-Checkout war.

``post-rewrite``
    `post-rewrite <https://git-scm.com/docs/githooks#_post_rewrite>`_ wird
    aufgerufen, wenn Commits umgeschrieben werden, also von ``git commit
    --amend`` oder von ``git rebase``.

    .. code-block:: console

        $ pre-commit install --hook-type post-rewrite
        pre-commit installed at .git/hooks/post-rewrite

    Da ``post-rewrite`` nicht auf Dateien wirkt, muss ``always_run: true``
    gesetzt werden.

    Git teilt dem ``post-rewrite``-Hook mit, welcher Befehl das Rewrite
    ausgelöst hat. pre-commit gibt dies als ``$PRE_COMMIT_REWRITE_COMMAND`` aus.
