Docker-Container bauen
======================

Wir verwenden :doc:`ci-cd`, um unsere Python-Docker-Container zu erstellen.

#. Zunächst definieren wir die Python-Version in unserer
   :ref:`pyproject-toml`-Datei des Projekts:

   .. code-block:: toml

      [project]
      name = "my-app"
      requires-python = "==3.12.*"

#. Anschließend extrahieren wir diese Zeichenkette in unserer
   :file:`.gitlab-ci.yml`-Datei und übergeben sie als als Build-Argument an
   ``docker build``

   .. code-block:: yaml

      build:
        stage: build
        only: [main]
        script:
          - export PY=$(sed -nE 's/^requires-python = "==(3\.[0-9]+)\.*"$/python\1/p' pyproject.toml)
          - >
            docker build
            --build-arg PY=$PY

#. Schließlich können wir im im Dockerfile die extrahierte Version verwenden,
   um eine virtuelle Umgebung in der Build-Phase zu erstellen und die
   Python-Version in der ``application``-Stage zu installieren:

   .. code-block:: docker
      :emphasize-lines: 3, 6

      FROM your-docker/build-image as build

      ARG PY
      RUN --mount=type=cache,target=/root/.cache \
          set -ex \
          && virtualenv --python $PY /app
      …
      FROM your-docker/app-image
      …
      RUN set -ex \
          && apt-get update -qy \
          && apt-get install -qy \
              -o APT::Install-Recommends=false \
              -o APT::Install-Suggests=false \
      …
      COPY --from=build --chown=app /app /app
