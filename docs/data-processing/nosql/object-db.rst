.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Objektdatenbanksysteme
======================

Viele Programmiersprachen legen eine objektorientierte Programmierung nahe und
daher erscheint die Speicherung dieser Objekte natürlich. Daher liegt nahe, den
kompletten Prozess von der Implementierung bis zur Speicherung einheitlich und
einfach zu gestalten. Im Einzelnen sind die Vorteile:

Natürliche Modellierung und Repräsentation von Problemen
    Probleme lassen sich auf eine Weise modellieren, die der menschlichen
    Denkweise sehr nahe kommen.
Übersichtlicher, lesbarer und verständlicher
    Die Daten und die auf diesen operierenden Funktionen werden zu einer Einheit
    zusammengefasst, wodurch die Programme übersichtlicher, lesbarer und
    verständlicher werden.
Modular und wiederverwendbar
    Programmteile lassen sich einfach und flexibel wiederverwenden.
Erweiterbar
    Programme lassen sich einfach erweitern und an geänderte Anforderungen
    anpassen.

Object-relational impedance mismatch
------------------------------------

Objektorientierte Programmierung und relationale Datenhaltung sind aus
verschiedenen Gründen problematisch. So ist ein wichtiges Konzept der OOP zur
Umsetzung komplexer Modelle die Vererbung. Im relationalen Paradigma gibt es
jedoch nichts vergleichbares. Zur Umwandlung entsprechender Klassenhierarchien
in ein relationales Modell wurden objekt-relationale Mapper, ORM entwickelt, wie
z.B. :doc:`../postgresql/sqlalchemy`. Prinzipiell gibt es zwei verschiedene
Ansätze für ein ORM, wobei in beiden Fällen eine Tabelle für eine Klasse
angelegt wird:

Vertikale Partitionierung
    Die Tabelle enthält nur die Attribute der entsprechenden Klasse sowie einen
    Fremdschlüssel für die Tabelle der Oberklasse. Für jedes Objekt wird ein dann
    ein Eintrag in der zur Klasse gehörenden Tabelle sowie in den Tabellen aller
    Oberklassen angelegt. Beim Zugriff müssen die Tabellen mit Joins verbunden
    werden, wodurch es bei komplexen Modellen zu erheblichen
    Performance-Verlusten kommen kann.
Horizontale Partitionierung
    Jede Tabelle enthält die Attribute der zugehörigen Klasse sowie aller
    Oberklassen. Bei einer Änderung der Oberklasse müssen dann jedoch die
    Tabellen aller abgeleiteten Klassen ebenfalls aktualisiert werden.

Grundsätzlich müssen bei der Kombination von OOP und relationaler Datenhaltung
immer zwei Datenmodelle erstellt werden. Dies macht diese Architektur deutlich
komplexer, fehleranfälliger und in der Wartung aufwändiger.

Datenbanksysteme
----------------

Ein Beispiel für Objektdatenbanksysteme ist die ZODB.

+------------------------+----------------------------------------+
| **Home**               | `ZODB`_                                |
+------------------------+----------------------------------------+
| **GitHub**             | `zopefoundation/ZODB`_                 |
+------------------------+----------------------------------------+
| **Docs**               | `zodb.org/en/latest/tutorial.html`_    |
+------------------------+----------------------------------------+
| **Anwendungsgebiete**  | Plone, Pyramid, BTrees, volatile Daten |
+------------------------+----------------------------------------+
| **Entwicklungssprache**| Python                                 |
+------------------------+----------------------------------------+
| **Lizenzen**           | Zope Public License (ZPL) 2.1          |
+------------------------+----------------------------------------+
| **Datenmodell**        | PersistentList, PersistentMapping,     |
|                        | BTree                                  |
+------------------------+----------------------------------------+
| **Query-Language**     |                                        |
+------------------------+----------------------------------------+
| **Transaktionen,       | :term:`ACID`                           |
| Nebenläufigkeit**      |                                        |
+------------------------+----------------------------------------+
| **Replikation,         | `ZODB Replication Services (ZRS)`_     |
| Skalierung**           |                                        |
+------------------------+----------------------------------------+
| **Anmerkungen**        |                                        |
+------------------------+----------------------------------------+

.. _`ZODB`: https://zodb.org/en/latest/
.. _`zopefoundation/ZODB`: https://github.com/zopefoundation/ZODB
.. _`zodb.org/en/latest/tutorial.html`: https://zodb.org/en/latest/tutorial.html
.. _`ZODB Replication Services (ZRS)`: https://pypi.org/project/zc.zrs/
