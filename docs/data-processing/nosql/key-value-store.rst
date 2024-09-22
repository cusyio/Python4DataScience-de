.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Schlüssel-Werte-Datenbanksysteme
================================

Schlüssel-Werte-Datenbanken, auch Key Value Stores genannt, speichern
:term:`Schlüssel/Wert-Paare <Schlüssel/Wert-Paar>`.

Datenbanksysteme
----------------

Schlüssel/Wert-Datenbanksysteme sind :abbr:`z.B. (zum Beispiel)` Riak,
Cassandra, Redis und MongoDB.

+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `Riak`_                        | `Cassandra`_                   | `Redis`_                       | `MongoDB`_                     |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `basho/riak`_                  | `apache/cassandra`_            | `redis/redis`_                 | `mongodb/mongo`_               |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `docs.riak.com`_               | `cassandra.apache.org/doc/`_   | `redis.io/docs`_               | `www.mongodb.com/docs/`_       |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anwendungsgebiete**  | Session storage, Log data,     | Georedundanz, hohe             | Session Cache, Full Page       | IoT, Mobile apps, CMS,         |
|                        | Sensor data, CMS               | Schreibgeschwindigkeit,        | Cache (FPC), Queues, Pub/Sub   | `einfache Geodaten`_, …        |
|                        |                                | demokratische Peer-to-peer     |                                |                                |
|                        |                                | (P2P)-Architektur, Daten mit   |                                |                                |
|                        |                                | definierter Lebenszeit         |                                |                                |
|                        |                                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Entwicklungssprache**| Erlang                         | Java                           | ANSI C                         | C++                            |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Lizenzen**           | Apache License 2.0             | Apache License 2.0             | Redis Source Available License | Server Side Public License     |
|                        |                                |                                | v2, Server-Side Public License |                                |
|                        |                                |                                | v1                             |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Datenmodell**        | Im Wesentlichen                | :term:`Column Family`          | Schlüssel werden als           | Flexibles Schema mit           |
|                        | :term:`Schlüssel/Wert-Paar`    | entsprechen Tabellen,          | Zeichenkette gespeichert,      | denormalisiertem Modell        |
|                        |                                | *Keyspaces* Datenbanken; keine | Werte als Zeichenkette, Hashes,|                                |
|                        |                                | logische Struktur, kein Schema | Listen, Sets und sortierten    |                                |
|                        |                                |                                | Sets                           |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query-Langauge**     | Keyfilter, :term:`MapReduce`,  | `Cassandra Query Language      |                                | jQuery, :term:`MapReduce`      |
|                        | Link-Walking, keine Ad-hoc     | (CQL)`_                        |                                |                                |
|                        | Queries möglich                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transaktionen,       | :term:`ACID`                   | :term:`Eventual Consistency`   | in-memory, asynchron on disc   | :term:`Two-phase locking (2PL)`|
| Nebenläufigkeit**      |                                |                                | mit *Append Only File Mode*    |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replikation,         | Multi-Master-Replikation       | SimpleStrategy,                | Master-N-Slaves-Replikation,   | Master-Slave-Replikation,      |
| Skalierung**           |                                | NetworkTopologyStrategy und    | Sharding mittels               | Auto-Sharding                  |
|                        |                                | OldNetworkTopologyStrategy     | :term:`consistent hashing      |                                |
|                        |                                |                                | <Konsistente Hashfunktion>`    |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Anmerkungen**        |                                | Siehe auch `Scylla`_, eine     | Siehe auch:                    | `BSON` mit einre maximalen     |
|                        |                                | Cassandra-kompatible           |                                | Dokumentengröße von 16 MB.     |
|                        |                                | Reimplementierung in C.        | `KeyDB`_                       |                                |
|                        |                                |                                |     ein Fork mit Multithreading|                                |
|                        |                                |                                | `Redict`_                      |                                |
|                        |                                |                                |     ein Fork, lizenziert unter |                                |
|                        |                                |                                |     LGPL-3.0                   |                                |
|                        |                                |                                | `Valkey`_                      |                                |
|                        |                                |                                |     ein Fork der Linux         |                                |
|                        |                                |                                |     Foundation                 |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+


.. _`Riak`: https://riak.com/
.. _`Cassandra`: https://cassandra.apache.org/_/index.html
.. _`Redis`: https://redis.io/
.. _`MongoDB`: https://www.mongodb.com/
.. _`basho/riak`: https://github.com/basho/riak
.. _`apache/cassandra`: https://github.com/apache/cassandra
.. _`redis/redis`: https://github.com/redis/redis
.. _`mongodb/mongo`: https://github.com/mongodb/mongo
.. _`docs.riak.com`: https://docs.riak.com/
.. _`cassandra.apache.org/doc/`: https://cassandra.apache.org/doc/latest/
.. _`redis.io/docs`: https://redis.io/docs/latest/
.. _`www.mongodb.com/docs/`: https://www.mongodb.com/docs/
.. _`einfache Geodaten`: https://www.mongodb.com/docs/manual/core/indexes/index-types/geospatial/2d/internals/
.. _`Cassandra Query Language (CQL)`: https://cassandra.apache.org/doc/stable/cassandra/cql/
.. _`Scylla`: https://www.scylladb.com/
.. _`KeyDB`: https://github.com/Snapchat/KeyDB
.. _`Redict`: https://redict.io/
.. _`Valkey`: https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community
.. _`BSON`: http://www.bsonspec.org/
