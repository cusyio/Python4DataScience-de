Foreign Data Wrappers (FDW)
===========================

2003 wurde SQL erweitert um  SQL/MED (*SQL Management of External Data*).
PostgreSQL 9.1 unterstützte dies *read-only*, 9.3 dann auch schreibend.
Seitdem sind eine Reihe von Foreign Data Wrappers (FDW) für PostgreSQL
entwickelt worden.

Im Folgenden nur eine kleine Auswahl der bekanntesten FDW:

.. note::
   Beachtet bitte, dass die meisten dieser Wrapper nicht offiziell von der
   PostgreSQL Global Development Group (PGDG) unterstützt werden.

Generische SQL-Wrapper
----------------------

ODBC
    Nativer ODBC FDW für PostgreSQL ≥9.5

    * `GitHub <https://github.com/CartoDB/odbc_fdw>`__

Multicorn
    `Multicorn <https://multicorn.org/>`_ erleichtert die Entwicklung von FDWs.
    So verwendet z.B. `SQLAlchemy <http://www.sqlalchemy.org/>`_ `Multicorn
    <https://multicorn.org/>`_ um seine Daten in PostgreSQL zu speichern.

    * `GitHub <sqlalchem://github.com/Kozea/Multicorn>`__
    * `PGXN <https://pgxn.org/dist/multicorn/>`__
    * `Docs <https://multicorn.org/foreign-data-wrappers/#sqlalchemy-foreign-data-wrapper>`__

VirtDB
    Nativer Zugang zu VirtDB (SAP ERP, Oracle RDBMS)

    * `GitHub <https://github.com/dbeck/virtdb-fdw>`__

Spezifische SQL-Wrapper
-----------------------

postgres_fdw
    Mit `postgres_fdw
    <https://www.postgresql.org/docs/current/postgres-fdw.html>`__ kann auf Daten
    aus anderen PostgreSQL-Servern zugegriffen werden.

    * `Git
      <https://git.postgresql.org/gitweb/?p=postgresql.git;a=tree;f=contrib/postgres_fdw;hb=HEAD>`__
    * `PGXN <https://pgxn.org/dist/postgres_fdw/>`__
    * `Docs <https://www.postgresql.org/docs/current/postgres-fdw.html>`__

Oracle
    FDW für Oracle-Datenbanken

    * `GitHub <https://github.com/laurenz/oracle_fdw>`__
    * `PGXN <https://pgxn.org/dist/oracle_fdw/>`__
    * `Docs <http://laurenz.github.io/oracle_fdw/>`__

MySQL
    FDW für MySQL ab PostgrSQL≥9.3

    * `GitHub <https://github.com/EnterpriseDB/mysql_fdw>`__
    * `PGXN <https://pgxn.org/dist/mysql_fdw/>`__

SQLite
    FDW für SQLite3

    * `GitHub <https://github.com/pgspider/sqlite_fdw>`__
    * `PGXN <https://pgxn.org/dist/sqlite_fdw>`__
    * `Docs <https://github.com/pgspider/sqlite_fdw/blob/master/README.md>`__


NoSQL-Database-Wrappers
-----------------------

Cassandra
    FDW für `Cassandra <https://cassandra.apache.org//>`_

    * `GitHub <https://github.com/rankactive/cassandra-fdw>`__
    * `rankactive <https://rankactive.com/resources/postgresql-cassandra-fdw>`__

Neo4j
    FWD für `Neo4j <https://neo4j.com/>`_, die auch eine Cypher-Funktion für
    PostgreSQL bereitstellt

    * `GitHub <https://github.com/sim51/neo4j-fdw>`__
    * `Docs <https://github.com/sim51/neo4j-fdw/blob/master/README.adoc>`__

Redis
    FDW für `Redis <https://redis.io/>`_

    * `GitHub <https://github.com/pg-redis-fdw/redis_fdw>`__

Riak
    FDW für `Riak <https://github.com/basho/riak>`_

    * `GitHub <https://github.com/kiskovacs/riak-multicorn-pg-fdw>`__

File-Wrappers
-------------

CSV
    Offizielle Erweiterung für PostgreSQL 9.1

    * `Git <https://git.postgresql.org/gitweb/?p=postgresql.git;a=tree;f=contrib/file_fdw;hb=HEAD>`__
    * `Docs <https://www.postgresql.org/docs/current/file-fdw.html>`__

JSON
    FDW für JSON-Dateien

    * `GitHub <https://github.com/nkhorman/json_fdw>`__
    * `Beispiel <https://www.citusdata.com/blog/2013/05/30/run-sql-on-json-files-without-any-data-loads/>`_

XML
    FDW für XML-Dateien

    * `GitHub <https://github.com/Kozea/Multicorn>`__
    * `PGXN <https://pgxn.org/dist/multicorn/>`__

Geo Wrappers
------------

GDAL/OGR
    FDW für den `GDAL/OGR <https://gdal.org/>`_-Treiber einschließlich
    Datenbanken wie Oracle und SQLite sowie Dateiformate wie MapInfo, CSV,
    Excel, OpenOffice, OpenStreetMap PBF und XML.

    * `GitHub <https://github.com/pramsey/pgsql-ogr-fdw>`__

Geocode/GeoJSON
    Eine Sammlung von FDWs für PostGIS

    * `GitHub <https://github.com/bosth/geofdw>`__

Open Street Map PBF
    FDW für `Open Street Map PBF
    <https://wiki.openstreetmap.org/wiki/PBF_Format>`_

    * `GitHub <https://github.com/vpikulik/postgres_osm_pbf_fdw>`__

Generische Web-Wrappers
-----------------------

ICAL
    FDW für ICAL

    * `GitHub <https://github.com/daamien/Multicorn/blob/master/python/multicorn/icalfdw.py>`__
    * `Docs <https://wiki.postgresql.org/images/7/7e/Conferences-write_a_foreign_data_wrapper_in_15_minutes-presentation.pdf>`__

IMAP
    FDW für das *Internet Message Access Protocol (IMAP)*

    * `Docs <https://multicorn.org/foreign-data-wrappers/#imap-foreign-data-wrapper>`__

RSS
    FDQ für RSS-Feeds

    * `Docs <https://multicorn.org/foreign-data-wrappers/#rss-foreign-data-wrapper>`__

.. seealso::
   * `PostgreSQL Wiki
     <https://wiki.postgresql.org/wiki/Foreign_data_wrappers>`_
   * `PGXN-Website <https://pgxn.org/>`_
