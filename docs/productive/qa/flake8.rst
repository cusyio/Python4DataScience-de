.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

``flake8``
==========

`flake8 <https://pypi.org/project/flake8/>`_ ist ein Wrapper um `PyFlakes
<https://pypi.org/project/pyflakes/>`_, `pycodestyle
<https://pypi.org/project/pycodestyle/>`_ und `McCabe
<https://pypi.org/project/mccabe/>`_. Eine automatische Formatierung,
:abbr:`z.B. (zum Beispiel)` mit :doc:`black`, ist jedoch noch komfortabler.

Installation
------------

.. code-block:: console

    $ spack env activate python-311
    $ spack install py-flake8

Überprüfen
----------

.. code-block:: console

    $ flake8 path/to/your/code


``flake8`` kann für :doc:`python-basics:test/tox` konfiguriert werden in der
``tox.ini``-Datei eines Pakets, z.B.:

.. code-block:: ini

    [tox]
    envlist = py38, py311, flake8, docs

    [testenv:flake8]
    basepython = python
    deps =
        flake8
        flake8-isort
    commands =
        flake8 src tests setup.py conftest.py docs/conf.py

.. seealso::
    * `Configuring flake8
      <https://flake8.pycqa.org/en/latest/user/configuration.html>`_
    * `flake8 error/violation codes
      <https://flake8.pycqa.org/en/latest/user/error-codes.html>`_
    * `pycodestyle error codes
      <https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes>`_
