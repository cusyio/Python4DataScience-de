.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Reproduzieren
=============

Um die Ergebnisse eines Projekts zu reproduzieren, clonen wir den Code und rufen
anschließend die mit DVC verwalteten Daten ab:

.. code-block:: console

   $ git clone https://github.com/veit/dvc-example.git
   $ cd dvc-example
   $ uv sync
   $ uv run dvc pull -TR
   Collecting                                            |23.0 [00:02, 7.77entry/s]
   Fetching
   Building workspace index                              |1.00 [00:00,  119entry/s]
   Comparing indexes                                    |25.0 [00:00, 1.92kentry/s]
   Applying changes                                      |14.0 [00:00, 4.10kfile/s]
   A       data/features/
   A       data/prepared/
   A       eval/
   A       data/data.xml
   A       model.pkl
   17 files fetched and 14 files added
   $ tree data
   data
   ├── data.xml
   ├── data.xml.dvc
   ├── features
   │   ├── test.pkl
   │   └── train.pkl
   └── prepared
       ├── test.tsv
       └── train.tsv

Anschließend könnt ihr die Ergebnisse einfach reproduzieren mit `dvc repro
<https://dvc.org/doc/command-reference/repro>`_:

.. code-block:: console

   $ uv run dvc repro
   'data/data.xml.dvc' didn't change, skipping
   Stage 'prepare' didn't change, skipping
   Stage 'featurize' didn't change, skipping
   Stage 'train' didn't change, skipping
   Running stage 'evaluate':
   > uv run python src/dvc_example/evaluate.py model.pkl data/features
   Use `dvc exp run` to save experiment.
