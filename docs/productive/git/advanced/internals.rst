.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Datenmodell
===========

Ihr werdet Git besser nutzen können, wenn ihr das Datenmodell verstanden habt.

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

Git verwaltet vier Arten von Daten:

Objekte
-------

.. include:: ../glossary.rst
   :start-after: start-object
   :end-before: end-object

Referenzen
----------

.. include:: ../glossary.rst
   :start-after: start-refs
   :end-before: end-refs

Index
-----

.. include:: ../glossary.rst
   :start-after: start-index
   :end-before: end-index

Reflog
------

.. include:: ../glossary.rst
   :start-after: start-reflog
   :end-before: end-reflog
