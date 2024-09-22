.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Mypy
====

Mit Mypy könnt ihr eine statische Typüberprüfung vornehmen.

.. seealso::
    * `Home <https://mypy-lang.org>`_
    * `GitHub <https://github.com/python/mypy>`_
    * `Docs <https://mypy.readthedocs.io/en/stable/>`_
    * `PyPI <https://pypi.org/project/mypy/>`_
    * `Using Mypy in production at Spring
      <https://notes.crmarsh.com/using-mypy-in-production-at-spring>`_

Installation
------------

Mypy erfordert Python≥3.5. Dann kann es installiert werden, :abbr:`z.B. (zum
Beispiel)` mit:

.. code-block:: console

    $ pipenv install mypy

Überprüfen
----------

Dann könnt ihr es überprüfen, :abbr:`z.B. (zum Beispiel)` mit:

.. code-block:: console

    $ pipenv run mypy myprogram.py

.. note::
    Obwohl Mypy mit Python3 installiert werden muss, kann es auch Python2-Code
    analysieren, :abbr:`z.B. (zum Beispiel)` mit:

    .. code-block:: console

        $ pipenv run mypy --py2 myprogram.py
