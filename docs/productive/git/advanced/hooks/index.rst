.. SPDX-FileCopyrightText: 2023 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git Hooks
=========

Git-Hooks sind Skripte, die bei bestimmten Ereignissen in einem Git-Repository
automatisch ausgeführt werden, :abbr:`u.a. (unter anderem)`:

+---------------+-------------------------------------------------------+
| Befehl        | Hooks                                                 |
+===============+=======================================================+
| ``git commit``| `prepare-commit-msg`_, `pre-commit`_, `commit-msg`_,  |
|               | `post-commit`_                                        |
+---------------+-------------------------------------------------------+
| ``git merge`` | `pre-merge-commit`_, `commit-msg`_,  `post-merge`_    |
+---------------+-------------------------------------------------------+
| ``git rebase``| `pre-rebase`_, `post-rewrite`_                        |
+---------------+-------------------------------------------------------+
| ``git pull``  | `post-merge`_                                         |
+---------------+-------------------------------------------------------+
| ``git push``  | `pre-push`_, `pre-receive`_, `update`_,               |
|               | `post-update`_, `proc-receive`_, `post-receive`_,     |
|               | `push-to-checkout`_                                   |
+---------------+-------------------------------------------------------+

Sie können sich entweder in lokalen oder serverseitigen Repositories befinden.
So können Git-Repositories individuell angepasst und benutzerdefinierte Aktionen
ausgelöst werden.

Git Hooks befinden sich im Verzeichnis :file:`.git/hooks/`. Beim Anlegen eines
Repository werden dort auch bereits einige Beispielskripte angelegt:

.. code-block:: console

   .git/hooks
   ├── applypatch-msg.sample
   ├── commit-msg.sample
   ├── fsmonitor-watchman.sample
   ├── post-update.sample
   ├── pre-applypatch.sample
   ├── pre-commit.sample
   ├── pre-merge-commit.sample
   ├── pre-push.sample
   ├── pre-rebase.sample
   ├── pre-receive.sample
   ├── prepare-commit-msg.sample
   ├── push-to-checkout.sample
   ├── sendemail-validate.sample
   └── update.sample

Damit die Skripte ausgeführt werden, muss lediglich der Suffix ``.sample``
entfernt werden und :abbr:`ggf. (gegebenenfalls)` die Dateiberechtigung
ausführbar sein, :abbr:`z.B. (zum Beispiel)` mit :samp:`chmod +x
.git/{PREPARE-COMMIT-MSG}`.

Die integrierten Skripte sind Shell- und Perl-Skripte, es können jedoch
beliebige Skriptsprachen verwenden werden. Dabei bestimmt die Shebang-Zeile
(:samp:`#!/bin/sh`), wie die Datei interpretiert werden soll.

Die Skripte können jedoch nicht in das serverseitige Repository kopiert werden.

.. seealso::
   * `Hooks <https://git-scm.com/docs/githooks#_hooks>`_

.. toctree::
    :hidden:

    pre-commit
    hooks
    advanced
    ci
    skip
    template

.. _`prepare-commit-msg`: https://git-scm.com/docs/githooks#_prepare_commit_msg
.. _`pre-commit`: https://git-scm.com/docs/githooks#_pre_commit
.. _`post-commit`: https://git-scm.com/docs/githooks#_post_commit
.. _`commit-msg`: https://git-scm.com/docs/githooks#_commit_msg
.. _`pre-merge-commit`: https://git-scm.com/docs/githooks#_pre_merge_commit
.. _`post-merge`: https://git-scm.com/docs/githooks#_post_merge
.. _`pre-rebase`: https://git-scm.com/docs/githooks#_pre_rebase
.. _`post-rewrite`: https://git-scm.com/docs/githooks#_post_rewrite
.. _`pre-push`: https://git-scm.com/docs/githooks#_pre_push
.. _`pre-receive`: https://git-scm.com/docs/githooks#pre-receive
.. _`update`: https://git-scm.com/docs/githooks#update
.. _`post-update`: https://git-scm.com/docs/githooks#post-update
.. _`proc-receive`: https://git-scm.com/docs/githooks#proc-receive
.. _`post-receive`: https://git-scm.com/docs/githooks#post-receive
.. _`push-to-checkout`: https://git-scm.com/docs/githooks#_push_to_checkout
