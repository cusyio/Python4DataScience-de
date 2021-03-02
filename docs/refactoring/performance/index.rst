Performance-Messung und Optimierung
===================================

Profiling
---------

Bei der Entwicklung von Code kann es häufig zu Kompromissen zwischen
verschiedenen Implementierungen kommen. Zu Beginn der Entwicklung eines
Algorithmus ist es jedoch meist kontraproduktiv, sich um die Effizienz des Codes
zu kümmern.

    «We should forget about small efficiencies, say about 97% of the time:
    premature optimization is the root of all evil. Yet we should not pass up
    our opportunities in that critical 3%.»[#]_

.. [#] Donald Knuth in Computer Programming as an Art (1974)

Wenn ihr aber erst einmal mit eurem Code gearbeitet habt, kann es nützlich sein,
die Effizienz genauer zu untersuchen. Hierfür kann der :doc:`ipython-profiler`
oder :doc:`scalene` genutzt werden.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ipython-profiler.ipynb
    scalene

Parallele Programmierung
------------------------

Anhand von drei Beispielen zu :doc:`Threading <threading-example>`,
:doc:`Multiprocessing <multiprocessing>` und :doc:`Async
<async-example>` werden die Regeln und Best Practices bei der Nutzung von
paralleler Programmierung in Python veranschaulicht.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    introduction.ipynb
    threading-example.ipynb
    multiprocessing.ipynb
    threading-forking-combined.ipynb
    async-example.ipynb
    ipyparallel/index
    parallelise-pandas

.. seealso::
    * `Faster CPython <https://faster-cpython.readthedocs.io/>`_
    * `Python Speed Center <https://speed.python.org/>`_
    * `Tracing the Python GIL <https://www.maartenbreddels.com/perf/jupyter/python/tracing/gil/2021/01/14/Tracing-the-Python-GIL.html>`_
