Psycopg
=======

`Pycopg <https://www.psycopg.org/>`_ ist ein PostgreSQL-Adapter, der auf der
C-Bibliothek für PostgreSQL `libpq
<https://www.postgresql.org/docs/current/libpq.html>`_ basiert. Er bietet
:abbr:`u.a. (unter anderem)`:

* DB-API-2.0-Kompatibilität
* Multithreading bei Thread Safety
* `Connections pooling <https://www.psycopg.org/docs/pool.html>`_
  um einen Cache von bestehenden Datenbankverbindungen für Anfragen verwenden
  zu können.
* `Asynchronous
  <https://www.psycopg.org/docs/advanced.html#asynchronous-support>`_ und
  `Coroutines support
  <https://www.psycopg.org/docs/advanced.html#support-for-coroutine-libraries>`_
* `Adaptation der Python Typen in SQL
  <https://www.psycopg.org/docs/usage.html#adaptation-of-python-values-to-sql-types>`_

Installation
------------

Ihr könnt psycopg2 mit Spack installieren, :abbr:`z.B. (zum Beispiel)` mit

.. code-block:: console

    $ spack env activate python-311
    $ spack install py-psycopg2
