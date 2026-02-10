.. SPDX-FileCopyrightText: 2026 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Memray
======

Die Speichernutzung ist in Python-Projekten nur schwer zu kontrollieren, da die
Sprache nicht explizit deutlich macht, wo Speicher zugewiesen wird, Modulimporte
können den Verbrauch erheblich steigern, und es ist nur allzu leicht, eine
Datenstruktur zu erstellen, die versehentlich unbegrenzt wächst.
Data-Science-Projekte sind besonders anfällig für hohen Speicherverbrauch, da
sie meist viele große Abhängigkeiten wie :doc:`/workspace/numpy/index`
importieren, selbst wenn diese nur an wenigen Stellen verwendet werden.

`Memray <https://bloomberg.github.io/memray/>`_ hilft euch, die Speichernutzung
eures Programms zu verstehen, wobei nachverfolgt wird, wo während der
Programmausführung Speicher zugewiesen und freigegeben wird. Diese Daten können
dann auf verschiedene Weise dargestellt werden, :abbr:`u. a. (uter anderem)`
werden in `Flame Graphs <https://www.brendangregg.com/flamegraphs.html>`_ die
`Stacktraces <https://de.wikipedia.org/wiki/Stacktrace>`_ in einem Diagramm
zusammengefasst, wobei die Balkenbreite die Größe der Speicherzuweisung
darstellt.

Mit ``memray run`` kann jeder Python-Befehl profiliert werden. Für die meisten
Projekte empfiehlt sich, zunächst mit ``check`` die Funktion zu profilieren, die
euer Projekt lädt. Damit wird der Mindestaufwand überprüft, der zum Starten
eurer Anwendung erforderlich ist, :abbr:`z.B. (zum Beispiel)`:

.. code-block:: console

   $ uv run memray run src/items/__init__.py check
   Writing profile results into src/items/memray-__init__.py.72633.bin
   [memray] Successfully generated profile results.

   You can now generate reports from the stored allocation records.
   Some example commands to generate reports:

   /Users/veit/items/.venv/bin/python3 -m memray flamegraph src/items/memray-__init__.py.72633.bin

Der Befehl gibt die Meldung ``Successfully generated profile results.`` aus und
erstellt eine Datei :samp:`{PROCESS-ID}.bin`-Datei. Den *Flame Graph* können wir
dann erstellen mit:

.. code-block:: console

   $ uv run python -m memray flamegraph src/items/memray-__init__.py.72633.bin
   Wrote src/items/memray-flamegraph-__init__.py.72633.html

.. tip::
   In vielen Konsolen könnt ihr die beiden Befehle zusammenfassen mit ``&&``:

   .. code-block:: console

      $ uv run memray run src/items/__init__.py check && uv run python -m memray flamegraph src/items/memray-__init__.py.72633.bin

Das Ergebnis ist folgende HTML-Datei:

.. figure:: memray-flamegraph.png
   :alt: memray flamegraph report

   memray flamegraph report

Der Kopfbereich der Seite enthält einige Steuerelemente, :abbr: `u.a. (unter anderem)` zu

*Memory Graph*
    Anzeige des Speicherplatzes eines Prozesses im Arbeitsspeicher (`Resident
    set size <https://en.wikipedia.org/wiki/Resident_set_size>`_) und des
    `dynamischen Speichers
    <https://de.wikipedia.org/wiki/Dynamischer_Speicher>`_ (Heap Memory) über
    die Zeit
*Stats*
    Speicherstatistiken, in diesem Fall

    .. code-block:: text

        Command line: /Users/veit/items/.venv/bin/memray run src/items/api.py check
        Start time: Sun Feb 08 2026 12:12:27 GMT+0100 (Central European Standard Time)
        End time: Sun Feb 08 2026 12:12:27 GMT+0100 (Central European Standard Time)
        Duration: 0:00:00.068000
        Total number of allocations: 11142
        Total number of frames seen: 0
        Peak memory usage: 4.6 MB
        Python allocator: pymalloc

Darunter befindet sich der *Flame-Graph* als Eiszapfendiagramm mit den
Speicherzuweisungen über die Zeit, wobei der letzte Aufruf ganz unten steht. Die
Grafik zeigt die zu einem bestimmten Zeitpunkt ausgeführte Codezeile an wobei
die Breite proportional zur zugewiesenen Speichermenge ist; bewegt ihr die Maus
darüber, seht ihr weitere Details wie Dateiname, Zeilennummer, zugewiesener
Speicher und Anzahl der Zuweisungen.

.. tip::
   Mit :ref:`python-basics:pytest_memray` gibt es auch ein Plugin für
   :doc:`python-basics:test/pytest/index`, mit dem ihr überprüfen könnt, ob
   von euch festgelegte Obergrenzen für den Speicherverbrauch und Speicherlecks
   eingehalten werden.
