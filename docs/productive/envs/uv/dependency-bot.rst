Dependency-Bot
==============

Es ist eine bewährte Praxis, Abhängigkeiten regelmäßig zu aktualisieren, um
Schwachstellen zu vermeiden, Inkompatibilitäten zwischen Abhängigkeiten
einzuschränken und komplexe Upgrades zu vermeiden, wenn von einer zu alten
Version aktualisiert wird. Eine Vielzahl von Werkzeugen kann dabei helfen, auf
dem neuesten Stand zu bleiben. In :ref:`update-uv-lock` ist beschrieben, wie ihr
mit ``uv lock --upgrade`` alle Abhängigkeiten und mit :samp:`uv lock
--upgrade-package {PACKAGE}=={VERSION}` einzelne Abhängigkeiten kontrolliert
aktualisieren könnt. Ihr könnt euch jedoch hierbei auch von `Renovate
<https://docs.renovatebot.com/>`_ unterstützen lassen.

Renovate nutzt die :ref:`uv_lock`-Datei, um festzustellen, dass ``uv`` für die
Verwaltung von Abhängigkeiten verwendet wird, und schlägt Aktualisierungen für
Projektabhängigkeiten, optionale Abhängigkeiten und Entwicklungsabhängigkeiten
vor. Renovate aktualisiert sowohl die Dateien :file:`pyproject.toml` als auch
:file:`uv.lock`.

Installation und Konfiguration
------------------------------

Das Renovate CLI-Tool kann installiert werden mit

.. code-block:: console

   $ npm install renovate

.. tip::
   Der Renovate-Bot sollte unter einem eigenen Service-User laufen. Daher
   empfehlen wir, einen eigenen Account, ``renovate-bot``, für den Bot zu
   erstellen und zu verwenden. Erstellt und speichert anschließend ein
   Zugangs-Token für dieses Konto.

Für euren :doc:`/productive/git/advanced/gitlab/index`-Server könnt ihr nun
Renovate konfigurieren. Renovate sucht standardmäßig nach einer
:file:`config.js`-Datei im aktuellen Arbeitsverzeichnis. Ihr könnt dies jedoch
außer Kraft setzen, indem ihr die Umgebungsvariable ``RENOVATE_CONFIG_FILE``
definiert. Die Konfiguration kann dann :abbr:`z.B. (zum Beispiel)` so aussehen:

.. code-block:: js
   :caption: config.js

   module.exports = {
     endpoint: 'https://ce.cusy.io/api/v4/',
     token: 'GITLAB_TOKEN',
     platform: 'gitlab',
     onboardingConfig: {
       extends: ['config:recommended'],
     },
     repositories: ['USERNAME/REPO', 'ORGNAME/REPO'],
   };

.. note::
   Ändert die Pfade zu den Repositories in etwas Passendes. Ersetzt auch den
   Wert GitLab-Token durch den im vorherigen Schritt erstellten Wert.

.. seealso::
   * `Renovate configuration overview
     <https://docs.renovatebot.com/config-overview/>`_

Wenn ihr nun die :file:`uv.lock`-Datei in eurem Repository regelmäßig
aktualisieren wollt, solltet ihr :abbr:`z.B. (zum Beispiel)` in der
:file:`renovate.json5`-Datei in eurem Repository die Option `lockFileMaintenance
<https://docs.renovatebot.com/configuration-options/#lockfilemaintenance>`_
verwenden:

.. code-block:: json5
   :caption: renovate.json5

   {
     $schema: "https://docs.renovatebot.com/renovate-schema.json",
     lockFileMaintenance: {
       enabled: true,
     },
   }

Renovate erkennt jedoch nicht automatisch Dateien mit
:ref:`inline-script-metadata`. Ihr müsst diese Python-Skripte explizit mit
`fileMatch
<https://docs.renovatebot.com/configuration-options/#filematch>`_ angegeben,
:abbr:`z.B. (zum Beispiel)` mit:

.. code-block:: json5
   :caption: renovate.json5
   :emphasize-lines: 4-5

   {
     $schema: "https://docs.renovatebot.com/renovate-schema.json",
     pep723: {
       fileMatch: [
         "app\\.py",
       ],
     },
   }

.. seealso::
   * `lockFileMaintenance
     <https://docs.renovatebot.com/configuration-options/#lockfilemaintenance>`_

Schließlich sollte noch die zeitliche Ausführung von Renovate geplant werden,
:abbr:`z.B. (zum Beispiel)` mit `Cron <https://de.wikipedia.org/wiki/Cron>`_:

.. code-block:: bash

   #!/bin/bash

   export PATH="/home/renovate-bot/.node_modules/.bin/renovate:$PATH"
   export RENOVATE_CONFIG_FILE="/home/renovate-bot/config.js"
   export RENOVATE_TOKEN="GITLAB_TOKEN"

   0 * * * * renovate

CI/CD-Pipeline
--------------

Renovate kann auch in :doc:`cicd` eingebunden werden:

* `GitHub Action <https://github.com/renovatebot/github-action>`_
* `GitLab Runner <https://gitlab.com/renovate-bot/renovate-runner/>`_
