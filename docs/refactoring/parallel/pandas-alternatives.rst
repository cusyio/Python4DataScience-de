Pandas-Alternativen
===================

In :doc:`pandas:user_guide/enhancingperf` werden einige Möglichkeiten
beschrieben, wie die Performance von Pandas verbessert werden kann. Es gibt
jedoch auch spezielle Bibliotheken, die die Verarbeitung von Dataframes
parallelisieren können.

cuDF
----

cuDF ist eine GPU-DataFrame-Bibliothek, die eine `Pandas-ähnliche API
<https://docs.rapids.ai/api/cudf/stable/api.html>`_ implementiert.

.. seealso::

    * `Docs <https://docs.rapids.ai/api/cudf/stable/>`_
    * `GitHub <https://github.com/rapidsai/cudf>`_
    * `PyPI <https://pypi.org/project/cudf/>`_
    * `Beispiel Notebooks
      <https://github.com/rapidsai-community/notebooks-contrib>`_

Modin
=====

Modin parallelisiert fast die gesamte Pandas-API. Dabei muss der bestehende
Pandas-Code meist nur um folgenden Import erweitert werden:

.. code-block:: python

    import modin.pandas as pd

Die Einschränkungen beziehen sich auf ``pd.read_json``, das nur für
``lines=True`` implementiert ist.

.. seealso::

    * `Docs <https://modin.readthedocs.io/en/latest/>`_
    * `GitHub <https://github.com/modin-project/modin>`_

Dask
====

Dask DataFrame ist ein großer paralleler DataFrame aus mehreren Pandas
DataFrames. Dabei ist die ``dask.dataframe``-API eine Teilmenge der Pandas-API,
wobei es jedoch geringfügige Änderungen gibt.

.. seealso::

    * `Home <https://docs.dask.org/en/latest/dataframe.html>`_
    * `API docs <https://docs.dask.org/en/latest/dataframe-api.html>`_
    * `Example notebook <https://examples.dask.org/dataframe.html>`_
    * `Tutorial <https://tutorial.dask.org/04_dataframe.html>`_
