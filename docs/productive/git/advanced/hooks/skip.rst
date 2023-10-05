.. SPDX-FileCopyrightText: 2023 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Hooks überspringen
==================

Die meisten :doc:`index` lassen sich mit der Option ``--no-verify`` umgehen. So
könnt ihr :abbr:`z.B. (zum Beispiel)` den pre-Commit-Hook überspringen mit:

.. code-block:: console

   $ git commit --no-verify -m "Quick and dirty"

Wenn ihr nur bestimmte :doc:`hooks` überspringen möchtet, könnt ihr hierfür die
Umgebungsvariable ``SKIP`` mit einer kommagetrennten Liste von Hook-IDs
verwenden, :abbr:`z.B. (zum Beispiel)`:

.. code-block:: console

   $ SKIP=check-added-large-file,no-commit-to-branch git commit -m "Hotfix"
