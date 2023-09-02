.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Umgebungen reproduzieren
========================

Reproduzierbare und sichere Python-Umgebungen sind nur schwer zu gewährleisten.
Mit dem Python Paketmanager :term:`pip`, würde das so aussehen:

.. code-block:: console

    $ python -m pip install --no-deps --require-hashes ----only-binary=:all:

Dezidierte Umgebungen (:abbr:`z.B. (zum Beispiel)` mit :doc:`pipenv/index`,
und :doc:`Spack <spack/index>` vereinfachen dies, wenn ihr die Dateien mit den
Spezifikationen speichert, also :abbr:`z.B. (zum Beispiel)` mit ``Pipfile``,
``Pipfile.lock``, ``package-lock.json`` :abbr:`etc (et cetera)`. Auf diese Weise
könnt ihr und andere eure Umgebungen reproduzieren.

.. toctree::
    :hidden:

    spack/index
    pipenv/index
