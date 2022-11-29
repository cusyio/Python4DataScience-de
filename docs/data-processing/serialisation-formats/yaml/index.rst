YAML
====

Übersicht
---------

+-----------------------+-------+-------------------------------------------------------+
| Unterstützung für     | ++    | YAML, kurz für *YAML Ain’t Markup Language*,          |
| Datenstrukturen       |       | unterstützt die meisten Datentypen, einschließlich    |
|                       |       | Zeichenfolgen, Ganzzahlen, Gleitkommazahlen und       |
|                       |       | Datumsangaben. YAML unterstützt sogar Referenzen und  |
|                       |       | externe Daten.                                        |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | \+    | YAML ist ein stark typisierter formaler Standard, aber|
|                       |       | es ist schwierig, Schema-Validatoren zu finden.       |
+-----------------------+-------+-------------------------------------------------------+
| Schema-IDL            | +-    | Teilweise mit `Kwalify`_, `Rx`_ und integrierten      |
|                       |       | Sprachtypdefinitionen.                                |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | +-    | Es gibt Bibliotheken für die beliebtesten Sprachen.   |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | \+    | Grundlegendes YAML ist wirklich einfach zu lesen, aber|
|                       |       | die Komplexität von YAML kann Leser stark verwirren.  |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | -\-   | YAML kann nur langsam serialisiert und deserialisiert |
|                       |       | werden.                                               |
+-----------------------+-------+-------------------------------------------------------+
| File size             | +-    | YAML liegt im mittleren Bereich ähnlich wie           |
|                       |       | :doc:`../json/index` und :doc:`../toml`.              |
+-----------------------+-------+-------------------------------------------------------+

.. seealso::

    * `Home <https://yaml.org/>`_
    * `Specification <https://yaml.org/spec/>`_
    * `YAML Validator <https://codebeautify.org/yaml-validator>`_
    * `StrictYAML <https://github.com/crdoconnor/strictyaml>`_
    * `noyaml.com <https://noyaml.com/>`_

.. _`Kwalify`: http://www.kuwata-lab.com/kwalify/
.. _`Rx`: http://rx.codesimply.com/

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    example.ipynb
