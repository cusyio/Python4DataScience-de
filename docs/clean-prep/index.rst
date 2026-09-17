.. SPDX-FileCopyrightText: 2021 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Daten bereinigen und validieren
===============================

*„Garbage In, Garbage Out“* ist der verzweifelte Hinweis, dass aus mangelhaften
Daten kaum gute Erkenntnisse gezogen werden können. Zwar gibt es stark
regulierte, sicherheitskritische Bereiche, in denen Daten routinemäßig in allen
Phasen überprüft werden, das allgemeine Niveau der Datenvalidierung ist in den
meisten Analyseprojekten jedoch eher gering.

Wenn wir jedoch Code schreiben, um Daten auszuwerten, die Daten jedoch nicht
vorher überprüfen, werden einige Ergebnisse irreführend, falsch oder ungültig
sein. Ähnlich verhält es sich, wenn wir unsere Ausgaben nicht validieren. So
tragen wir dann auch noch zu den *„schlechten Daten“* bei, gegen das wir alle
wettern. Hilfreich ist hier das *Postelsche Gesetz*, für das im TCP-Standard
vorgeschlagene Prinzip der Robustheit:

    *„Sei konservativ in dem, was du tust, sei liberal in dem, was du von
    anderen akzeptierst.“* [#]_

Dies steht in auffälligem Kontrast zu einer der Prinzipien von Python:

    *„Fehler sollten niemals unbemerkt bleiben.“* [#]_

Auch die :doc:`XML
<../data-processing/serialisation-formats/xml-html/index>`-Spezifikation
schreibt vor, dass nicht wohlgeformte XML-Dokumente zurückgewiesen werden
sollen:

    *„Validierende Prozessoren MÜSSEN … Verstöße gegen … die Nichteinhaltung der
    in dieser Spezifikation festgelegten Gültigkeitsbedingungen melden.“* [#]_

Die Abschnitte :doc:`procedures/index`, :doc:`procedures/ranges` und
:doc:`procedures/regression_tests` setzen keine Python-Kenntnisse voraus und
sind damit auch allgemein für Fachkräfte aus den Bereichen Datenmanagement,
Unternehmensführung und Qualitätssicherung geeignet.

Anschließend geben wir euch einen praktischen Überblick über verschiedene
:doc:`libs-methods/index` zur `Datenbereinigung
<https://de.wikipedia.org/wiki/Datenbereinigung>`_ und -validierung mit Python.

.. tip::
   `cusy Seminar: Daten bereinigen und validieren mit Python
   <https://cusy.io/de/our-training-courses/cleanse-and-validate-data-with-python.html>`_

----

.. [#] Jon Postel: `Transmission Control Protocol
       <https://www.rfc-editor.org/info/rfc761/#section-2.10>`_, 1980
.. [#] Tim Peters: :pep:`The Zen of Python <20>`, 1999
.. [#] `XML-Spezifikation 1.0, Abschnitt 5.1
       <https://www.w3.org/TR/2008/REC-xml-20081126/#proc-types>`_, 1998

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    categories
    procedures/index
    libs-methods/index
