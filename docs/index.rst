.. SPDX-FileCopyrightText: 2019 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

=======================
Python für Data Science
=======================

Dies ist ein Tutorium über Data Science mit Python. Das wirft sofort die Frage
auf: Was ist Data Science? Der Begriff ist mittlerweile allgegenwärtig, aber es
gibt keine einheitliche Definition. Manche halten den Begriff sogar für
überflüssig, denn welche Wissenschaft hat nicht mit Daten zu tun? Dennoch
scheint mir, dass Data Science mehr als nur ein Hype ist: Wissenschaftliche
Daten werden immer umfangreicher und lassen sich mit herkömmlichen
mathematischen und statistischen Methoden allein oft nicht mehr adäquat
erschließen – zusätzliche Hacking-Fähigkeiten sind gefragt. Es handelt sich
jedoch nicht um ein neues Wissensgebiet, das ihr erlernen müsst, sondern um eine
Reihe von Fähigkeiten, die ihr in eurem Bereich anwenden könnt. Ob ihr nun
astronomische Objekte oder Maschinen analysiert, Börsenkurse prognostiziert oder
in anderen Bereichen mit Daten arbeitet, das Ziel dieses Tutorials ist es, euch
in die Lage zu versetzen, Aufgaben in eurem Bereich programmatisch zu lösen.

Dieses Tutorial ist nicht als Einführung in Python oder in die Programmierung im
Allgemeinen gedacht; dafür gibt es das :doc:`python-basics:index`-Tutorial.
Stattdessen soll es den Python Data Science Stack – Bibliotheken wie
:doc:`/workspace/ipython/index`, :doc:`/workspace/numpy/index`,
:doc:`/workspace/pandas/index`, und verwandte Tools – vorstellen, damit ihr
anschließend eure Daten effektiv analysieren könnt. Darüberhinaus gibt es von
uns noch das `Jupyter Tutorial
<https://jupyter-tutorial.readthedocs.io/de/latest/>`_ und das `PyViz Tutorial
<https://pyviz-tutorial.readthedocs.io/de/latest/index.html>`_ sowie im `cusy
Design System <https://www.cusy.design/de/latest/index.html>`_ eine Anleitung
zur `Datenvisualisierung <https://www.cusy.design/de/latest/viz/index.html>`_.

Alle Tutorials dienen als Seminarunterlagen für unsere aufeinander abgestimmten
Trainings:

+---------------+--------------------------------------------------------------+
| Dauer         | Titel                                                        |
+===============+==============================================================+
| 3 Tage        | `Einführung in Python`_                                      |
+---------------+--------------------------------------------------------------+
| 2 Tage        | `Fortgeschrittenes Python`_                                  |
+---------------+--------------------------------------------------------------+
| 2 Tage        | `Entwurfsmuster in Python`_                                  |
+---------------+--------------------------------------------------------------+
| 2 Tage        | `Effizient Testen mit Python`_                               |
+---------------+--------------------------------------------------------------+
| 1 Tag         | `Software-Dokumentation mit Sphinx`_                         |
+---------------+--------------------------------------------------------------+
| 2 Tage        | `Technisches Schreiben`_                                     |
+---------------+--------------------------------------------------------------+
| 3 Tage        | `Jupyter-Notebooks für effiziente Data-Science-Workflows`_   |
+---------------+--------------------------------------------------------------+
| 2 Tage        | `Numerische Berechnungen mit NumPy`_                         |
+---------------+--------------------------------------------------------------+
| 2 Tage        | `Daten analysieren mit pandas`_                              |
+---------------+--------------------------------------------------------------+
| 3 Tage        | `Daten lesen, schreiben und bereitstellen mit Python`_       |
+---------------+--------------------------------------------------------------+
| 2 Tage        | `Daten bereinigen und validieren mit Python`_                |
+---------------+--------------------------------------------------------------+
| 5 Tage        | `Daten visualisieren mit Python`_                            |
+---------------+--------------------------------------------------------------+
| 1 Tag         | `Datenvisualisierungen gestalten`_                           |
+---------------+--------------------------------------------------------------+
| 2 Tage        | `Dashboards erstellen`_                                      |
+---------------+--------------------------------------------------------------+
| 3 Tage        | `Code und Daten versioniert und reproduzierbar speichern`_   |
+---------------+--------------------------------------------------------------+
| Abonnement    | `Neues aus Python für Data-Science`_                         |
| à 2 h im      |                                                              |
| Quartal       |                                                              |
+---------------+--------------------------------------------------------------+

.. _`Einführung in Python`:
   https://cusy.io/de/unsere-schulungsangebote/einfuehrung-in-python
.. _`Fortgeschrittenes Python`:
   https://cusy.io/de/unsere-schulungsangebote/fortgeschrittenes-python
.. _`Entwurfsmuster in Python`:
   https://cusy.io/de/unsere-schulungsangebote/entwurfsmuster-in-python
.. _`Effizient Testen mit Python`:
   https://cusy.io/de/unsere-schulungsangebote/effizient-testen-mit-python
.. _`Software-Dokumentation mit Sphinx`:
   https://cusy.io/de/unsere-schulungsangebote/software-dokumentation-mit-sphinx
.. _`Technisches Schreiben`:
   https://cusy.io/de/unsere-schulungsangebote/technisches-schreiben
.. _`Jupyter-Notebooks für effiziente Data-Science-Workflows`:
   https://cusy.io/de/unsere-schulungsangebote/jupyter-notebooks-fuer-effiziente-data-science-workflows
.. _`Numerische Berechnungen mit NumPy`:
   https://cusy.io/de/unsere-schulungsangebote/numerische-berechnungen-mit-numpy
.. _`Daten analysieren mit pandas`:
   https://cusy.io/de/unsere-schulungsangebote/daten-analysieren-mit-pandas
.. _`Daten lesen, schreiben und bereitstellen mit Python`:
   https://cusy.io/de/unsere-schulungsangebote/daten-lesen-schreiben-und-bereitstellen-mit-python
.. _`Daten bereinigen und validieren mit Python`:
   https://cusy.io/de/unsere-schulungsangebote/daten-bereinigen-und-validieren-mit-python
.. _`Daten visualisieren mit Python`:
   https://cusy.io/de/unsere-schulungsangebote/daten-visualisieren-mit-python
.. _`Datenvisualisierungen gestalten`:
   https://cusy.io/de/unsere-schulungsangebote/datenvisualisierungen-gestalten
.. _`Dashboards erstellen`:
   https://cusy.io/de/unsere-schulungsangebote/dashboards-erstellen
.. _`Code und Daten versioniert und reproduzierbar speichern`:
   https://cusy.io/de/unsere-schulungsangebote/code-und-daten-versioniert-und-reproduzierbar-speichern
.. _`Neues aus Python für Data-Science`:
   https://cusy.io/de/unsere-schulungsangebote/neues-aus-python-fuer-data-science

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    intro
    workspace/index
    data-processing/index
    clean-prep/index
    viz/index
    performance/index
    productive/index
    web/index
    genindex

.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
