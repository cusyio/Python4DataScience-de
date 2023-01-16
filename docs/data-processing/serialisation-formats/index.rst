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

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    serialisation.ipynb
    csv/index
    json/index
    excel.ipynb
    xml-html/index
    yaml/index
    toml/index
    pickle/index
    protobuf
    others
