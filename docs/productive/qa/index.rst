.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Code-Qualität und Komplexität überprüfen und verbessern
=======================================================

Wenn die Qualität von Software vernachlässigt wird, führt dies schnell zu
überflüssigem Code, auch *Cruft* genannt, der dann die Weiterentwicklung von
Funktionen bremst. Das passiert auch großen Teams, die keine Zeit für die Pflege
einer hohen Codequalität aufwenden dürfen. Eine hohe Codequalität reduziert
Cruft auf ein Minimum und ermöglicht es dem Team, Funktionen mit weniger
Aufwand, Zeit und Kosten hinzuzufügen. Es gibt zwar einige Indikatoren, die zur
Messung der internen Qualität herangezogen werden können, diese können jedoch
nur einen ersten Hinweis auf die weitere Produktivität geben. Eine kürzlich
durchgeführte `Studie <https://arxiv.org/abs/2203.04374>`_ zeigt jedoch, dass
die Korrektur von Code mit niedriger Qualität mehr als doppelt so lange dauert
wie die von Code mit hoher Qualität, und dass die Fehlerdichte bei Code mit
niedriger Qualität 15 Mal höher ist.

Im Folgenden zeige ich euch einige :doc:`code-smells` und dann einige Tools, mit
denen ihr automatisierte statische Analysen durchführen und den Code neu
formatieren könnt. Einige dieser Tools könnt ihr sowohl in euren Editor wie auch
über das :doc:`../git/advanced/hooks/pre-commit` einbinden. Zum Schluss stelle
ich euch noch :doc:`rope` vor, ein Tool, das euch bei Refactorings unterstützt.

.. seealso::
   * `PyCQA Meta Documentation <https://meta.pycqa.org/en/latest/>`_
   * `github.com/PyCQA <https://github.com/PyCQA>`_


.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   code-smells

Checker
-------

:doc:`flake8`
    ist ein Wrapper um `PyFlakes <https://pypi.org/project/pyflakes/>`_,
    `pycodestyle <https://pypi.org/project/pycodestyle/>`_ und `McCabe
    <https://pypi.org/project/mccabe/>`_. Eine automatische Formatierung,
    :abbr:`(zum Beispiel)` mit :doc:`black`, ist jedoch noch bequemer.
:doc:`mypy`
    ist ein statischer Typ-Checker.
:doc:`pytype`
    ist ein statisches Analysewerkzeug, das Typen aus eurem Python-Code
    ableitet, ohne dass Typ-Annotationen erforderlich sind.
:doc:`wily`
    ist ein Kommandozeilenwerkzeug zur Überprüfung der Komplexität von
    Python-Code in Tests und Anwendungen.
:doc:`pystra`
    analysiert die strukturelle Zuverlässigkeit von Python-Code und fasst sie in
    einem Bericht zusammen.
:doc:`pysa`
    führt eine `Taint <https://en.wikipedia.org/wiki/Taint_checking>`_-Analyse
    durch, um potenzielle Sicherheitsprobleme zu identifizieren. Pysa verfolgt
    Datenströme von ihrem Ursprung bis zu ihrem Endpunkt und identifiziert
    verwundbaren Code.
:doc:`manifest`
    ist ein Werkzeug, mit dem ihr schnell überprüfen könnt, ob die Datei
    :ref:`python-basics:manifest-in` für Python-Pakete vollständig ist.

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   flake8
   mypy
   pytype
   wily
   pystra
   pysa
   manifest

Formatter
---------

:doc:`black`
    formatiert euren Code in ein schönes und deterministisches Format.
:doc:`isort`
    formatiert eure ``import``-Anweisungen in separaten und sortierten Blöcken.
:doc:`prettier`
    bietet automatische Formatierer für andere Dateitypen.

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   black
   isort
   prettier

Refactoring
-----------

:doc:`rope`
    ist eine Python-Bibliothek zum Refactoring.

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   rope.ipynb

.. seealso::
   * `Martin Fowler: Refactoring
     <https://www.mitp.de/IT-WEB/Software-Entwicklung/Refactoring.html>`_
