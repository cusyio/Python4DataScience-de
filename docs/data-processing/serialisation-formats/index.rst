Serialisierungsformate
======================

Datenserialisierung konvertiert strukturierte Daten in ein Format, das geteilt
und gespeichert werden kann. Bevor ihr jedoch die Daten serialisiert, müsst ihr
Euch entscheiden, wie die Daten strukturiert werden sollen – flach oder
verschachtelt. Der Unterschied zwischen den beiden Stilen seht ihr an folgendem
Beispiel:

Flacher JSON-Stil:
    .. code-block:: javascript

        {
          "id"          :  "veit",
          "first_name"  :  "Veit",
          "last_name"   :  "Schiele",
        }

Verschachtelter JSON-Stil:
    .. code-block:: javascript

      {
        "veit" : {
          "first_name"  :  "Veit",
          "last_name"   :  "Schiele",
        },
      }

Datenserialisierung
-------------------

Wenn die Daten flach serialisiert werden sollen, bietet Python zwei Funktionen
an:

``repr``
~~~~~~~~

:func:`python:repr` gibt eine druckbare Repräsentation der Eingabe aus,
:abbr:`z.B. (zum Beispiel)`:

.. code-block:: python

    >>> a = { "id" : "veit", "first_name": "Veit", "last_name": "Schiele" }
    >>> print(repr(a))
    {'id': 'veit', 'first_name': 'Veit', 'last_name': 'Schiele'}
    >>> with open('data.py', 'w') as f:
    ...     f.write(repr(a))
    ...
    60

``ast.literal_eval``
~~~~~~~~~~~~~~~~~~~~

Die :func:`python:ast.literal_eval`-Funktion parst und analysiert den
Python-Datentyp eines Ausdrucks. Unterstützte Datentypen sind
:doc:`python-basics:types/strings`, :doc:`python-basics:types/numbers`,
:doc:`python-basics:types/tuples`, :doc:`python-basics:types/lists`,
:doc:`python-basics:types/dicts` und :doc:`python-basics:types/none`.

.. code-block:: python

    >>> import ast
    >>> with open('data.py', 'r') as f:
    ...     inp = ast.literal_eval(f.read())

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    csv/index
    json/index
    excel.ipynb
    xml-html/index
    yaml
    toml
    pickle/index
    protobuf
    others
