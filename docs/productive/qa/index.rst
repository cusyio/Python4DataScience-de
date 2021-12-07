Code-Qualität und Komplexität überprüfen und verbessern
=======================================================

Bevor ihr mit dem Refactoring beginnt, solltet ihr die Komplexität eures Codes
messen. Im Folgenden möchte ich Euch einige Werkzeuge und Konzepte vorstellen,
die die Konplexität eures Codes überprüfen und die Wartung und Pflege von
Python-Paketen und anderem Quellcode vereinfachen. Häufig lässt sich zusammen
mit :doc:`/productive/git/pre-commit` die Code-Qualität auch automatisiert
überprüfen und verbessern.

.. seealso::
   * `PyCQA Meta Documentation <https://meta.pycqa.org/en/latest/>`_
   * `github.com/PyCQA <https://github.com/PyCQA>`_

Checker
-------

.. toctree::
   :maxdepth: 1

   flake8
   manifest
   mypy
   pytype
   wily
   pyre
   pysa

Formatter
---------

.. toctree::
   :maxdepth: 1

   black
   isort
   prettier

Refactoring
-----------

.. toctree::
   :maxdepth: 1

   anti-patterns
   rope.ipynb
