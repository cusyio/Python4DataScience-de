FastDS
======

`FastDS <https://dagshub.com/pages/fds>`_ ist ein Open-Source-Tool, das
:doc:`Git <../git/index>` und :doc:`DVC <index>` kombiniert, um eine einfache
Versionierung von Code und Daten zu ermöglichen.

Installation
------------

FastDS kann einfach installiert werden mit:

.. code-block:: console

    $ pipenv install fastds

Einführung
----------

Schon das Erstellen des initialen Repositories wird deutlich vereinfacht:

.. code-block:: console

    $ git init
    $ dvc init
    $ git add .
    $ dvc add data/data.xml
    $ git add data/.gitignore data/data.xml.dvc
    $ git commit -m "Initial commit"
    $ dvc push -r origin
    $ git push origin

wird zu:

.. code-block:: console

    $ fds init
    $ fds add .
    $ fds save -m "Initial commit"

FastDS kürzt Git- und DVC-Befehle ab, um Eingabefehler zu minimieren und sich
wiederholende Aufgaben zu automatisieren:

``init``
    initialisiert sowohl das Git- wie auch das DVC-Repository.
``status``
    gibt den Status beider Repositories zurück.
``add``
    fügt Dateien dem Git- oder DVC-Repository hinzu.
``commit``
    übrgibt Änderungen an das Git- oder DVC-Repository.
``clone``
    klont das Git-Repository und holt Daten vom entfernten DVC-Repository.
``push``
    überträgt Daten an die entfernten Git- und DVC-Repositories.
``save``
    fügt Änderungen in das Projekt ein und überträgt diese mit einer
    Commit-Nachricht an die entfernten Git- und DVC-Repositories.
