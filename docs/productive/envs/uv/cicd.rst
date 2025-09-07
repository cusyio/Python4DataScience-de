CI/CD-Pipelines
===============

.. _uv-gitlab:

GitLab CI/CD
------------

Für :doc:`/productive/git/advanced/gitlab/ci-cd/index`-Pipelines gibt es
verschiedene Docker-Images mit vorinstalliertem ``uv``: `Available images
<https://docs.astral.sh/uv/guides/integration/docker/#available-images>`_.

.. code-block:: yaml
   :caption: .gitlab-ci.yml
   :linenos:

   variables:
     UV_VERSION: 0.4
     PYTHON_VERSION: 3.12
     BASE_LAYER: bookworm-slim


   stages:
     - build

   uv-install:
     stage: build
     image: ghcr.io/astral-sh/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
     variables:
       UV_CACHE_DIR: .uv-cache
     cache:
       - key:
           files:
             - uv.lock
         paths:
           - $UV_CACHE_DIR
     script:
       # YOUR UV COMMANDS
       - uv cache prune --ci

Zeile 23
    Dies reduziert die Cache-Größe, :abbr:`s.a. (siehe auch)` `Caching in
    continuous integration
    <https://docs.astral.sh/uv/concepts/cache/#caching-in-continuous-integration>`_.

.. seealso::
   * `Using uv in GitLab CI/CD
     <https://docs.astral.sh/uv/guides/integration/gitlab/>`_

GitHub Actions
--------------

Die offizielle `astral-sh/setup-uv
<https://github.com/astral-sh/setup-uv>`_-GitHub Action installiert uv, fügt es
PATH hinzu und stellt einen Cache für die installierten Pakete bereit:

.. code-block:: yaml
   :caption: ci.yml

   name: ci

   jobs:
     test:
       name: python
       runs-on: ubuntu-latest

       steps:
         - uses: actions/checkout@v4

         - name: Install uv
           uses: astral-sh/setup-uv@v3
           with:
             version: "0.4.24"

Anschließend könnt ihr entweder eine einzelne Python-Version oder eine Matrix
mit uv installieren:

.. code-block:: yaml
   :caption: ci.yml

        - name: Set up Python
          uses: actions/setup-python@v5
          with:
            python-version-file: "pyproject.toml"

oder

.. code-block:: yaml
   :caption: ci.yml

        - name: Set up Python
          uses: actions/setup-python@v5
          with:
            python-version-file: ".python-version"

oder

.. code-block:: yaml
   :caption: ci.yml

   name: ci

   strategy:
     matrix:
       python-version:
         - "3.9"
         - "3.10"
         - "3.11"
         - "3.12"
         - "3.13"

   jobs:
     test:
       name: python
       # ...
         - name: Set up Python ${{ matrix.python-version }}
           run: uv python install ${{ matrix.python-version }}

.. seealso::
   * `Using uv in GitHub Actions
     <https://docs.astral.sh/uv/guides/integration/github/>`_

``uv sync`` und ``uv run``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sobald uv und Python installiert sind, kann das Projekt mit ``uv sync``
installiert werden und Befehle können in der Umgebung mit ``uv run`` ausgeführt
werden, :abbr:`z.B. (zum Beispiel)` für :doc:`python-basics:test/pytest/index`:

.. code-block:: yaml
   :caption: ci.yml

         - name: Install the project
           run: uv sync --all-extras --dev

         - name: Run tests
           run: uv run pytest tests

Caching
~~~~~~~

Der Cache von uv verbessert die Laufzeiten:

.. code-block:: yaml
   :caption: ci.yml

         - name: Enable caching
           uses: astral-sh/setup-uv@v3
           with:
             enable-cache: true

Macht den Cache ungültig, wenn sich :file:`uv.lock` ändert:

.. code-block:: yaml
   :caption: ci.yml

         - name: Define a cache dependency glob
           uses: astral-sh/setup-uv@v3
           with:
             enable-cache: true
             cache-dependency-glob: "uv.lock"
