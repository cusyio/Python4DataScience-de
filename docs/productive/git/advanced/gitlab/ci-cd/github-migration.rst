.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Migration von GitHub-Aktionen
=============================

GitLab CI/CD und GitHub Actions weisen einige Ähnlichkeiten in der Konfiguration
auf, wodurch die Migration zu GitLab CI/CD relativ einfach ist:

* Workflow-Konfigurationsdateien sind in
  :doc:`/data-processing/serialisation-formats/yaml/index` geschrieben und
  werden im Repository zusammen mit dem Code gespeichert.
* Workflows enthalten einen oder mehrere Jobs.
* Jobs umfassen einen oder mehrere Schritte oder einzelne Befehle.
* Jobs können entweder auf verwalteten oder selbst gehosteten Rechnern laufen.

Es gibt jedoch auch einige Unterschiede, und dieser Leitfaden wird euch die
wichtigsten Unterschiede aufzeigen, damit ihr euren Workflow auf GitLab CI/CD
migrieren könnt.

Jobs
----

Jobs in GitHub Actions sind den Jobs in GitLab CI/CD sehr ähnlich. Beide haben
folgende Merkmale:

* Jobs enthalten eine Reihe von Schritten oder Skripten, die nacheinander
  ausgeführt werden.
* Jobs können auf separaten Rechnern oder in separaten Containern ausgeführt
  werden.
* Jobs werden standardmäßig parallel ausgeführt, können aber auch für
  sequentielle Ausführung konfiguriert werden.
* Jobs können ein Skript oder einen Shell-Befehl ausführen, wobei in
  GitHub-Aktionen alle Skripte mit dem Schlüssel ``run`` angegeben werden. In
  GitLab CI/CD werden die Skript-Schritte hingegen mit dem ``script``-Schlüssel
  angegeben.

Im Folgenden findet ihr ein Beispiel für die Syntax der beiden Systeme.

GitHub Actions-Syntax für Jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 5

   jobs:
     my_job:
       steps:
         - uses: actions/checkout@v4
         - run: echo "Run my script here"

GitLab CI/CD-Syntax für Jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 4-5

   my_job:
     variables:
       GIT_CHECKOUT: "true"
     script:
       - echo "Run my script here"

Runners
-------

Runner sind Maschinen, auf denen die Jobs ausgeführt werden. Sowohl GitHub
Actions als auch GitLab CI/CD bieten verwaltete und selbst gehostete Varianten
von Runners. In GitHub Actions wird der ``runs-on``-Schlüssel verwendet, um Jobs
auf verschiedenen Plattformen auszuführen, während dies in GitLab CI/CD mit
``tags`` erfolgt.

GitHub Actions-Syntax für Runner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 2

   my_job:
     runs-on: ubuntu-latest
     steps:
       - run: echo "Hello Pythonistas!"

GitLab CI/CD-Syntax für Runner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 3

   my_job:
     tags:
       - linux
     script:
       - echo "Hello Pythonistas!"

Docker-Images
-------------

GitHub Actions-Syntax für Docker-Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 3

    jobs:
      my_job:
        container: python:3.10

GitLab CI/CD-Syntax für Docker-Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 2

    my_job:
      image: python:3.10

.. seealso::
   * `Run your CI/CD jobs in Docker containers
     <https://docs.gitlab.com/ee/ci/docker/using_docker_images.html>`_

Syntax für Bedingungen und Ausdrücke
------------------------------------

GitHub Actions verwendet das ``if``-Schlüsselwort, um zu verhindern, dass ein
Job ausgeführt wird, wenn eine Bedingung nicht erfüllt ist. GitLab CI/CD
verwendet ``rules``, um zu bestimmen, ob ein Job unter einer bestimmten
Bedingung ausgeführt wird.

Im Folgenden findet ihr ein Beispiel für die Syntax der beiden Systeme.

GitHub-Syntax für Bedingungen und Ausdrücke
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 3

   jobs:
     deploy:
       if: contains( github.ref, 'main')
       runs-on: ubuntu-latest
       steps:
         - run: echo "Deploy to production server"

GitLab-Syntax für Bedingungen und Ausdrücke
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml
   :emphasize-lines: 5-6

   deploy:
     stage: deploy
     script:
       - echo "Deploy to production server"
     rules:
       - if: '$CI_COMMIT_BRANCH == "main"'

Neben ``if`` bietet GitLab auch noch weitere Regeln wie ``changes``, ``exists``,
``allow_failure``, ``variables`` und ``when``.

.. seealso::
   * `rules <https://docs.gitlab.com/ee/ci/yaml/#rules>`_
   * `Specify when jobs run with rules
     <https://docs.gitlab.com/ee/ci/jobs/job_rules.html>`_

Abhängigkeiten zwischen Jobs
----------------------------

Sowohl GitHub Actions als auch GitLab CI/CD ermöglichen euch, Abhängigkeiten für
einen Job festzulegen. In beiden Systemen werden Jobs standardmäßig parallel
ausgeführt, aber GitLab CI/CD verfügt über ein ``stages``-Konzept, bei dem Jobs
einer Stufe gleichzeitig ausgeführt werden, die nächste Stufe aber erst dann
beginnt, wenn alle Aufträge der vorherigen Stufe abgeschlossen sind. In GitHub
Actions können Abhängigkeiten zwischen Jobs explizit mit dem ``needs``-Schlüssel
nachgebildet werden.

Nachfolgend findet ihr ein Beispiel für die Syntax für jedes System. Die
Workflows beginnen mit zwei parallel laufenden Jobs mit den Namen ``unit-test``
und ``lint``. Wenn diese Jobs abgeschlossen sind, wird ein weiterer Job mit dem
Namen ``deploy-to-stage`` ausgeführt. Wenn ``deploy-to-stage`` abgeschlossen
ist, wird schließlich der Auftrag ``deploy-to-prod`` ausgeführt.

GitHub Actions-Syntax für Abhängigkeiten zwischen Jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   jobs:
     unit-test:
       runs-on: ubuntu-latest
       steps:
         - run: echo "Running unit tests... This will take about 60 seconds."
         - run: sleep 60
         - run: echo "Code coverage is 0%"

     lint:
       runs-on: ubuntu-latest
       steps:
         - run: echo "Linting code... This will take about 10 seconds."
         - run: sleep 10
         - run: echo "No lint issues found."

     deploy-to-stage:
       runs-on: ubuntu-latest
       needs: [unit-test,lint]
       steps:
         - run: echo "Deploying application in staging environment..."
         - run: echo "Application successfully deployed to staging."

     deploy-to-prod:
       runs-on: ubuntu-latest
       needs: [deploy-to-stage]
       steps:
         - run: echo "Deploying application in production environment..."
         - run: echo "Application successfully deployed to production."

GitLab CI/CD-Syntax für Abhängigkeiten zwischen Jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    stages:
      - test
      - stage
      - prod

    unit-test:
      stage: test
      script:
        - echo "Running unit tests... This will take about 60 seconds."
        - sleep 60
        - echo "Code coverage is 0%"

    lint:
      stage: test
      script:
        - echo "Linting code... This will take about 10 seconds."
        - sleep 10
        - echo "No lint issues found."

    deploy-to-stage:
      stage: stage
      script:
        - echo "Deploying application in staging environment..."
        - echo "Application successfully deployed to staging."

    deploy-to-prod:
      stage: prod
      script:
        - echo "Deploying application in production environment..."
        - echo "Application successfully deployed to production."

Artefakte
---------

Sowohl GitHub Actions als auch GitLab CI/CD können Dateien und Verzeichnisse,
die von einem Job erstellt wurden, als Artefakte hochladen. Diese Artefakte
können verwendet werden, um Daten über mehrere Jobs hinweg zu erhalten.

Im Folgenden findet ihr ein Beispiel für die Syntax der beiden Systeme.

GitHub Actions Syntax für Artefakte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   - name: Archive code coverage results
     uses: actions/upload-artifact@v3
     with:
       name: code-coverage-report
       path: output/test/code-coverage.html

GitLab CI/CD-Syntax für Artefakte
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   script:
   artifacts:
     paths:
       - output/test/code-coverage.html

Datenbanken und Service-Container
---------------------------------

Beide Systeme ermöglichen euch, zusätzliche Container für Datenbanken, Caching
oder andere Abhängigkeiten einzubinden.

GitHub Actions verwendet den ``container``-Schlüssel, während in GitLab CI/CD
ein Container für den Job mit dem ``image``-Schlüssel angegeben wird. In beiden
Systemen werden zusätzliche Service-Container mit dem ``services``-Schlüssel
angegeben.

Im Folgenden findet ihr ein Beispiel für die Syntax der beiden Systeme.

GitHub Actions-Syntax für Datenbanken und Service-Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    jobs:
      test:
        runs-on: ubuntu-latest

        services:
          postgres:
            image: postgres
            env:
              POSTGRES_USER: postgres
              POSTGRES_PASSWORD: postgres
              POSTGRES_DB: postgres
            options: >-
              --health-cmd pg_isready
              --health-interval 10s
              --health-timeout 5s
              --health-retries 5

        steps:
          - name: Python
            uses: actions/checkout@v4
            uses: actions/setup-python@v5
            with:
              python-version: '3.10'

          - name: Test with pytest
            run: python -m pytest
            env:
              DATABASE_URL: 'postgres://postgres:postgres@localhost:${{ job.services.postgres.ports[5432] }}/postgres'

GitLab CI/CD-Syntax für Datenbank- und -Service-Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   test:
     variables:
       POSTGRES_PASSWORD: postgres
       POSTGRES_HOST: postgres
       POSTGRES_PORT: 5432
     image: python:latest
     services:
       - postgres
     script:
       - python -m pytest

Zuordnungen
-----------


+-----------------------------------------------+-----------------------------------------------+
| GitHub                                        | GitLab                                        |
+===============================================+===============================================+
| **Konzepte**                                                                                  |
+-----------------------------------------------+-----------------------------------------------+
| ``actions/upload-artifact@v2``                | ``artifacts``                                 |
+-----------------------------------------------+-----------------------------------------------+
| ``actions/cache@v4``                          | ``cache``                                     |
+-----------------------------------------------+-----------------------------------------------+
| ``actions/download-artifact@v2``              | ``dependencies``                              |
+-----------------------------------------------+-----------------------------------------------+
| ``environment``                               | ``environment``                               |
+-----------------------------------------------+-----------------------------------------------+
| ``container``                                 | ``image``                                     |
+-----------------------------------------------+-----------------------------------------------+
| ``actions/deploy-pages@main``                 | ``pages``                                     |
+-----------------------------------------------+-----------------------------------------------+
| ``actions/create-release@v1``                 | ``release``                                   |
+-----------------------------------------------+-----------------------------------------------+
| ``run``                                       | ``script``, ``after_script``,                 |
|                                               | ``before_script``, ``trigger``                |
+-----------------------------------------------+-----------------------------------------------+
| ``hashicorp/vault-action@v2.5.0``             | ``secrets``                                   |
+-----------------------------------------------+-----------------------------------------------+
| ``services``                                  | ``services``                                  |
+-----------------------------------------------+-----------------------------------------------+
| ``runs-on``                                   | ``tags``                                      |
+-----------------------------------------------+-----------------------------------------------+
| ``timeout-minutes``                           | ``timeout``                                   |
+-----------------------------------------------+-----------------------------------------------+
| **Umgebungsvariablen**                                                                        |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.api_url }}``                     | ``CI_API_V4_URL``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.workspace }}``                   | ``CI_BUILDS_DIR``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.ref }}``                         | ``CI_COMMIT_BRANCH``,                         |
|                                               | ``CI_COMMIT_REF_NAME``,                       |
|                                               | ``CI_COMMIT_REF_SLUG``,                       |
|                                               | ``CI_COMMIT_TAG``,                            |
|                                               | ``CI_MERGE_REQUEST_REF_PATH``                 |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.sha }}``                         | ``CI_COMMIT_SHA``,                            |
|                                               | ``CI_COMMIT_SHORT_SHA``                       |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.job }}``                         | ``CI_JOB_ID``,                                |
|                                               | ``CI_JOB_NAME``                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.event_name ==                    | ``CI_JOB_MANUAL``                             |
| 'workflow_dispatch' }}``                      |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ job.status }}``                         | ``CI_JOB_STATUS``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.server_url }}/${{                | ``CI_MERGE_REQUEST_PROJECT_URL``              |
| github.repository }}``                        |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.token }}``                       | ``CI_NODE_INDEX``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ strategy.job-total }}``                 | ``CI_NODE_TOTAL``                             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.repository}}/${{                 | ``CI_PIPELINE_ID``                            |
| github.workflow }}``                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.workflow }}``                    | ``CI_PIPELINE_IID``                           |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.event_name }}``                  | ``CI_PIPELINE_SOURCE``                        |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.actions }}``                     | ``CI_PIPELINE_TRIGGERED``                     |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.server_url }}/${{                | ``CI_PIPELINE_URL``                           |
| github.repository }}/actions/runs/${{         |                                               |
| github.run_id }}``                            |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.workspace }}``                   | ``CI_PROJECT_DIR``                            |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.repository }}``                  | ``CI_PROJECT_ID``                             |
|                                               | ``CI_PROJECT_PATH_SLUG``,                     |
|                                               | ``CI_PROJECT_PATH``,                          |
|                                               | ``CI_MERGE_REQUEST_PROJECT_ID``,              |
|                                               | ``CI_MERGE_REQUEST_PROJECT_PATH``             |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.event.repository.name            | ``CI_PROJECT_NAME``                           |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.repository_owner }}``            | ``CI_PROJECT_NAMESPACE``                      |
|                                               | ``CI_PROJECT_ROOT_NAMESPACE``                 |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_PROJECT_TITLE``                          |
| github.event.repository.full_name }}``        |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.server_url }}/${{                | ``CI_PROJECT_URL``                            |
| github.repository }}``                        |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_REPOSITORY_URL``                         |
| github.event.repository.clone_url }}``        |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ runner.os }}``                          | ``CI_RUNNER_EXECUTABLE_ARCH``                 |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.server_url }}``                  | ``CI_SERVER_HOST``, ``CI_SERVER_URL``         |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.actions }}``                     | ``CI_SERVER``, ``GITLAB_CI``                  |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.actor }}``                       | ``GITLAB_USER_EMAIL``,                        |
|                                               | ``GITLAB_USER_ID``,                           |
|                                               | ``GITLAB_USER_LOGIN``,                        |
|                                               | ``GITLAB_USER_NAME``                          |
+-----------------------------------------------+-----------------------------------------------+
| ``${{ github.event_path }}``                  | ``TRIGGER_PAYLOAD``                           |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_ASSIGNEES``                |
| github.event.pull_request.assignees           |                                               |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_ID``,                      |
| github.event.pull_request.number }}``         | ``CI_MERGE_REQUEST_IID``                      |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_LABELS``                   |
| github.event.pull_request.labels }}``         |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_MILESTONE``                |
| github.event.pull_request.milestone           |                                               |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         |``CI_MERGE_REQUEST_SOURCE_BRANCH_NAME``,       |
| github.event.pull_request.head.ref }}``       |``CI_EXTERNAL_PULL_REQUEST_SOURCE_BRANCH_NAME``|
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_SOURCE_BRANCH_SHA``,       |
| github.event.pull_request.head.sha }}``       | ``CI_EXTERNAL_PULL_REQUEST_SOURCE_BRANCH_SHA``|
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_SOURCE_BRANCH_SHA``,       |
| github.event.pull_request.head.repo.full_name | ``CI_MERGE_REQUEST_SOURCE_PROJECT_PATH``      |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_SOURCE_PROJECT_URL``       |
| github.event.pull_request.head.repo.url }}``  |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         |``CI_MERGE_REQUEST_TARGET_BRANCH_NAME``,       |
| github.event.pull_request.base.ref }}``       |``CI_EXTERNAL_PULL_REQUEST_TARGET_BRANCH_NAME``|
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_TARGET_BRANCH_SHA``,       |
| github.event.pull_request.base.sha }}``       | ``CI_EXTERNAL_PULL_REQUEST_TARGET_BRANCH_SHA``|
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_MERGE_REQUEST_TITLE``                    |
| github.event.pull_request.title }}``          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_EXTERNAL_PULL_REQUEST_IID``              |
| github.event.pull_request.number }}``         |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         | ``CI_EXTERNAL_PULL_REQUEST_SOURCE_REPOSITORY``|
| github.event.pull_request.head.repo.full_name |                                               |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
| ``${{                                         |``RCI_EXTERNAL_PULL_REQUEST_TARGET_REPOSITORY``|
| github.event.pull_request.base.repo.full_name |                                               |
| }}``                                          |                                               |
+-----------------------------------------------+-----------------------------------------------+
