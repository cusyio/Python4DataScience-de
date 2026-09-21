.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Transformieren
==============

Zum Transformieren der Daten legen wir eine Pipeline an, bei der wir die Erkenntnisse aus
dem :doc:`extract` der Metadaten nutzen. Lediglich die fehlerhafte ``ID`` und den
fehlenden Wert in der ``population``-Spalte müssen wir manuell korrigieren:

.. code-block:: yaml
   :caption: countries.pipeline.yaml

   steps:
     - type: cell-replace
       fieldName: neighbor_id
       pattern: '22'
       replace: '2'
     - type: cell-replace
       fieldName: population
       pattern: 'n/a'
       replace: '67'
     - type: row-filter
       formula: population
     - type: field-update
       name: neighbor_id
       descriptor:
         type: integer
     - type: field-update
       name: population
       descriptor:
         type: integer
     - type: table-normalize
     - type: table-write
       path: countries-cleaned.csv

.. tab:: Terminal

   .. code-block:: console

      $ uv run frictionless transform countries.csv --pipeline countries.pipeline.yaml

      ## Schema

      +-------------+---------+------------+
      | name        | type    | required   |
      +=============+=========+============+
      | id          | integer |            |
      +-------------+---------+------------+
      | neighbor_id | integer |            |
      +-------------+---------+------------+
      | name        | string  |            |
      +-------------+---------+------------+
      | population  | integer |            |
      +-------------+---------+------------+

      ## Table

      +----+-------------+---------+------------+
      | id | neighbor_id | name    | population |
      +====+=============+=========+============+
      |  1 | None        | Britain |         67 |
      +----+-------------+---------+------------+
      |  2 |           3 | France  |         67 |
      +----+-------------+---------+------------+
      |  3 |           2 | Germany |         83 |
      +----+-------------+---------+------------+
      |  4 | None        | Italy   |         60 |
      +----+-------------+---------+------------+

.. tab:: Python

   .. code-block:: pycon

      >>> from frictionless import Resource, Pipeline, describe, transform, steps
      >>> pipeline = Pipeline(
      ...     steps=[
      ...         steps.cell_replace(
      ...             field_name="neighbor_id", pattern="22", replace="2"
      ...         ),
      ...         steps.cell_replace(
      ...             field_name="population", pattern="n/a", replace="67"
      ...         ),
      ...         steps.row_filter(formula="population"),
      ...         steps.field_update(name="neighbor_id", descriptor={"type": "integer"}),
      ...         steps.table_normalize(),
      ...         steps.table_write(path="countries-cleaned.csv"),
      ...     ]
      ... )
      >>> source = Resource("countries.csv")
      >>> target = source.transform(pipeline)
      >>> print(target.read_rows())
      [{'id': 1, 'neighbor_id': None, 'name': 'Britain', 'population': '67'}, {'id': 2, 'neighbor_id': 3, 'name': 'France', 'population': '67'}, {'id': 3, 'neighbor_id': 2, 'name': 'Germany', 'population': '83'}, {'id': 4, 'neighbor_id': None, 'name': 'Italy', 'population': '60'}]

Die Pipeline hat im letzten Schritt die Datei :file:`countries-cleaned.csv` erzeugt:

.. code-block:: csv
   :caption: countries-cleaned.csv

   id,neighbor_id,name,population
   1,,Britain,67
   2,3,France,67
   3,2,Germany,83
   4,,Italy,60

Neben ``cell-replace``, ``row-filter``, ``field-update``, ``table-normalize`` und
``table-write`` gibt es noch eine Vielzahl weiterer Transformationstypen für `Ressourcen
<https://framework.frictionlessdata.io/docs/steps/resource.html>`_, `Tabellen
<https://framework.frictionlessdata.io/docs/steps/table.html>`_, `Feldern
<https://framework.frictionlessdata.io/docs/steps/field.html>`_, `Zeilen
<https://framework.frictionlessdata.io/docs/steps/row.html>`_ und `Zellen
<https://framework.frictionlessdata.io/docs/steps/cell.html>`_. Darüberhinaus könnt ihr
auch eigene ``steps`` definieren.

.. seealso::
   * `Custom Steps
     <https://framework.frictionlessdata.io/docs/guides/transforming-data.html#custom-steps>`_
   * `Working with PETL
     <https://framework.frictionlessdata.io/docs/guides/transforming-data.html#working-with-petl>`_
