Serialisierungsformate
======================

Datenserialisierung konvertiert strukturierte Daten in ein Format, das geteilt
und gespeichert werden kann. Bevor Ihr jedoch die Daten serialisiert, müsst Ihr
Euch entscheiden, wie die Daten strukturiert werden sollen – flach oder
verschachtelt. Der Unterschied zwischen den beiden Stilen seht Ihr an folgendem
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

Wenn die Daten flach serialisiert werden sollen, bietet Python zwei Methoden an.

``repr``
~~~~~~~~

.. code-block:: python

    a =  { "id" : "veit", "first_name": "Veit", "last_name": "Schiele" }

    # Return a printable representation of the input
    print(repr(a))

    # Write contet to the file
    with open('data.py', 'w') as f:f.write(repr(a))

``ast.literal_eval``
~~~~~~~~~~~~~~~~~~~~

Die ``literal_eval``-Methode parst und analysiert den Python-Datentyp eines
Ausdrucks. Unterstützte Datentypen sind Zeichenketten, Zahlen, Tupel, Listen,
Dicts, Booleans und Nichts.

.. code-block:: python

    with open('data.py', 'r') as f: inp = ast.literal_eval(f.read())

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    csv
    json
    protobuf
    toml
    xml
    yaml
    others
