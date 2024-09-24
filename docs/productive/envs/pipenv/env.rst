.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Umgebungsvariablen
==================

``pipenv``-Umgebungsvariablen
-----------------------------

``pipenv --envs`` gibt Optionen der Environment-Variablen aus.

Weitere Informationen hierzu findet ihr unter
`Configuration With Environment Variables
<https://docs.pipenv.org/advanced/#configuration-with-environment-variables>`_.

:file:`.env`-Datei
------------------

Wenn eine :file:`.env`-Datei in eurer virtuellen Umgebung vorhanden ist, werden
``$ pipenv shell`` und ``$ pipenv run`` diese automatisch laden:

.. code-block:: console

    $ cat .env
    USERNAME=veit

    $ pipenv run python
    Loading .env environment variables...
    …

.. code-block:: pycon

    >>> import os
    >>> os.environ["USERNAME"]
    'veit'

Auch die Credentials, :abbr:`z.B. (zum Beispiel)` der Versionsverwaltung lassen
sich in der :file:`Pipfile`-Datei angeben, :abbr:`z.B. (zum Beispiel)`:

.. code-block:: ini

    [[source]]
    url = "https://$USERNAME:${PASSWORD}@ce.cusy.io/api/v4/projects/$PROJECT_ID/packages/pypi/simple"
    verify_ssl = true
    name = "gitlab"

.. note::
   ``pipenv`` hasht die :file:`Pipfile`-Datei, bevor die Umgebungsvariablen
   ermittelt werden, und auch die Umgebungsvariablen aus der
   :file:`Pipfile.lock`-Datei werden ersetzt, sodass keine Credentials in der
   Versionsverwaltung gespeichert werden müssen.

Ihr könnt die :file:`.env`-Datei auch außerhalb eures Virtual Environments
speichern. Ihr müsst dann nur den Pfad zu dieser Datei angeben in
``PIPENV_DOTENV_LOCATION``:

.. code-block:: console

    $ PIPENV_DOTENV_LOCATION=/path/to/.env pipenv shell

Ihr könnt auch verhindern, dass ``pipenv`` eine vorhandene :file:`.env`-Datei
verwenet mit:

.. code-block:: console

    $ PIPENV_DONT_LOAD_ENV=1 pipenv shell
