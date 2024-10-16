.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Code-Smells
===========

Code-Smells sind Codierungsmuster, die darauf hinweisen, dass mit dem Entwurf
eines Programms etwas nicht stimmt. Zum Beispiel ist die übermäßige Verwendung
von ``isinstance``-Prüfungen gegen konkrete Klassen ein Code-Smell, da das
Programm dadurch schwieriger zu erweitern ist, um mit neuen Typen in der Zukunft
umzugehen.

.. tip::
   `Entwurfsmuster in Python
   <https://cusy.io/de/unsere-schulungsangebote/entwurfsmuster-in-python>`_

Erkennen von Code-Smells
------------------------

Eine Möglichkeit, Code-Smells besser zu erkennen, besteht darin, die Merkmale
von Code zu beschreiben. Notiert euch die Dinge, die euch auffallen; fügt alle
Muster hinzu, die ihr seht, die ihr mögt oder nicht versteht. Möglicherweise
können euch die folgenden Fragen zu weiteren Überlegungen anregen:

* Gibt es Methoden, die die gleiche Form haben?
* Gibt es Methoden, die ein Argument mit demselben Namen haben?
* Bedeuten gleichnamige Argumente immer das Gleiche?
* Wenn ihr eine private Methode einer Klasse hinzufügen wollt, wo würde sie
  hingehören?
* Wenn ihr die Klasse in zwei Teile aufteilen würdet, wo wäre die Trennlinie?
* Haben die Tests in den Bedingungen etwas gemeinsam?
* Wie viele Verzweigungen haben die Bedingungen?
* Enthalten die Methoden außer der Bedingung noch weiteren Code?
* Hängt jede Methode mehr vom übergebenen Argument ab oder von der Klasse als
  Ganzes?

Typische Code-Smells in Python
------------------------------

Funktionen, die Objekte sein sollten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python unterstützt neben der objektorientierten auch die prozedurale
Programmierung mithilfe von Funktionen und vererbbaren Klassen. Beide Paradigmen
sollten jedoch auf die passenden Probleme angewendet werden.

Typische Symptome von funktionalem Code, der in Klassen umgestaltet werden
sollte, sind

* ähnliche Argumente über Funktionen hinweg
* hohe Anzahl eindeutiger Halstead-Operanden
* Mix aus mutable und immutable Funktionen

So können :abbr:`z.B. (zum Beispiel)` drei Funktionen mit unklarer Verwendung
so reorganisiert werden, dass ``load_image()`` durch ``.__init__()`` ersetzt
wird, ``crop()`` eine Klassenmethode wird und ``get_thumbnail()`` eine
Eigenschaft:

.. code-block:: python

    class Image(object):
        thumbnail_resolution = 128

        def __init__(self, path):
            "..."

        def crop(self, width, height):
            "..."

        @property
        def thumbnail(self):
            "..."
            return thumb

Objekte, die Funktionen sein sollten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Manchmal sollte jedoch auch objektorientierter Code besser in Funktionen
aufgelöst werden, :abbr:`z.B. (zum Beispiel)` wenn in einer Klasse außer
``.__init__()`` nur eine weitere Methode oder nur statische Methoden enthalten
sind.

.. note::
   Ihr müsst nicht händisch nach solchen Klassen suchen, sondern es gibt eine
   `pylint <https://github.com/pylint-dev/pylint>`_-Regel dafür:

   .. code-block:: console

    $ uv run pylint --disable=all --enable=R0903 requests
    ************* Module requests.auth
    requests/auth.py:72:0: R0903: Too few public methods (1/2) (too-few-public-methods)
    requests/auth.py:100:0: R0903: Too few public methods (1/2) (too-few-public-methods)
    ************* Module requests.models
    requests/models.py:60:0: R0903: Too few public methods (1/2) (too-few-public-methods)

    -----------------------------------
    Your code has been rated at 9.99/10

   Dies zeigt uns, dass in ``auth.py`` zwei Klassen mit nur einer öffentlichen
   Methode definiert wurden und zwar in den Zeilen 72ff. und 100ff. Auch in
   ``models.py`` gibt es ab Zeile 60 eine Klasse mit nur einer öffentlichen
   Methode.

Verschachtelter Code
~~~~~~~~~~~~~~~~~~~~

    *«Flat is better than nested.»*

– Tim Peters, `Zen of Python <https://peps.python.org/pep-0020/>`_

Verschachtelter Code erschwert das Lesen und Verstehen. Ihr müsst die
Bedingungen verstehen und merken, wenn ihr durch die Zweige geht. Objektiv
erhöht sich die zyklomatische Komplexität bei steigender Anzahl der
Code-Verzweigungen.

Ihr könnt verschachtelte Methoden mit mehreren ineinandergesteckten
``if``-Anweisungen reduzieren, indem ihr Ebenen durch Methoden ersetzt, die :abbr:`ggf. (gegebenenfalls)` ``False`` zurückgeben. Anschließend könnt ihr mit
``.count()`` überprüfen, ob die Anzahl der Fehler ``> 0`` ist.

Eine andere Möglichkeit besteht in der Verwendung von *List Comprehensions*. So
kann der Code

.. code-block:: python

    results = []
    for item in iterable:
        if item == match:
            results.append(item)

ersetzt werden durch:

.. code-block:: python

    results = [item for item in iterable if item == match]

.. note::
   Die `itertools <https://docs.python.org/3/library/itertools.html>`_ der
   Python-Standardbibliothek sind häufig ebenfalls gut geeignet, um die
   Verschachtelungstiefe zu reduzieren indem Funktionen zum Erstellen von
   Iteratoren aus Datenstrukturen erstellt werden.

.. note::
   Zudem könnt ihr mit den itertools auch filtern, :abbr:`z.B. (zum Beispiel)`
   mit `filterfalse
   <https://docs.python.org/3/library/itertools.html#itertools.filterfalse>`_:

   .. code-block::

      >>> from itertools import filterfalse
      >>> from math import isnan
      >>> from statistics import median
      >>> data = [20.7, float('NaN'),19.2, 18.3, float('NaN'), 14.4]
      >>> sorted(data)
      [20.7, nan, 14.4, 18.3, 19.2, nan]
      >>> median(data)
      16.35
      >>> sum(map(isnan, data))
      2
      >>> clean = list(filterfalse(isnan, data))
      >>> clean
      [20.7, 19.2, 18.3, 14.4]
      >>> sorted(clean)
      [14.4, 18.3, 19.2, 20.7]
      >>> median(clean)
      18.75


Query-Tools für komplexe Dicts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`JMESPath <https://jmespath.org/>`_, `glom <https://github.com/mahmoud/glom>`_,
`asq <https://asq.readthedocs.io/en/latest/>`_ und `flupy
<https://flupy.readthedocs.io/en/latest/>`_ können die Abfrage von Dicts in
Python deutlich vereinfachen.

Code reduzieren mit ``dataclasses`` und ``attrs``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`python-basics:dataclasses`
    sollen die Definition von Klassen vereinfachen, die hauptsächlich zum
    Speichern von Werten erstellt werden, und auf die dann über die
    Attributsuche zugegriffen werden kann. Einige Beispiele sind
    :func:`collections.namedtuple`, :py:class:`typing.NamedTuple`, Rezepte zu
    `Records
    <https://web.archive.org/web/20170904185553/http://code.activestate.com/recipes/576555-records/>`_
    und `Verschachtelte Dicts
    <https://web.archive.org/web/20100604034714/http://code.activestate.com/recipes/576586-dot-style-nested-lookups-over-dictionary-based-dat>`_.
    ``dataclasses`` ersparen euch das Schreiben und Verwalten dieser Methoden.

    .. seealso::
       * :pep:`557` – Data Classes

`attrs <https://www.attrs.org/en/stable/>`_
    ist ein Python-Paket, das es schon viel länger als ``dataclasses`` gibt,
    umfangreicher ist und auch mit älteren Versionen von Python verwendet werden
    kann.

.. seealso::
   * `Effective Python <https://effectivepython.com/>`_
     by Brett Slatkin
   * `When Python Practices Go Wrong
     <https://rhodesmill.org/brandon/slides/2019-11-codedive/>`_
     by Brandon Rhodes
