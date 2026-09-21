.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Validieren
==========

Ihr könnt mit Frictionless auch die Daten validieren:

.. tab:: Terminal

   .. code-block:: console

      $ uv run frictionless validate countries.csv
      ──────────────────────────────────────── Dataset ────────────────────────────────────────
                          dataset
      ┏━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┓
      ┃ name      ┃ type  ┃ path          ┃ status  ┃
      ┡━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━┩
      │ countries │ table │ countries.csv │ INVALID │
      └───────────┴───────┴───────────────┴─────────┘
      ──────────────────────────────────────── Tables ─────────────────────────────────────────
                                              countries
      ┏━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      ┃ Row ┃ Field ┃ Type         ┃ Message                                                  ┃
      ┡━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
      │ 4   │ 5     │ extra-cell   │ Row at position "4" has an extra value in field at       │
      │     │       │              │ position "5"                                             │
      │ 7   │ 2     │ missing-cell │ Row at position "7" has a missing cell in field          │
      │     │       │              │ "neighbor_id" at position "2"                            │
      │ 7   │ 3     │ missing-cell │ Row at position "7" has a missing cell in field "name"   │
      │     │       │              │ at position "3"                                          │
      │ 7   │ 4     │ missing-cell │ Row at position "7" has a missing cell in field          │
      │     │       │              │ "population" at position "4"                             │
      └─────┴───────┴──────────────┴──────────────────────────────────────────────────────────┘

.. tab:: Python

   .. code-block:: pycon

      >>> from frictionless import validate
      >>> report = validate("countries.csv")
      >>> print(report.flatten(["rowNumber", "fieldNumber", "type"]))
      [[4, 5, 'extra-cell'], [7, 2, 'missing-cell'], [7, 3, 'missing-cell'], [7, 4, 'missing-cell']]

Wir erwarteten schon, dass einige Zellen fehlen und andere überzählig sind. Legen wir
unsere Metadaten aus der :file:`countries.resource.yaml`-Datei zugrunde, sieht das
Ergebnis folgendermaßen aus:

.. tab:: Terminal

   .. code-block:: console

      $ uv run frictionless validate countries.resource.yaml
      ──────────────────────────────────────── Dataset ────────────────────────────────────────
                          dataset
      ┏━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┓
      ┃ name      ┃ type  ┃ path          ┃ status  ┃
      ┡━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━┩
      │ countries │ table │ countries.csv │ INVALID │
      └───────────┴───────┴───────────────┴─────────┘
      ──────────────────────────────────────── Tables ─────────────────────────────────────────
                                              countries
      ┏━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      ┃ Row ┃ Field ┃ Type         ┃ Message                                                  ┃
      ┡━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
      │ 3   │ 2     │ type-error   │ Type error in the cell "Ireland" in row "3" and field    │
      │     │       │              │ "neighbor_id" at position "2": type is "integer/default" │
      │ 4   │ 5     │ extra-cell   │ Row at position "4" has an extra value in field at       │
      │     │       │              │ position "5"                                             │
      │ 5   │ None  │ foreign-key  │ Row at position "5" violates the foreign key: for        │
      │     │       │              │ "neighbor_id": values "22" not found in the lookup table │
      │     │       │              │ "" as "id"                                               │
      │ 7   │ 2     │ missing-cell │ Row at position "7" has a missing cell in field          │
      │     │       │              │ "neighbor_id" at position "2"                            │
      │ 7   │ 3     │ missing-cell │ Row at position "7" has a missing cell in field "name"   │
      │     │       │              │ at position "3"                                          │
      │ 7   │ 4     │ missing-cell │ Row at position "7" has a missing cell in field          │
      │     │       │              │ "population" at position "4"                             │
      └─────┴───────┴──────────────┴──────────────────────────────────────────────────────────┘

.. tab:: Python

   .. code-block:: pycon

      >>> from frictionless import validate
      >>> report = validate("countries.resource.yaml")
      >>> print(report.flatten(["rowNumber", "fieldNumber", "type"]))
      [[3, 2, 'type-error'], [4, 5, 'extra-cell'], [5, None, 'foreign-key'], [7, 2, 'missing-cell'], [7, 3, 'missing-cell'], [7, 4, 'missing-cell']]

Jetzt sieht es sogar noch schlimmer aus, dennoch konnten wir dank der Metadaten einige
Fehler aufdecken:

* den falschen Datentypen ``Irland`` anstelle einer ID
* die fehlerhafte Beziehung zwischen ``ID`` und ``neighbor_id``: es gibt kein Land mit
  der ID ``22``

In :doc:`transform` werden wir die Metadaten verwenden, um die Probleme mit den
Datentypen zu beheben.

Es können jedoch nicht nur die Daten validiert werden, auch die Metadaten des Schema, die
Daten und Metadaten der Ressource oder des Pakets sowie ein spezielles
``Inquiry``-Objekt, das Anweisungen für eine Validierungsaufgabe enthält.

.. tab:: Terminal

   :samp:`$ uv run frictionless validate {SOURCE_FILE}`
       erkennt den Quelltyp und validiert die Daten entsprechend
   :samp:`$ uv run frictionless validate {SCHEMA}.yaml --type schema`
       validiert die Metadaten eines Schemas
   :samp:`$ uv run frictionless validate {SOURCE_FILE} --type resource`
       validiert die Daten und Metadaten einer Ressource
   :samp:`$ uv run frictionless validate {PACKAGE_FILE} --type package`
       validiert die Daten und Metadaten eines Pakets
   :samp:`$ uv run frictionless validate {INQUIRE}.yaml --type inquiry`
       validiert ein spezielles ``Inquiry``-Objekt

.. tab:: Python

   :samp:`frictionless.validate({SOURCE_FILE}, type="table")`
       erkennt den Quelltyp und validiert die Daten entsprechend
   :samp:`frictionless.validate({SCHEMA}.yaml, type="schema")`
       validiert die Metadaten eines Schemas
   :samp:`frictionless.validate({SOURCE_FILE}, type="resource")`
       validiert die Daten und Metadaten einer Ressource
   :samp:`frictionless.validate({PACKAGE_FILE}, type="package")`
       validiert die Daten und Metadaten eines Pakets
   :samp:`frictionless.validate({INQUIRE}.yaml, type="inquiry")`
       validiert ein spezielles ``Inquiry``-Objekt

.. seealso::
   * `Validating Data
     <https://framework.frictionlessdata.io/docs/guides/validating-data.html>`_
