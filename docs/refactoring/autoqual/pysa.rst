Pysa
====

Der Python Static Analyzer Pysa führt `Taint
<https://en.wikipedia.org/wiki/Taint_checking>`_-Analysen durch um potenzielle
Sicherheitsprobleme zu identifizieren. Dabei verfolgt Pysa Datenströme von ihrem
Ursprung zu ihrem Endpunkt und identifiziert dabei anfälligen Code.

.. seealso::
   * `What Is Taint Analysis and Why Should I Care?
     <https://dzone.com/articles/what-is-taint-analysis-and-why-should-i-care>`_
   * `How Pysa works <https://pyre-check.org/docs/pysa-basics>`_
   * `Running Pysa <https://pyre-check.org/docs/pysa-running/>`_
   * `Pysa Tutorial <https://github.com/facebook/pyre-check/tree/master/documentation/pysa_tutorial>`_

Konfiguration
-------------

Pysa verwendet zwei Dateitypen für die Konfiguration:

* eine ``taint.config``-Datei im JSON-Format, in der ``sources``, ``sinks``,
  ``features`` und ``rules`` definiert werden.

  .. code-block:: javascript

    {
      "comment": "UserControlled, Test, Demo sources are predefined. Same for Demo, Test and RemoteCodeExecution sinks",
      "sources": [],
      "sinks": [],
      "features": [],
      "rules": []
    }

* Dateien mit der Endung ``.pysa`` in einem Verzeichnis, das mit
  ``taint_models_path`` in Eurer ``.pyre_configuration``-Datei konfiguriert
  wurde.

Praktische Beispiele findet Ihr im `Pyre-Repository
<https://github.com/facebook/pyre-check/tree/master/stubs/taint/core_privacy_security>`_.

Verwendung
----------

Pyre kann aufgerufen werden, z.B. mit

.. code-block:: console

    $ $ pipenv run pyre analyze --save-results-to ./

Die Option ``--save-results-to`` speichert detaillierte Ergebnisse in
``./taint-output.json``.

Pysa Postprozessor
------------------

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pipenv install fb-sapp

Verwendung
~~~~~~~~~~

#. Parsen der JSON-Datei, z.B. mit

   .. code-block:: console

    $ pipenv run sapp --database-name sapp.db analyze ./taint-output.json

   Die Ergebnisse werden in der lokalen SQLite-Datei ``sapp.db`` gespeichert.

#. Erkunden der Probleme mit

   .. code-block:: console

    $ pipenv run sapp --database-name sapp.db explore

   Dies startet ein IPython-Interface, das mit der SQLite-Datenbank verbunden
   ist:

   ``issues``
    listet alle Probleme auf
   ``issue 1``
    wählt das erste Problem aus
   ``trace``
    zeigt den Datenfluss von ``source`` bis ``sink`` an
   ``n``
    springt zum nächsten Aufruf
   ``list``
    zeigt den Quellcode des Aufrufs
   ``jump 1``
    springt zum ersten Aufruf und zeigt den Quellcode an

Weitere Kommandos erhaltet Ihr in `Commands
<https://pyre-check.org/docs/static-analysis-post-processor#commands>`_.
