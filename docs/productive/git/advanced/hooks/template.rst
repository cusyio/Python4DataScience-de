.. SPDX-FileCopyrightText: 2023 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Vorlage für Git-Repositories
============================

``prek init-templatedir`` kann verwendet werden, um eine Vorlage für die
`init.templateDir
<https://git-scm.com/docs/git-init#_template_directory>`_-Option von Git
einzurichten, womit jedes neu geklonte Repository automatisch die
pre-commit-Checks erhält, ohne dass ``prek install`` ausgeführt werden muss,
:abbr:`z. B. (zum Beispiel)`:

.. code-block:: console

    $ git config --global init.templateDir ~/.config/git/template
    $ prek init-templatedir ~/.config/git/template
    prek installed at /Users/veit/.config/git/template/hooks/pre-commit
