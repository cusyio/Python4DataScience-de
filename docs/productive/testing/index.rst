Testen
======

.. seealso::
   * `Python Testing and Continuous Integration
     <http://carpentries-incubator.github.io/python-testing/>`_

Konzepte
--------

.. glossary::

    Test Case (Testfall)
        testet eine einzelnes Szenario.

    Test Fixture (Prüfvorrichtung)
        ist eine konsistente Testumgebung.

        .. seealso::
            * `pytest fixtures
              <https://docs.pytest.org/en/stable/fixture.html>`_

    Test Suite
        ist eine Sammlung mehrerer Test Cases.

    Test Runner
        durchläuft eine Test Suite und stellt die Ergebnisse dar.

Notebooks
---------

.. toctree::
   :maxdepth: 1

   unittest.ipynb
   unittest2.ipynb
   doctest.ipynb
   ipytest.ipynb

Tools
-----

.. toctree::
   :titlesonly:
   :maxdepth: 1

   hypothesis
   tox
   unittest2
   mock
   coverage/index
