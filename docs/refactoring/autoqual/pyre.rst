Strukturelle Zuverlässigkeitsanalyse mit PyRe
=============================================

PyRe (Python Reliability) analysiert die strukturelle Zuverlässigkeit von
Python-Code und fasst sie in einem Report zusammen. Aktuell werden jedoch nur
Zufälligkeitsmethoden erster Ordnung unterstützt wie Crude
Monte-Carlo-Simulation und Importance Sampling.

.. seealso::
   * `Docs <https://hackl.science/pyre/>`_
   * `GitHub <https://github.com/hackl/pyre>`_

Installation
------------

.. code-block:: console

    $ pipenv install git+git://github.com/hackl/pyre.git

Zuverlässigkeitsanalyse
-----------------------

Eine FORM-Analyse kann z.B. zu folgendem Ergebnis führen:

.. code-block:: console

    ==================================================

     RESULTS FROM RUNNING FORM RELIABILITY ANALYSIS

     Number of iterations:      17
     Reliability index beta:    1.75397614074
     Failure probability:       0.039717297753
     Number of calls to the limit-state function: 164

    ==================================================
