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
     UV_VERSION: 0.11
     PYTHON_VERSION: 3.14
     BASE_LAYER: trixie-slim
     # GitLab CI creates a separate mountpoint for the build directory,
     # so we need to copy instead of using hard links.
     UV_LINK_MODE: copy

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

Zeile 25
    Dies reduziert die Cache-Größe, :abbr:`s.a. (siehe auch)` `Caching in
    continuous integration
    <https://docs.astral.sh/uv/concepts/cache/#caching-in-continuous-integration>`_.

.. seealso::
   * `Using uv in GitLab CI/CD
     <https://docs.astral.sh/uv/guides/integration/gitlab/>`_

.. _github-actions:

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
       - uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
         with:
           persist-credentials: false

       - name: Setup cached uv
         uses: hynek/setup-cached-uv@4300ec2180bc77d705e626a34e381b81a4772c51 # v2.5.0

Anschließend könnt ihr entweder eine einzelne Python-Version oder eine Matrix
mit uv installieren:

.. code-block:: yaml
   :caption: ci.yml

   - uses: actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1 # v6.3.0
     with:
       python-version-file: .python-version

oder

.. code-block:: yaml
   :caption: ci.yml

   name: ci

   strategy:
     matrix:
       python-version:
         - "3.10"
         - "3.11"
         - "3.12"
         - "3.13"
         - "3.14"

   steps:
     - uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
     - name: Install uv and set the Python version
       uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
       with:
         python-version: ${{ matrix.python-version }}

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
     run: uv sync --group tests

   - name: Run tests
     run: uv run pytest

Caching
~~~~~~~

Der Cache von uv verbessert die Laufzeiten:

.. code-block:: yaml
   :caption: ci.yml

   - name: Enable caching
     uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
     with:
       enable-cache: true

Macht den Cache ungültig, wenn sich :file:`uv.lock` ändert:

.. code-block:: yaml
   :caption: ci.yml

   - name: Define a cache dependency glob
     uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0

     with:
       enable-cache: true
       cache-dependency-glob: "uv.lock"
