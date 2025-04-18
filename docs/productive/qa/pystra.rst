.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Pystra
======

:abbr:`Pystra (Python Structural Reliability Analysis)` analysiert die
strukturelle Zuverlässigkeit von Python-Code und fasst sie in einem Report
zusammen. Aktuell werden jedoch nur Zufälligkeitsmethoden erster Ordnung
unterstützt wie *Crude Monte-Carlo*-Simulation und *Importance Sampling*.

.. seealso::
   * `Docs <http://pystra.github.io/pystra/>`_
   * `GitHub <https://github.com/pystra/pystra>`_

Installation
------------

.. code-block:: console

    $ uv add pystra

Zuverlässigkeitsanalyse
-----------------------

Eine FORM (first-order reliability method)-Analyse kann :abbr:`z.B. (zum
Beispiel)` zu folgendem Ergebnis führen:

.. code-block:: console

    ==================================================

     RESULTS FROM RUNNING FORM RELIABILITY ANALYSIS

     Number of iterations:      17
     Reliability index beta:    1.75397614074
     Failure probability:       0.039717297753
     Number of calls to the limit-state function: 164

    ==================================================
