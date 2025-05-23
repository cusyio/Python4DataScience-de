.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Pickle
======

Überblick
---------

+-----------------------+-------+-------------------------------------------------------+
| Unterstützung von     | +\-   | Pickle wird zum Speichern von Python-Objektstrukturen |
| Datenstrukturen       |       | wie ``list`` oder ``dict`` in einem Byte-Stream       |
|                       |       | verwendet. Im Gegensatz zu ``marshal`` werden bereits |
|                       |       | serialisierte Objekte getrackt, sodass spätere        |
|                       |       | Verweise nicht erneut serialisiertt werden. Auch      |
|                       |       | rekursive Objekte sind möglich.                       |
+-----------------------+-------+-------------------------------------------------------+
| Standardisierung      | ++    | Pickle ist definiert in den Python Enhancement        |
|                       |       | Proposals `307`_, `3154`_ und `574`_.                 |
+-----------------------+-------+-------------------------------------------------------+
| Schema IDL            | -\-   | Nein                                                  |
+-----------------------+-------+-------------------------------------------------------+
| Sprachunterstützung   | -\-   | Python-spezifisch                                     |
+-----------------------+-------+-------------------------------------------------------+
| Menschliche Lesbarkeit| +\-   | Pickle ist ein binäres Serialisierungsformat,         |
|                       |       | das jedoch einfach mit Python gelesen werden kann.    |
+-----------------------+-------+-------------------------------------------------------+
| Geschwindigkeit       | +\-   | Das Pickle-Format kann von Python meist schnell       |
|                       |       | serialisiert und deserialisiert werden; siehe jedoch  |
|                       |       | `Don’t pickle your data`_.                            |
+-----------------------+-------+-------------------------------------------------------+
| Dateigröße            | ++    | Kompaktes Binärformat, das jedoch noch weiter         |
|                       |       | komprimiert werden kann, s. `Data Compression         |
|                       |       | and Archiving                                         |
|                       |       | <https://docs.python.org/3/library/archiving.html>`_. |
+-----------------------+-------+-------------------------------------------------------+

.. seealso::

    `pickle – Python object serialization <https://docs.python.org/3/library/pickle.html>`_
        Dokumentation des ``pickle``-Moduls
    `shelve – Python object persistence <https://docs.python.org/3/library/shelve.html#module-shelve>`_
        Indizierte Datenbanken von ``pickle``-Objekten
    `Uwe Korn: The implications of pickling ML models <https://uwekorn.com/2021/04/26/implications-of-pickling-ml-models.html>`_
        Alternativen zu ``pickle`` für ML-Modelle
    `Ned Batchelder: Pickle’s nine flaws <https://nedbatchelder.com/blog/202006/pickles_nine_flaws.html>`_
        Nachteile von ``pickle`` und Alternativen

.. _`307`: https://peps.python.org/pep-0307/
.. _`3154`: https://peps.python.org/pep-3154/
.. _`574`: https://peps.python.org/pep-0574/
.. _`Don’t pickle your data`:
   https://www.benfrederickson.com/dont-pickle-your-data/

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    pickle-examples
