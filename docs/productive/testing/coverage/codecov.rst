Codecov
=======

Codecov sammelt Coverage-Reports für die Sprachen Python, C#/.net, Java,
Node/Javascript/Coffee, C/C++, D, Go, Groovy, Kotlin, PHP, R, Scala, Xtern,
Xcode, Lua und anderen, um sie dann an `codecov.io <https://about.codecov.io/>`_
zu übermitteln.

.. seealso::
   * `GitHub <https://github.com/codecov/codecov-python>`_
   * `Docs <https://docs.codecov.io/docs>`_

Installation
------------

Codecov kann einfach installiert werden mit

.. code-block:: console

    $ pipenv install codecov

Verwendung
----------

…  im Terminal
~~~~~~~~~~~~~~

.. code-block:: console

    $ codecov -t <repository-upload-token>

… zusammen mit GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Eine minimale Konfiguration für öffentliche Repos:

.. code-block:: yaml

    steps:
      …
      - name: "Upload coverage to Codecov"
        uses: codecov/codecov-action@v1
        with:
          fail_ci_if_error: true

.. seealso::
   * `Codecov GitHub Action <https://github.com/codecov/codecov-action>`_

…  zusammen mit Travis CI
~~~~~~~~~~~~~~~~~~~~~~~~~

Hierfür könnt Ihr in der ``.travis.yml``-Datei folgendes hinzufügen:

.. code-block:: yaml

    language:
      python
    after_success:
      - bash <(curl -s https://codecov.io/bash)

… zusammen mit ``tox``
~~~~~~~~~~~~~~~~~~~~~~

Codecov kann mit :doc:`../tox` eingerichtet werden:

.. code-block:: ini

    [testenv]
    passenv = TOXENV CI TRAVIS TRAVIS_* CODECOV_*
    deps = codecov>=1.4.0
    commands = codecov -e TOXENV
