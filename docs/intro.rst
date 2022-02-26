Einführung
==========

.. include:: ../README.rst
   :start-after: badges
   :end-before: first-steps

Zielgruppe
----------

Die Nutzung von Jupyter-Notebooks ist vielfältig und reicht von den
Datenwissenschaften über Data-Engineering und Datenanalyse bis hin zu
System-Engineering. Dabei sind die Fähigkeiten und Arbeitsabläufe der einzelnen
Zielgruppen sehr unterschiedlich. Eine der großen Stärken von Jupyter-Notebooks
ist jedoch, dass sie eine enge Zusammenarbeit dieser unterschiedlichen
Fachgruppen in funktionsübergreifenden Teams ermöglichen.

* **Data Scientists** erforschen Daten mit verschiedenen Parametern und fassen
  die Ergebnisse zusammen.
* **Data-Engineers** iüberprüfen die Qualität des Codes und machen den Code
  robuster, effizienter und skalierbar.
* **Data-Analysts** verwenden den von Data-Engineers bereitgestellten Code um
  systematisch die Daten zu analysieren.
* **System-Engineers** stellen die Forschungsplattform auf Basis des
  :doc:`workspace/jupyter/hub/index` bereit, auf der die anderen Rollen ihre
  Arbeit ausführen können.

Im ersten Teil dieses Tutorial wenden wir uns zunächst an das
System-Engineering, das eine Plattform auf Basis von Jupyter-Notebooks aufbauen
und betreiben will. In der Folge erläutern wir dann, wie diese Plattform
effektiv von den Fachgruppen in den Datenwissenschaften, im Data-Engineering und
und in der Datenanalyse genutzt werden kann.

Aufbau des Jupyter-Tutorial
---------------------------

Das Jupyter-Tutorial folgt ab Kapitel 3 dem prototypischen Verlauf eines
Forschungsprojekts:

3. **Arbeitsbereich einrichten** mit der Installation und Konfiguration von
   :doc:`workspace/ipython/index`, :doc:`workspace/jupyter/index` mit
   :doc:`workspace/jupyter/nbextensions/index` und
   :doc:`workspace/jupyter/ipywidgets/index`.
4. **Daten sammeln**, entweder durch eine :doc:`Rest-API
   <data-processing/requests/index>` oder direkt von einer :doc:`HTML-Seite
   <data-processing/serialisation-formats/xml-html/beautifulsoup>`.
5. **Daten bereinigen** ist eine wiederkehrende Aufgabe, die u.a. redundante,
   inkonsistente oder falsch formatierte Daten entfernen oder modifizieren soll.
6. **Erschließen der Daten –** :doc:`viz/index` umfasst expolorative Analysen und
   das Visualisieren von Daten.
7. **Refactoring** umfasst das Parametrisieren, Validieren und
   Performance-Optimierungen, u.a. durch :doc:`Nebenläufigkeit
   <performance/concurrency>`.
8. **Produkt erstellen** umfasst das :doc:`productive/testing`,
   :doc:`productive/logging/index` und :doc:`productive/documenting/index` der
   Methoden und Funktionen sowie das :doc:`Erstellen von Paketen
   <productive/packaging/index>`.
9. **Web-Anwendungen** können entweder aus Jupyter-Notebooks
   :doc:`web/dashboards/index` generieren oder umfassendere
   Applikationslogik benötigen, wie z.B. in
   :doc:`pyviz:bokeh/embedding-export/flask` demonstriert, oder Daten über eine
   `RESTful API
   <https://de.wikipedia.org/wiki/Representational_State_Transfer>`_
   bereitstellen.

Warum Jupyter?
--------------

Wie können nun diese vielfältigen Aufgaben vereinfacht werden? Es wird sich
kaum ein Werkzeug finden, das all diese Aufgaben abdeckt und selbst für einzelne
Aufgaben sind häufig mehrere Werkzeuge notwendig. Daher suchen wir auf einer
abstrakteren Ebene allgemeinere Muster für Tools und Sprachen, mit denen Daten
analysiert und visualisiert sowie ein Projekt dokumentiert und präsentiert
werden kann. Genau dies wir mit dem `Project Jupyter <https://jupyter.org/>`_
angestrebt.

Das Projekt Jupyter startete 2014 mit dem Ziel, ein konsistentes Set von
Open-Source-Tools für wissenschaftliche Forschung, reproduzierbare Workflows,
`Computational Narratives
<https://blog.jupyter.org/project-jupyter-computational-narratives-as-the-engine-of-collaborative-data-science-2b5fb94c3c58>`_
und Datenanalyse zu erstellen. Bereits 2017 wurde Jupyter dann mit dem `ACM
Software Systems Award
<https://blog.jupyter.org/jupyter-receives-the-acm-software-system-award-d433b0dfe3a2>`_
ausgezeichnet - eine prestigeträchtige Auszeichnung, die es u.a. mit Unix und
dem Web teilt.

Um zu verstehen, warum Jupyter-Notebooks so erfolgreich sind, schauen wir uns
die Kernfunktionen einmal genauer an:

`Jupyter Notebook Format <https://nbformat.readthedocs.io/>`_
    Jupyter Notebooks sind ein offenes, auf JSON basierendes Dokumentenformat
    mit vollständigen Aufzeichnungen der Sitzungen des Benutzers und des
    enthalten Code.
Interactive Computing Protocol
    Das Notebook kommuniziert mit Rechenkernel über das *Interactive Computing
    Protocol*, einem offenen Netzwerkprotokoll basierend auf JSON-Daten über
    `ZMQ <https://zeromq.org/>`_ und `WebSockets
    <https://de.wikipedia.org/wiki/WebSocket>`_.
:doc:`workspace/jupyter/kernels/index`
    Kernel sind Prozesse, die interaktiven Code in einer bestimmten
    Programmiersprache ausführen und die Ausgabe an den Benutzer zurückgeben.

.. seealso::
   * `Jupyter celebrates 20 years
     <https://data.berkeley.edu/news/project-jupyter-celebrates-20-years-fernando-perez-reflects-how-it-started-open-sciences>`_

Jupyter-Infrastruktur
---------------------

Eine Plattform für die oben genannten Use Cases erfordert eine umfangreiche
Infrastruktur, die nicht nur die Bereitstellung der Kernel sowie die
Parametrisierung, Zeitsteuerung und Parallelisierung von Notebooks erlaubt,
sondern darüberhinaus auch die gleichmäßige Bereitstellung der Ressourcen.

Mit diesem Tutorial wird eine Plattform bereitgestellt, die über Jupyter
Notebooks hinaus schnelle, flexible und umfassende Datenanalysen ermöglicht.
Aktuell gehen wir jedoch noch nicht darauf ein, wie sie sich um *Streaming
Pipelines* und *Domain Driven Data Stores* erweitern lässt.

Die Beispiele des Jupyter-Tutorials könnt ihr jedoch auch lokal erstellen und
ausführen.
