Performance-Messung und Optimierung
===================================

Performance-Messung
-------------------

Wenn ihr aber erst einmal mit eurem Code gearbeitet habt, kann es nützlich sein,
die Effizienz genauer zu untersuchen. Hierfür kann der :doc:`ipython-profiler`
oder :doc:`scalene` genutzt werden.

.. seealso::
   `airspeed velocity (asv) <https://asv.readthedocs.io/en/stable/>`_
    ist ein Werkzeug zum Benchmarking von Python-Paketen während ihrer
    Lebensdauer. Laufzeit, Speicherverbrauch und sogar benutzerdefinierte Werte
    können aufgezeichnet und in einem interaktiven Web-Frontend angezeigt
    werden.
   `perflint <https://github.com/tonybaloney/perflint>`_
    `pylint <https://pylint.org/>`_-Erweiterung für Performance-Anti-Patterns,
    u.a.:

    * W8101: Unnötige ``list()`` bei bereits iterierbarem Typ
    * W8102: Falsche Iterator-Methode für dict
    * W8201: Loop-invariant-statement
    * W8202: Globale Namensverwendung in einer Schleife
      (loop-invariant-global-usage)
    * R8203: Try-except-Blöcke haben einen erheblichen Overhead; vermeidet
      daher deren Verwendung innerhalb einer Schleife (loop-try-except-usage)
    * W8204: Looped-Slicing von Bytes-Objekten ist ineffizient; Verwendet
      stattdessen ``memoryview()`` (memoryview-over-bytes)
    * W8205: Der direkte Import des Namens ``%s`` ist in dieser Schleife
      effizienter (dotted-import-in-loop)

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ipython-profiler.ipynb
    scalene.ipynb

Parallele Programmierung
------------------------

Anhand von drei Beispielen zu :doc:`Threading <threading-example>`,
:doc:`Multiprocessing <multiprocessing>` und :doc:`Async
<asyncio-example>` werden die Regeln und Best Practices bei der Nutzung von
paralleler Programmierung in Python veranschaulicht.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    concurrency
    threading-example.ipynb
    multiprocessing.ipynb
    threading-forking-combined.ipynb
    asyncio-example.ipynb
    parallelise-pandas
    ipyparallel/index
    dask.ipynb

.. seealso::
    * `Faster CPython <https://faster-cpython.readthedocs.io/>`_
    * `Python Speed Center <https://speed.python.org/>`_
    * `Tracing the Python GIL <https://www.maartenbreddels.com/perf/jupyter/python/tracing/gil/2021/01/14/Tracing-the-Python-GIL.html>`_
