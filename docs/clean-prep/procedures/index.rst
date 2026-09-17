.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Testverfahren
=============

Bei der Datenverarbeitung (→ :term:`DataOps`) und -analyse kommt es immer wieder
zu Fehlern, sei es bei einfachen Abfragen oder bei komplexen Datenpipelines für
maschinelles Lernen (→ :term:`MLOps`).

Zu Problemen mit der :doc:`Datanqualität <../categories>` kommen noch weitere,
die in den verschiedenen :ref:`Phasen eines Data-Science-Projekts <ds-phases>`
auftreten können.

Prozessfehler
-------------

Zu den häufigsten Fehlerursachen zählen:

* schlecht dokumentierte, unzureichend verstandene und uneinheitlich erfasste
  Eingabedaten mit irreführenden oder undurchsichtigen Feldnamen und schwer zu
  interpretierenden Werten
* unzureichend spezifizierte Analyseziele
* die fehlende Validierung der Eingabe- und Ausgabedaten
* die unzureichende Überprüfung der Lösung für die Datenanalyse
* ungeeignete Methoden
* fehlende automatisierte Tests der endgültigen Analyse-Pipeline
* mangelhaft dokumentierte Ergebnisse ohne klares Verständnis ihrer
  Einschränkungen und Gültigkeitsbedingungen
* unzureichende Überwachung der Datenpipeline

Unser Ziel ist es, die Häufigkeit und den Schweregrad solcher Fehler zu
reduzieren.

Testgetriebene Datenanalysen
----------------------------

Dabei lassen sich zwei Arten testgetriebener Datenanalysen
unterscheiden:

:doc:`Wertebereichtests <ranges>`
    Üblicherweise sind Sensoren nur für einen klar definierten Messbereich
    geeicht. Liefern diese Sensoren dann Ergebnisse, die außerhalb dieses
    Bereichs liegen, kann ihnen nicht mehr vertraut werden.
:doc:`regression_tests`
    Fehler in den Daten werden automatisiert dadurch erkannt, dass sie von einer
    Referenz abweichen, :abbr:`z. B. (zum Beispiel)` der Messzeitpunkt in der
    Zukunft liegt.

Andere Bereiche lassen sich weniger offensichtlich durch Software unterstützen,
beispielsweise Formalisierungs- und Implementierungsfehler. Dennoch gehen wir
auf einige Konzepte ein und erläutern Ansätze, um deren Auftreten zu vermeiden
oder zumindest zu reduzieren.

.. _ds-phases:

Phasen eines typischen Data-Science-Projekts
--------------------------------------------

+-----------------------+-----------------------+-----------------------+
| Phase                 | Fehlerklasse          | Erläuterung           |
+=======================+=======================+=======================+
| 1. Strategie          | Formalisierungsfehler | Daten, Fachdomäne     |
|                       |                       | oder Methoden wurden  |
|                       |                       | nicht verstanden      |
+-----------------------+-----------------------+-----------------------+
| 2. Prototypische      | Implementierungsfehler| Bug                   |
|    Datenanalyse       |                       |                       |
+-----------------------+-----------------------+-----------------------+
| 3. Automatisierte     | Anwendungsfehler      | Keine oder fehlerhafte|
|    Datenanalyse       |                       | Daten im Betrieb      |
|                       |                       | :abbr:`z. B. (zum     |
|                       |                       | Beispiel)`            |
|                       |                       | unvollständig         |
|                       |                       | aktualisierte Daten   |
+-----------------------+-----------------------+-----------------------+
| 4. Analyseergebnisse  | Analysefehler         | Disprepanz zwischen   |
|                       |                       | Daten und Annahmen,   |
|                       |                       | die während der       |
|                       |                       | Entwicklung           |
|                       |                       | bereitstanden und     |
|                       |                       | denenjenigen, die im  |
|                       |                       | Betrieb verarbeitet   |
|                       |                       | werden                |
+-----------------------+-----------------------+-----------------------+
| 5. Interpretation     | Interpretationsfehler | Fehlinterpretation der|
|                       |                       | Ergebnisse            |
+-----------------------+-----------------------+-----------------------+

Fehler analytischer Prozesse vermeiden
--------------------------------------

Um die verschiedenen Arten der oben genannten Fehler zu minimieren, sind
unterschiedliche Ansätze erforderlich. Der grundlegendste davon ist das ständige
Bewusstsein dafür, wie leicht man sich bei jeder Datenanalyse täuschen lassen
kann. Wir müssen ständig darauf achten, dass die ausgegebenen Ergebnisse
möglicherweise Unsinn sind, der nur durch elegante Präsentationen oder den
Anschein objektiver Unfehlbarkeit plausibler erscheint.

Die Fehlerwahrscheinlichkeit kann zwar in allen Kategorien verringert werden,
jedoch lassen sich nur drei der Fehlerklassen leicht mithilfe von Software
beheben:

* Implementierungsfehler (Bugs) lassen sich durch :doc:`regression_tests`
  beheben
* Anwendungs- und Analysefehler lassen sich reduzieren, wenn die Daten in allen
  Phasen der Pipelines sorgfältig überprüft werden
* Interpretationsfehler lassen sich jedoch kaum durch Software erkennen.

    „Es gibt drei Arten von Lügen: Lügen, verdammte Lügen und Statistiken.“ [#]_

  Einige der von Darrell Huff 1991 [#]_ vorgeschlagenen schlechten Praktiken
  sollten dennoch vermieden werden.

  .. figure:: error_types_2x.png
     :alt: TYPE I ERROR: FALSE POSITIVE
           TYPE II ERROR: FALSE NEGATIVE
           TYPE III ERROR: TRUE POSITIVE FOR INCORRECT REASONS
           TYPE IV ERROR: TRUE NEGATIVE FOR INCORRECT REASONS
           TYPE V ERROR: INCORRECT RESULT WHICH LEADS YOU TO A CORRECT
           CONCLUSION DUE TO UNRELATED ERRORS
           TYPE VI ERROR: CORRECT RESULT WHICH YOU INTERPRET WRONG
           TYPE VII ERROR: INCORRECT RESULT WHICH PRODUCES A COOL GRAPH
           TYPE VIII ERROR: INCORRECT RESULT WHICH SPARKS FURTHER RESEARCH AND
           THE DEVELOPMENT OF NEW TOOLS WHICH REVEAL THE FLAW IN THE ORIGINAL
           RESULT WHILE PRODUCING NOVEL CORRECT RESULTS
           TYPE IX ERROR: THE RISE OF SKYWALKER
     :target: https://xkcd.com/2303/

     Error Types

  Auch die Erstellung und Pflege guter Metadaten sowie Konzepte zur
  :doc:`Reproduzierbarkeit <../../productive/index>` sind hier relevant.

----

.. [#] In Mark Twains Autobiographie wird dieses Zitat Benjamin Disraeli
       zugeschrieben.
.. [#] “How to Lie with Statistics” by Darrell Huff, 1991

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ranges
    regression_tests
