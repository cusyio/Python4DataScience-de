.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git Notes
=========

`Git Notes <https://git-scm.com/docs/git-notes>`_ fügen Textnotizen zu Commits,
Tags und anderen Objekten hinzu. Solche Notizen können alle Arten von Metadaten
enthalten, :abbr:`z.B. (zum Beispiel)` Kommentare zur Codeüberprüfung, Links zu
Fehlerberichten :abbr:`usw (und so weiter)`:

#. Hinzufügen einer Git-Notiz:

   .. code-block:: console

      $ git notes add -m 'Example note'

#. Anzeigen einer Git-Notiz:

   .. code-block:: console

      $ git log
      commit 859de540cda23f510f4ecbe0f38d07666e933f08 (HEAD -> main)
      Author: Veit Schiele <veit@cusy.io>
      Date:   Sun Mar 24 11:17:56 2024 +0100

          A commit message

      Notes:
          Example note

#. Ändern einer Git-Notiz:

   .. code-block:: console

      $ git notes edit

Git Notes werden jedoch nicht standardmäßig mit ``git push`` oder ``git pull``
an das entfernte Repository übermittelt; sie müssen mit ``git push origin
'refs/notes/*'`` und ``git fetch origin 'refs/notes/*:refs/notes/*'``
synchronisiert werden.

.. warning::
   Verwendet nicht ``git pull`` anstelle von ``git fetch``: ihr könnt
   ``refs/notes/commits`` nicht mit eurem aktuellen Zweig zusammenführen.

.. note::
   Git Notes werden nicht in die Git-Commit-Historie aufgenommen, sodass sie
   nicht sind nicht für Regulatorisches verwendet werden können, bei dem die
   Herkunft, Nichtabstreitbarkeit oder Manipulationssicherheit nachgewiesen
   werden muss. Sie könnxen jedoch :abbr:`z.B. (zum Beispiel)` für Build-Tags
   und ähnliches nützlich sein.

.. seealso::
   * `Git Notes: Git’s Coolest, Most Unloved­ Feature
     <https://tylercipriani.com/blog/2022/11/19/git-notes-gits-coolest-most-unloved-feature/>`_
   * `git-appraise <https://github.com/google/git-appraise>`_
   * `github-issues-git-notes
     <https://github.com/TomasHubelbauer/github-issues-git-notes>`_
