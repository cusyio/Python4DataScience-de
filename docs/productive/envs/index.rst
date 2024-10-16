.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Python-Umgebungen
=================

Im Python Basics Tutorial ist bereits beschrieben, wie ihr mit
:ref:`python-basics:venv` eine Python-Umgebung erstellen könnt. Diese jedoch
reproduzierbar und sicher zu erstellen, ist deutlich komplexer.  Mit dem Python
Paketmanager :term:`pip`, könnte das :abbr:`z.B. (zum Beispiel)` so aussehen:

.. code-block:: console

    $ python -m pip install --no-deps --require-hashes ----only-binary=:all:

Dezidierte Umgebungen (:abbr:`z.B. (zum Beispiel)` mit :term:`uv` oder
:doc:`Spack <spack/index>` vereinfachen dies, wenn ihr die Dateien mit den
Spezifikationen speichert, also :abbr:`z.B. (zum Beispiel)` mit :file:`uv.lock`
oder :file:`spack.lock`. Auf diese Weise könnt ihr und andere eure Umgebungen
reproduzieren.

.. toctree::
    :hidden:

    uv/index
    spack/index
