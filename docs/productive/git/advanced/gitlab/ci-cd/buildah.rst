.. SPDX-FileCopyrightText: 2022–2025 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Multi-Arch-Images mit Buildah
=============================

`Buildah <https://buildah.io>`_ erlaubt euch, Container-Images zu erstellen ohne
dass ihr eine vollständige Container-Runtime benötigt. Buildah ist ein
Open-Source-Tool auf Linux-Basis, das `Docker <https://www.docker.com>`_- und
`Kubernetes <https://kubernetes.io>`_-kompatible Images erstellen kann. Zudem kann Buildah nicht nur funktionierende Container von Grund auf neu erstellen,
sondern auch aus einer bereits vorhandenen Dockerdatei. Schließlich lässt es
sich leicht in Skripte und Build-Pipelines einbinden.

Erste Schritte
--------------

#. Umgebungsvariablen einrichten

   ``DEPLOY_USER``
       Name des Accounts.
   ``DEPLOY_KEY_FILE``
       Pfad zu einem privaten SSH-Schlüssel, der zur Authentifizierung gegenüber
       dem Server verwendet werden soll.
   ``DEPLOY_HOST``
       Hostname oder IP-Adresse des Servers, auf den verteilt werden soll.

#. Einrichten der CI/CD-Pipeline

   .. code-block:: yaml
      :caption: .gitlab-ci.yml
      :linenos:

      stages:
        - build
        - deploy

      build_docker:
        stage: build
        variables:
          DOCKER_STEM: $CI_REGISTRY_IMAGE
        image: quay.io/buildah/stable:v1.27
        script:
          - apk add --no-cache openssh
          - chmod 0600 "$DEPLOY_KEY_FILE"
          - ./build.sh

      deploy_app:
        stage: deploy
        image: alpine
        environment:
          name: app
          deployment_tier: staging
        when: manual
        script:
          - apk add --no-cache openssh
          - chmod 0600 "$DEPLOY_KEY"
          - ./deploy.sh

#. Bauen des Docker-Containers

   .. code-block:: sh
      :caption: build.sh
      :linenos:
      :emphasize-lines: 2, 5, 8

      # Registry login
      echo "$CI_REGISTRY_PASSWORD" | buildah login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"

      # Set docker tag
      if [ "$CI_COMMIT_BRANCH" == main ]; then export DOCKER_TAG="latest"; else export DOCKER_TAG="${CI_COMMIT_TAG:-$CI_COMMIT_REF_SLUG}"; fi; export DOCKER_TAG_FULL="$DOCKER_STEM:$DOCKER_TAG"; echo "DOCKER_TAG_FULL=$DOCKER_TAG_FULL"

      # Build and push
      buildah build --isolation chroot --storage-driver vfs --jobs 2 --platform linux/amd64,linux/arm/v7 --manifest "$DOCKER_TAG_FULL" && buildah --storage-driver vfs images && buildah manifest push --storage-driver vfs --format v2s2 --all "$DOCKER_TAG_FULL" "docker://$DOCKER_TAG_FULL"

   Zeile 2
       meldet sich bei der :doc:`../package-registry` an.
   Zeile 5
       kennzeichnet die Images anhand ihrer Branch- oder Tag-Namen mit Ausnahme
       von ``main``, der mit ``latest`` gekennzeichnet wird.
   Zeile 8
       baut die Images und stellt sie mit dem `VFS
       <https://docs.docker.com/engine/storage/drivers/vfs-driver/>`_-Treiber
       bereit.

#. Bereitstellen

   .. code-block:: sh
      :caption: deploy.sh
      :linenos:

      # Set docker tag
      if [ "$CI_COMMIT_BRANCH" == main ]; then export DOCKER_TAG="latest"; else export DOCKER_TAG="${CI_COMMIT_TAG:-$CI_COMMIT_REF_SLUG}"; fi; export DOCKER_TAG_FULL="$DOCKER_STEM:$DOCKER_TAG"; echo "DOCKER_TAG_FULL=$DOCKER_TAG_FULL"

      echo "$CI_REGISTRY $DEPLOY_USER $DEPLOY_PASSWORD MYAPP $DOCKER_TAG" | ssh -o 'BatchMode yes' -o 'StrictHostKeyChecking accept-new' -i "$DEPLOY_KEY" root@$DEPLOY_HOST
