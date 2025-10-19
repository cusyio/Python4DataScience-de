.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Daten verwalten
===============

Daten und Verzeichnisse hinzufügen
----------------------------------

Mit DVC könnt ihr Dateien, ML-Modelle, Verzeichnisse und Zwischenergebnisse mit
Git speichern und versionieren, ohne dass der Dateiinhalt in Git eingecheckt
werden muss:

.. code-block:: console

    $ uv run dvc get https://github.com/iterative/dataset-registry \
        get-started/data.xml -o data/data.xml
    $ uv run dvc add data/data.xml

Dies fügt die Datei :file:`data/data.xml` in :file:`data/.gitignore` hinzu und
schreibt die Meta-Angaben in :file:`data/data.xml.dvc`.

.. seealso::
   `.dvc Files <https://dvc.org/doc/user-guide/project-structure/dvc-files>`_

Um nun verschiedene Versionen eurer Projektdaten mit Git verwalten zu können,
fügt ihr nur :file:`data/.gitignore` und :file:`data/data.xml.dvc` hinzu:

.. code-block:: console

    $ git add data/.gitignore data/data.xml.dvc
    $ git commit -m ":monocle_face: Add data to dvc"

.. seealso::
   `External Dependencies and Outputs
   <https://dvc.org/doc/user-guide/pipelines/external-dependencies-and-outputs>`_

Daten speichern und abrufen
---------------------------

Die Daten können vom Arbeitsverzeichnis eures Git-Repository auf den entfernten
Speicherplatz kopiert werden mit

.. code-block:: console

    $ uv run dvc push

Falls ihr aktuellere Daten abrufen wollt, könnt ihr dies mit

.. code-block:: console

    $ uv run dvc pull

Daten importieren und aktualisieren
-----------------------------------

Alternativ zu ``dvc get`` könnt ihr auch Daten und Modelle aus einem anderen
Projekts mit ``dvc import`` importieren, :abbr:`z. B. (zum Beispiel)`:

.. code-block:: console

   $ uv run dvc import https://github.com/iterative/dataset-registry  get-started/data.xml -o data/data.xml
   Importing 'get-started/data.xml (https://github.com/iterative/dataset-registry)' -> 'data/data.xml'

Dies lädt die Datei aus der `dataset-registry
<https://github.com/iterative/dataset-registry>`_ in unser
:file:`data`-Verzeichnis, fügt sie :file:`.gitignore` hinzu und erstellt
:file:`data.xml.dvc`.

Mit ``dvc update`` könnt ihr diese Datenquellen aktualisieren, bevor ihr eine
Pipeline reproduziert, die von diesen Datenquellen abhängt, :abbr:`z. B. (zum
Beispiel)`:

.. code-block:: console

   $ uv run dvc update data/data.xml.dvc
   'data/data.xml.dvc' didn't change, skipping

.. seealso::
   * `Discovering and accessing data
     <https://dvc.org/doc/user-guide/data-management/discovering-and-accessing-data>`_
   * `External Data
     <https://dvc.org/doc/user-guide/data-management/importing-external-data>`_

Daten löschen
-------------

Wenn ihr Dateien oder Verzeichnisse aus der Verwaltung von DVC entfernen
möchtet, könnt ihr dies mit `dvc remove
<https://dvc.org/doc/command-reference/remove>`_:

.. code-block::

   $ uv run dvc remove data/data.xml.dvc

Anschließend könnt ihr ``dvc gc -w`` verwenden, um alle Dateien und ihre
früheren Versionen aus dem Cache zu löschen.
