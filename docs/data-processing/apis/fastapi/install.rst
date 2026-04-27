.. SPDX-FileCopyrightText: 2021 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Installation
============

Anforderungen
-------------

.. code-block:: console

    $ uv add fastapi
    Adding fastapi to Pipfile's [packages]…
    ✔ Installation Succeeded
    Locking [dev-packages] dependencies…
    ✔ Success!
    Locking [packages] dependencies…
    ✔ Success!
    …

Optionale Anforderungen
~~~~~~~~~~~~~~~~~~~~~~~

Für die Produktion benötigt ihr außerdem einen `ASGI
<https://asgi.readthedocs.io/en/latest/>`_-Server wie `uvicorn
<http://www.uvicorn.org/>`_:

.. code-block:: console

    $ uv add uvicorn
    Adding uvicorn to Pipfile's [packages]…
    ✔ Installation Succeeded
    Locking [dev-packages] dependencies…
    ✔ Success!
    Locking [packages] dependencies…
    ✔ Success!
    Updated Pipfile.lock (051f02)!
    …

Pydantic kann die folgenden optionalen Abhängigkeiten verwenden:

`ujson <https://github.com/ultrajson/ultrajson>`_
    für schnelleres JSON-Parsing.

    .. image:: https://raster.shields.io/github/stars/ultrajson/ultrajson
       :alt: Stars
       :target: https://github.com/ultrajson/ultrajson

    .. image:: https://raster.shields.io/github/contributors/ultrajson/ultrajson
       :alt: Contributors
       :target: https://github.com/ultrajson/ultrajson/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/ultrajson/ultrajson
       :alt: Commit activity
       :target: https://github.com/ultrajson/ultrajson/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/ultrajson/ultrajson
       :alt: Lizenz

`email_validator <https://github.com/JoshData/python-email-validator>`_
    zur E-Mail-Validierung.

    .. image:: https://raster.shields.io/github/stars/JoshData/python-email-validator
       :alt: Stars
       :target: https://github.com/JoshData/python-email-validator

    .. image:: https://raster.shields.io/github/contributors/JoshData/python-email-validator
       :alt: Contributors
       :target: https://github.com/JoshData/python-email-validator/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/JoshData/python-email-validator
       :alt: Commit activity
       :target: https://github.com/JoshData/python-email-validator/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/JoshData/python-email-validator
       :alt: Lizenz


Starlette kann die folgenden optionalen Abhängigkeiten verwenden:

:doc:`httpx <../../httpx/index>`
    wenn ihr den ``TestClient`` verwenden wollt.

    .. image:: https://raster.shields.io/github/stars/encode/httpx
       :alt: Stars
       :target: https://github.com/encode/httpx

    .. image:: https://raster.shields.io/github/contributors/encode/httpx
       :alt: Contributors
       :target: https://github.com/encode/httpx/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/encode/httpx
       :alt: Commit activity
       :target: https://github.com/encode/httpx/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/encode/httpx
       :alt: Lizenz

`jinja <https://jinja.palletsprojects.com/>`_
    wenn ihr die Standard-Template-Konfiguration verwenden wollt.

    .. image:: https://raster.shields.io/github/stars/pallets/jinja
       :alt: Stars
       :target: https://github.com/pallets/jinja

    .. image:: https://raster.shields.io/github/contributors/pallets/jinja
       :alt: Contributors
       :target: https://github.com/pallets/jinja/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/pallets/jinja
       :alt: Commit activity
       :target: https://github.com/pallets/jinja/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/pallets/jinja
       :alt: Lizenz

`graphene <https://graphene-python.org/>`_
    für die Unterstützung von ``GraphQLApp``.

    .. image:: https://raster.shields.io/github/stars/graphql-python/graphene
       :alt: Stars
       :target: https://github.com/graphql-python/graphene

    .. image:: https://raster.shields.io/github/contributors/graphql-python/graphene
       :alt: Contributors
       :target: https://github.com/graphql-python/graphene/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/graphql-python/graphene
       :alt: Commit activity
       :target: https://github.com/graphql-python/graphene/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/graphql-python/graphene
       :alt: Lizenz

`orjson <https://github.com/ijl/orjson>`_
    wenn ihr ``ORJSONResponse`` verwenden wollt.

    .. image:: https://raster.shields.io/github/stars/ijl/orjson
       :alt: Stars
       :target: https://github.com/ijl/orjson

    .. image:: https://raster.shields.io/github/contributors/ijl/orjson
       :alt: Contributors
       :target: https://github.com/ijl/orjson/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/ijl/orjson
       :alt: Commit activity
       :target: https://github.com/ijl/orjson/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/ijl/orjson
       :alt: Lizenz

`aiofiles <https://github.com/Tinche/aiofiles>`_
    wenn ihr ``FileResponse`` oder ``StaticFiles`` verwenden wollt.

    .. image:: https://raster.shields.io/github/stars/Tinche/aiofiles
       :alt: Stars
       :target: https://github.com/Tinche/aiofiles

    .. image:: https://raster.shields.io/github/contributors/Tinche/aiofiles
       :alt: Contributors
       :target: https://github.com/Tinche/aiofiles/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/Tinche/aiofiles
       :alt: Commit activity
       :target: https://github.com/Tinche/aiofiles/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/Tinche/aiofiles
       :alt: Lizenz

`itsdangerous <https://itsdangerous.palletsprojects.com/>`_
    erforderlich für die Unterstützung von ``SessionMiddleware``.

    .. image:: https://raster.shields.io/github/stars/pallets/itsdangerous
       :alt: Stars
       :target: https://github.com/pallets/itsdangerous

    .. image:: https://raster.shields.io/github/contributors/pallets/itsdangerous
       :alt: Contributors
       :target: https://github.com/pallets/itsdangerous/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/pallets/itsdangerous
       :alt: Commit activity
       :target: https://github.com/pallets/itsdangerous/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/pallets/itsdangerous
       :alt: Lizenz

`pyyaml <https://pyyaml.org/wiki/PyYAMLDocumentation>`_
    für die Unterstützung von Starlette’s ``SchemaGenerator``.

    .. image:: https://raster.shields.io/github/stars/yaml/pyyaml
       :alt: Stars
       :target: https://github.com/yaml/pyyaml

    .. image:: https://raster.shields.io/github/contributors/yaml/pyyaml
       :alt: Contributors
       :target: https://github.com/yaml/pyyaml/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/yaml/pyyaml
       :alt: Commit activity
       :target: https://github.com/yaml/pyyaml/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/yaml/pyyaml
       :alt: Lizenz

`python-multipart <https://multipart.fastapiexpert.com>`_
    wenn ihr das Parsen von Formularen mit ``request.form()`` unterstützen
    wollt.

    .. image:: https://raster.shields.io/github/stars/Kludex/python-multipart
       :alt: Stars
       :target: https://github.com/Kludex/python-multipart

    .. image:: https://raster.shields.io/github/contributors/Kludex/python-multipart
       :alt: Contributors
       :target: https://github.com/Kludex/python-multipart/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/Kludex/python-multipart
       :alt: Commit activity
       :target: https://github.com/Kludex/python-multipart/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/Kludex/python-multipart
       :alt: Lizenz

Sie können installiert werden, :abbr:`z. B. (zum Beispiel)` mit:

.. code-block:: console

    $ uv add fastapi[ujson]

Alternativ könnt ihr alle installieren mit:

.. code-block:: console

    $ uv add fastapi[all]

.. seealso::
   * `FastAPI Dependencies <https://fastapi.tiangolo.com/#dependencies>`_
