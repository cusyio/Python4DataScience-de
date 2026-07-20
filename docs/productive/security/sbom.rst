.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Software Bill-of-Materials (SBOM)
=================================

Eine Software Bill-of-Materials (SBOM) ist ein Dokument zum Austausch von
Informationen über Software und deren Zusammensetzung. Dieses Format wird vor
allem im Sicherheitsbereich verwendet, um Software und ihre Abhängigkeiten
mithilfe von Schwachstellendatenbanken wie `CVE <https://www.cve.org/>`_ und
`OSV <https://osv.dev/>`_ auf Schwachstellen zu überprüfen. Das vom
CPython-Projekt verwendete SBOM-Format ist `SPDX
<https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Sbom/>`_, das
bei Bedarf in andere Formate konvertiert werden kann. Die SBOM-Datei für die in
CPython enthaltenen Abhängigkeiten wird unter `Misc/sbom.spdx.json
<https://github.com/python/cpython/blob/main/Misc/sbom.spdx.json>`_ verwaltet.
Die Datei wird erstellt mit `Tools/build/generate_sbom.py
<https://github.com/python/cpython/blob/main/Tools/build/generate_sbom.py>`_.

SBOM-Datei erstellen
--------------------

… mit uv
~~~~~~~~

:term:`uv` bietet eine einfache Möglichkeit, eine SBOM-Datei im Format CycloneDX
v1.5 zu erstellen mit:

.. code-block:: console

   $ uv export --format='cyclonedx1.5' > sbom.cdx.json

Die Datei enthält jedoch nur sehr rudimentäre Angaben, :abbr:`z. B. (zum
Beispiel)` für `cusy.tasks <https://github.com/cusyio/cusy.tasks>`_:

.. code-block:: json

    "component": {
      "type": "library",
      "bom-ref": "cusy-tasks-1@26.2.0",
      "name": "cusy-tasks",
      "version": "26.2.0",
      "properties": [
        {
          "name": "uv:package:is_project_root",
          "value": "true"
        }
      ]
    }

Mit ``uv export  --all-groups --format='cyclonedx1.5' > sbom.cdx.json`` könnt
ihr auch alle Dependency-Groups in die SBOM-Datei übernehmen.

… mit CycloneDX Python
~~~~~~~~~~~~~~~~~~~~~~

Deutlich umfangreicher ist die Ausgabe von `CycloneDX Python
<https://cyclonedx-bom-tool.readthedocs.io/en/latest/index.html>`_:

.. code-block:: json

    {
      "bom-ref": "cusy-tasks==26.2.0",
      "description": "",
      "externalReferences": [
        {
          "comment": "PackageSource: Local",
          "type": "distribution",
          "url": "file:///Users/veit/cusy/prj/cusy.tasks"
        },
        {
          "comment": "from packaging metadata Project-URL: Documentation",
          "type": "documentation",
          "url": "https://tasks.cusy.io/"
        },
        {
          "comment": "from packaging metadata Project-URL: Mastodon",
          "type": "other",
          "url": "https://mastodon.social/@Python4DataScience"
        },
        {
          "comment": "from packaging metadata Project-URL: GitHub",
          "type": "vcs",
          "url": "https://github.com/cusyio/cusy.tasks"
        }
      ],
      "licenses": [
        {
          "license": {
            "acknowledgement": "declared",
            "id": "BSD-3-Clause"
          }
        }
      ],
      "name": "cusy-tasks",
      "type": "library",
      "version": "26.2.0"
    }

Der Kommandozeilenaufruf zum Erstellen der Datei ist:

.. code-block:: console

   $ uvx --from cyclonedx-bom cyclonedx-py environment .venv --output-file sbom.cdx.json

.. warning::
   CycloneDX Python erstellt die SBOM-Datei aus dem aktuellen
   :file:`.venv`-Verzeichnis. Ruft ihr ``cyclonedx-bom`` also in eurer
   Entwicklungsumgebung auf, werdet ihr auch alle Entwicklungswerkzeuge in eurer
   SBOM-Datei wiederfinden.

… mit sbomify
~~~~~~~~~~~~~

sbomify stellt eine GitHub Action zum Erstellen der SBOM-Datei bereit, die unter
der Haube CycloneDX Python verwendet. Mit `actions/attest-sbom
<https://github.com/actions/attest-sbom>`_ kann die Datei dann attestiert
werden:

.. literalinclude:: sbomify.yml
   :caption: .github/workflows/sbomify.yml
   :language: yaml

In GitLab CI könnt ihr sbomify folgendermaßen verwenden:

.. literalinclude:: .gitlab-ci.yml
   :caption: .gitlab-ci.yml
   :language: yaml
   :lines: 1-12, 32-

Ihr könnt auch Dependency Scanning integrieren:

.. literalinclude:: .gitlab-ci.yml
   :caption: .gitlab-ci.yml
   :language: yaml
   :lines: 13-30

.. seealso::
   * `SBOM Generation in CI/CD Pipelines <https://sbomify.com/guides/ci-cd/>`_
   * `Dependency scanning by using SBOM
     <https://docs.gitlab.com/user/application_security/dependency_scanning/dependency_scanning_sbom/>`_

PEP 770 – SBOMs in Python-Paketen
---------------------------------

:pep:`770` standardisiert die Einbindung von SBOMs in Python-Wheels über das
Verzeichnis :file:`.dist-info/sboms/`. Wenn ihr Python-Pakete auf :term:`PyPI`
veröffentlicht, bedeutet dies, dass eure User die SBOM-Datei automatisch
erhalten, wenn sie euer Paket installieren, :abbr:`z. B. (zum Beispiel)`:

.. code-block:: console

   myapp-26.2.0.dist-info
   ├── METADATA
   ├── RECORD
   └── sboms/
       └── myapp.cdx.json

Build-Backends wie Hatchling≥1.28 unterstützen dies bereits mit der
``sbom-files``-Konfiguration:

.. code-block:: toml
   :caption: pyproject.toml

   [tool.hatch.build.targets.wheel]
   sbom-files = ["myapp.cdx.json"]

Anstatt die SBOM-Datei  beim Build von Grund auf neu zu generieren, kann eine
minimale CycloneDX-SBOM-Datei in das Repository eingecheckt werden:

.. code-block:: json

   {
     "bomFormat": "CycloneDX",
     "specVersion": "1.6",
     "version": 1,
     "metadata": {
       "component": {
         "type": "library",
         "name": "mylib",
         "version": "0.0.0-placeholder"
       }
     },
     "components": []
   }

Im :term:`CI`-Workflow wird die Platzhalter-SBOM-Datei dann mit dem Code
ausgecheckt. sbomify reichert sie dann mit den aktuellen Informationen an.
Anschließend baut hatchling das :term:`Wheel` mit der aktuellen SBOM-Datei und
schließlich wird das Wheel auf :term:`PyPI` veröffentlicht.

Analyse
-------

Zur Sicherheits- und Lizenzprüfung stehen zahlreiche Tools zur Verfügung, die
sich auf unterschiedliche Problembereiche konzentrieren. Zwei Open-Source-Tools
für die SBOM-Analyse sind `Dependency Track <https://dependencytrack.org>`_ und
`GUAC <https://guac.sh>`_. Mit ``sbomify-action`` könnt ihr SBOMs aus der
CI-Pipeline direkt in eure Dependency Track-Instanz hochladen mit:

.. code-block:: yaml

   UPLOAD_DESTINATIONS=dependency-track
