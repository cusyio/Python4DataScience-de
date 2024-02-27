.. SPDX-FileCopyrightText: 2019 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Einführung
==========

Zielgruppe
----------

Die Zielgruppen sind vielfältig, von Data-Scientists über Data-Engineers und
-Analysts  bis hin zu Systems-Engineers. Ihre Fähigkeiten und Arbeitsabläufe
sind sehr unterschiedlich. Eine der großen Stärken von Python für Data Science
ist jedoch, dass es diesen verschiedenen Expert*innen ermöglicht, in
funktionsübergreifenden Teams eng zusammenzuarbeiten.

Data-Scientists
    untersuchen Daten mit verschiedenen Parametern und fassen die Ergebnisse
    zusammen.
Data-Engineers
    überprüfen die Qualität des Codes und machen ihn robuster, effizienter und
    skalierbarer.
Data-Analysts
    nutzen den von Data-Engineers bereitgestellten Code, um die Daten
    systematisch zu analysieren.
Systems-Engineers
    stellen die Forschungsplattform auf Basis von
    :doc:`jupyter-tutorial:hub/index` bereit, auf der die anderen ihre Arbeit
    verrichten können.

In diesem Tutorial wenden wir uns an Systems-Engineers, die eine auf
Jupyter-Notebooks basierende Plattform aufbauen und betreiben wollen. Wir
erklären dann, wie diese Plattform von Data-Scientists, Data-Engineers und
-Analysts effektiv genutzt werden kann.

Aufbau des Tutorials Python für Data Science
--------------------------------------------

Ab Kapitel 2 folgt das Tutorial dem Prototyp eines Forschungsprojekts:

2. :doc:`workspace/index` mit der Installation und Konfiguration von
   :doc:`workspace/ipython/index`, :doc:`Jupyter notebooks
   <jupyter-tutorial:index>` mit :doc:`jupyter-tutorial:nbextensions/index`
   und :doc:`jupyter-tutorial:ipywidgets/index`.
#. :doc:`data-processing/index` entweder über eine :doc:`REST API
   <data-processing/httpx/index>` oder direkt über eine :doc:`HTML-Seite
   <data-processing/serialisation-formats/xml-html/beautifulsoup>`.
#. :doc:`clean-prep/index` ist eine wiederkehrende Aufgabe, bei der redundante,
   inkonsistente oder falsch formatierte Daten entfernt oder geändert werden.
#. :doc:`viz/index` wurde in ein separates Tutorial mit den vielen
   verschiedenen Möglichkeiten verschoben.
#. :doc:`performance/index` stellt Möglichkeiten vor, wie ihr euren Code
   schneller laufen lassen könnt.
#. :doc:`productive/index` product zeigt, was notwendig ist, um reproduzierbare
   Ergebnisse zu erzielen: Es werden nicht nur :doc:`reproducible environments
   <productive/envs/index>` benötigt, sondern auch die Versionierung des
   :doc:`Quellcodes <productive/git/index>` und der :doc:`Daten
   <productive/dvc/index>`. Der Quellcode sollte in :doc:`Programmbibliotheken
   verpackt werden <productive/packaging>` mit :doc:`Dokumentation
   <productive/documenting>`, :doc:`Lizenz(en) <productive/licensing>`,
   :doc:`Rests <productive/testing>` und :doc:`Logging
   <productive/logging/index>`. Schließlich enthält das Kapitel Ratschläge zur
   :doc:`Verbesserung der Codequalität <productive/qa/index>` und des
   :doc:`sicheren Betriebs <productive/security>`.
#. :doc:`web/index` kann entweder Dashboards aus Jupyter-Notebooks generieren
   oder eine umfassendere Anwendungslogik erfordern, wie in
   :doc:`pyviz:bokeh/embedding-export/flask`, demonstriert, oder Daten über
   eine `RESTful API
   <https://en.wikipedia.org/wiki/Representational_state_transfer>`_
   bereitstellen.

.. include:: ../README.rst
   :start-after: badges
   :end-before: first-steps

.. include:: ../README.rst
   :start-after: follow-us
