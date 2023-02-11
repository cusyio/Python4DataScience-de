PostGIS installieren
====================

Für Ubuntu 22.04 könnt ihr PostGIS einfach installieren mit:

code-block:: console

    $ sudo apt install postgis

Anschließend könnt ihr PostGIS aktivieren.

#. Wechseln zum PostgreSQL-User:

   .. code-block:: console

    $ sudo -i -u postgres

#. Testuser und Datenbank erstellen:

   .. code-block:: console

    $ createuser postgis
    $ createdb postgis_db -O postgis

#. Verbindung zur Datenbank herstellen:

   .. code-block:: console

    $ psql -d postgis_db
    psql (14.5 (Ubuntu 14.5-0ubuntu0.22.04.1))
    Type "help" for help.

#. Aktivieren der PostGIS-Erweiterung in der Datenbank:

   .. code-block:: console

    ppostgis_db = # CREATE EXTENSION postgis;
    CREATE EXTENSION

#. Überprüfen, ob PostGIS funktioniert:

   .. code-block:: console

        postgis_db=# SELECT PostGIS_version();
                postgis_version
    ---------------------------------------
     3.2 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
    (1 row)

.. seealso::
   * `PostGIS Installation
     <https://postgis.net/docs/postgis_installation.html>`_
