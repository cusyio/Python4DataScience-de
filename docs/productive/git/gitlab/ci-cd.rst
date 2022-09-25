GitLab CI/CD
============

GitLab CI/CD kann bei iterativen Code-Änderungen eure Anwendungen automatisch
erstellen, testen, bereitstellen und überwachen. Dies verringert die Gefahr, dass
ihr neuen Code auf der Grundlage fehlerhafter Vorgängerversionen entwickelt.
Dabei sollen von der Entwicklung bis zu seiner Bereitstellung von Code-Änderungen
wenige oder gar keine menschlichen Eingriffe erforderlich sein.

Die drei wichtigsten Ansätze für diese kontinuierliche Entwicklung sind:

Continuous Integration
    führt eine Reihe von Skripten sequentiell oder parallel aus, die eure
    Anwendung automatisch erstellt und testet, :abbr:`z.B. (zum Beispiel)` nach
    jedem ``git pull`` in einem :doc:`Feature-Branch
    <../workflows/feature-branches>`. Damit soll es weniger wahrscheinlich
    werden, dass ihr Fehler in eure Anwendung einbringt.

    Wenn die Überprüfungen wie erwartet funktionieren, könnt ihr einen
    :doc:`Merge Request <merge-requests>` stellen; schlagen die Überprüfungen
    fehl, könnt ihr die Änderungen :abbr:`ggf. (gegebenenfalls)` zurücknehmen. 

    .. seealso::
       * `Kontinuierliche Integration
         <https://de.wikipedia.org/wiki/Kontinuierliche_Integration>`_

Continuous Delivery
    geht einen Schritt weiter als Kontinuierliche Integration und stellt die
    Anwendung auch kontinuierlich bereit. Dies erfordert jedoch noch einen
    manuellen Eingriff, um die Änderungen manuell in einem :ref:`Deployment
    Branch <deployment-branches>` bereitzustellen.

    .. seealso::
       * `Continuous Delivery <https://continuousdelivery.com>`_
       * `Continuous Delivery
         <https://de.wikipedia.org/wiki/Continuous_Delivery>`__

Continuous Deployment
    führt auch die Bereitstellung der Software auf die Produktiv-Infrastruktur
    automatisch durch.

Aktivieren von CI/CD in einem Projekt
-------------------------------------

#. Wählt in der oberen Leiste :menuselection:`Menü --> Projekte` und sucht euer
   Projekt.
#. Wählt in der linken Seitenleiste :menuselection:`Einstellungen --> Allgemein`.
#. Erweitert :guilabel:`Visibility, project features, permissions`.
#. Aktiviert im Abschnitt :menuselection:`Repository` die Option
   :guilabel:`CI/CD`.
#. Wählt :guilabel:`Änderungen speichern`.

CI/CD-Pipelines
---------------

Pipelines sind die wichtigste Komponente der Continuous Integration, Delivery und
Deployment.

Pipelines bestehen aus:

Jobs
    legen fest, was zu tun ist, :abbr:`z.B. (zum Beispiel)` Kompilieren von Code
    oder Testen.

    .. seealso::
       `Jobs <https://docs.gitlab.com/ee/ci/jobs/index.html>`_

Stages
    legen fest, wann die Jobs ausgeführt werden sollen, :abbr:`z.B. (zum
    Beispiel)` die Phase ``test``, die nach der Phase ``build`` ausgeführt werden
    soll.

    .. seealso::
       `Stages <https://docs.gitlab.com/ee/ci/yaml/index.html#stages>`_

*Jobs* werden von :abbr:`sog. (sogenannten)` `Runners
<https://docs.gitlab.com/ee/ci/runners/index.html>`_ ausgeführt. Mehrere *Jobs*
in einem *Stage* werden parallel ausgeführt, sofernes genügend gleichzeitige
Runner zur Verfügung stehen.

Wenn alle *Jobs* in einem *Stage* erfolgreich sind, fährt die Pipeline mit dem
nächsten *Stage* fort.

Schlägt ein *Job* in einem *Stage* fehl, wird der nächste *Stage* normalerweise
nicht ausgeführt, und die Pipeline wird vorzeitig beendet.

Im Allgemeinen werden Pipelines automatisch ausgeführt und erfordern nach ihrer
Erstellung keinen Eingriff. Es gibt jedoch auch Fälle, in denen ihr manuell in
eine Pipeline eingreifen könnt.

Eine typische Pipeline kann aus vier *Stages* bestehen, die in der folgenden
Reihenfolge ausgeführt werden:

#. Eine ``build``-*Stage* mit einem *Job* namens ``compile``.
#. Eine ``test``-*Stage* mit zwei parallelen *Jobs* namens ``unit-test`` und
   ``lint``.
#. Eine ``staging``-*Stage* mit einem *Job* namens ``deploy-to-stage``.
#. Eine ``production``-*Stage* mit einem *Job* namens ``deploy-to-prod``.

Die zugehörige ``.gitlab-ci.yml``-Datei könnte dann so aussehen:

.. code-block:: yaml

    stages:
      - build
      - test
      - staging
      - production

    compile:
      stage: build
      script:
        - echo "Compiling the code..."
        - echo "Compile complete."

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

    deploy-to-production:
      stage: production
      script:
        - echo "Deploying application in production environment..."
        - echo "Application successfully deployed to production."

Pipelines anzeigen
~~~~~~~~~~~~~~~~~~

Ihr findet die aktuellen und historischen Pipeline-Runs auf der Seite
:menuselection:`CI/CD --> Pipelines` eures Projekts. Ihr könnt auch auf Pipelines
für einen :doc:`Merge-Request <merge-requests>` zugreifen, indem ihr zu deren
Registerkarte :guilabel:`Pipelines` navigiert. Wählt eine Pipeline aus, um die
Seite *Pipeline-Details* zu öffnen und die *Jobs* anzuzeigen, die für diese
Pipeline ausgeführt wurde. Von hier aus könnt ihr eine laufende Pipeline
abbrechen, *Jobs* in einer fehlgeschlagenen Pipeline erneut versuchen oder eine
Pipeline löschen.

.. figure:: ci-cd-pipeline.png
   :alt: GitLab-CI/CD-Pipeline

   GitLab-CI/CD-Pipeline

.. seealso::
   * `Customize pipeline configuration
     <https://docs.gitlab.com/ee/ci/yaml/index.html>`_
   * `Scheduled pipelines
     <https://docs.gitlab.com/ee/ci/pipelines/schedules.html>`_
   * `GitLab CI/CD variables
     <https://docs.gitlab.com/ee/ci/variables/index.html>`_
   * `Predefined variables reference
     <https://docs.gitlab.com/ee/ci/variables/predefined_variables.html>`_
