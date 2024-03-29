.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

CI-freundliche Git-Repos
========================

Im Folgenden möchte ich einige Tipps geben, wie Git-Repositories und
`Kontinuierliche Integration
<https://de.wikipedia.org/wiki/Kontinuierliche_Integration>`_ mit `GitLab CI/CD
<https://docs.gitlab.com/ee/ci/>`_ oder `GitHub Actions
<https://docs.github.com/en/actions>`_ gut zusammenspielen können.

Speichert große Dateien außerhalb eures Repositories
----------------------------------------------------

Jedes Mal, wenn ein neuer *Build*  erstellt wird, muss das Arbeitsverzeichnis
geklont werden. Wenn euer Repository jedoch mit großen Artefakten aufgebläht
ist, verlangsamt sich dieser und ihr müsst länger auf die Ergebnisse warten.

Wenn euer Build jedoch von Binaries aus anderen Projekten oder großen Artefakten
abhängt, kann ein externes Speichersystem sinnvoll sein, das diejenigen Dateien,
die ihr zu Beginn eures Builds im Build-Verzeichnis benötigt, zum Download
bereitstellt.

Verwendet Shallow-Clones
------------------------

Jedes Mal, wenn ein Build ausgeführt wird, klont euer Build-Server euer
Projektarchiv in das aktuelle Arbeitsverzeichnis. Dabei klont Git üblicherweise
die gesamte Historie des Repos, wodurch dieser Vorgang mit der Zeit immer länger
dauert. Es sei denn, ihr verwendet :abbr:`sog. (sogenannte)` Shallow-Clones, bei
denen mit :ref:`git-clone-depth` nur der aktuelle Snapshot des Repos und mit
:ref:`git-clone-branch` nur der relevante Zweig heruntergezogen wird. Das
verkürzt die Build-Zeit vor allem bei Repositories mit einer langen Geschichte
und vielen Zweigen.

Dabei kann Git seit Version 1.9 einfache Änderungen an Dateien, wie :abbr:`z.B.
(zum Beispiel)` das Aktualisieren einer Versionsnummer, vornehmen, ohne dass die
gesamte Historie gepusht wurde.

.. warning::
    In einem shallow clone kann ``git fetch`` dazu führen, dass ein fast
    vollständiger Commit-Verlauf heruntergeladen wird. Auch andere
    Git-Operationen können zu unerwarteten Ergebnissen führen und die
    vermeintlichen Vorteile von Shallow-Clones zunichte machen, sodass wir
    empfehlen, Shallow-Clones nur für Builds zu verwenden und das Repository
    sofort danach wieder zu löschen.

Wollt ihr die Repositories jedoch weiterverwenden, kann der folgende Tipp
hilfreich sein.

Cache des Repos auf Build-Servern
---------------------------------

Dies beschleunigt auch das Klonen, da die Repos nur aktualisiert werden
müssen.

.. note::
    Der Cache von Repos ist nur dann von Vorteil, wenn die Build-Umgebung von
    Build zu Build bestehen bleibt. Wenn euer Build-Agent, :abbr:`z.B. (zum
    Beispiel)` Amazon EC2, den Build wieder abbaut, könnt ihr mit Caching jedoch
    nichts gewinnen.

Wählt die Trigger mit Bedacht
-----------------------------

Es versteht sich fast von selbst, dass es eine gute Idee ist, CI auf all euren
aktiven Zweigen laufen zu lassen. Aber es ist meist keine gute Idee, alle Builds
auf allen Zweigen gegen alle Commits laufen zu lassen.

Üblicherweise geben wir allen im Entwicklungsteam die Möglichkeit, ihre
Zweig-Builds auf Knopfdruck zu erstellen, anstatt sie automatisch auszulösen.
Dies scheint uns ein guter Weg, um ein Gleichgewicht zwischen regelmäßigen Tests
und der Einsparung von Ressourcen zu schaffen. In kritischen Zweigen wie
``main`` oder ``stable`` werden Builds jedoch automatisch ausgelöst. Zudem
erhalten wir automatisiert auch bei jedem Merge- oder Pull-Request zeitnahe
Testergebnisse.
