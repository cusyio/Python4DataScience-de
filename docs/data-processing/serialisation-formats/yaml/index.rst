.. SPDX-FileCopyrightText: 2021 Veit Schiele
.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

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
|                       |       | :doc:`../json/index` und :doc:`../toml/index`.        |
+-----------------------+-------+-------------------------------------------------------+

.. seealso::

    * `Home <https://yaml.org/>`_
    * `Specification <https://yaml.org/spec/>`_
    * `YAML Validator <https://codebeautify.org/yaml-validator>`_
    * `StrictYAML <https://hitchdev.com/strictyaml/>`_
    * `What YAML features does StrictYAML remove?
      <https://hitchdev.com/strictyaml/features-removed/>`_
    * `noyaml.com <https://noyaml.com/>`_

.. _`Kwalify`: http://www.kuwata-lab.com/kwalify/
.. _`Rx`: https://rx.codesimply.com

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    example.ipynb
