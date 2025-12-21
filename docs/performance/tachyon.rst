Tachyon
=======

Tachyon ist ein neuer statistischer Sampling-Profiler, der in Python 3.15 als
:mod:`profiling.sampling` hinzugefügt wurde. Dieser Profiler ermöglicht eine
leistungsstarke Analyse laufender Python-Prozesse mit geringem Overhead, ohne
dass Codeänderungen oder ein Neustart des Prozesses erforderlich sind.

Im Gegensatz zu deterministischen Profiler wie :mod:`profiling.tracing`, die
jeden Funktionsaufruf instrumentieren, erfasst :mod:`profiling.sampling`
regelmäßig Stack-Traces aus laufenden Prozessen.

Zu den wichtigsten Funktionen gehören:

Profiling ohne Overhead
    :mod:`profiling.sampling` fügt sich in jeden laufenden Python-Prozess ein,
    ohne dessen Leistung zu beeinträchtigen. Dies ist Ideal für die
    Fehlerbehebung in Produktiv-Umgebungen, wo eure Anwendung nicht neu
    gestartet oder verlangsamt werden darf.
Keine erforderlichen Codeänderungen
    Bestehende Anwendungen können ohne Neustart profiliert werden. Ihr müsst
    einfach anhand der PID den Profiler auf einen laufenden Prozess richten und
    mit der Datenerhebung beginnen.
Profiliert laufende Prozesse oder Module
    :samp:`attach`
        profiliert laufende Prozesse anhand der PID.
    :samp:`run -m {MODULE}`
        führt Module aus und profiliert sie.
Mehrere Profiling-Modi
    Ihr könnt auswählen, was gemessen werden soll:

    ``--mode wall``
        Standardwert, der die tatsächlich verstrichene Zeit misst einschließlich
        I/O, Netzwerkwartezeiten und Blockierungsvorgängen. Dies ist ideal
        geeignet um zu verstehen, wo euer Programm Zeit verbraucht,
        einschließlich der Wartezeiten auf externe Ressourcen.
    ``--mode cpu``
        misst nur die aktive CPU-Ausführungszeit, ohne I/O-Wartezeiten und
        Blockierungen. Verwendet diese Option, um CPU-gebundene Engpässe zu
        identifizieren und die Rechenleistung zu optimieren.
    ``--mode gil``
        misst die Zeit für das :abbr:`GIL (Global Interpreter Lock)` von Python.
        Verwendet diese Option, um zu ermitteln, welche Threads durch das GIL
        ausgebremst werden.
    ``--mode exception``
        erfasst nur Samples von Threads mit einer aktiven Ausnahme. Verwendet
        diese Option, um den Overhead beim Exception Handling zu analysieren.
    ``-a``
        profiliert alle Threads oder nur den Haupt-Thread, wodurch das
        Verständnis für des Verhalten von Multithread-Anwendungen wächst.

Mehrere Ausgabeformate
    Wählt die Visualisierung, die am besten zu Ihrem Workflow passt:

    ``--pstats``
        liefert detaillierte tabellarische Statistiken, kompatibel mit
        :mod:`pstats`. Es zeigt die Zeitmessung auf Funktionsebene mit direkten
        und kumulativen Stichproben an und ist am besten geeignet für
        detaillierte Analysen und die Integration mit vorhandenen
        Python-Profiling-Tools.
    ``--collapsed``
        erzeugt zusammengefasste Stack-Traces. Dieses Format wurde speziell für
        die Erstellung von `Flame Graphs
        <https://www.brendangregg.com/flamegraphs.html>`_ mit externen Tools wie
        `Brendan Greggs FlameGraph-Skripten
        <https://github.com/brendangregg/FlameGraph>`_ oder `Speedscope
        <https://jamie-wong.com/post/speedscope/>`_ entwickelt.
    ``--flamegraph``
        erzeugt einen eigenständigen interaktiven HTML-Flamegraph mit `D3.js
        <https://d3js.org/>`_, der sich direkt in Ihrem Browser für eine
        sofortige visuelle Analyse öffnet.
    ``--gecko``
        erzeugt ein Gecko-Profiler-Format, das mit `Firefox Profiler
        <https://profiler.firefox.com>`_ kompatibel ist. Die Ausgabe kann in
        Firefox Profiler hochgeladen werden, um eine erweiterte
        zeitachsenbasierte Analyse mit Funktionen wie Stapeldiagrammen, Markern
        und Netzwerkaktivitäten durchzuführen.
    ``--heatmap``
        erzeugt eine interaktive HTML-Heatmap-Visualisierung und erstellt eine
        Heatmap je Datei, die genau zeigen, wo Zeit auf Quellcodeebene
        verbraucht wird.

``--live``
    `top <https://man7.org/linux/man-pages/man1/top.1.html>`_-ähnliche
    Oberfläche, wodurch ihr die Leistung eurer Anwendung während der Ausführung
    mit interaktiver Sortierung und Filterung Überwachen könnt.
``--async-aware``
    Profilerstellung für :doc:`async/await-Code <asyncio-example>`, die euch
    anzeigt, welche Coroutinen Zeit verbrauchen. Weitere Optionen zeigen euch
    nur laufende Aufgaben oder alle Aufgaben einschließlich der wartenden an.
``--opcodes``
    sammelt Bytecode-Opcode-Informationen für das Profiling auf Befehlsebene und
    zeigt an, welche Bytecode-Befehle ausgeführt werden, einschließlich
    Spezialisierungen aus dem adaptiven Interpreter.

.. seealso::
   :mod:`profiling.sampling`
