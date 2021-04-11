Daten lesen, speichern und bereitstellen
========================================

Einen Überblick über öffentliche Repositories mit Forschungsdaten erhaltet ihr
z.B. in :doc:`opendata`.

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

Als nächstes zeigen wir Euch, wie Ihr mit :doc:`fastapi/index` oder
:doc:`grpc/index` Daten bereitstellen könnt.

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

    opendata
    serialisation-formats/index
    requests/index
    beautifulsoup
    intake/index
    postgresql/index
    nosql/index
    grpc/index
    fastapi/index
    glossary
