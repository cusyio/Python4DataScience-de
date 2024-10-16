.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Starten der IPython-Shell
=========================

Ihr könnt IPython einfach in einer Konsole starten:

.. code-block:: console

   $ uv run ipython
   Python 3.11.10 (main, Sep  7 2024, 01:03:31) [Clang 16.0.0 (clang-1600.0.26.3)]
   Type 'copyright', 'credits' or 'license' for more information
   IPython 8.21.0 -- An enhanced Interactive Python. Type '?' for help.

   In [1]:

Alternativ könnt ihr IPython auch in einem Jupyter-Notebook verwenden. Hierfür
startet ihr zunächst den Notebook-Server:

.. code-block:: console

    $ uv run --with jupyter jupyter notebook
    [I 17:35:02.419 NotebookApp] Serving notebooks from local directory: /Users/veit/cusy/trn/Python4DataScience
    [I 17:35:02.419 NotebookApp] The Jupyter Notebook is running at:
    [I 17:35:02.427 NotebookApp] http://localhost:8888/?token=72209334c2e325a68115902a63bd064db436c0c84aeced7f
    [I 17:35:02.428 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 17:35:02.497 NotebookApp]

Anschließend sollte der Standardbrowser mit der angegebenen URL geöffnet
werden. Häufig ist dies ``http://localhost:8888``.

Nun könnt ihr im Browser einen Python-Prozess starten, indem ihr ein neues
Notebook erstellt.
