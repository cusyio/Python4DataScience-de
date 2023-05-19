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
<https://zenodo.org/>`_- als auch das `figshare
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
     <https://zenodo.org/record/2842910>`_
   * `Recognizing the value of software: a software citation guide
     <https://f1000research.com/articles/9-1257/v2>`_
   * Stephan Druskat, Radovan Bast, Neil Chue Hong, Alexander Konovalov, Andrew
     Rowley, Raniere Silva: `A standard format for CITATION files
     <https://www.software.ac.uk/blog/2017-12-12-standard-format-citation-files>`_
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


Erstellen eines DOI mit Zenodo
------------------------------

`Zenodo <https://zenodo.org/>`_ ermöglicht die Archivierung von Software und die
Bereitstellung eines DOI für diese Software. Im Folgenden werde ich am Beispiel
des Jupyter-Tutorials zeigen, welche Schritte hierzu erforderlich sind:

#. Wenn ihr noch keinen `Account für Zenodo <https://zenodo.org/signup/>`_
   habt, erstellt einen, bevorzugt mit GitHub.

#. Nun wählt das Repository aus, das ihr archivieren wollt:

   .. figure:: zenodo-github.png
      :alt: Repositories für Zenodo aktivieren

#. Überprüft, ob Zenodo einen Webhook in eurem Repository für das
   *Releases*-Event erstellt hat:

   .. figure:: zenodo-webhook.png
      :alt: Zenodo Webhook

#. Erstellt ein neues Release:

   .. figure:: github-release.png
      :alt: Github Release

#. Überprüft, ob der DOI korrekt erstellt wurde:

   .. figure:: zenodo-release.png
      :alt: Zenodo Release

#. Schließlich könnt ihr den Badge in der README-Datei eurer Software einbinden:

   Markdown:
    .. code-block:: md

        [![DOI](https://zenodo.org/badge/307380211.svg)](https://zenodo.org/badge/latestdoi/307380211)

   reStructedText:
    .. code-block:: rst

        .. image:: https://zenodo.org/badge/307380211.svg
           :target: https://zenodo.org/badge/latestdoi/307380211

Metadaten-Formate
-----------------

Die `FORCE11 <https://www.force11.org/group/software-citation-working-group>`_
-Arbeitsgruppe hat ein Paper veröffentlicht, in denen Prinzipien des
wissenschaftlichen Software-zitierens dargelegt werden: Arfon Smith, Daniel
Katz, Kyle Niemeyer: `FORCE11 Software Citation Working Group
<https://doi.org/10.7717/peerj-cs.86>`_, 2016. Dabei kristallisieren sich
aktuell zwei Projekte für strukturierte Metadaten heraus:

.. _codemeta:

CodeMeta
~~~~~~~~

`CodeMeta <https://codemeta.github.io/>`_ ist ein Austauschschema für allgemeine
Software-Metadaten und Referenzimplementierung für JSON for Linking Data
(`JSON-LD <https://json-ld.org/>`_).

Dabei wird eine ``codemeta.json``-Datei im Stammverzeichnis des
Software-Repository erwartet. Die Datei kann :abbr:`z.B. (zum Beispiel)` so
aussehen:

.. code-block:: javascript

    {
        "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
        "@type": "SoftwareSourceCode",
        "author": [{
            "@type": "Person",
            "givenName": "Stephan",
            "familyName": "Druskat",
            "@id": "http://orcid.org/0000-0003-4925-7248"
        }],
        "name": "My Research Tool",
        "softwareVersion": "2.0",
        "identifier": "https://doi.org/10.5281/zenodo.1234",
        "datePublished": "2017-12-18",
        "codeRepository": "https://github.com/research-software/my-research-tool"
    }

.. seealso::
    * `CodeMeta generator <https://codemeta.github.io/codemeta-generator/>`_
    * `Codemeta Terms <https://codemeta.github.io/terms/>`_
    * `GitHub Repository
      <https://github.com/codemeta/codemeta-generator/>`_

.. _cff:

Citation File Format
~~~~~~~~~~~~~~~~~~~~

`Citation File Format <https://citation-file-format.github.io/>`_ ist ein Schema
für Software-Citation-Metadaten in maschinenlesbarem
:doc:`/data-processing/serialisation-formats/yaml/index`-Format. Dabei sollte
eine Datei ``CITATION.cff`` im Stammverzeichnis des Software-Repository
abgelegt werden. Der Inhalt der Datei kann :abbr:`z.B. (zum Beispiel)` so
aussehen:

.. code-block:: yaml

    cff-version: "1.1.0"
    message: "If you use this tutorial, please cite it as below."
    authors:
      -
        family-names: Schiele
        given-names: Veit
        orcid: "https://orcid.org/https://orcid.org/0000-0002-2448-8958"
    identifiers:
      -
        type: doi
        value: "10.5281/zenodo.4147287"
    keywords:
      - "data-science"
      - jupyter
      - "jupyter-notebooks"
      - "jupyter-kernels"
      - ipython
      - pandas
      - spack
      - pipenv
      - ipywidgets
      - "ipython-widget"
      - dvc
    title: "Jupyter tutorial"
    version: "0.8.0"
    date-released: 2020-10-08
    license: "BSD-3-Clause"
    repository-code: "https://github.com/veit/jupyter-tutorial"

Ihr könnt einfach das obige Beispiel anpassen um eure eigene
``CITATION.cff``-Datei zu erzeugen oder die Website `cffinit
<https://citation-file-format.github.io/cff-initializer-javascript/>`_
verwenden.

Mit `cff-validator <https://github.com/marketplace/actions/cff-validator>`_
steht euch eine GitHub-Action zur Verfügung, die ``CITATION.cff``-Dateien mit
dem R-Paket ``V8`` überprüft.

Es gibt auch einige Tools zum Workflow von :ref:`CITATION.cff <cff>`-Dateien:

* `cff-converter-python
  <https://github.com/citation-file-format/cff-converter-python>`_ konvertiert
  ``CITATION.cff``-Dateien in BibTeX, RIS, :ref:`codemeta`- und andere
  Dateiformate
* `doi2cff <https://github.com/citation-file-format/doi2cff>`_ erstellt eine
  ``CITATION.cff``-Datei aus einem Zenodo DOI

Auch GitHub bietet einen Service um die Informationen aus der
``CITATION.cff``-Datei eures GitHub-Repository im APA- und BibTex-Format zu
kopieren.

.. figure:: github-cite.png
   :alt: Popup auf der Zielseite eines GitHub-Repositorys mit der Möglichkeit,
         ADA- und BibTex-Formate zu exportieren.

.. seealso::
   * `GitHub Docs: About CITATION files
     <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files>`_

Wenn ihr einen DOI mit Zenodo registriert, wird die ``CITATION.cff``-Datei aus
dem GitHub-Repository ebenfalls verwendet. Auch `Zotero
<https://www.zotero.org/>`_ interpretiert die :ref:`cff`-Datei in
GitHub-Repositories; Zotero kann jedoch auch ohne :ref:`cff`-Datei
Metainformationen des Repository, wie Unternehmen, Programmiersprache
:abbr:`etc. (et cetera)`, übernehmen.

Git2PROV
--------

`Git2PROV <https://github.com/IDLabResearch/Git2PROV>`_ generiert PROV-Daten
aus den Informationen eines Git-Repository.

Auf der Kommandozeile kann die Konvertierung einfach ausgeführt werden mit:

.. code-block:: console

    $ git2prov git_url [serialization]

Zum Beispiel:

.. code-block:: console

    $ git2prov git@github.com:veit/jupyter-tutorial.git PROV-JSON

Insgesamt stehen die folgenden Serialisierungsformate zur Verfügung:

* ``PROV-N``
* ``PROV-JSON``
* ``PROV-O``
* ``PROV-XML``

Alternativ stellt Git2PROV auch einen Web-Server bereit mit:

.. code-block:: console

    $ git2prov-server [port]

.. seealso::
   * `Git2PROV: Exposing Version Control System Content as W3C PROV
     <http://ceur-ws.org/Vol-1035/iswc2013_demo_32.pdf>`_
   * `GitHub-Repository <https://github.com/IDLabResearch/Git2PROV>`_

hermes
------

`hermes <https://project.software-metadata.pub>`_ vereinfacht die Publikation
von Forschungssoftware, indem kontinuierlich in :ref:`cff`, :ref:`codemeta` und
:doc:`../git/index` vorhandene Metadaten abegrufen werden. Anschließend werden
die Metadaten auch für `InvenioRDM
<https://invenio-software.org/products/rdm/>`_ und `Dataverse
<https://dataverse.org/>`_ passend zusammengestellt. Schließlich werden auch
:ref:`CITATION.cff <cff>` und :ref:`codemeta.json <codemeta>` für die
Publikationsrepositories aktualisiert. Eine examplarische GitHub-Action findet
ihr in `TEMPLATE_hermes_github_to_zenodo.yml
<https://github.com/hermes-hmc/ci-templates/blob/main/TEMPLATE_hermes_github_to_zenodo.yml>`_.

.. seealso::
   * `GitHub <https://github.com/hermes-hmc/workflow>`_
