Daten lesen, speichern und bereitstellen
========================================

Einen Überblick über öffentliche Repositories mit Forschungsdaten erhaltet ihr
z.B. in :doc:`opendata`.

Neben spezifischen Python-Bibliotheken zum Zugriff auf :ref:`entfernte
Speichermedien </data-processing/overview.rst#entfernte-speichermedien>` und
:ref:`/data-processing/overview.rst#geodaten` stellen wir Euch
:doc:`serialisation-formats/index` und drei Werkzeuge genauer vor:

* :doc:`/data-processing/pandas-io`
* :doc:`/data-processing/requests/index`
* :doc:`/data-processing/serialisation-formats/xml-html/beautifulsoup`
* :doc:`/data-processing/intake/index`

.. seealso::
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

Als nächstes zeigen wir euch, wie ihr die Daten über ein :doc:`apis/index`
bereitstellen könnt.

Mit :doc:`DVC <../productive/dvc/index>` stellen wir Euch ein Werkzeug vor, das
Euch Datenprovenienz erlaubt, d.h. die Herkunft und den Entstehungsweg von Daten
nachvollziehen zu können.

Schließlich lernt ihr im nächsten Kapitel einige Good Practices und hilfreiche
Python-Pakete zum :doc:`Bereinigen und Validieren von Daten
<../clean-prep/index>` kennen.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    opendata
    overview
    pandas-io
    serialisation-formats/index
    requests/index
    intake/index
    postgresql/index
    nosql/index
    apis/index
    glossary
