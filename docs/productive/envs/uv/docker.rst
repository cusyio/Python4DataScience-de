Python Docker Container mit ``uv``
==================================

Wir unterteilen unseren Docker-Workflow in unterschiedliche Layer. Dies erlaubt
uns schneller neue Builds bereitzustellen. Dabei beginnen wir mit den Layern,
die sich am wenigsten ändern, damit wir die Artefakte so lange wie möglich
zwischenspeichern können. Dies ist auch der Grund, weswegen wir die
Installationen der Abhängigkeiten aus :file:`uv.lock` und Installation unserer
:doc:`Anwendung <python-basics:packs/apps>` strikt getrennthalten –
wahrscheinlich ändert sich unser Code schneller als der der Abhängigkeiten.

.. seealso::
   * `Order your layers
     <https://docs.docker.com/build/cache/optimize/#order-your-layers>`_

#. Zunächst bauen wir einen initialen Build-Container, der verhindert, dass wir
   unsere Build-Tools ausliefern müssen.

   .. seealso::
      * `Multi-stage builds
        <https://docs.docker.com/build/building/multi-stage/>`_

   .. code-block:: docker
      :linenos:
      :emphasize-lines: 4

      # syntax=docker/dockerfile:1.9
      FROM ubuntu:noble AS build

      SHELL ["sh", "-exc"]

      RUN <<EOT
      apt update -qy
      apt install -qyy \
          -o APT::Install-Recommends=false \
          -o APT::Install-Suggests=false \
          build-essential \
          ca-certificates \
          python3-setuptools \
          python3.12-dev
      EOT

   Zeile 4:
       Falls ihr `Podman <https://podman.io>`_ verwendet, solltet ihr den
       Docker-Kompatibilitätsmodus verwenden.
   Zeile 6:
       :abbr:`Ggf. (Gegebenenfalls)` könnt ihr jedem ``RUN``-Skript auch
       ``set -ex`` voranstellen, wodurch die Fehlersuche einfacher wird.

       .. seealso::
          * https://github.com/containers/podman/issues/8477

#. Anschließend bauen wir eine :ref:`virtuelle Python-Umgebung <venv>` mit
   unserer Anwendung im Verzeichnis :file:`/app` und kopieren diese dann in
   unseren Runtime-Container. Das hat :abbr:`u.a. (unter anderem)` den Vorteil,
   dass derselbe Basiscontainer für verschiedene Python-Versionen und
   :ref:`virtuelle Umgebungen <venv>` verwendet werden kann. Mit
   :doc:`/productive/envs/uv/index` 0.4.4 ist dies sehr viel einfacher geworden
   dank der Umgebungsvariable ``UV_PROJECT_ENVIRONMENT``:

   .. code-block:: docker
      :linenos:
      :emphasize-lines: 1, 3, 4, 6, 7

      COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

      ENV UV_LINK_MODE=copy \
          UV_COMPILE_BYTECODE=1 \
          UV_PYTHON_DOWNLOADS=never \
          UV_PYTHON=python3.12 \
          UV_PROJECT_ENVIRONMENT=/app

   Zeile 1:
       Sicherheitsbewußte Organisationen sollten ``uv`` selbst überprüfen und
       packen.
   Zeile 3:
       Dies verhindert, dass :doc:`/productive/envs/uv/index` sich beschwert,
       keine Hardlinks verwenden zu können.
   Zeile 4:
       Die Python-Pakete werden Byte-kompiliert, damit die Startzeiten des
       Containers verkürzt werden.

   Zeile 6:
       Python-Version auswählen.
   Zeile 7:
       :file:`/app` als Ziel für ``uv sync`` deklarieren.

#. Nun erstellen wir das ``app``-Dockerfile:

   .. code-block:: docker
      :linenos:
      :emphasize-lines: 1-2, 6-9, 14

      COPY pyproject.toml /_lock/
      COPY uv.lock /_lock/

      RUN --mount=type=cache,target=/root/.cache <<EOT
      cd /_lock
      uv sync \
          --locked \
          --no-dev \
          --no-install-project
      EOT

      COPY . /src
      RUN --mount=type=cache,target=/root/.cache \
          cd /src && uv sync --locked --no-dev --no-editable

   Zeilen 1–2:
       Die :file:`lock`-Dateien werden in ein Verzeichnis verschoben, das
       **nicht** im Runtime-Container liegt. Der Schrägstrich am Ende sorgt
       dafür, dass ``COPY`` automatisch `/_lock/` erstellt.

   Zeile 4:
       Der Build-Cache-Mount verhindert :abbr:`z.B. (zum Beispiel)`, dass alle
       :term:`Wheels <Wheel>` neu gebaut werden müssen, wenn der Layer mit euren
       Abhängigkeiten neu gebaut werden muss.

       .. seealso::
          * `Use cache mounts
            <https://docs.docker.com/build/cache/optimize/#use-cache-mounts>`_

   Zeilen 6–9:
       Die Abhängigkeiten werden ohne die Anwendung selbst synchronisiert.
       Dieser Layer wird zwischengespeichert, bis sich die :ref:`uv_lock` oder
       :file:`pyproject.toml` ändern.
   Zeile 14:
       ``myapp`` wird aus :file:`/src` ohne jegliche Abhängigkeiten installiert.

#. Schließlich erstellen wir den Runtime-Container:

   .. code-block:: docker
      :linenos:
      :emphasize-lines: 4, 6-9, 13, 20-21, 29-30, 32, 37-41

      FROM python:3.12-slim
      SHELL ["sh", "-exc"]

      ENV PATH=/app/bin:$PATH

      RUN <<EOT
      groupadd -r app
      useradd -r -d /app -g app -N app
      EOT

      ENTRYPOINT ["/docker-entrypoint.sh"]

      STOPSIGNAL SIGINT

      RUN <<EOT
      apt update -qy
      apt install -qyy \
          -o APT::Install-Recommends=false \
          -o APT::Install-Suggests=false \
          python3.12 \
          libpython3.12 \
          libpcre3 \
          libxml2

      apt clean
      rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
      EOT

      COPY docker-entrypoint.sh /
      COPY . /app/

      COPY --from=build --chown=app:app /app /app

      USER app
      WORKDIR /app

      RUN <<EOT
      python -V
      python -Im site
      python -Ic 'import myapp'
      EOT

   Zeile 4:
       Optional: Fügt die :ref:`virtuelle Umgebung <venv>` zum Suchpfad hinzu.

   Zeilen 6–9:
       Führt die Anwendung als Service-User ``app`` aus.

   Zeile 13:
       Im Python Ökosystem ist es nicht unbedingt üblich, dass eure Anwendung
       auf ein ``SIGTERM`` reagiert. ``STOPSIGNAL SIGINT`` ist eine einfache
       Möglichkeit, dies zu umgehen.

       .. seealso::
          * `Why Your Dockerized Application Isn’t Receiving Signals
            <https://hynek.me/articles/docker-signals>`_

   Zeilen 20–21:
       Beachtet, dass sich die Abhängigkeiten zur Laufzeit von den
       Abhängigkeiten zur Build-Zeit unterscheiden. Zudem gibt es auch kein
       ``uv``.

   Zeilen 29–30:
       Wenn eure Anwendung kein :doc:`Python-Paket
       <python-basics:packs/distribution>` ist, das mit ``uv sync`` installiert
       wurde, müsst ihr eure Anwendung hier in den Container kopieren.

   Zeile 32:
       Dies kopiert das vorgefertigte Verzeichnis :file:`/app` in den
       Runtime-Container und ändert die Berechtigungen auf den Service-User
       ``app`` und die Gruppe ``app`` in einem Schritt.

   Zeilen 37–41:
       Optional: Üblicherweise nutze ich diese Introspektion für einen
       Smoke-Test, der sicherstellt, dass die Anwendung auch tatsächlich
       importiert werden kann.
