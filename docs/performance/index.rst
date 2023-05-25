Performance
===========

Mit Python lässt sich zwar schnell Code schreiben und testen, da es eine
interpretierte Sprache ist, die dynamisch typisiert. Dies sind jedoch auch die
Gründe, die sie bei der wiederholten Ausführung von einfachen Aufgaben,
:abbr:`z.B. (zum Beispiel)` in Schleifen, langsam macht.

Bei der Entwicklung von Code kann es häufig zu Kompromissen zwischen
verschiedenen Implementierungen kommen. Zu Beginn der Entwicklung eines
Algorithmus ist es jedoch meist kontraproduktiv, sich um die Effizienz des Codes
zu kümmern.

    »Wir sollten kleine Effizienzsteigerungen in sagen wir etwa 97 % der Zeit,
    vergessen: Vorzeitige Optimierung ist die Wurzel allen Übels. Dennoch
    sollten wir unsere Chancen in diesen kritischen 3 % nicht verpassen.«[#]_

.. [#] Donald Knuth, Begründer des `Literate programming
       <http://www.literateprogramming.com/>`_, in Computer Programming as an
       Art (1974)

k-Means-Beispiel
----------------

Im Folgenden zeige ich Beispiele für den `k-Means-Algorithmus
<https://de.wikipedia.org/wiki/K-Means-Algorithmus>`_, um aus einer Menge von
Objekten eine vorher bekannte Anzahl von Gruppen zu bilden. Dies lässt sich in
den folgenden drei Schritten ereichen:

#. Wähle die ersten :samp:`k` Elemente als Clusterzentren
#. Weise jedes neue Element dem Cluster zu, bei dem sich die Varianz am
   wenigsten erhöht
#. Aktualisiere das Clusterzentrum

Die Schritte 2 und 3 werden dabei so lange wiederholt, bis sich die Zuordnungen
nicht mehr ändern.

Eine mögliche Implementierung mit reinem Python könnte so aussehen:

.. literalinclude:: py_kmeans.py
   :caption: py_kmeans.py
   :name: py_kmeans.py

Beispieldaten können wir uns erstellen mit:

.. code-block:: python

    from sklearn.datasets import make_blobs
    points, labels_true = make_blobs(n_samples=1000, centers=3,
                                 random_state=0, cluster_std=0.60)

Und schließlich können wir die Berechnung ausführen mit:

.. code-block:: python

    kmeans(points, 10)

Performance-Messungen
---------------------

Wenn ihr erst einmal mit eurem Code gearbeitet habt, kann es nützlich sein, die
Effizienz genauer zu untersuchen. Hierfür kann der :doc:`ipython-profiler` oder
:doc:`scalene` genutzt werden.

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

Suche nach bestehenden Implementierungen
----------------------------------------

Ihr solltet nicht das Rad neu erfinden wollen: Wenn es bestehende
Implementierungen gibt, solltet ihr diese auch verwenden. für den
k-Means-Algorithmus gibt es sogar gleich zwei Implementierungen:

* `sklearn.cluster.KMeans
  <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html>`_

  .. code-block:: python

        from sklearn.cluster import KMeans

        KMeans(10).fit_predict(points)

* `dask_ml.cluster.KMeans
  <https://ml.dask.org/modules/generated/dask_ml.cluster.KMeans.html>`_

  .. code-block:: python

        from dask_ml.cluster import KMeans

        KMeans(10).fit(points).predict(points)

Gegen diese bestehenden Lösungen könnte bestenfalls sprechen, dass sie einen
erheblichen Overhead in eurem Projekt erzeugen könnten wenn ihr nicht schon
an anderen Stellen `scikit-learn <https://scikit-learn.org/stable/>`_ oder
`Dask-ML <https://ml.dask.org>`_ einsetzt. Im Folgenden werde ich daher weitere
Möglichkeiten zeigen, euren eigenen Code zu optimieren.

Anti-Patterns finden
--------------------

Anschließend könnt ihr mit :doc:`perflint` euren Code durchsuchen nach den
häufigsten Performance-Anti-Patterns in Python.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    perflint

.. seealso::
   * `Effective Python <https://effectivepython.com>`_

Vektorisierungen mit NumPy
--------------------------

:doc:`../workspace/numpy/index` verlagert sich wiederholte Operationen in eine
statisch typisierte kompilierte Schicht, um so  die schnelle Entwicklungszeit von
Python mit der schnellen Ausführungszeit von C zu kombinieren. :abbr:`Evtl. (Eventuell)` könnt ihr :doc:`../workspace/numpy/ufunc`, :doc:`Vektorisierung
<../workspace/numpy/vectorisation>` und
:doc:`../workspace/numpy/indexing-slicing` in allen Kombinationen nutzen um sich
wiederholende Operationen in kompilierten Code zu verschieben und damit langsame
Schleifen zu vermeiden.

Mit NumPy können wir auf einige Schleifen verzichten:

.. literalinclude:: np_kmeans.py
   :caption: np_kmeans.py
   :name: np_kmeans.py
   :lines: 1-8

Die Vorteile von NumPy sind, dass der Python-Overhead nur je Array und nicht je
Array-Element auftritt. Da NumPy eine spezifische Sprache für Array-Operationen
verwendet, erfordert es jedoch auch eine andere Denkweise beim Schreiben von
Code. Schließlich können die Batch-Operationen auch zu übermäßigem
Speicherverbrauch führen.

Spezielle Datenstrukturen
-------------------------

:doc:`../workspace/pandas/index`
    für SQL-ähnliche :doc:`../workspace/pandas/group-operations` und
    :doc:`../workspace/pandas/aggregation`.

    So könnt ihr auch die Schleife in der Methode ``compute_centers`` umgehen:

    .. literalinclude:: pd_kmeans.py
       :caption: pd_kmeans.py
       :name: pd_kmeans.py
       :lines: 2-4, 11-15

`scipy.spatial <https://docs.scipy.org/doc/scipy/reference/spatial.html>`_
    für räumliche Abfragen wie Entfernungen, nächstgelegene Nachbarn,  k-Means
    :abbr:`usw. (und so weiter)`

    Unsere ``find_labels``-Methode kann dann noch spezifischer geschrieben
    werden:

    .. literalinclude:: sp_kmeans.py
       :caption: sp_kmeans.py
       :name: sp_kmeans.py
       :lines: 4-10

`scipy.sparse <https://docs.scipy.org/doc/scipy/reference/sparse.html>`_
    `dünnbesetzte Matrizen <https://de.wikipedia.org/wiki/Dünnbesetzte_Matrix>`_
    für 2-dimensionale strukturierte Daten.
`Sparse <https://sparse.pydata.org/en/stable/>`_
    für N-diemensional strukturierte Daten.
`scipy.sparse.csgraph <https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html>`_
    für graphenähnliche Probleme, :abbr:`z.B. (zum Beispiel)` die Suche nach
    kürzesten Wegen.
`Xarray <https://docs.xarray.dev/en/stable/>`_
    für die Gruppierung über mehrere Dimensionen hinweg.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    parallelise-pandas

Compiler wählen
---------------

Faster Cpython
~~~~~~~~~~~~~~

Auf der PyCon US im Mai 2021 stellte Guido van Rossum mit `Faster CPython
<https://github.com/faster-cpython>`_ ein Projekt vor, das die Geschwindigkeit
von Python 3.11 verdoppeln soll. Die Zusammenarbeit mit den anderen
Python-Kernentwicklern ist in :pep:`PEP 659 – Specializing Adaptive Interpreter
<659>` geregelt. Zudem gibt es einen offenen `Issue Tracker
<https://github.com/faster-cpython/ideas/issues>`_ und diverse `Werkzeuge zum
Sammeln von Bytecode-Statistiken <https://github.com/faster-cpython/tools>`_.
Von den Änderungen profitieren dürfte vor allem CPU-intensiver Python-Code;
bereits in C geschriebener Code, I/O-lastige Prozesse und Multithreading-Code
dürften hingegen kaum profitieren.

.. seealso::
    * `Faster CPython <https://faster-cpython.readthedocs.io/>`__

Wenn ihr mit eurem Projekt nicht bis zur Veröffentlichung von Python 3.11 in der
finalen Version voraussichtlich am 24. Oktober 2022 warten wollt, könnt ihr euch
auch die folgenden Python-Interpreter anschauen:

Cython
~~~~~~

Bei intensiven numerischen Operationen kann Python sehr langsam sein, auch wenn
ihr alle Anti-Patterns vermieden und Vektorisierungen mit NumPy genutzt habt.
Dann kann das Übersetzen von Code in `Cython <https://cython.org>`_ hilfreich
sein.  Leider muss der Code jedoch häufig umstrukturiert werden und nimmt
dadurch an Komplexität zu. Auch werden explizite Type Annotations und das
Bereitstellen des Codes umständlicher.

Unser Beispiel könnte dann so aussehen:

.. literalinclude:: cy_kmeans.pyx
   :caption: cy_kmeans.pyx
   :name: cy_kmeans.pyx
   :lines: 1-28

.. seealso::
    * `Cython Tutorials
      <https://cython.readthedocs.io/en/latest/src/tutorial/>`_

Numba
~~~~~

`Numba <http://numba.pydata.org/>`_ ist ein JIT-Compiler, der vor allem
wissenschaftlichen Python- und NumPy-Code in schnellen Maschinencode
übersetzt, :abbr:`z.B. (zum Beispiel)`:

.. literalinclude:: nb_kmeans.py
   :caption: nb_kmeans.py
   :name: nb_kmeans.py
   :lines: 1-25

Numba benötigt allerdings `LLVM <https://de.wikipedia.org/wiki/LLVM>`_ und
einige Python-Konstrukte werden nicht unterstützt.

Aufgabenplaner
--------------

:doc:`ipyparallel/index`, :doc:`dask` und `Ray <https://docs.ray.io/>`_
können Aufgaben in einem Cluster verteilen. Dabei haben sie unterschiedliche
Schwerpunkte:

* ``ipyparallel`` integriert sich einfach in ein
  :doc:`../workspace/jupyter/hub/index`.
* Dask imitiert Pandas, NumPy, Iteratoren, Toolz und PySpark bei der Verteilung
  ihrer Aufgaben.
* Ray bietet eine einfache, universelle API für den Aufbau verteilter
  Anwendungen.

  * `RLlib <https://docs.ray.io/en/latest/rllib.html>`_ skaliert insbesondere
    reinforcement Learning.
  * Ein `Backend für Joblib <https://docs.ray.io/en/latest/joblib.html>`_
    unterstützt verteilte `scikit-learn
    <https://scikit-learn.org/stable/>`_-Programme.
  * `XGBoost-Ray <https://docs.ray.io/en/latest/xgboost-ray.html>`_ ist ein
    Backend für verteiltes `XGBoost
    <https://xgboost.readthedocs.io/en/latest/>`_.
  * `LightGBM-Ray <https://docs.ray.io/en/latest/lightgbm-ray.html>`_ ist ein
    Backend für verteiltes `LightGBM
    <https://lightgbm.readthedocs.io/en/latest/>`_
  * `Collective Communication Lib
    <https://docs.ray.io/en/latest/ray-collective.html>`_ bietet eine Reihe von
    nativen Collective-Primitiven für `Gloo
    <https://github.com/facebookincubator/gloo>`_ und die `NVIDIA Collective
    Communication Library (NCCL)
    <https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html>`_.

Unser Beispiel könnte mit Dask so aussehen:

.. literalinclude:: ds_kmeans.py
   :caption: ds_kmeans.py
   :name: ds_kmeans.py
   :lines: 1-32

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ipyparallel/index
    dask.ipynb

Multithreading, Multiprocessing und Async
-----------------------------------------

Nach einem kurzen :doc:`Überblick <multiprocessing-threading-async>`
werden anhand von drei Beispielen zu :doc:`Threading <threading-example>`,
:doc:`Multiprocessing <multiprocessing>` und :doc:`Async <asyncio-example>`
die Regeln und Best Practices veranschaulicht.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    multiprocessing-threading-async
    threading-example.ipynb
    multiprocessing.ipynb
    threading-forking-combined.ipynb
    asyncio-example.ipynb
