.. SPDX-FileCopyrightText: 2025 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

npm-Deployment mit rsync
========================

`npm <https://www.npmjs.com>`_ ist ein Paketmanager für die
JavaScript-Laufzeitumgebung `Node.js <https://nodejs.org/en/>`_, und mit `rsync
<https://rsync.samba.org>`_ können die Daten mit dem entfernten Server
synchronisiert werden.

Erste Schritte
--------------

#. Umgebungsvariablen einrichten

   ``DEPLOY_DIR``
       Verzeichnis auf dem entfernten Server, in das verteilt werden soll.
   ``DEPLOY_HOST``
       Hostname oder IP-Adresse des Servers, auf den verteilt werden soll.
   ``DEPLOY_KEY_FILE``
       Pfad zu einem privaten SSH-Schlüssel, der zur Authentifizierung gegenüber
       dem Server verwendet werden soll.
   ``DEPLOY_USER``
       Name des SSH-Accounts.
   ``KNOWN_HOSTS_FILE``
       Pfad zu einer Datei mit vordefinierten :file:`known_hosts`-Einträgen, mit
       denen die Verbindung überprüft werden soll.

#. Einrichten der CI/CD-Pipeline

   .. code-block:: yaml
      :caption: .gitlab-ci.yml
      :emphasize-lines: 13, 14, 15

      stages:
        - deploy

      deploy-static-assets:
        stage: deploy
        rules:
          - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
        environment:
          name: prod
          deployment_tier: production
        image: node:alpine
        script:
          - apk add --no-cache git nodejs npm openssh-client-default rsync
          - chmod 0600 "$DEPLOY_KEY_FILE"
          - ./deploy.sh

   Zeile 13
       installiert die für das Bauen und Hochladen erforderlichen Pakete
   Zeile 14
       ändert die Zugriffsberechtigungen für den ssh-Schlüssel
   Zeile 15
       ruft die :file:`deploy.sh`-Datei auf

#. Verschieben der statischen Dateien auf den Server

   .. code-block:: sh
      :caption: deploy.sh
      :linenos:
      :emphasize-lines: 7-13, 18, 19, 24, 25-31

      #!/bin/sh
      set -e

      # Deploy static assets to a server via rsync.

      # Create SSH config.
      cat >deploy.ssh_config <<-END
          Host deploy
              HostName $DEPLOY_HOST
              User $DEPLOY_USER
              IdentityFile $DEPLOY_KEY_FILE
              UserKnownHostsFile $KNOWN_HOSTS_FILE
      END


      # Build the JavaScript application & related files.
      cd vite-app
      npm ci
      npx vite build

      # Deploy the application and GeoJSON data.
      rsync \
          -rtlv \
          --rsh 'ssh -F ../deploy.ssh_config' \
          --rsync-path "mkdir -p \"$DEPLOY_DIR\" && rsync" \
          ../data/cusy.geojson \
          cusy.html \
          dist/cusy-map.css \
          dist/cusy-map.js \
          dist/cusy-map.js.map \
          "deploy:$DEPLOY_DIR"

   Zeile 7–13
       erstellt die ssh-Konfigurationsdatei

   Zeile 18
       installiert die Abhängigkeiten des Projekts aus der
       :file:`vite-app/package.json`-Datei

       .. seealso::
          `npm-ci <https://docs.npmjs.com/cli/v9/commands/npm-ci>`_

   Zeile 19
       erstellt das `vite <https://vite.dev>`_-Projekt für die Produktion.

   Zeile 24
       verschiebt die ssh-Konfiguration auf den Server

   Zeile 25–31
       verschiebt die Anwendung und GeoJSON-Daten auf den Server
