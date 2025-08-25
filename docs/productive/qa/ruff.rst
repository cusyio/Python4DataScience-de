.. SPDX-FileCopyrightText: 2025 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Ruff
====

`Ruff <https://docs.astral.sh/ruff/>`_ ist ein extrem schneller Python-Linter
und Code-Formatierer, geschrieben in Rust, der :abbr:`u.a. (unter anderem)` die
Regeln von :doc:`flake8`, :doc:`isort`, :doc:`/performance/perflint`,
:doc:`black` und :ref:`Bandit <bandit>` ausführen kann. Insgesamt kann Ruff
`über 800 Regeln <https://docs.astral.sh/ruff/rules/>`_ überprüfen.

Installation
------------

.. code-block:: console

    $ uv add --dev ruff

Überprüfen
----------

Anschließend könnt ihr die Installation überprüfen mit

.. code-block:: console

    $ uv run ruff check /PATH/TO/YOUR/SOURCE/FILE

Shell-Autovervollständigung
---------------------------

Ruff unterstützt Autovervollständigung für die meisten Shells. Ein
shellspezifisches Skript kann mit :samp:`uv run ruff generate-shell-completion
{SHELL}` generiert werden, wobei :samp:`{SHELL}` entweder ``bash``, ``elvish``,
``fig``, ``fish``, ``powershell`` oder ``zsh`` ist, :abbr:`z. B. (zum Beispiel)`

.. tab:: Bash

   .. code-block:: console

      $ ruff generate-shell-completion zsh >> ~/.bash_completion

.. tab:: Zsh

   .. code-block:: console

      % ruff generate-shell-completion zsh > ~/.zfunc/_ruff

   Anschließend müssen dann die folgenden Zeilen in eure :file:`~/.zshrc`
   eingefügt werden, falls sie dort noch nicht vorhanden sind:

   .. code-block:: zsh

      fpath+=~/.zfunc
      autoload -Uz compinit && compinit

.. tab:: Oh My Zsh

   .. code-block:: console

      % mkdir $ZSH_CUSTOM/plugins/ruff
      % ruff generate-shell-completion zsh > $ZSH_CUSTOM/plugins/ruff/_ruff

.. seealso::
   `Shell autocompletion
   <https://docs.astral.sh/ruff/configuration/#shell-autocompletion>`_

Konfiguration
-------------

Im Gegensatz zur Standardformatierung von :doc:`black` mit 88 Zeichen bevorzuge
ich eine Zeilenlänge von 79 Zeichen. Hierfür könnt ihr in die
:file:`pyproject.toml`-Datei folgendes eintragen:

.. code-block:: toml

    [tool.ruff]
    line-length = 79

.. tip::
   Üblicherweise fügen wir ``ruff lint`` zunächst alle Regeln hinzu, bevor wir
   dann einzelne wieder ausschließen, also :abbr:`z. B. (zum Beispiel)`:

   .. code-block:: toml

      [tool.ruff.lint]
      select = ["ALL"]
      ignore = [
          "A",       # Shaddowing is fine
      ]

Ruff unterstützt auch auch Monorepos mit unterschiedlichen Regeln durch
`hierarchische und kaskadierende Konfigurationen
<https://docs.astral.sh/ruff/configuration/#config-file-discovery>`_.

.. seealso::
   Weitere Informationen zur Konfiguration von ruff in der
   :file:`pyproject.toml`-Datei erhaltet ihr in `Configuring Ruff
   <https://docs.astral.sh/ruff/configuration/>`_.

Integration
-----------

Jupyter Notebooks
~~~~~~~~~~~~~~~~~

Ruff unterstützt das Linting und Formatieren von :doc:`Jupyter Notebooks
<jupyter-tutorial:notebook/index>` mit :ref:`nbQA <nbqa>`. Mit `jupyter-ruff
<https://github.com/leotaku/jupyter-ruff>`_ könnt ihr ruff auch in euren
Notebooks verwenden.

IDE
~~~

Auch die Integration in andere Editoren wie Visual Studio Code, PyCharm oder Vim
ist  möglich, :abbr:`s. (siehe)` `Editor Integrations
<https://docs.astral.sh/ruff/editors/>`_.

pre-commit
~~~~~~~~~~

Ruff kann über `ruff-pre-commit <https://github.com/astral-sh/ruff-pre-commit>`_
als :doc:`Pre-Commit-Hook </productive/git/advanced/hooks/pre-commit>` verwendet
werden:

.. code-block:: yaml

   repos:
     - repo: https://github.com/astral-sh/ruff-pre-commit
       rev: v0.12.10
       hooks:
       - id: ruff-check
         args: [--fix, --exit-non-zero-on-fix]
         exclude: docs
       - id: ruff-format
