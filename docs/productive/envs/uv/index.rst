``uv``
======

:term:`uv` ist ein extrem schneller Python-Paket- und Projektmanager.

Sowohl die :ref:`Installation von uv <python-basics:uv>` wie auch das Erstellen
der Dateistrukturen für  :ref:`Bibliotheken
<python-basics:uv-package-structure>` oder :doc:`python-basics:packs/apps` sind
bereits in unserem :doc:`python-basics:index`-Tutorial beschrieben.

.. _inline-script-metadata:

Inline script metadata
----------------------

``uv`` ist jedoch auch hervorragend geeignet für einzelne Python-Skripte, die
`Inline script metadata
<https://packaging.python.org/en/latest/specifications/inline-script-metadata/>`_
enthalten, also :abbr:`z.B. (zum Beispiel)`:

.. code-block:: python
   :caption: app.py

    #!/usr/bin/env -S uv run
    # /// script
    # requires-python = ">=3.12"
    # dependencies = [
    #     "rich",
    # ]
    # ///
    import rich

Sofern die Berechtigungen für die Datei :file:`app.py` ausführbar sind, also
:abbr:`z.B. (zum Beispiel)` mit ``chmod 755``, könnt ihr sie auf jedem Rechner
mit installiertem ``uv`` ausführen:

.. code-block:: console

   ./app.py

Es wird automatisch eine eigene isolierte Umgebung erstellt mit korrekter
Python-Version und Abhängigkeiten.

Pakete erstellen
----------------

Mit :ref:`uv build <uv-build>` könnt ihr einfach :term:`Distribution Packages
<Distribution Package>` und :term:`Wheels <wheel>` erstellen.

Abhängigkeiten deklarieren, festschreiben und automatisch aktualisieren
-----------------------------------------------------------------------

In :ref:`update-uv-lock` ist beschrieben, wie ihr mit ``uv lock --upgrade`` alle
Abhängigkeiten und mit :samp:`uv lock --upgrade-package {PACKAGE}=={VERSION}`
einzelne Abhängigkeiten kontrolliert aktualisieren könnt. Wie ihr regelmäßig
automatisiert die Abhängigkeiten eures Projekts aktualisieren könnt, beschreiben
wir in :doc:`dependency-bot`. Diese Maßnahmen erhöhen die Sicherheit eures
Projekts erheblich.

.. seealso::
   * :ref:`lock-dependencies`
   * :ref:`automatic-update`

Testen in verschiedenen Python-Umgebungen
-----------------------------------------

Mit uv vereinfacht sich die :ref:`parallele Installation verschiedener
Python-Versionen, einschließlich PyPy und free-threaded Python 3.13
<various-python-versions>`. Mit :ref:`tox_uv` könnt ihr euer Projekt dann
automatisiert in den verschiedenen Python-Umgebungen testen.

.. toctree::
   :hidden:

   cicd
   dependency-bot
   docker
