.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Erstellen eines DOI mit Zenodo
==============================

`Zenodo <https://zenodo.org/>`__ ermöglicht die Archivierung von Software und
die Bereitstellung eines DOI für diese Software. Im Folgenden werde ich am
Beispiel des Jupyter-Tutorials zeigen, welche Schritte hierzu erforderlich sind:

#. Wenn ihr noch keinen `Account für Zenodo <https://zenodo.org/signup/>`_ habt,
   erstellt einen, bevorzugt mit GitHub.

#. Aktiviert in :menuselection:`Upload --> New Upload` unter :guilabel:`Basic
   information` den Button :guilabel:`Reserve DOI` um einen :abbr:`DOI (Digital
   Object Identifier)` für euren Upload zu reservieren. Lasst das Formular offen
   um später eure Software hochladen zu können.

#. Erstellt oder ändert die :doc:`codemeta`- und :doc:`cff`-Dateien in eurem
   Software-Verzeichnis.

#. Bindet den Badge in der :file:`README`-Datei eurer Software ein:

   Markdown:

   .. code-block:: md

      [![DOI](https://zenodo.org/badge/307380211.svg)](https://zenodo.org/badge/latestdoi/307380211)

   reStructedText:

   .. code-block:: rst

      .. image:: https://zenodo.org/badge/307380211.svg
         :target: https://zenodo.org/badge/latestdoi/307380211

#. Nun wählt das Repository aus, das ihr archivieren wollt:

   .. figure:: zenodo-github.png
      :alt: Enable repositories for Zenodo

#. Überprüft, ob Zenodo einen Webhook in eurem Repository für das
   *Releases*-Event erstellt hat:

   .. figure:: zenodo-webhook.png
      :alt: Zenodo webhook

#. Erstellt ein neues Release:

   .. figure:: github-release.png
      :alt: Github releases

#. Überprüft, ob der :abbr:`DOI (Digital object identifier)` korrekt erstellt
   wurde:

   .. figure:: zenodo-release.png
      :alt: Zenodo release
