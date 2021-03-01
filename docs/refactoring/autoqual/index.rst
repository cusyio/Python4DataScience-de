Code-Qualität und Komplexität überprüfen und verbessern
=======================================================

Bevor Ihr mit dem Refactoring beginnt, solltet Ihr die Komplexität Eures Codes
messen. Hierfür könnt Ihr folgende Metriken verwenden:

`McCabe-Metrik <https://de.wikipedia.org/wiki/McCabe-Metrik>`_
    auch zyklomatische Komplexität genannt, misst die Komplexität von Code durch
    die Anzahl linear unabhängiger Pfade im Kontrollflussgraphen.
`Halstead-Metrik <https://de.wikipedia.org/wiki/Halstead-Metrik>`_
    statisch analysierendes Verfahren, das aus der Anzahl der Operatoren und
    Operanden die Schwierigkeit des Programms, den Aufwand und die
    Implementierungszeit berechnet.
Wartbarkeitsindex (engl. Maintainability Index)
    basiert auf der McCabe- und Halstead-Metrik

Im Folgenden möchte ich einige Werkzeuge und Konzepte vorstellen, die die
Wartung und Pflege von Python-Paketen und anderem Quellcode vereinfachen.
Häufig lässt sich zusammen mit :doc:`/productive/git/pre-commit` die
Code-Qualität automatisiert überprüfen und verbessern.

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

Formatter
---------

.. toctree::
   :maxdepth: 1

   black
   isort
   prettier
