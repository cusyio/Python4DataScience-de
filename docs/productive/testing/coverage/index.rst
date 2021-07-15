Coverage.py
===========

Ihr könnt Coverage-Reports erstellen mit `coverage.py
<https://github.com/nedbat/coveragepy>`_.

.. seealso::
   * `GitHub <https://github.com/nedbat/coveragepy>`_
   * `Docs <https://coverage.readthedocs.io/>`_

Installation
------------

.. code-block:: console

    $ pipenv install coverage

.. note::
   Wollt ihr die Testabdeckung für Python 2 and Python<3.6 ermitteln, müsst ihr
   Coverage<6.0 verwenden.

Nutzung
-------

Ihr könnt euren üblichen Test-Runner zusammen mit Coverage ausführen

* … mit `pytest <https://docs.pytest.org/>`_:

  .. code-block:: console

    $ pipenv install pytest-cov

  oder für verteilte Tests

  .. code-block:: console

    $ pipenv install pytest-xdist

  Anschließend könnt ihr die Testabdeckung überprüfen mit

  .. code-block:: console

    $ pytest --cov=myproj tests/

  .. seealso::
     * `pytest-cov’s documentation <https://pytest-cov.readthedocs.io/>`_

* … mit :doc:`../unittest`:

  .. code-block:: console

    $ coverage run -m unittest discover

* … mit `nose <https://nose.readthedocs.io/>`_:

  .. code-block:: console

    $ coverage run -m nose arg1 arg2

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    opencoverage
    codecov
