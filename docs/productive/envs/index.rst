Umgebungen reproduzieren
========================

Reproduzierbare und sichere Python-Umgebungen sind nur schwer zu gewährleisten.
Mit dem Python Paketmanager :term:`pip`, würde das so aussehen:

.. code-block:: console

    $ python -m pip install --no-deps --require-hashes ----only-binary=:all:

Dezidierte Umgebungen (z.B. mit :doc:`pipenv/index`, :doc:`devpi` und
:doc:`Spack <spack/index>` vereinfachen dies, wenn ihr die Dateien mit den
Spezifikationen speichert, also z.B. mit ``Pipfile``, ``Pipfile.lock``,
``package-lock.json`` etc. Auf diese Weise könnt ihr und andere eure
Umgebungen reproduzieren.

.. toctree::
    :hidden:

    spack/index
    pipenv/index
