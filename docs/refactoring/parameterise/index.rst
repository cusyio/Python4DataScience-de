Parametrisierung und Zeitplanung
================================

Mit `papermill <https://papermill.readthedocs.io/en/latest/>`_ könnt ihr
Notebooks parametrieren und automatisieren. Ihr könnt die Notebooks
zeit- oder ereignisgesteuert ablaufen lassen.

Installieren
------------

.. code-block:: console

    $ pipenv install papermill
    Installing papermill…
    Adding papermill to Pipfile's [packages]…
    ✔ Installation Succeeded
    …

Verwenden
---------

#. Parametrisieren

   Der erste Schritt ist die Parametrisierung des Notebook. Dazu werden die
   Zellen in :menuselection:`View --> Cell Toolbar --> Tags` als Parameter
   markiert.

#. Überprüfen

   Ihr könnt das Notebook inspizieren, z.B. mit

   .. code-block:: console

        $ pipenv run papermill --help-notebook docs/refactoring/parameterise/input.ipynb
        Usage: papermill [OPTIONS] NOTEBOOK_PATH [OUTPUT_PATH]

        Parameters inferred for notebook 'docs/refactoring/parameterise/input.ipynb':
          msg: Unknown type (default None)

#. Ausführen

   Es gibt zwei Möglichkeiten, ein Notebook mit Parametern auszuführen:

   * … via Python API

     Die Funktion  ``execute_notebook`` kann aufgerufen werden, um ein Notebook
     mit einem dict von Parametern auszuführen:

     .. code-block:: python

        execute_notebook(INPUT_NOTEBOOK, OUTPUT_NOTEBOOK, DICTIONARY_OF_PARAMETERS)

     z.B. für :doc:`input.ipynb <input>`:

     .. code-block:: python

        import papermill as pm

        pm.execute_notebook(
            'PATH/TO/INPUT_NOTEBOOK.ipynb',
            'PATH/TO/OUTPUT_NOTEBOOK.ipynb',
            parameters=dict(salutation='Hello', name='pythonistas')
        )

     Das Ergebnis ist :doc:`output.ipynb <output>`.

     .. seealso::
        * `Workflow reference
          <https://papermill.readthedocs.io/en/latest/reference/papermill-workflow.html>`_

   * … via CLI

     .. code-block:: console

        $ pipenv run papermill input.ipynb output.ipynb -p salutation 'Hello' -p name 'pythonistas'

     Alternativ kann auch eine YAML-Datei mit den Parametern angegeben werden,
     z.B.
     ``params.yaml``:

     .. literalinclude:: params.yaml

     .. code-block:: console

        $ pipenv run papermill input.ipynb output.ipynb -f params.yaml

     Mit ``-b`` kann ein base64-kodierte YAML-String angegeben werden, die die
     Parameterwerte enthält:

     .. code-block:: console

        $ pipenv run papermill input.ipynb output.ipynb -b c2FsdXRhdGlvbjogIkhlbGxvIgpuYW1lOiAiUHl0aG9uaXN0YXMi

     .. seealso::
        * `CLI reference
          <https://papermill.readthedocs.io/en/latest/usage-cli.html>`_

     Ihr könnt dem Dateinamen auch einen Zeitstempel hinzufügen:

     .. code-block:: console

        $ dt=$(date '+%Y-%m-%d_%H:%M:%S')
        $ pipenv run papermill input.ipynb output_$(date '+%Y-%m-%d_%H:%M:%S').ipynb -f params.yaml

     Dies erzeugt eine Ausgabedatei, deren Dateiname einen Zeitstempel enthält,
     z.B. :doc:`output_2021-09-13_10:42:33.ipynb <output_2021-09-13_10:42:33>`.

     Schließlich könnt ihr ``crontab -e`` verwenden, um die beiden Befehle
     automatisch zu bestimmten Zeiten auszuführen, z.B. am ersten Tag eines
     jeden Monats:

     .. code-block::

        dt=$(date '+%Y-%m-%d_%H:%M:%S')
        0 0 1 * * cd ~/jupyter-notebook && pipenv run papermill input.ipynb output_$(date '+%Y-%m-%d_%H:%M:%S').ipynb -f params.yaml

#. Speichern

   Papermill kann Notebooks an einer Reihe von Orten speichern, einschließlich
   S3, Azure Data Blobs und Azure Data Lakes. Papermill erlaubt auch, neue
   Datenspeicher hinzuzufügen.

   .. seealso::
        * `papermill Storage
          <https://papermill.readthedocs.io/en/latest/reference/papermill-storage.html>`_
        * `Extending papermill through entry points
          <https://papermill.readthedocs.io/en/latest/extending-entry-points.html>`_
