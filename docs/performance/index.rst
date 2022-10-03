Performance
===========

Messungen
---------

Wenn ihr aber erst einmal mit eurem Code gearbeitet habt, kann es nützlich sein,
die Effizienz genauer zu untersuchen. Hierfür kann der :doc:`ipython-profiler`
oder :doc:`scalene` genutzt werden.

.. seealso::
    * `airspeed velocity (asv) <https://asv.readthedocs.io/en/stable/>`_ ist ein
      Werkzeug zum Benchmarking von Python-Paketen während ihrer Lebensdauer.
      Laufzeit, Speicherverbrauch und sogar benutzerdefinierte Werte können
      aufgezeichnet und in einem interaktiven Web-Frontend angezeigt werden.
    * `Python Speed Center <https://speed.python.org/>`_
    * `Tracing the Python GIL
      <https://www.maartenbreddels.com/perf/jupyter/python/tracing/gil/2021/01/14/Tracing-the-Python-GIL.html>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ipython-profiler.ipynb
    scalene.ipynb

Anti-Patterns
-------------

Mit :doc:`perflint` lassen sich einige der häufigsten Performance-Anti-Patterns
in Python auffinden.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    perflint

.. seealso::
   * `Effective Python <https://effectivepython.com>`_

Optimierungen
-------------

Faster Cpython
~~~~~~~~~~~~~~

Auf der PyCon US im Mai 2021 stellte Guido van Rossum mit `Faster CPython
<https://github.com/faster-cpython>`_ ein Projekt vor, das die Geschwindigkeit
von Python 3.11 verdoppeln soll. Die Zusammenarbeit mit den anderen
Python-Kernentwicklern ist in `PEP 659 – Specializing Adaptive Interpreter
<https://peps.python.org/pep-0659/>`_ geregelt. Zudem gibt es einen offenen
`Issue Tracker <https://github.com/faster-cpython/ideas/issues>`_ und diverse
`Werkzeuge zum Sammeln von Bytecode-Statistiken
<https://github.com/faster-cpython/tools>`_. Von den Änderungen profitieren
dürfte vor allem CPU-intensiver Python-Code; bereits in C geschriebener Code,
I/O-lastige Prozesse und Multithreading-Code dürften hingegen kaum profitieren.

.. seealso::
    * `Faster CPython <https://faster-cpython.readthedocs.io/>`__

Cython
~~~~~~

Bei intensiven numerischen Operationen kann Python sehr langsam sein, auch wenn
ihr alle Anti-Patterns vermieden und :doc:`Vektorisierungen mit NumPy
<../workspace/numpy/vectorisation>` genutzt habt. Dann kann das Übersetzen von
Code in `Cython <https://cython.org>`_ hilfreich sein. Ein Beispiel hierfür
findet ihr in
:ref:`/workspace/pandas/apply.ipynb#optimieren-von-apply-mit-cython`. Leider
muss der Code jedoch häufig umstrukturiert werden und nimmt dadurch an
Komplexität zu. Auch werden explizite Type Annotations umständlich.

.. seealso::
    * `Cython Tutorials
      <https://cython.readthedocs.io/en/latest/src/tutorial/>`_

Numba
~~~~~

`Numba <http://numba.pydata.org/>`_ ist ein JIT-Compiler, der vor allem
wissenschaftlichen Python- und NumPy-Code in schnellen Maschinencode
übersetzt.

Nebenläufigkeit
~~~~~~~~~~~~~~~

Anhand von drei Beispielen zu :doc:`Threading <threading-example>`,
:doc:`Multiprocessing <multiprocessing>` und :doc:`Async <asyncio-example>`
werden die Regeln und Best Practices bei der Nutzung von :doc:`Nebenläufigkeit
in Python <concurrency>` veranschaulicht.

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
