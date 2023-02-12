Vorlage für Git-Repositories
============================

``pre-commit init-templatedir`` kann verwendet werden, um eine Vorlage für die
`init.templateDir
<https://git-scm.com/docs/git-init#_template_directory>`_-Option von Git
einzurichten, womit jedes neu geklonte Repository automatisch die
pre-commit-Hooks erhält, ohne dass ``pre-commit install`` ausgeführt werden
muss, :abbr:`z.B. (zum Beispiel)`:

.. code-block:: console

    $ git config --global init.templateDir ~/.config/git/template
    $ pre-commit init-templatedir ~/.config/git/template
    pre-commit installed at /Users/veit/.config/git/template/hooks/pre-commit
