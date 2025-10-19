.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Versuchsmetriken
================

Mit DVC lassen sich :ref:`Metriken <metrics>` einfach erfassen und :ref:`plotten
<plots>`, die Leistung in
Diagrammen visualisieren und :doc:`Parameter <params>` aktualisieren. So könnt
ihr viele Iterationen eures ML-Projekts ausführen und vergleichen.

Um die passenden Werte für unsere ML-Attribute zu finden, ,fügen wir unserer
früheren Pipeline eine abschließende Auswertungsphase hinzu:

.. code-block:: console

   $ uv run dvc stage add \
       -n evaluate \
       -d src/dvc_example/evaluate.py \
       -d model.pkl \
       -d data/features \
       -o eval \
       uv run python src/dvc_example/evaluate.py model.pkl data/features

Dies fügt eine neue Stufe in der :file:`dvc.yaml`-Datei hinzu:

.. code-block:: yaml
   :lineno-start: 34

   evaluate:
     cmd: uv run python src/dvc_example/evaluate.py model.pkl data/features
     deps:
     - data/features
     - model.pkl
     - src/dvc_example/evaluate.py
     outs:
     - eval

Zeile 39
    `evaluate.py
    <https://github.com/veit/dvc-example/blob/main/src/dvc_example/evaluate.py>`_
    verwendet `DVCLive <https://dvc.org/doc/dvclive>`_, um  (:abbr:`z. B. (zum
    Beispiel)` :abbr:`AUC (Area Under the Curve, deutsch Fläche unter der
    Kurve)`) und :abbr:`ROC (Receiver Operating Characteristic, deutsch
    Operationscharakteristik)`-Kurve) in das :file:`eval`-Verzeichnis zu
    schreiben, die DVC analysieren kann, um sie über Iterationen hinweg zu
    vergleichen und zu visualisieren. Üblicherweise konfiguriert DVCLive
    Metriken und Plots in der :file:`dvc.yaml`-Datei, in diesem Beispiel jedoch
    passen wir sie an, indem wir Trainings- und Testplots kombinieren.

    .. seealso::
       * `Visualizing Plots
         <https://dvc.org/doc/user-guide/experiment-management/visualizing-plots>`_
       * `DVCLive <https://dvc.org/doc/dvclive>`_

Zeile 41
    Die Metriken und Plots werden im :file:`eval`-Verzeichnis gespeichert,
    sodass diese Dateien keinen Einfluss auf den Git-Verlauf nehmen. Alternativ
    kann in bestimmten Fällen auch sinnvoll sein, bestimmte Metriken und Plots
    auch in Git nachverfolgen zu können.

Nun können wir unsere Auswertungen laufen lassen und die Ergebnisse sichern:

.. code-block:: console

   $ uv run dvc repro
   'data/data.xml.dvc' didn't change, skipping
   Stage 'prepare' didn't change, skipping
   Stage 'featurize' didn't change, skipping
   Stage 'train' didn't change, skipping
   Running stage 'evaluate':
   > uv run python src/dvc_example/evaluate.py model.pkl data/features
   $ git add .gitignore dvc.lock dvc.yaml pyproject.toml src/dvc_example/evaluate.py
   $ git commit -m ':sparkles: Add evaluation step'

.. _metrics:

Mit `dvc metrics <https://dvc.org/doc/command-reference/metrics>`_ könnt ihr
euch Metriken auch über die Kommandozeile erstellen lassen:

``dvc metrics show``
    zeigt Metriken mit optionaler Formattierung, :abbr:`z. B. (zum
    Beispiel)`:

    .. code-block:: console

       $ uv run dvc metrics show
       Path               avg_prec.test    avg_prec.train    roc_auc.test    roc_auc.train
       eval/metrics.json  0.9014           0.95704           0.93196         0.97743

    .. seealso::
       `dvc metrics show <https://dvc.org/doc/command-reference/metrics/show>`_

``dvc metrics diff``
    zeigt Änderungen in den Metriken zwischen Commits, :abbr:`z. B. (zum
    Beispiel)`:

    .. code-block:: console

       $ uv run dvc metrics diff
       Path               Metric          HEAD    workspace    Change
       eval/metrics.json  avg_prec.test   -       0.9014       -
       eval/metrics.json  avg_prec.train  -       0.95704      -
       eval/metrics.json  roc_auc.test    -       0.93196      -
       eval/metrics.json  roc_auc.train   -       0.97743      -

    .. seealso::
       `dvc metrics diff <https://dvc.org/doc/command-reference/metrics/diff>`_

.. _plots:

``dvc plots show``
    generiert eine HTML-Seite mit Plots:

    .. raw:: html
       :file: plots.html

.. seealso::
   * `dvc plots show <https://dvc.org/doc/command-reference/plots/show>`_
   * `dvc plots diff <https://dvc.org/doc/command-reference/plots/diff>`_

Metriken vergleichen
--------------------

Wenn ihr jetzt in der :file:`params.yaml`-Datei die Parameter ändert, könnt ihr
euer aktuelles Arbeitsverzeichnis mit dem letzten Commit (``HEAD``) vergleichen:

.. code-block:: console

   $ uv run dvc params diff
   Path         Param                   HEAD    workspace
   params.yaml  featurize.max_features  100     200
   params.yaml  featurize.ngrams        1       2

.. code-block:: console

   $ uv run dvc metrics diff
   Path               Metric          HEAD     workspace    Change
   eval/metrics.json  avg_prec.test   0.9014   0.925        0.0236
   eval/metrics.json  avg_prec.train  0.95704  0.97437      0.01733
   eval/metrics.json  roc_auc.test    0.93196  0.94602      0.01406
   eval/metrics.json  roc_auc.train   0.97743  0.98667      0.00924

.. code-block:: console

   $ uv run dvc plots diff
   file:///Users/veit/dvc-example/dvc_plots/index.html

.. raw:: html
   :file: plots-diff.html
