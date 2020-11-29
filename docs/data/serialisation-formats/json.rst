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
|                       |       | unterstützt und Ihr gegebenenfalls darum herumarbeiten|
|                       |       | müsst, z.B. mit einem ``__comment__``                 |
|                       |       | Schlüssel/Wert-Paar.                                  |
+-----------------------+-------+-------------------------------------------------------+
| Standardisierung      | \+    | JSON hat einen formal streng typisierten `Standard`_  |
|                       |       | siehe auch `RFC 8259`_).                              |
|                       |       | Jedoch enthalten JSON-Daten auch einige Fallstricke   |
|                       |       | aufgrund der Mehrdeutigkeit der JSON-Specifikationen: |
|                       |       |                                                       |
|                       |       | *A JSON parser MUST accept all texts that conform to  |
|                       |       | the JSON grammar* (`RFC 7159`_)                       |
|                       |       |                                                       |
|                       |       | und                                                   |
|                       |       |                                                       |
|                       |       | *An implementation may set limits on the size of texts|
|                       |       | that it accepts. An implementation may set limits on  |
|                       |       | the maximum depth of nesting. An implementation may   |
|                       |       | set limits on the range and precision of numbers. An  |
|                       |       | implementation may set limits on the length and       |
|                       |       | character contents of strings* (`RFC 7158 #9`_).      |
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
|                       |       | :doc:`yaml` und :doc:`toml`.                          |
+-----------------------+-------+-------------------------------------------------------+

Beispiel
--------

Antwort der :ref:`OSM-Nomination-API <Example-OSM-Nomination-API>`:

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
.. _`RFC 8259`: https://tools.ietf.org/html/rfc8259
.. _`RFC 7159`: https://tools.ietf.org/html/rfc7159
.. _`RFC 7158 #9`: https://www.ietf.org/rfc/rfc7158.html#section-9
.. _`JSON_Checker`: http://www.json.org/JSON_checker/
.. _`JSON Schema Proposal`: http://json-schema.org/
.. _`JSON Encoding Rules (JER)`: https://www.itu.int/rec/T-REC-X.697-201710-I/
.. _`Kwalify`: http://www.kuwata-lab.com/kwalify/
.. _`Rx`: http://rx.codesimply.com/
.. _`JSON-LD`: https://json-ld.org#
.. _`JMESPath`: https://jmespath.org/
.. _`validators`: https://json-schema.org/implementations.html#validators
