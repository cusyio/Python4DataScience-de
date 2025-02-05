.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

FastAPI
=======

FastAPI ist ein Web-Framework zum Erstellen von APIs mit auf Python 3.6+
basierenden Type-Hints.

Hauptmerkmale sind:

* sehr hohe Leistung dank `pydantic <https://docs.pydantic.dev/latest/>`_ für
  den Datenteil und `Starlette <https://www.starlette.io/>`_ für den Web-Teil
* schnell und einfach zu codieren
* Validierung für die meisten Python-Datentypen, einschließlich

  * JSON-Objekte (``dict``)
  * JSON-Array (``list``)
  * String (``str``), definiert die minimale und maximale Länge
  * Zahlen (``int``, ``float``) mit Min- und Max-Werten usw.
  * URLs
  * E -Mail mit `python-email-validator
    <https://github.com/JoshData/python-email-validator>`_
  * UUID
  * … und andere

* robuster, produktionsreifer Code mit automatischer interaktiver Dokumentation
* basierend auf den offenen Standards für APIs: `OpenAPI
  <https://www.openapis.org/>`_ (früher bekannt als Swagger) und `JSON Schema
  <https://json-schema.org>`_

.. seealso::
    * `Home <https://fastapi.tiangolo.com/>`_
    * `GitHub <https://github.com/fastapi/fastapi>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    install
    example
    extensions
