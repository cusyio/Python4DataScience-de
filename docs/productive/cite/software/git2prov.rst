.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git2PROV
========

`Git2PROV <https://github.com/IDLabResearch/Git2PROV>`_ generiert PROV-Daten
aus den Informationen eines Git-Repository.

Auf der Kommandozeile kann die Konvertierung einfach ausgeführt werden mit:

.. code-block:: console

    $ git2prov git_url [serialization]

Zum Beispiel:

.. code-block:: console

    $ git2prov git@github.com:veit/python4datascience.git PROV-JSON

Insgesamt stehen die folgenden Serialisierungsformate zur Verfügung:

* ``PROV-N``
* ``PROV-JSON``
* ``PROV-O``
* ``PROV-XML``

Alternativ stellt Git2PROV auch einen Web-Server bereit mit:

.. code-block:: console

    $ git2prov-server [port]

.. seealso::
   * `Git2PROV: Exposing Version Control System Content as W3C PROV
     <https://ceur-ws.org/Vol-1035/iswc2013_demo_32.pdf>`_
   * `GitHub-Repository <https://github.com/IDLabResearch/Git2PROV>`_
