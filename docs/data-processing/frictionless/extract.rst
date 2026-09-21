.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Extrahieren
===========

Um die Daten als Tabelle zu extrahieren können wir ``frictionless extract`` verwenden.
Zunächst ignorieren wir hierfür die Metadaten in der
:file:`countries.resource.yaml`-Datei:

.. tab:: Terminal

   .. code-block:: console

      $ uv run frictionless extract countries.csv
      ──────────────────────────────────────── Dataset ────────────────────────────────────────
                     dataset
      ┏━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┓
      ┃ name      ┃ type  ┃ path          ┃
      ┡━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━┩
      │ countries │ table │ countries.csv │
      └───────────┴───────┴───────────────┘
      ──────────────────────────────────────── Tables ─────────────────────────────────────────
                       countries
      ┏━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━┓
      ┃ id ┃ neighbor_id ┃ name    ┃ population ┃
      ┡━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━┩
      │ 1  │ Ireland     │ Britain │ 67         │
      │ 2  │ 3           │ France  │ n/a        │
      │ 3  │ 22          │ Germany │ 83         │
      │ 4  │ None        │ Italy   │ 60         │
      │ 5  │ None        │ None    │ None       │
      └────┴─────────────┴─────────┴────────────┘

.. tab:: Python

   .. code-block:: pycon

      >>> from frictionless import extract
      >>> rows = extract("countries.csv")
      >>> print(rows)
      {'countries': [{'id': 1, 'neighbor_id': 'Ireland', 'name': 'Britain', 'population': '67'}, {'id': 2, 'neighbor_id': '3', 'name': 'France', 'population': 'n/a'}, {'id': 3, 'neighbor_id': '22', 'name': 'Germany', 'population': '83'}, {'id': 4, 'neighbor_id': None, 'name': 'Italy', 'population': '60'}, {'id': 5, 'neighbor_id': None, 'name': None, 'population': None}]}

Jetzt erst wird so richtig deutlich, dass die Quelldaten so nicht wirklich nützlich sind:

* da Ganzzahlen mit Zeichenketten vermischt sind, lassen sich die Daten beispielsweise
  nicht in eine SQL-Datenbank importieren
* Es gibt einen leeren Datensatz
* In der Spalte ``neighbor_id`` befinden sich gleich mehrere Fehler

Wenn wir unsere Metadaten aus :file:`countries.resource.yaml` verwenden, wird die Ausgabe
besser:

.. tab:: Terminal

   .. code-block:: console

      $ uv run frictionless extract countries.resource.yaml
      ──────────────────────────────────────── Dataset ────────────────────────────────────────
                     dataset
      ┏━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┓
      ┃ name      ┃ type  ┃ path          ┃
      ┡━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━┩
      │ countries │ table │ countries.csv │
      └───────────┴───────┴───────────────┘
      ──────────────────────────────────────── Tables ─────────────────────────────────────────
                       countries
      ┏━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━┓
      ┃ id ┃ neighbor_id ┃ name    ┃ population ┃
      ┡━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━┩
      │ 1  │ None        │ Britain │ 67         │
      │ 2  │ 3           │ France  │ None       │
      │ 3  │ 22          │ Germany │ 83         │
      │ 4  │ None        │ Italy   │ 60         │
      │ 5  │ None        │ None    │ None       │
      └────┴─────────────┴─────────┴────────────┘

.. tab:: Python

   .. code-block:: pycon

      >>> from frictionless import extract
      >>> rows = extract("countries.resource.yaml")
      >>> print(rows)
      {'countries': [{'id': 1, 'neighbor_id': None, 'name': 'Britain', 'population': 67}, {'id': 2, 'neighbor_id': 3, 'name': 'France', 'population': None}, {'id': 3, 'neighbor_id': 22, 'name': 'Germany', 'population': 83}, {'id': 4, 'neighbor_id': None, 'name': 'Italy', 'population': 60}, {'id': 5, 'neighbor_id': None, 'name': None, 'population': None}]}

Nun sind die Daten schon ein wenig besser geworden:

* Felder sind nun numerisch geworden
* Es gibt nun keine textuellen Markierungen mehr für fehlende Werte
* Fehlende Werte werden in Python nun als :doc:`python-basics:types/none`-Werte
  dargestellt
* Schließlich könnten die Daten nun beispielsweise in SQL-Datenbanken exportiert werden

Es können jedoch nicht nur die Daten extrahiert werden, auch die Tabelle oder Metadaten
können zurückgegeben werden:

.. tab:: Terminal

   :samp:`$ uv run frictionless extract {SOURCE_FILE}`
       erkennt den Typ der Quelldatei und extrahiert die Daten entsprechend
   :samp:`$ uv run frictionless extract {SOURCE_FILE} --type resource`
       gibt eine Datentabelle zurück
   :samp:`$ uv run frictionless extract {SOURCE_FILE} --type package`
       gibt die Metadaten des Datenpakets zurück

.. tab:: Python

   :samp:`frictionless.extract({SOURCE_FILE})`
       erkennt den Typ der Quelldatei und extrahiert
   :samp:`frictionless.extract({SOURCE_FILE}, type="resource")`
       gibt eine Datentabelle zurück
   :samp:`frictionless.extract({SOURCE_FILE}, type="package")`
       gibt die Metadaten des Datenpakets zurück

.. seealso::
   * `Extracting Data
     <https://framework.frictionlessdata.io/docs/guides/extracting-data.html>`_
