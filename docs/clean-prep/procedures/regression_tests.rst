.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Regressionstests
================

Regressionstests sollen gewährleisten, dass bei einer Änderung des
Analyseprozesses die bisher ermittelten Ergebnisse unverändert gültig bleiben.
Es kann jedoch auch vorkommen, dass sich die Ergebnisse ändern auch wenn der
Quellcode unverändert bleibt.

#. Erfassen der exemplarischen Eingangsdaten und der erwarteten
   Referenzergebnisse
#. Tests zur Überprüfung, ob die erfassten Eingangsdaten zu den erwarteten
   Referenzergebnissen führen; diese können :abbr:`z .B. (zum Beispiel)` mit
   `tdda gentest <https://tdda.readthedocs.io/en/latest/gentest.html>`_ erstellt
   werden. Alternativ stellt die :doc:`../libs-methods/tdda`-Bibliothek
   Werkzeuge bereit, allen voran `tdda diff
   <https://tdda.readthedocs.io/en/latest/tddadiff.html>`_, um eigene Tests zu
   schreiben.
#. Vollständig automatisierter Prozess zur Datenanalyse

.. seealso::
   * :doc:`../../productive/index`
   * :doc:`python-basics:test/tdd`
