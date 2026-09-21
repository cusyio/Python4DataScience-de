.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Beschreiben
===========

Angenommen, euch sind Daten im :doc:`../serialisation-formats/csv/index`-Format zur
Verfügung gestellt worden. Mit ``frictionless describe`` oder :func:`frictionless
describe` könnt ihr euch einfach einen ersten Überblick verschaffen, :abbr:`z. B. (zum
Beispiel)` für die Datei :download:`countries.csv
<https://raw.githubusercontent.com/frictionlessdata/frictionless-py/main/data/countries.csv>`
mit

.. tab:: Terminal

   .. code-block:: console

      $ uv run frictionless describe countries.csv
      ──────────────────────────────────────── Dataset ────────────────────────────────────────
                     dataset
      ┏━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┓
      ┃ name      ┃ type  ┃ path          ┃
      ┡━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━┩
      │ countries │ table │ countries.csv │
      └───────────┴───────┴───────────────┘
      ──────────────────────────────────────── Tables ─────────────────────────────────────────
                         countries
      ┏━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┓
      ┃ id      ┃ neighbor_id ┃ name   ┃ population ┃
      ┡━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━┩
      │ integer │ string      │ string │ string     │
      └─────────┴─────────────┴────────┴────────────┘

.. tab:: Python

   .. code-block:: pycon

      >>> from frictionless import describe
      >>> resource = describe("countries.csv")
      >>> print(resource)
      {'name': 'countries',
       'type': 'table',
       'path': 'countries.csv',
       'scheme': 'file',
       'format': 'csv',
       'mediatype': 'text/csv',
       'encoding': 'utf-8',
       'dialect': {'headerRows': [2]},
       'schema': {'fields': [{'name': 'id', 'type': 'integer'},
                             {'name': 'neighbor_id', 'type': 'string'},
                             {'name': 'name', 'type': 'string'},
                             {'name': 'population', 'type': 'string'}]}}

Wir können diese Metainformationen auch in eine Datei schreiben:

.. tab:: Terminal

   .. code-block:: console

      $ uv run frictionless describe countries.csv --yaml > countries.resource.yaml
      $ cat countries.resource.yaml

   .. code-block:: yaml

      name: countries
      type: table
      path: countries.csv
      scheme: file
      format: csv
      mediatype: text/csv
      encoding: utf-8
      dialect:
        headerRows:
          - 2
      schema:
        fields:
          - name: id
            type: integer
          - name: neighbor_id
            type: string
          - name: name
            type: string
          - name: population
            type: string

.. tab:: Python

   .. code-block:: pycon

      >>> from frictionless import describe
      >>> resource = describe("countries.csv")
      >>> resource.to_yaml("countries.resource.yaml")
      'name: countries\ntype: table\npath: countries.csv\nscheme: file\nformat: csv\nmediatype: text/csv\nencoding: utf-8\ndialect:\n  headerRows:\n    - 2\nschema:\n  fields:\n    - name: id\n      type: integer\n    - name: neighbor_id\n      type: string\n    - name: name\n      type: string\n    - name: population\n      type: string\n'

Frictionless hat zwar erkannt, dass die erste Zeile ein Kommentar ist, dennoch gibt es
noch ein paar Probleme: ``n/a`` soll für fehlende Werte verwendet werden und
``neighbor_id`` soll numerisch sein. Hierfür aktualisieren wir unsere Metadaten und
speichern sie dauerhaft in einer Datei:

.. tab:: Python

   .. code-block:: pycon
      :emphasize-lines: 29, 33, 34-36, 37-

      >>> from frictionless import Detector, describe
      >>> detector = Detector(field_missing_values=["", "n/a"])
      >>> resource = describe("countries.csv", detector=detector)
      >>> resource.schema.set_field_type("neighbor_id", "integer")
      {'name': 'neighbor_id', 'type': 'string'}
      >>> resource.schema.foreign_keys.append(
      ...     {
      ...         "fields": ["neighbor_id"],
      ...         "reference": {"resource": "", "fields": ["id"]},
      ...     }
      ... )
      >>> resource.to_yaml("countries.resource.yaml")
      "name: countries\ntype: table\npath: countries.csv\nscheme: file\nformat: csv\nmediatype: text/csv\nencoding: utf-8\ndialect:\n  headerRows:\n    - 2\nschema:\n  fields:\n    - name: id\n      type: integer\n    - name: neighbor_id\n      type: integer\n    - name: name\n      type: string\n    - name: population\n      type: integer\n  missingValues:\n    - ''\n    - n/a\n  foreignKeys:\n    - fields:\n        - neighbor_id\n      reference:\n        resource: ''\n        fields:\n          - id\n"
      >>> with open("countries.resource.yaml") as file:
      ...     print(file.read())
      ...
      name: countries
      type: table
      path: countries.csv
      scheme: file
      format: csv
      mediatype: text/csv
      encoding: utf-8
      dialect:
        headerRows:
          - 2
      schema:
        fields:
          - name: id
            type: integer
          - name: neighbor_id
            type: integer
          - name: name
            type: string
          - name: population
            type: integer
        missingValues:
          - ''
          - n/a
        foreignKeys:
          - fields:
              - neighbor_id
            reference:
              resource: ''
              fields:
                - id

Neben :func:`frictionless.describe` gibt es noch weitere :func:`describe`-Funktionen in
Python:

:func:`frictionless.Schema.describe`
    gibt immer Metadaten zum Tabellenschema zurück
:func:`frictionless.Resource.describe`
    gibt immer Metadaten der Datenressource zurück
:func:`frictionless.Package.describe`
    gibt immer die Metadaten des Datenpakets zurück

M Terminal gibt es nur einen Befehl ``frictionless describe``, aber dessen Verhalten
lässt sich durch Flags anpassen:

.. dropdown:: ``$ uv run frictionless describe --help``

   .. code-block:: console

       Usage: frictionless describe [OPTIONS] [source]...

       Describe a data source.

       Based on the inferred data source type it will return resource or package descriptor.
       Default output format is YAML with a front matter.

      ╭─ Arguments ───────────────────────────────────────────────────────────────────────────╮
      │   source      <str>  Data source                                                      │
      ╰───────────────────────────────────────────────────────────────────────────────────────╯
      ╭─ Options ─────────────────────────────────────────────────────────────────────────────╮
      │ --name                                              <str>    Name of resource or      │
      │                                                              table                    │
      │ --type                                              <str>    Specify type e.g.        │
      │                                                              "package"                │
      │ --path                                              <str>    Specify the data path    │
      │                                                              explicitly (e.g. you     │
      │                                                              need to use it if your   │
      │                                                              data is JSON)            │
      │ --scheme                                            <str>    Specify scheme           │
      │ --format                                            <str>    Specify format           │
      │ --encoding                                          <str>    Specify encoding  .      │
      │                                                              Output will be utf-8     │
      │                                                              encoded                  │
      │ --innerpath                                         <str>    Specify in-archive path  │
      │ --compression                                       <str>    Specify compression      │
      │ --dialect                                           <str>    An inline JSON object or │
      │                                                              a path to a JSON file    │
      │                                                              that provides the        │
      │                                                              dialect (configuration   │
      │                                                              for the parser)          │
      │ --header-rows                                       <str>    Comma-separated row      │
      │                                                              numbers                  │
      │ --header-join                                       <str>    Multiline header joiner  │
      │ --comment-char                                      <str>    A char indicating that   │
      │                                                              the row is a comment     │
      │                                                              e.g. "#"                 │
      │ --comment-rows                                      <str>    Comma-separated rows to  │
      │                                                              be considered as         │
      │                                                              comments e.g. "2,3,4,5"  │
      │ --sheet                                             <str>    The sheet to use from    │
      │                                                              the input data (only     │
      │                                                              with XLS and ODS         │
      │                                                              files/plugins)           │
      │ --table                                             <str>    The table to use from    │
      │                                                              the SQL database (SQL    │
      │                                                              plugin)                  │
      │ --keys                                              <str>    The keys to use as       │
      │                                                              column names for the     │
      │                                                              Inline or JSON data      │
      │                                                              plugins                  │
      │ --keyed                   --no-keyed                         Whether the input data   │
      │                                                              is keyed for the Inline  │
      │                                                              or JSON data plugins     │
      │ --buffer-size                                       <int>    Limit the amount of      │
      │                                                              bytes to be extracted as │
      │                                                              a buffer                 │
      │                                                              [default: 100000]        │
      │ --sample-size                                       <int>    Limit the number of rows │
      │                                                              to be extracted as a     │
      │                                                              sample                   │
      │                                                              [default: 100]           │
      │ --field-type                                        <str>    Force all the fields to  │
      │                                                              have this type           │
      │ --field-names                                       <str>    Comma-separated list of  │
      │                                                              field names              │
      │ --field-confidence                                  <float>  Infer confidence. A      │
      │                                                              float from 0 to 1. If 1, │
      │                                                              (sampled) data is        │
      │                                                              guaranteed to be valid   │
      │                                                              against the inferred     │
      │                                                              schema                   │
      │                                                              [default: 0.9]           │
      │ --field-float-numbers     --no-field-float-numb…             Make number floats       │
      │                                                              instead of decimals      │
      │                                                              [default:                │
      │                                                              no-field-float-numbers]  │
      │ --field-missing-values                              <str>    Comma-separated list of  │
      │                                                              missing values           │
      │                                                              [default: ""]            │
      │ --basepath                                          <str>    Basepath of the          │
      │                                                              resource/package         │
      │ --stats                   --no-stats                         Infer stats              │
      │ --yaml                    --no-yaml                          Return in pure YAML      │
      │                                                              format                   │
      │                                                              [default: no-yaml]       │
      │ --json                    --no-json                          Return in JSON format    │
      │                                                              [default: no-json]       │
      │ --debug                   --no-debug                         Enable debug mode        │
      │                                                              [default: no-debug]      │
      │ --trusted                 --no-trusted                       Follow unsafe paths      │
      │                                                              [default: no-trusted]    │
      │ --standards                                         <str>    Possible options: v1, v2 │
      │                                                              (default: v2)            │
      │ --help                                                       Show this message and    │
      │                                                              exit.                    │
      ╰───────────────────────────────────────────────────────────────────────────────────────╯

.. seealso::
   * `Describing Data
     <https://framework.frictionlessdata.io/docs/guides/describing-data.html>`_
