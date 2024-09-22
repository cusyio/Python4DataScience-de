.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

HERMES
======

`HERMES <https://project.software-metadata.pub>`_ vereinfacht die Publikation
von Forschungssoftware, indem kontinuierlich in :doc:`cff`, :doc:`codemeta` und
:doc:`Git <../../git/index>` vorhandene Metadaten abegrufen werden. Anschließend
werden die Metadaten auch für `InvenioRDM
<https://invenio-software.org/products/rdm/>`_ und `Dataverse
<https://dataverse.org/>`_ passend zusammengestellt. Schließlich werden auch
:doc:`CITATION.cff <cff>` und :doc:`codemeta.json <codemeta>` für die
Publikationsrepositories aktualisiert.

#. ``.hermes/`` in der :ref:`.gitignore <gitignore>`-Datei hinzufügen
#. :doc:`CITATION.cff <cff>`-Datei mit zusätzlichen Metadaten bereitstellen

   .. important::
      Stellt sicher, dass ``license`` in der Datei :doc:`CITATION.cff <cff>`
      definiert ist; andernfalls wird eure Veröffentlichung von der :doc:`Zenodo
      <doi>`-Sandbox nicht als Open Access akzeptiert.

#. HERMES-Workflow konfigurieren

   Der HERMES-Workflow wird konfiguriert in der
   :doc:`/data-processing/serialisation-formats/toml/index`-Datei
   :file:`hermes.toml`, wobei jeder Schritt einen eigenen Abschnitt erhält.

   Wenn ihr HERMES so konfigurieren wollt, dass die Metadaten aus :doc:`Git
   <../../git/index>` und :doc:`CITATION.cff <cff>` verwendet werden und die
   Ablage in der Zenodo Sandbox, die auf InvenioRDM aufbaut, erfolgen soll,
   sieht die :file:`hermes.toml`-Datei folgendermaßen aus:

   .. literalinclude:: hermes.toml
      :caption: hermes.toml
      :name: hermes.toml

#. Zugangstoken für Zenodo Sandbox

   Damit GitHub Actions euer Repository in der Zenodo Sandbox veröffentlichen
   kann, benötigt ihr ein persönliches Zugangstoken. Hierfür müsst ihr euch bei
   der `Zenodo Sandbox <https://sandbox.zenodo.org/>`_ anmelden, um dann in
   eurem Benutzerprofil einen `persönliches Zugangstoken
   <https://sandbox.zenodo.org/account/settings/applications/tokens/new/>`_ mit
   dem Namen :samp:`HERMES workflow` und den Geltungsbereichen
   :guilabel:`deposit:actions` und :guilabel:`deposit:write` zu erstellen:

   .. image:: zenodo-personal-access-token.png
      :alt: Zenodo: Neues persönliches Zugangstoken

#. Kopiert das neu erstellte Token in ein neues `GitHub Secret
   <https://docs.github.com/de/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository>`_
   namens :samp:`ZENODO_SANDBOX` in Ihrem Repository: :menuselection:`Settings
   --> Secrets and Variables --> Actions --> New repository secret`:

   .. image:: github-new-action-secret.png
      :alt: GitHub: Neues Action-Secret

#. Konfiguriert die GitHub-Aktion

   Das HERMES-Projekt stellt Vorlagen zur kontinuierlichen Integration in einem
   speziellen Repository bereit: `softwarepub/ci-templates
   <https://github.com/softwarepub/ci-templates>`_. Kopiert die Vorlagendatei
   `TEMPLATE_hermes_github_to_zenodo.yml
   <https://github.com/softwarepub/ci-templates/blob/main/TEMPLATE_hermes_github_to_zenodo.yml>`_
   in das Verzeichnis :file:`.github/workflows/` eures Repository und benennt
   sie um, :abbr:`z.B. (zum Beispiel)` in :file:`hermes_github_to_zenodo.yml`.

   Anschließend solltet ihr die Datei durchgehen und nach Kommentaren, die mit
   :samp:`# ADAPT` gekennzeichnet sind, suchen. Passt die Datei an eure
   Bedürfnisse an.

   Schließlich fügt ihr die Workflow-Datei zur Versionskontrolle hinzu und
   schiebt sie auf den GitHub-Server:

   .. code-block:: console

      $ git add .github/workflows/hermes_github_to_zenodo.yml
      $ git commit -m ":construction_worker: GitHub action for automatic publication with HERMES"
      $ git push

#. GitHub-Actions sollen Pull Requests in eurem Repository erstellen dürfen

   Der HERMES-Workflow wird keine Metadaten ohne eure Zustimmung
   veröffentlichen. Stattdessen erstellt er einen Pull-Request, damit ihr die
   hinterlegten Metadaten genehmigen oder ändern könnt. Um dies zu aktivieren,
   geht in eurem Repository zu :menuselection:`Settings --> Actions --> General`
   und aktiviert im Abschnitt :guilabel:`Workflow permissions` :guilabel:`Allow
   GitHub Actions to create and approve pull requests`.
