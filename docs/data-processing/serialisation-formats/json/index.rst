.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

JSON
====

Überblick
---------

+-----------------------+-------+-------------------------------------------------------+
| Unterstützung von     | +-    | JSON unterstützt Array- und Map- oder Objectstrukturen|
| Datenstrukturen       |       | vieler verschiedener Datentypen einschließlich        |
|                       |       | Zeichenfolgen, Zahlen, Boolesche Werte, Null usw.,    |
|                       |       | aber keine Datumsformate.                             |
|                       |       |                                                       |
|                       |       | Jedoch unterstützt JSON auch nicht alle Datentypen von|
|                       |       | JavaScript: ``NaN`` und ``Infinity`` werden zu        |
|                       |       | ``null``.                                             |
|                       |       |                                                       |
|                       |       | Bitte beachtet auch, dass die JSON keine Kommentare   |
|                       |       | unterstützt und ihr gegebenenfalls darum herumarbeiten|
|                       |       | müsst, z.B. mit einem ``__comment__``                 |
|                       |       | Schlüssel/Wert-Paar.                                  |
+-----------------------+-------+-------------------------------------------------------+
| Standardisierung      | \+    | JSON hat einen formal streng typisierten `Standard`_  |
|                       |       | siehe auch :rfc:`8259`).                              |
|                       |       | Jedoch enthalten JSON-Daten auch einige Fallstricke   |
|                       |       | aufgrund der Mehrdeutigkeit der JSON-Specifikationen: |
|                       |       |                                                       |
|                       |       | *Ein JSON-Parser MUSS alle Texte akzeptieren, die der |
|                       |       | JSON-Grammatik entsprechen* (:rfc:`7159`).            |
|                       |       |                                                       |
|                       |       | und                                                   |
|                       |       |                                                       |
|                       |       | *Eine Implementierung kann Grenzen für die Größe der  |
|                       |       | akzeptierten Texte setzen. Eine Implementierung kann  |
|                       |       | Grenzen für die maximale Verschachtelungstiefe        |
|                       |       | festlegen. Eine Implementierung kann Grenzen für den  |
|                       |       | Bereich und die Genauigkeit von Zahlen festlegen. Eine|
|                       |       | Implementierung kann Grenzen für die Länge und den    |
|                       |       | Zeicheninhalt von Zeichenketten festlegen*            |
|                       |       | (:rfc:`7158#section-9`).                              |
|                       |       |                                                       |
|                       |       | Unglücklicherweise gibt es weder eine                 |
|                       |       | Referenzimplementierung noch eine offizielle          |
|                       |       | Testsuite, die das erwartete Verhalten zeigen würden  |
|                       |       | – immerhin gibt zumindest `JSON_Checker`_ einige      |
|                       |       | Hinweise.                                             |
+-----------------------+-------+-------------------------------------------------------+
| Schema IDL            | +-    | Zum Teil mit `JSON Schema Proposal`_, `JSON Encoding  |
|                       |       | Rules (JER)`_, `Kwalify`_, `Rx`_, `JSON-LD`_ oder     |
|                       |       | `JMESPath`_.                                          |
|                       |       |                                                       |
|                       |       | Immerhin gibt es viele verschiedene `Validatoren`_.   |
+-----------------------+-------+-------------------------------------------------------+
| Sprachunterstützung   | ++    | Das JSON-Format wird sehr gut von den meisten         |
|                       |       | Programmiersprachen unterstützt.                      |
|                       |       |                                                       |
|                       |       | Die Datenstrukturen von JSON sind nahe an den Objekten|
|                       |       | der meisten Sprachen, z.B. kann ein Python ``dict``   |
|                       |       | einfach als JSON-``object`` und eine Python ``list``  |
|                       |       | einfach als JSON-``array`` dargestellt werden.        |
+-----------------------+-------+-------------------------------------------------------+
| Menschliche Lesbarkeit| +-    | JSON ist ein menschlich lesbares                      |
|                       |       | Serialisierungsformat, aber es unterstützt keine      |
|                       |       | Kommentare.                                           |
+-----------------------+-------+-------------------------------------------------------+
| Geschwindigkeit       | ++    | JSON ist eines der menschlich lesbaren                |
|                       |       | Serialisierungsformate, die schnell zu serialisieren  |
|                       |       | und zu deserialisieren sind.                          |
+-----------------------+-------+-------------------------------------------------------+
| Dateigröße            | +-    | Die Dateigröße von JSON liegt im Mittelfeld, ähnlich  |
|                       |       | :doc:`../yaml/index` und :doc:`../toml/index`.        |
+-----------------------+-------+-------------------------------------------------------+

.. seealso::

    * `JC – JSON Convert <https://github.com/kellyjonbrazil/jc>`_
    * `fx <https://github.com/antonmedv/fx>`_
    * `gron <https://github.com/tomnomnom/gron>`_
    * `python-json-patch <https://github.com/stefankoegl/python-json-patch>`_

Beispiel
--------

Antwort der :ref:`OSM-Nominatim-API
</data-processing/httpx/install-example.ipynb#Beispiel-OSM-Nominatim-API>`:

.. code-block:: javascript

    [
        {
            'place_id': 234847916,
            'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'relation',
            'osm_id': 131761,
            'boundingbox': ['52.5200695', '52.5232601', '13.4103097', '13.4160798'],
            'lat': '52.521670650000004',
            'lon': '13.413278026558228',
            'display_name': 'Alexanderplatz, Mitte, Berlin, 10178, Deutschland',
            'class': 'highway',
            'type': 'pedestrian',
            'importance': 0.6914982526373583
        },
        {
            'place_id': 53256307,
            'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'node',
            'osm_id': 4389211800,
            'boundingbox': ['52.5231653', '52.5232653', '13.414475', '13.414575'],
            'lat': '52.5232153',
            'lon': '13.414525',
            'display_name': 'Alexanderplatz, Alexanderstraße, Mitte, Berlin, 10178, Deutschland',
            'class': 'highway',
            'type': 'bus_stop',
            'importance': 0.22100000000000003,
            'icon': 'https://nominatim.openstreetmap.org/images/mapicons/transport_bus_stop2.p.20.png'
        },
        {
            'place_id': 90037579,
            'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'way',
            'osm_id': 23853138,
            'boundingbox': ['52.5214702', '52.5217276', '13.4037885', '13.4045026'],
            'lat': '52.5215991',
            'lon': '13.404112295159964',
            'display_name': 'Alexander Plaza, 1, Rosenstraße, Mitte, Berlin, 10178, Deutschland',
            'class': 'tourism',
            'type': 'hotel',
            'importance': 0.11100000000000002,
            'icon': 'https://nominatim.openstreetmap.org/images/mapicons/accommodation_hotel2.p.20.png'
        }
    ]

.. _`standard`: https://www.json.org/json-en.html
.. _`JSON_Checker`: http://www.json.org/JSON_checker/
.. _`JSON Schema Proposal`: https://json-schema.org
.. _`JSON Encoding Rules (JER)`: https://www.itu.int/rec/T-REC-X.697-201710-I/
.. _`Kwalify`: http://www.kuwata-lab.com/kwalify/
.. _`Rx`: https://rx.codesimply.com
.. _`JSON-LD`: https://json-ld.org#
.. _`JMESPath`: https://jmespath.org/
.. _`Validatoren`: https://json-schema.org/tools?query=&sortBy=name&sortOrder=ascending&groupBy=toolingTypes&licenses=&languages=&drafts=&toolingTypes=#validator

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    example.ipynb
