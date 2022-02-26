XML/HTML
========

Übersicht
---------

+-----------------------+-------+-------------------------------------------------------+
| Unterstützung für     | ++    | XML ist sehr flexibel, da jedes Element Attribute und |
| Datenstrukturen       |       | beliebige Kindelemente haben kann.                    |
+-----------------------+-------+-------------------------------------------------------+
| Standardisierung      | ++    | XML ist gut stadnardisiert, die Spezifikation findet  |
|                       |       | ihr unter https://www.w3.org/TR/xml/. XML unterstützt |
|                       |       | sowohl DOM-Parser als auch streaming SAX-Parser.      |
+-----------------------+-------+-------------------------------------------------------+
| Schema-IDL            | ++    | `XML schema`_, `RELAX NG`_                            |
+-----------------------+-------+-------------------------------------------------------+
| Sprachunterstützung   | \+    | Wird in allen wichtigen Sprachen unterstützt,         |
|                       |       | üblicherweise mit integrierten Bibliotheken.          |
+-----------------------+-------+-------------------------------------------------------+
| Menschliche Lesbarkeit| +-    | XML ist ein lesbares Serialisierungsprotokoll. Ein    |
|                       |       | Nachteil vom XML ist die Ausführlichket, insbesondere |
|                       |       | die beschreibenden End-Tags.                          |
+-----------------------+-------+-------------------------------------------------------+
| Geschwindigkeit       | \+    | XML ist ziemlich schnell obwohl es normalerweise      |
|                       |       | langsamer als JSON ist.                               |
+-----------------------+-------+-------------------------------------------------------+
| Dateigröße            | -\-   | XML ist im Vergleich am größten.                      |
+-----------------------+-------+-------------------------------------------------------+

Beispiel
--------

.. code-block:: xml

    <?xml version="1.0" encoding="ISO-8859-1" ?>
    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"></xs:schema>

.. seealso::

    * `Home <https://www.w3.org/XML/>`_
    * `Specification <https://www.w3.org/TR/REC-xml/>`_
    * `Validator <http://validator.w3.org/>`_
    * `The XML FAQ <http://xml.silmaril.ie/>`_

.. _`XML schema`: https://www.w3.org/TR/xmlschema-0/
.. _`RELAX NG`: https://relaxng.org/

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    xml-html-examples.ipynb
    beautifulsoup.ipynb
