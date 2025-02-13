.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Daten zitieren
==============

DataCite Metadata Schema
------------------------

Die DataCite Metadata Working Group veröffentlichte 2019 die `DataCite Metadata
Schema <https://schema.datacite.org/meta/kernel-4.3/>`_ zum Veröffentlichen und
Zitieren von Forschungsdaten zusammen mit einer XSD (XML Schema Definition):
`metadata.xsd <https://schema.datacite.org/meta/kernel-4.3/metadata.xsd>`_.

Ein einfaches Datacite-Beispiel kann folgendermaßen aussehen:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <resource xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://datacite.org/schema/kernel-4" xsi:schemaLocation="http://datacite.org/schema/kernel-4 http://schema.datacite.org/meta/kernel-4.3/metadata.xsd">
      <identifier identifierType="DOI">10.5072/D3P26Q35R-Test</identifier>
      <creators>
        <creator>
          <creatorName nameType="Personal">Fosmire, Michael</creatorName>
          <givenName>Michael</givenName>
          <familyName>Fosmire</familyName>
        </creator>
        <creator>
          <creatorName nameType="Personal">Wertz, Ruth</creatorName>
          <givenName>Ruth</givenName>
          <familyName>Wertz</familyName>
        </creator>
        <creator>
          <creatorName nameType="Personal">Purzer, Senay</creatorName>
           <givenName>Senay</givenName>
          <familyName>Purzer</familyName>
        </creator>
      </creators>
      <titles>
        <title xml:lang="en">Critical Engineering Literacy Test (CELT)</title>
      </titles>
      <publisher xml:lang="en">Purdue University Research Repository (PURR)</publisher>
      <publicationYear>2013</publicationYear>
      <subjects>
        <subject xml:lang="en">Assessment</subject>
        <subject xml:lang="en">Information Literacy</subject>
        <subject xml:lang="en">Engineering</subject>
        <subject xml:lang="en">Undergraduate Students</subject>
        <subject xml:lang="en">CELT</subject>
        <subject xml:lang="en">Purdue University</subject>
      </subjects>
      <language>en</language>
      <resourceType resourceTypeGeneral="Dataset">Dataset</resourceType>
      <version>1.0</version>
      <descriptions>
        <description xml:lang="en" descriptionType="Abstract">
          We developed an instrument, Critical Engineering Literacy Test (CELT), which is a multiple choice instrument designed to measure undergraduate students’ scientific and information literacy skills. It requires students to first read a technical memo
          and, based on the memo’s arguments, answer eight multiple choice and six open-ended response questions. We collected data from 143 first-year engineering students and conducted an item analysis. The KR-20 reliability of the instrument was .39. Item
          difficulties ranged between .17 to .83. The results indicate low reliability index but acceptable levels of item difficulties and item discrimination indices. Students were most challenged when answering items measuring scientific and mathematical
          literacy (i.e., identifying incorrect information).
        </description>
      </descriptions>
    </resource>

W3C-PROV
--------

Die `PROV-Dokumentenfamilie der W3C-Arbeitsgruppe
<https://www.w3.org/TR/prov-overview/>`_ definiert verschiedene Aspekte, die
erforderlich sind, um Herkunftsinformationen interoperabel austauschen zu
können.


.. seealso::
   * Luc Moreau, Paul Groth: `Provenance: An Introduction to PROV
     <https://www.provbook.org/>`_
   * `Provenance storage and distribution <https://openprovenance.org/store/>`_
   * `ProvStore’s API documentation
     <https://openprovenance.org/store/help/api/>`_

Python prov
~~~~~~~~~~~

Mit `prov <https://prov.readthedocs.io/en/latest/>`_ steht eine
Python-Bibliothek zur Verfügung, die den Im- und Export des `PROV-Datenmodells
<https://www.w3.org/TR/prov-dm/>`_ in folgende Serialisierungsformate
unterstützt:

* `PROV-O (RDF) <https://www.w3.org/TR/2013/REC-prov-o-20130430/>`_
* `PROV-XML <https://www.w3.org/TR/2013/NOTE-prov-xml-20130430/>`_
* `PROV-JSON <https://www.w3.org/submissions/prov-json/>`_

Zudem können mit :doc:`pyviz:matplotlib/networkx` `MultiDiGraph
<https://networkx.org/documentation/stable/reference/classes/multidigraph.html>`_
PROV-Dokumente erstellt werden und umgekehrt. Schließlich können PROV-Dokumente
auch als Graphen in den Formaten PDF, PNG und SVG generiert werden.

.. seealso::
   * Dong Huynh: `A Short Tutorial for Prov Python
     <https://trungdong.github.io/prov-python-short-tutorial.html>`_
   * `PROV Tutorial.ipynb
     <https://nbviewer.org/github/trungdong/notebooks/blob/master/PROV%20Tutorial.ipynb>`_
