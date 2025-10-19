.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Daten verwalten mit DVC
=======================

Für Datenanalysen und vor allem bei Machine Learning ist es äußerst wertvoll,
verschiedene Versionen von Analysen, die mit verschiedenen Datensätzen und
Parametern durchgeführt wurden, reproduzieren zu können. Um jedoch
reproduzierbare Analysen zu erhalten, müssen sowohl die Daten als auch das
Modell (einschließlich der Algorithmen, Parameter. :abbr:`etc. (et cetera)`)
versioniert werden. Die Versionierung von Daten für reproduzierbare Analysen ist
aufgrund der Datengröße ein größeres Problem als die Versionierung von Modellen.
Werkzeuge wie `DVC <https://dvc.org/>`_ helfen bei der Verwaltung von Daten,
indem Nutzer diese mit einem :doc:`Git <../git/index>`-artigen Workflow an einen
entfernten Datenspeicher übertragen können. Hierdurch vereinfacht sich der Abruf
bestimmter Versionen von Daten um eine Analyse zu reproduzieren.

DVC wurde entwickelt, um :abbr:`ML (Machine Learning)`-Modelle und Datensätze
gemeinsam nutzen zu können und nachvollziehbar zu verwalten. Es nutzt ein
eigenes System zum Speichern der Dateien mit Unterstützung :abbr:`u.a. (unter
anderem)` für :abbr:`SSH (Secure Shell)` und :abbr:`HDFS (Hadoop Distributed
File System)`.

.. tip::
   `cusy Seminar: Code und Daten versioniert und reproduzierbar speichern
   <https://cusy.io/de/unsere-schulungsangebote/code-und-daten-versioniert-und-reproduzierbar-speichern>`_

.. seealso::
   * `Get Started with DVC <https://dvc.org/doc/start>`_
   * `Documentation <https://dvc.org/doc>`_
   * `Git Repository <https://github.com/iterative/dvc>`_

Vergleich mit verwandten Technologien
-------------------------------------

git-annex
~~~~~~~~~

`git-annex <https://git-annex.branchable.com/>`_ konzentriert sich mehr auf die
Entdeckung und Verwendung von Datensätzen, die dann einfach mit Git verwaltet
werden. DVC hingegen speichert die Daten, die bei jeden Schritt der Pipeline
erzeugt werden, in :file:`.dvc`-Dateien, die dann durch Git verwaltet werden
kann. DVC stellt zudem praktische Tools zur Manipulation und Visualisierung von Daten-Pipelines bereit, siehe :abbr:`z.B. (zum Beispiel)` :doc:`dvc status
<dag>`. Schließlich lassen sich mit :ref:`dvc remote <dvc-remote>` auch externe
Abhängigkeiten angeben.

Workflow-Management-Systeme wie Airflow und Luigi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DVC konzentriert sich auf Data-Science-Workflows und Modellierung; daher sind
DVC-Pipelines sehr viel leichtgewichtiger, einfacher zu erstellen und zu ändern
als bei `Airflow <https://airflow.incubator.apache.org>`_ und `Luigi
<https://luigi.readthedocs.io/en/stable/>`_. Allerdings fehlen DVC erweiterte
Funktionen wie die Überwachung der Ausführung, Optimierung und Fehlertoleranz.
Auch ist DVC ein reines Befehlszeilen-Tool ohne grafische Benutzeroberfläche und
es führt auch keine Daemons oder Server aus. `CML <https://cml.dev>`_ versucht
hier, einige der Lücken leichtgewichtig mit GitHub, GitLab oder Bitbucket zu
schließen. DVC und CML eignen sich jedoch gut für iterative
Machine-Learning-Prozesse; und wenn mit den beiden ein gutes Modell gefunden
wurde, steht euch immer noch frei, die Pipeline in Luigi oder Airflow zu
integrieren.

Installation
------------

DVC lässt sich mit :term:`uv` installieren. Beachtet dabei jedoch, dass ihr
hierbei die Extras explizit angeben müsst. Dies können ``[ssh]``, ``[s3]``,
``[gs]``, ``[azure]``, und ``[oss]`` oder ``[all]`` sein. Für ``ssh`` sieht das
Kommando dann so aus:

.. code-block:: console

    $ uv add dvc[ssh]

Alternativ kann DVC auch über andere Paketmanager installiert werden:

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo wget https://dvc.org/deb/dvc.list -O /etc/apt/sources.list.d/dvc.list
      $ sudo apt update
      $ sudo apt install dvc

.. tab:: macOS

   .. code-block:: console

      $ brew install iterative/homebrew-dvc/dvc

.. toctree::
   :hidden:

   init
   data
   pipeline
   params
   metrics
   experiments
   dag
   reproduce
   integration
   fds
