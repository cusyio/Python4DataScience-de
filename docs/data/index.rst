Daten lesen, speichern und bereitstellen
========================================

Einen Überblick über öffentliche Repositories mit Forschungsdaten erhaltet ihr
z.B. in:

* `Registry of research data repositories (re3data) <https://www.re3data.org/>`_
* `Awesome Public Datasets
  <https://github.com/awesomedata/awesome-public-datasets>`_
* `Public APIs <https://github.com/public-apis/public-apis>`_
* `Machine learning datasets <https://www.datasetlist.com/>`_
* `Roboflow Computer Vision Datasets <https://public.roboflow.com/>`_
* `DBpedia <https://wiki.dbpedia.org/>`_
* `World Health Data Platform/Global Health Observatory
  <https://www.who.int/data/gho/>`_
* `UNICEF Data <https://data.unicef.org/>`_
* `World Bank Open Data <https://data.worldbank.org/>`_
* `EU Open Data Portal Data <>http://open-data.europa.eu/en/data/`_
* `US Census Bureau <https://www.census.gov/data.html>`_
* `data.gov <https://www.data.gov/>`_
* `Google Dataset Search <https://datasetsearch.research.google.com/>`_
* `Google Public Data Search <https://www.google.com/publicdata/directory>`_
* `Registry of Open Data on AWS <https://registry.opendata.aws/>`_
* `Yelp Open Dataset <https://www.yelp.com/dataset>`_
* `Kaggle Datasets <https://www.kaggle.com/datasets>`_
* `OpenDataMonitor
  <https://opendatamonitor.eu/frontend/web/index.php?r=dashboard%2Findex>`_
* `Open Data Impact Map <https://opendataimpactmap.org/>`_
* `CKAN <https://ckan.org/>`_
* `UC Irvine Machine Learning Repository
  <https://archive.ics.uci.edu/ml/index.php>`_
* `Hugging Face Datasets <https://github.com/huggingface/datasets>`_
* `Dataverse Project <https://dataverse.org/>`_
* `Open Data Kit <https://opendatakit.org/>`_
* `LODUM University of Münster‘s Open Data initiative
  <https://www.uni-muenster.de/LODUM/>`_
* `freeCodeCamp open-data <https://github.com/freeCodeCamp/open-data>`_
* `Reddit Datasets Community <https://www.reddit.com/r/datasets/>`_

Neben spezifischen Python-Bibliotheken zum Zugriff auf :ref:`entfernte
Speichermedien </data/overview.rst#entfernte-speichermedien>` und
:ref:`/data/overview.rst#geodaten` stellen wir Euch
:doc:`serialisation-formats/index` und drei Werkzeuge genauer vor:

* :doc:`requests/index`
* :doc:`beautifulsoup`
* :doc:`intake/index`

.. seealso::
    `pandas I/O API <https://pandas.pydata.org/docs/user_guide/io.html>`_
        Die pandas I/O API ist eine Sammlung von ``reader``-Funktionen, die ein
        pandas-Objekt zurückgeben. Meist stehen auch entsprechende
        ``write``-Methoden zur Verfügung.
    `Scrapy <https://scrapy.org/>`_
        Framework zum Extrahieren von Daten aus Websites als JSON-, CSV- oder
        XML-Dateien.
    `Pattern <https://github.com/clips/pattern>`_
        Python-Modul zum Data Mining, Verarbeitung natürlicher Sprache, ML und
        Netzwerkanalyse
    `Web Scraping Reference <https://blog.hartleybrody.com/web-scraping-cheat-sheet/#javascript-heavy-websites>`_
        Übersicht zu Web Scraping mit Python

Zum Speichern von relationalen Daten, Python-Objekten und Geodaten stellen wir
Euch :doc:`postgresql/index`, :doc:`postgresql/sqlalchemy` und
:doc:`postgresql/postgis/index` vor.

Mit :doc:`fastapi/index` zeigen wir Euch eine Möglichkeit, Daten über eine
REST-Server bereitzustellen.

Mit :doc:`DVC <../productive/dvc/index>` stellen wir Euch ein Werkzeug vor, das
Euch Datenprovenienz erlaubt, d.h. die Herkunft und den Entstehungsweg von Daten
nachvollziehen zu können.

Schließlich lernt Ihr im nächsten Kapitel einige Good Practices und hilfreiche
Python-Pakete zum :doc:`Bereinigen und Validieren von Daten
<../clean-prep/index>` kennen.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    serialisation-formats/index
    requests/index
    beautifulsoup
    intake/index
    postgresql/index
    nosql/index
    fastapi/index
    glossary
