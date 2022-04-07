Erweiterungen
=============

Administration
--------------

`SQLAlchemy Admin for Starlette/FastAPI <https://github.com/aminalaee/sqladmin>`_
    Flexible Admin-Schnittstelle für
    :doc:`/data-processing/postgresql/sqlalchemy`-Modelle
`Piccolo Admin <https://github.com/piccolo-orm/piccolo_admin>`_
    Einfache, aber leistungsstarke Admin-Oberfläche über Piccolo-Tabellen, mit
    der ihr eure Daten leicht hinzufügen, bearbeiten und filtern könnt

Authentifizierung
-----------------

`AuthX <https://github.com/yezz123/AuthX>`_
    Gebrauchsfertige und anpassbare Authentifizierungen und Oauth2-Management
`FastAPI Security <https://github.com/jacobsvante/fastapi-security>`_
    Authentifizierung und Autorisierung
`FastAPI simple security <https://github.com/mrtolkien/fastapi_simple_security>`_
    Auf API-Schlüsseln basierendes Sicherheitspaket, das fokusiert ist auf die
    enfache Nutzung
`FastAPI Users <https://github.com/fastapi-users/fastapi-users>`_
    Fügt schnell ein anpassungsfühiges Registrierungs- und
    Authentifizierungssystem hinzu

ORMs
----

`FastAPI-SQLAlchemy <https://github.com/mfreeborn/fastapi-sqlalchemy>`_
    Einfache Integration zwischen FastAPI,
    :doc:`/data-processing/postgresql/sqlalchemy` und Anwendung
`FastAPIwee <https://github.com/Ignisor/FastAPIwee>`_
    Einfache Möglichkeit, eine REST-API auf der Grundlage von `PeeWee
    <https://github.com/coleifer/peewee>`_-Modellen zu erstellen
`GINO <https://github.com/python-gino/gino>`_
    leichtgewichtiger asynchroner ORM, der auf SQLAlchemy Core für Python
    :doc:`asyncio </performance/asyncio-example>` aufbaut und PostgreSQL mit
    `asyncpg <https://github.com/MagicStack/asyncpg>`_, und MySQL mit `aiomysql
    <https://github.com/aio-libs/aiomysql>`_ unterstützt (→ `Beispiel
    <https://github.com/leosussan/fastapi-gino-arq-uvicorn>`_)
`ORM <https://github.com/encode/orm>`_
    async ORM, der auf SQLAlchemy Core, `Databases
    <https://github.com/encode/databases>`_ und `TypeSystem
    <https://github.com/encode/typesystem>`_ aufbaut  
`ormar <https://github.com/collerek/ormar/>`_
    asynchroner Mini-ORM, mit dem ihr nur ein Set von Modellen pflegen und ggf.
    mit :doc:`/data-processing/postgresql/alembic` migrieren müsst (→ `Beispiel
    <https://collerek.github.io/ormar/fastapi/>`__); zudem wird er unterstützt
    von `fastapi-users <https://github.com/fastapi-users/fastapi-users>`_,
    `fastapi-crudrouter <https://github.com/awtkns/fastapi-crudrouter>`_ und
    `fastapi-pagination <https://github.com/uriyyo/fastapi-pagination>`_.
`Piccolo <https://github.com/piccolo-orm/piccolo>`_
    Schneller, benutzerfreundlicher ORM und Query Builder, das Asyncio
    unterstützt (→ `Beispiele
    <https://github.com/piccolo-orm/piccolo_examples>`__)
`Prisma Client Python <https://github.com/RobertCraigie/prisma-client-py>`_
    Aufbauend auf dem TypeScript ORM `Prisma
    <https://github.com/prisma/prisma>`_ mit Unterstützung von PostgreSQL,
    MySQL, SQLite, MongoDB und SQL Server (→ `Beispiel
    <https://github.com/RobertCraigie/prisma-client-py/tree/main/examples/fastapi-basic>`__)
`Tortoise ORM <https://github.com/tortoise/tortoise-orm>`_
    Einfach zu bedienender asyncio ORM, inspiriert von Django (→ `Beispiele
    <https://tortoise.github.io/examples/fastapi.html>`__); `Aerich
    <https://github.com/tortoise/aerich>`_ ist ein Datenbankmigrationswerkzeug
    für Tortoise ORM
`SQLModel <https://github.com/tiangolo/sqlmodel>`_
    Bibliothek für die Interaktion von SQL-Datenbanken mit Python-Objekten

SQL Query Builders
------------------

`asyncpgsa <https://github.com/CanopyTax/asyncpgsa>`_
    Python-Wrapper um `asyncpg <https://github.com/MagicStack/asyncpg>`_ für die
    Verwendung mit :doc:`/data-processing/postgresql/sqlalchemy`
`Databases <https://github.com/encode/databases>`_
    Einfache Asyncio-Unterstützung für die Datenbanktreiber `asyncpg
    <https://github.com/MagicStack/asyncpg>`_, `aiopg
    <https://github.com/aio-libs/aiopg>`_, `aiomysql
    <https://github.com/aio-libs/aiomysql>`_, `asyncmy
    <https://github.com/long2ice/asyncmy>`_ und `aiosqlite
    <https://github.com/omnilib/aiosqlite>`_

ODMs
----

`Beanie <https://github.com/roman-right/beanie>`_
    Asynchroner Python-Objekt-Dokumenten-Mapper (ODM) für MongoDB, basierend auf
    `Motor <https://motor.readthedocs.io/en/stable/>`_ und `Pydantic
    <https://pydantic-docs.helpmanual.io/>`__
`MongoEngine <https://github.com/MongoEngine/mongoengine>`_
    Python Object-Document Mapper für die Arbeit mit MongoDB
`ODMantic <https://github.com/art049/odmantic/>`_
    Asynchroner ODM (Object Document Mapper) für MongoDB basierend auf
    Python-Typ-Hints und `pydantic <https://pydantic-docs.helpmanual.io/>`__

Code-Generatoren
----------------

`fastapi-code-generator <https://github.com/koxudaxi/fastapi-code-generator>`_
    Code-Generator erstellt eine FastAPI-Anwendung aus einer openapi-Datei,
    wobei `datamodel-code-generator
    <https://github.com/koxudaxi/datamodel-code-generator>`_ zum Generieren des
    pydantic-Modells verwendet wird
`FastAPI-based API Client Generator <https://github.com/dmontagu/fastapi_client>`_
    mypy- und IDE-freundlicher API-Client aus einer OpenAPI-Spezifikation unter
    Verwendung des `OpenAPI Generator
    <https://github.com/OpenAPITools/openapi-generator>`_

Dienstprogramme
---------------

Caching
~~~~~~~

`FastAPI Cache <https://github.com/comeuplater/fastapi_cache>`_
    Leichtgewichtiges Cache-System
`fastapi-cache <https://github.com/long2ice/fastapi-cache>`_
    Caching von Fastapi-Antworten und Funktionsergebnissen, mit Backends, die
    `redis`, `memcache` und `dynamodb` unterstützen.

E-Mail
~~~~~~

`Fastapi-mail <https://github.com/sabuhish/fastapi-mail>`_
    Leichtes Mailsystem zum Versenden von E-Mails und Anhängen, einzeln oder
    auch in großen Mengen

GraphQL
~~~~~~~

`Strawberry GraphQL <https://github.com/strawberry-graphql/strawberry>`_
    Python GraphQL Bibliothek basierend auf Datenklassen

Logging
~~~~~~~

`ASGI Correlation ID middleware <https://github.com/snok/asgi-correlation-id>`_
    Middleware zum Laden oder Erzeugen von Korrelations-IDs für jede eingehende
    Anfrage
`starlette context <https://github.com/tomwojcik/starlette-context>`_
    Middleware für Starlette, die euch ermöglicht, die Kontextdaten einer
    Anfrage zu speichern und darauf zuzugreifen

Prometheus
~~~~~~~~~~

`Prometheus FastAPI Instrumentator <https://github.com/trallnag/prometheus-fastapi-instrumentator>`_
    Konfigurierbarer und modularer Prometheus-Instrumentator
`starlette_exporter <https://github.com/stephenhillier/starlette_exporter>`_
    Prometheus-Exportprogramm für Starlette und FastAPI
`Starlette Prometheus <https://github.com/perdy/starlette-prometheus>`_
    Prometheus-Integration für Starlette

Templating
~~~~~~~~~~

`fastapi-jinja <https://github.com/AGeekInside/fastapi-jinja>`_
    Integration der Jinja-Template-Sprache
`fastapi-chameleon <https://github.com/mikeckennedy/fastapi-chameleon>`_
    Integration der Template-Sprache Chameleon

Paginierung
~~~~~~~~~~~

`FastAPI Pagination <https://github.com/uriyyo/fastapi-pagination>`_
    Einfach zu verwendende Paginierung für FastAPI mit Integration u.a. in
    sqlalchemy, gino, databases und ormar

Websockets
~~~~~~~~~~

`fastapi-socketio <https://github.com/pyropy/fastapi-socketio>`_
    Einfache Integration von `socket.io in <https://socket.io/>`_ eure
    FastAPI-Anwendung
`FastAPI Websocket Pub/Sub <https://github.com/permitio/fastapi_websocket_pubsub>`_
    Schneller und dauerhafter Pub/Sub-Kanal über Websockets
`FASTAPI Websocket RPC <https://github.com/permitio/fastapi_websocket_rpc>`_
    Schneller und dauerhafter bidirektionaler JSON RPC Kanal über Websockets

Andere Tools
------------

`Pydantic-SQLAlchemy <https://github.com/tiangolo/pydantic-sqlalchemy>`_
    Erzeugen von Pydantic-Modelle aus SQLAlchemy-Modellen
`Fastapi Camelcase <https://github.com/nf1s/fastapi-camelcase>`_
    Bereitstellung einer Klasse von Request- und Response-Bodies für fastapi
`fastapi_profiler <https://github.com/sunhailin-Leo/fastapi_profiler>`_
    FastAPI Middleware basierend auf `pyinstrument
    <https://github.com/joerick/pyinstrument>`_ zur Leistungsüberprüfung
`fastapi-versioning <https://github.com/DeanWay/fastapi-versioning>`_
    Api-Versionierung für Fastapi-Webanwendungen
`Jupter Notebook REST API <https://github.com/Invictify/Jupter-Notebook-REST-API>`_
    Jupyter-Notebooks als REST-API-Endpunkt ausführen
`manage-fastapi <https://github.com/ycd/manage-fastapi>`_
    Projektgenerator und -manager für FastAPI
`msgpack-asgi <https://github.com/florimondmanca/msgpack-asgi>`_
    Automatisches Aushandeln von MessagePack-Inhalten in ASGI-Anwendungen
`fastapi-plugins <https://github.com/madkote/fastapi-plugins>`_
    Produktionsreife Plugins für das FastAPI-Framework, u.a. für das Caching mit
    memcached oder Redis, Scheduler, Konfiguration und Logging
`fastapi-serviceutils <https://github.com/skallfass/fastapi_serviceutils>`_
    Optimiertes Logging, Exception Handling und Konfigurieren
