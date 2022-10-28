Daten lesen, speichern und bereitstellen
========================================

Einen Überblick zu öffentlichen Repositories mit Forschungsdaten erhaltet ihr
z.B. in :doc:`opendata`.

Neben spezifischen Python-Bibliotheken zum Zugriff auf
:doc:`/data-processing/remote-file-systems` und :doc:`/data-processing/geodata`
stellen wir euch :doc:`serialisation-formats/index` und drei Werkzeuge genauer
vor:

* :doc:`/data-processing/pandas-io`
* :doc:`/data-processing/requests/index`
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
euch :doc:`postgresql/index`, :doc:`postgresql/sqlalchemy` und
:doc:`postgresql/postgis/index` vor.

Als nächstes zeigen wir euch, wie ihr die Daten über ein :doc:`apis/index`
bereitstellt.

Mit :doc:`DVC <../productive/dvc/index>` stellen wir euch ein Werkzeug vor, das
euch Datenprovenienz erlaubt. Damit vollzieht ihr die Herkunft und den 
Entstehungsweg von Daten nach.

Im Anschluß lernt ihr im nächsten Kapitel noch einige Good Practices und 
hilfreiche Python-Pakete zum :doc:`Bereinigen und Validieren von Daten
<../clean-prep/index>` kennen.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    opendata
    pandas-io
    serialisation-formats/index
    intake/index
    requests/index
    remote-file-systems
    geodata
    postgresql/index
    nosql/index
    apis/index
    glossary
