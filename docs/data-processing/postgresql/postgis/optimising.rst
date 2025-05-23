.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Optimieren von PostgreSQL für GIS-Datenbankobjekte
==================================================

In der Standardinstallation ist PostgreSQL sehr zurückhaltend konfiguriert um
auf möglichst vielen Systemen lauffähig zu sein. GIS-Datenbankobjekte sind
jedoch im Vergleich zu Textdaten groß. Daher sollte PostgreSQL so konfiguriert
werden, dass sie mit diesen Objekten besser funktioniert. Hierfür konfigurieren
wir die Datei ``/etc/postgresql/14/main/postgresql.conf`` folgendermaßen:

#. ``shared_buffer`` sollte auf ca. 75% des gesamten Arbeitsspeichers geändert
   werden, jedoch ``128kB`` nie unterschreiten:

   .. code-block:: ini

    shared_buffers = 768MB

#. ``work_mem`` sollte auf mindestens 16MB erhöht werden:

   .. code-block:: ini

    work_mem = 16MB

#. ``maintenance_work_mem`` sollte auf 128MB erhöht werden:

   .. code-block:: ini

    maintenance_work_mem = 128MB

#. Schließlich sollte noch ``random_page_cost`` auf ``2.0`` gesetzt werden.

   .. code-block:: ini

    random_page_cost = 2.0

Damit die Änderungen übernommen werden, sollte PostgreSQL neu gestartet werden:

.. code-block:: console

    $ sudo service postgresql restart
