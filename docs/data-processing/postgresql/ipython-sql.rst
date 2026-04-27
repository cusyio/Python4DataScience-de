.. SPDX-FileCopyrightText: 2021 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

ipython-sql
===========

`ipython-sql <https://github.com/catherinedevlin/ipython-sql>`_ führt die
``%sql`` oder ``%%sql``-Magics für iPython und Jupyter Notebooks ein.

Installation
------------

Ihr könnt ipython-sql einfach in eurem Jupyter-Kernel installieren mit:

.. code-block:: console

    $ uv add ipython-sql

Erste Schritte
--------------

#. Zunächst wird ipython-sql in eurem Notebook aktiviert mit

   .. code-block:: ipython

    In [1]: %load_ext sql

#. Für die Verbindung zur Datenbank wird die `SQLAlchemy URL
   <https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls>`_
   verwendet:

   .. code-block:: ipython

    In [2]: %sql postgresql://

#. Anschließend könnt ihr eine Tabelle erstellen, :abbr:`z.B. (zum Beispiel)`:

   .. code-block:: ipython

    In [3]: %%sql postgresql://
       ....: CREATE TABLE accounts (login, name, email)
       ....: INSERT INTO accounts VALUES ('veit', 'Veit Schiele', veit@example.org);

#. Die Inhalte der Tabelle ``accounts`` könnt ihr abfragen mit

   .. code-block:: ipython

    In [4]: result = %sql select * from accounts

Konfiguration
-------------

Abfrageergebnisse werden als Liste geladen sodass sehr große Datenmengen den
Arbeitsspeicher belegen können. Üblicherweise gibt es keine automatische
Begrenzung, mit ``Autolimit`` lässt sich  jedoch die Ergebnismenge limitieren.

.. note::
   ``displaylimit`` begrenzt nur die Menge der angezeigten Ergebnisse, nicht
   jedoch den Speicherbedarf.

Mit ``%config SqlMagic`` könnt ihr Euch die aktuelle Konfiguration ausgeben
lassen:

.. code-block:: ipython

    In [5]: %config SqlMagic
    SqlMagic options
    --------------
    SqlMagic.autocommit=<Bool>
        Current: True
        Set autocommit mode
    SqlMagic.autolimit=<Int>
        Current: 0
        Automatically limit the size of the returned result sets
    SqlMagic.autopandas=<Bool>
        Current: False
        Return pandas DataFrames instead of regular result sets
    ...

.. note::
   Wenn ``autopandas`` auf ``True`` gesetzt wurde, wird ``displaylimit`` nicht
   angewendet. In diesem Fall kann die ``max_rows``-Option von pandas verwendet
   werden wie in der `pandas-Dokumentation
   <https://pandas.pydata.org/pandas-docs/version/0.18.1/options.html#frequently-used-options>`_ beschrieben.

pandas
------

Wenn pandas installiert ist, kann die ``DataFrame``-Methode verwendet werden:

.. code-block:: ipython

    In [6]: result = %sql SELECT * FROM accounts

    In [7]: dataframe = result.DataFrame()

    In [8]: %sql --persist dataframe

    In [9]: %sql SELECT * FROM dataframe;

``--persist``
    Argument mit dem Namen eines ``DataFrame``-Objekts, erstellt aus diesem
    einen Tabellennahmen in der Datenbank.
``--append``
    Argument um in einer vorhandenen Tabelle Zeilen mit diesem namen
    hinzuzufügen.

PostgreSQL-Funktionen
---------------------

Meta-Befehle von ``psql`` lassen sich auch in ipython-sql verwenden:

:samp:`-l`, :samp:`--connections`
    listet alle aktiven Verbindungen auf
:samp:`-x`, :samp:`--close {SESSION-NAME}`
    schließt benannte Verbindung
:samp:`-c`, :samp:`--creator {CREATOR-FUNCTION}`
    gibt die Creator-Funktion für eine neue Verbindung an
:samp:`-s`, :samp:`--section {SECTION-NAME}`
    gibt Abschnitt von ``dsn_file`` an, der in einer Verbindung verwendet werden
    soll
:samp:`-p`, :samp:`--persist`
    erstellt aus einem benannten DataFrame eine Tabelle in der Datenbank
:samp:`--append`
    ähnlich wie :samp:`--persist`, die Inhalte werden jedoch an die Tabelle
    angehängt
:samp:`-a`, :samp:`--connection_arguments "\{{connection arguments}\}"`
    gibt ein Dict von Verbindungsargumenten an, die an den SQL-Treiber
    übergeben werden
:samp:`-f`, :samp:`--file {PATH}`
    führt SQL aus der Datei unter diesem Pfad aus

.. seealso::
   * `pgspecial <https://pypi.org/project/pgspecial/>`_

.. warning::
   Da ipython-sql ``--``-Optionen wie :abbr:`z.B. (zum Beispiel)` ``--persist``
   verarbeitet, und gleichzeitig ``--`` als SQL-Kommentar akzeptiert, muss der
   Parser einige Annahmen treffen: so wird :abbr:`z.B. (zum Beispiel)`
   ``--persist is great`` in der ersten Zeile als Argument und nicht als
   Kommentar verarbeitet.
