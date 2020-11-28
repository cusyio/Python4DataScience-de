TOML
====

Überblick
---------

+-----------------------+-------+-------------------------------------------------------+
| Unterstützung für     | \+    | TOML (Tom’s Obvious, Minimal Language) unterstützt die|
| Datenstrukturen       |       | meisten Datenstrukturen, einschließlich Zeichenfolgen,|
|                       |       | Ganzzahlen, Gleitkommazahlen und Datumsangaben, jedoch|
|                       |       | keine Referenzen wie YAML.                            |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | ++    | TOML ist ein formaler, stark typisierter Standard.    |
+-----------------------+-------+-------------------------------------------------------+
| Schema-IDL            | +-    | Teilweise mit `JSON Schema Everywhere`_               |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | ++    | TOML ist ein relativ junges Serialisierungsformat und |
|                       |       | findet noch nicht so breite Unterstützung wie  JSON,  |
|                       |       | CSV oder XML in den verschiedenen Programmiersprachen.|
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | ++    | Eines der Hauptziele von TOML war es, sehr einfach zu |
|                       |       | lesen zu sein.                                        |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | +-    | TOML kann mit mittlerer Geschwindigkeit verarbeitet   |
|                       |       | werden.                                               |
+-----------------------+-------+-------------------------------------------------------+
| File size             | \-    | Nur :doc:`xml` ist weniger kompakt.                   |
+-----------------------+-------+-------------------------------------------------------+

Beispiel
--------

`pyproject.toml
<https://github.com/veit/jupyter-tutorial/blob/master/pyproject.toml>`_

.. code-block:: toml

    [tool.black]
    line-length = 79

    [tool.isort]
    atomic=true
    force_grid_wrap=0
    include_trailing_comma=true
    lines_after_imports=2
    lines_between_types=1
    multi_line_output=3
    not_skip="__init__.py"
    use_parentheses=true

    known_first_party="jupyter-tutorial"
    known_third_party=["mpi4py", "numpy", "requests"]

.. seealso::

    * `Home <https://toml.io/>`_
    * `GitHub <https://github.com/toml-lang/toml>`_
    * `Wiki <https://github.com/toml-lang/toml/wiki>`_
    * `What is wrong with TOML?
      <https://hitchdev.com/strictyaml/why-not/toml/>`_
    * `An INI critique of TOML
      <https://github.com/madmurphy/libconfini/wiki/An-INI-critique-of-TOML>`_

.. _`JSON Schema Everywhere`: https://json-schema-everywhere.github.io/toml
