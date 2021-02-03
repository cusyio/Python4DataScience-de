ipython-sql
===========

`ipython-sql <https://github.com/catherinedevlin/ipython-sql>`_ führt die
``%sql`` oder ``%%sql``-Magics für iPython und Jupyter Notebooks ein.

Installation
------------

Ihr könnt ipython-sql einfach in Eurem Jupyter-Kernel installieren mit:

.. code-block:: console

    $ pipenv install ipython-sql

Erste Schritte
--------------

#. Zunächst wird ipython-sql in Eurem Notebook aktiviert mit

   .. code-block:: python

    In [1]: %load_ext sql

#. Für die Verbindung zur Datenbank wird die `SQLAlchemy URL
   <http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls>`_
   verwendet:

   .. code-block:: python

    In [2]: %sql postgresql://

#. Anschließend könnt Ihr eine Tabelle erstellen, z.B.:

   .. code-block:: python

    In [3]: %%sql postgresql://
       ....: CREATE TABLE accounts (login, name, email)
       ....: INSERT INTO accounts VALUES ('veit', 'Veit Schiele', veit@example.org);

#. Die Inhalte der Tabelle ``accounts`` könnt Ihr abfragen mit

   .. code-block:: python

    In [4]: result = %sql select * from accounts

Konfiguration
-------------

Abfrageergebnisse werden als Liste geladen sodass sehr große Datenmengen den
Arbeitsspeicher belegen können. Üblicherweise gibt es keine automatische
Begrenzung, mit ``Autolimit`` lässt sich  jedoch die Ergebnismenge limitieren.

.. note::
   ``displaylimit`` begrenzt nur die Menge der angezeigten Ergebnisse, nicht
   jedoch den Speicherbedarf.

Mit ``%config SqlMagic`` könnt Ihr Euch die aktuelle Konfiguration ausgeben
lassen:

.. code-block:: python

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
        Return Pandas DataFrames instead of regular result sets
    …

.. note::
   Wenn ``autopandas`` auf ``True`` gesetzt wurde, wird ``displaylimit`` nicht
   angewendet. In diesem Fall kann die ``max_rows``-Option von pandas verwendet
   werden wie in der `pandas-Dokumentation
   <https://pandas.pydata.org/pandas-docs/version/0.18.1/options.html#frequently-used-options>`_ beschrieben.

Pandas
------

Wenn pandas installiert ist, kann die ``DataFrame``-Methode verwendet werden:

.. code-block:: python

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

``-l``, ``--connections``
    listet alle aktiven Verbindungen auf
``-x``, ``--close <session-name>``
    schließt benannte Verbindung
``-c``, ``--creator <creator-function>``
    gibt die Creator-Funktion für eine neue Verbindung an
``-s``, ``--section <section-name>``
    gibt Abschnitt von ``dsn_file`` an, der in einer Verbindung verwendet werden
    soll
``-p``, ``--persist``
    erstellt aus einem benannten DataFrame eine Tabelle in der Datenbank
``--append``
    ähnlich wie ``--persist``, die Inhalte werden jedoch an die Tabelle
    angehängt
``-a``, ``--connection_arguments <"{connection arguments}">``
    gibt ein Dict von Verbindungsargumenten an, die an den SQL-Treiber
    übergeben werden
``-f``, ``--file <path>``
    führt SQL aus der Datei unter diesem Pfad aus

.. seealso::
   * `pgspecial <https://pypi.org/project/pgspecial/>`_

.. warning::
   Da ipython-sql ``--``-Optionen wie z.B. ``--persist`` verarbeitet, und
   gleichzeitig ``--`` als SQL-Kommentar akzeptiert, muss der Parser einige
   Annahmen treffen: so wird z.B. ``--persist is great`` in der ersten Zeile als
   Argument und nicht als Kommentar verarbeitet.
