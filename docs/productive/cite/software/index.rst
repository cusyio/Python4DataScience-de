.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Software zitieren
=================

James Howison und Julia Bullard führten in ihrem 2016 veröffentlichten Artikel
`Software in the scientific literature <https://doi.org/10.1002/asi.23538>`_
folgende Beispiele in absteigender Reputation auf:

#. zitieren von Veröffentlichungen, die die jeweilige Software beschreiben
#. zitieren von Bedienungsanleitungen
#. zitieren der Software-Projekt-Website
#. Link auf eine Software-Projekt-Website
#. erwähnen des Software-Namens

Die Situation bleibt für die Autor*innen von Software dennoch unbefriedigend,
zumal wenn sie sich von den Autor*innen der Software-Beschreibung unterscheiden.
Umgekehrt ist Forschungssoftware leider auch nicht immer gut geeignet um zitiert
zu werden. So werden andere eure Software kaum direkt zitieren können, wenn ihr
ihnen die Software als Anhang von E-Mails schickt. Auch ein Download-Link ist
hier noch nicht wirklich zielführend. Besser stellt ihr einen `Persistent
Identifier (PID) <https://de.wikipedia.org/wiki/Persistent_Identifier>`_ bereit,
um die langfristige Verfügbarkeit eurer Software sicherzustellen. Sowohl `Zenodo
<https://zenodo.org/>`__- als auch das `figshare
<https://figshare.com/>`_-Repository akzeptieren Quellcode einschließlich
Binärdateien und stellen `Digital Object Identifier (DOI)
<https://de.wikipedia.org/wiki/Digital_Object_Identifier>`_ hierfür bereit.
Gleiches gilt für `CiteAs <https://citeas.org/>`_, mit dem sich
Zitierinformationen für Software abrufen lassen.

.. seealso::
   * `Should I cite? <https://mr-c.github.io/shouldacite/index.html>`_
   * `How to cite software “correctly”
     <https://cite.research-software.org/>`_
   * Daniel S. Katz: `Compact identifiers for software: The last missing link in
     user-oriented software citation?
     <https://danielskatzblog.wordpress.com/2018/02/06/compact-identifiers-for-software-the-last-missing-link-in-user-oriented-software-citation/>`_
   * `Neil Chue Hong: How to cite software: current best practice
     <https://zenodo.org/records/2842910>`_
   * `Recognizing the value of software: a software citation guide
     <https://f1000research.com/articles/9-1257/v2>`_
   * Stephan Druskat, Radovan Bast, Neil Chue Hong, Alexander Konovalov, Andrew
     Rowley, Raniere Silva: `A standard format for CITATION files
     <https://www.software.ac.uk/blog/standard-format-citation-files>`_
   * `Module-5-Open-Research-Software-and-Open-Source
     <https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source/blob/master/content_development/README.md/>`_
   * Software Heritage: `Save and reference research software
     <https://www.softwareheritage.org/save-and-reference-research-software/>`_
   * `Mining software metadata for 80 M projects and even more
     <https://www.softwareheritage.org/2019/05/28/mining-software-metadata-for-80-m-projects-and-even-more/>`_
   * `Extensions to schema.org to support structured, semantic, and executable
     documents <https://github.com/stencila/schema>`_
   * `Guide to Citation File Format schema
     <https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md>`_
   * `schema.json
     <https://github.com/citation-file-format/citation-file-format/blob/main/schema.json>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    doi

Metadaten-Formate
-----------------

Die `FORCE11 <https://force11.org/group/software-citation-working-group>`_
-Arbeitsgruppe hat ein Paper veröffentlicht, in denen Prinzipien des
wissenschaftlichen Software-zitierens dargelegt werden: Arfon Smith, Daniel
Katz, Kyle Niemeyer: `FORCE11 Software Citation Working Group
<https://peerj.com/articles/cs-86/>`_, 2016. Dabei kristallisieren sich aktuell
zwei Projekte für strukturierte Metadaten heraus:

:doc:`codemeta`
    ist ein Austauschschema für allgemeine Software-Metadaten und
    Referenzimplementierung für JSON for Linking Data
    (`JSON-LD <https://json-ld.org/>`_).
:doc:`cff`
    ist ein Schema für Software-Citation-Metadaten in maschinenlesbarem
    :doc:`/data-processing/serialisation-formats/yaml/index`-Format.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    codemeta
    cff

Tools
-----

:doc:`git2prov`
    generiert PROV-Daten aus den Informationen eines Git-Repository.
:doc:`hermes`
    vereinfacht die Publikation von Forschungssoftware, indem kontinuierlich
    in :doc:`cff`, :doc:`codemeta` und :doc:`Git <../../git/index>` vorhandene
    Metadaten abegrufen werden.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    git2prov
    hermes
