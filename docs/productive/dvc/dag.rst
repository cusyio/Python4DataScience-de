.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Pipelines anzeigen
==================

DVC stellt eine Pipeline intern als gerichtete azyklische Graphen (engl.: :abbr:`DAG (directed acyclic graphs)` dar.

.. seealso::
   `DVC DAG <https://dvc.org/doc/user-guide/pipelines/running-pipelines#dag>`_

Ihr könnt ``dvc dag`` verwenden, um Pipelines zu visualisieren oder zu
exportieren:

.. code-block:: console

    $ uv run dvc dag

        +-------------------+
        | data/data.xml.dvc |
        +-------------------+
                  *
                  *
                  *
              +-------+
              | split |
              +-------+
                  *
                  *
                  *
            +-----------+
            | featurize |
            +-----------+
             **        **
           **            *
          *               **
    +-------+               *
    | train |             **
    +-------+            *
             **        **
               **    **
                 *  *
            +----------+
            | evaluate |
            +----------+

* Mit ``dvc dag --dot`` kann auch eine ``.dot``-Datei für `Graphviz
  <https://www.graphviz.org>`_ generiert werden:

.. graphviz::

    strict digraph  {
        "data/data.xml.dvc";
        "split";
        "train";
        "featurize";
        "evaluate";
        "data/data.xml.dvc" -> "split";
        "split" -> "featurize";
        "featurize" -> "train";
        "featurize" -> "evaluate";
        "train" -> "evaluate";
    }

Mit ``dvc status`` könnt ihr euch anzeigen lassen, ob die Stufen oder lokale und
entfernte Speicher geändert wurden:

.. code-block:: console

   $ uv run dvc status
   evaluate:
       changed deps:
           modified:           src/dvc_example/evaluate.py
       changed outs:
           modified:           eval

.. seealso::
   `dvc status <https://man.dvc.org/status>`_

In :doc:`CI-Jobs <../git/advanced/gitlab/ci-cd/index>` soll üblicherweise
überprüft werden, ob die Pipeline auf dem neuesten Stand ist, ohne etwas
abzurufen oder auszuführen. Mit ``dvc repro --dry`` erfahrt ihr, welche
Pipeline-Stufen ausgeführt werden müssten. Wenn jedoch Daten fehlen, schlägt der
Befehl fehl. Wenn fehlende Daten ignoriert werden sollen, könnt ihr ``dvc repro
--dry --allow-missing`` verwenden.

.. code-block:: console

   $ uv run dvc repro --allow-missing --dry
   'data/data.xml.dvc' didn't change, skipping
   Stage 'prepare' didn't change, skipping
   Stage 'featurize' didn't change, skipping
   Stage 'train' didn't change, skipping
   Stage 'evaluate' is cached - skipping run, checking out outputs
   Running stage 'evaluate':
   > uv run python src/dvc_example/evaluate.py model.pkl data/features
   Use `dvc push` to send your updates to remote storage.
