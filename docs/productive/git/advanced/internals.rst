.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git-Interna
===========

Bisher haben wir uns angeschaut, wie ihr mit Git die unterschiedlichen Zustände
eures Codes verwalten könnt. Hier wollen wir euch nun zeigen, welche
:ref:`Daten- <git-data-model>` und :ref:`Speichermodelle <git-storage-model>`
Git zugrundeliegen.

.. _git-data-model:

Datenmodell
-----------

Ihr werdet Git besser nutzen können, wenn ihr das Datenmodell verstanden habt.
Dabei verwaltet Git vier Arten von Daten:

Objekte
~~~~~~~

.. include:: ../glossary.rst
   :start-after: start-object
   :end-before: end-object

Commit
::::::

.. include:: ../glossary.rst
   :start-after: start-commit
   :end-before: end-commit

Tree
::::

.. include:: ../glossary.rst
   :start-after: start-tree
   :end-before: end-tree

Blob
::::

.. include:: ../glossary.rst
   :start-after: start-blob
   :end-before: end-blob

Tag
:::

.. include:: ../glossary.rst
   :start-after: start-tag
   :end-before: end-tag

Referenzen
~~~~~~~~~~

.. include:: ../glossary.rst
   :start-after: start-refs
   :end-before: end-refs

Index
~~~~~

.. include:: ../glossary.rst
   :start-after: start-index
   :end-before: end-index

Reflog
~~~~~~

.. include:: ../glossary.rst
   :start-after: start-reflog
   :end-before: end-reflog

.. _git-storage-model:

Speichermodell
--------------

.. seealso::
   Git’s database internals

   * `Part I: packed object store
     <https://github.blog/open-source/git/gits-database-internals-i-packed-object-store/>`_
   * `Part II: commit history queries
     <https://github.blog/open-source/git/gits-database-internals-ii-commit-history-queries/>`_
   * `Part III: file history queries
     <https://github.blog/open-source/git/gits-database-internals-iii-file-history-queries/>`_
   * `Part IV: distributed synchronization
     <https://github.blog/open-source/git/gits-database-internals-iv-distributed-synchronization/>`_
   * `Part V: scalability
     <https://github.blog/open-source/git/gits-database-internals-v-scalability/>`_

Packfiles
~~~~~~~~~

.. include:: ../glossary.rst
   :start-after: start-packfile
   :end-before: end-packfile
