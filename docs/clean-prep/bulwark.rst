Pandas DataFrame-Validierung mit Bulwark
========================================

`Bulwark <https://bulwark.readthedocs.io/en/stable/index.html>`_ ist ein Paket
zum eigenschaftsbasierten Testen von pandas-Dataframes. Das Projekt wurde stark
von der nicht mehr unterstützten :doc:`Engarde <engarde>`-Bibliothek
beeinflusst.

Installation
------------

.. code-block:: console

    $ pipenv install bulwark
    Installing bulwark…
    Adding bulwark to Pipfile's [packages]…
    ✔ Installation Succeeded
    Locking [dev-packages] dependencies…
    ✔ Success!
    Updated Pipfile.lock (0d075a)!

Verwendung
----------

Überprüfungen
~~~~~~~~~~~~~

Bulwark kommt mit Überprüfungen für viele der gängigen Annahmen.

.. code-block:: python

    import bulwark.checks as ck

    df.pipe(ck.has_no_nans())

Decorators
~~~~~~~~~~

Für jeden Check in ``check.py`` erstellt ``bulwark.decorators`` Dekoratoren,
z.B.:

.. code-block:: python

    import bulwark.decorators as dc

    @dc.IsShape((-1, 10))
    @dc.IsMonotonic(strict=True)
    @dc.HasNoNans()
    def compute(df):
        # complex operations to determine result
        ...
    return result_df

``CustomCheck``
~~~~~~~~~~~~~~~

Ihr könnt auch eure eigenen benutzerdefinierten Funktionen erstellen, z.B.:

.. code-block:: python

    import bulwark.checks as ck
    import bulwark.decorators as dc
    import numpy as np
    import pandas as pd

    def len_longer_than(df, l):
        if len(df) <= l:
            raise AssertionError("df is not as long as expected.")
        return df

    @dc.CustomCheck(len_longer_than, 10, enabled=False)
    def append_a_df(df, df2):
        return df.append(df2, ignore_index=True)

    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df2 = pd.DataFrame({"a": [1, np.nan, 3, 4], "b": [4, 5, 6, 7]})

    append_a_df(df, df2)  # doesn’t fail because the check is disabled

``MultiCheck``
~~~~~~~~~~~~~~

Mit der integrierten ``MultiCheck``-Funktion könnt ihr mehrere Tests
gleichzeitig ausführen und alle Fehler auf einmal sehen, z.B.:

.. code-block:: python

    @dc.MultiCheck(checks={ck.has_no_nans: {"columns": None},
                           len_longer_than: {"l": 6}},
                   warn=False)
    def append_a_df(df, df2):
        return df.append(df2, ignore_index=True)

    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df2 = pd.DataFrame({"a": [1, np.nan, 3, 4], "b": [4, 5, 6, 7]})

    append_a_df(df, df2)


.. note::

    Wenn ihr ``MultiCheck`` verwendet, müsst ihr nicht auch noch ``CustomCheck``
   aufrufen – ihr könnt einfach die Funktion aufrufen.
