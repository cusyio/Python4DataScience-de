.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

``tprof``
=========

`tprof <https://github.com/adamchainz/tprof>`_ misst ab Python 3.12 die Zeit,
die beim Ausführen eines Moduls in bestimmten Funktionen verbracht wird. Im
Gegensatz zu anderen Profilern verfolgt es nur die angegebenen Funktionen mit
:mod:`sys.monitoring`, wodurch man sich das Filtern sparen kann.

``tprof`` unterstützt die Verwendung als Befehlszeilenprogramm und mit einer
Python-Schnittstelle:

:samp:`uv run tprof -t {MODULE}:{FUNCTION} (-m {MODULE} | {PATH/TO/SCRIPT})`
    Angenommen, ihr habt festgestellt, dass die Erstellung von
    :class:`pathlib.Path`-Objekten im :mod:`main`-Modul euren Code verlangsamt.
    So könnt ihr dies mit ``tprof`` messen:

    .. code-block:: console

       $ uv run tprof -t pathlib:Path.open  -m main
       🎯 tprof results:
        function            calls total mean ± σ  min … max
        pathlib:Path.open()     1  93μs 93μs     93μs … 93μs

    Mit der ``-x``-Option könnt ihr auch zwei Funktionen miteinander
    vergleichen:

    .. code-block:: console

       $ uv run tprof -x -t old -m main -t new -m main
       🎯 tprof results:
        function   calls total mean ± σ  min … max  delta
        main:old()     1  41μs 41μs     41μs … 41μs -
        main:new()     1  20μs 20μs     20μs … 20μs -50.67%

``tprof(*targets, label: str | None = None, compare: bool = False)``
    verwendet diesen Code als :doc:`Kontextmanager
    <python-basics:control-flow/with>` in eurem Code, um ein Profil in einem
    bestimmten Block zu erstellen. Der Bericht wird jedes Mal ausgegeben,
    wenn der Block durchlaufen wurde.

    ``*targets``
        sind aufrufbare Elemente zum Profiling oder Referenzen zu Elementen, die
        mit :func:`pkgutil.resolve_name` aufgelöst werden.
    ``label``
        ist eine optionale Zeichenfolge, die als Kopfzeile dem Bericht
        hinzugefügt werden kann.
    ``compare``
        auf ``True`` gesetzt, wird der Vergleichsmodus aktiviert.

    Beispiel:

    .. code-block:: Python

       from pathlib import Path

       from tprof import tprof

       with tprof(Path.open):
           p = Path("docs", "save-data", "myfile.txt")
           f = p.open()

    .. code-block:: console

       $ uv run python main.py
       🎯 tprof results:
        function            calls total mean ± σ  min … max
        pathlib:Path.open()     1  82μs 82μs     82μs … 82μs
