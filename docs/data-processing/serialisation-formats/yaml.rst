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
|                       |       | :doc:`json` und :doc:`toml`.                          |
+-----------------------+-------+-------------------------------------------------------+

Beispiel
--------

`CITATION.cff <https://citation-file-format.github.io/>`_

.. code-block:: yaml

    # YAML 1.2
    ---
    cff-version: 1.1.0
    message: If you use this software, please cite it as below.
    authors:
      - family-names: Druskat
        given-names: Stephan
        orcid: https://orcid.org/0000-0003-4925-7248
    title: "My Research Software"
    version: 2.0.4
    doi: 10.5281/zenodo.1234
    date-released: 2017-12-18

.. seealso::

    * `Home <https://yaml.org/>`_
    * `Specification <https://yaml.org/spec/>`_
    * `YAML Validator <https://codebeautify.org/yaml-validator>`_
    * `StrictYAML <https://github.com/crdoconnor/strictyaml>`_
    * `noyaml.com <https://noyaml.com/>`_

.. _`Kwalify`: http://www.kuwata-lab.com/kwalify/
.. _`Rx`: http://rx.codesimply.com/
