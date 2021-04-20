Code-Smells und Anti-Patterns
=============================

.. seealso::
   * `Brett Slatkin: Effektiv Python programmieren
     <https://www.mitp.de/IT-WEB/Programmierung/Effektiv-Python-programmieren.html>`_

Funktionen, die Objekte sein sollten
------------------------------------

Python unterstützt neben der objektorientierten auch die prozedurale
Programmierung mithilfe von Funktionen und vererbbaren Klassen. Beide Paradigmen
sollten jedoch auf die passenden Probleme angewendet werden.

Typische Symptome von funktionalem Code, der in Klassen umgestaltet werden
sollte, sind

* ähnliche Argumente über Funktionen hinweg
* hohe Anzahl eindeutiger Halstead-Operanden
* Mix aus mutable und immutable Funktionen

So können z.B. drei Funktionen mit unklarer Verwendung so reorganisiert werden,
dass ``load_image()`` durch ``.__init__()`` ersetzt wird, ``crop()`` eine
Klassenmethode wird und ``get_thumbnail()`` eine Eigenschaft:

.. code-block:: python

    class Image(object):
        thumbnail_resolution = 128
        def __init__(self, path):
            …

        def crop(self, width, height):
            …

        @property
        def thumbnail(self):
            …
            return thumb

Objekte, die Funktionen sein sollten
------------------------------------

Manchmal sollte jedoch auch objektorientierter Code besser in Funktionen
aufgelöst werden, z.B. wenn in einer Klasse außer ``.__init__()`` nur eine
weitere Methode oder nur statische Methoden enthalten sind.

.. note::
   Ihr müsst nicht händisch nach solchen Klassen suchen, sondern es gibt eine
   `pylint <https://github.com/PyCQA/pylint>`_-Regel dafür:

   .. code-block:: console

    $ pipenv run pylint --disable=all --enable=R0903 requests
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
--------------------

    Flat is better than nested.

– Tim Peters, `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`_

Verschachtelter Code erschwert das Lesen und Verstehen. Ihr müsst die
Bedingungen verstehen und merken, wenn Ihr durch die Zweige geht. Objektiv
erhöht sich die zyklomatische Komplexität bei steigender Anzahl der
Code-Verzweigungen.

Ihr könnt verschachtelte Methoden mit mehreren ineinandergesteckten
``if``-Anweisungen reduzieren, indem Ihr Ebenen durch Methoden ersetzt, die ggf.
``False`` zurückgeben. Anschließend könnt Ihr mit ``.count()`` überprüfen, ob
die Anzahl der Fehler ``> 0`` ist.

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
   Iteratoren aus Datenstrukturen erstellt werden. Zudem könnt Ihr mit
   itertools auch Filtern, z.B. mit `filterfalse
   <https://docs.python.org/3/library/itertools.html#itertools.filterfalse>`_.

Query-Tools für komplexe Dicts
------------------------------

`JMESPath <https://jmespath.org/>`_, `glom <https://github.com/mahmoud/glom>`_,
`asq <https://asq.readthedocs.io/en/latest/>`_ und `flupy
<https://flupy.readthedocs.io/en/latest/>`_ können die Abfrage von Dicsts in
Python deutlich vereinfachen.

Code reduzieren mit ``dataclasses`` und ``attrs``
-------------------------------------------------

`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ wurde in
Python 3.7 eingeführt und es gibt auch einen Backport für Python 3.6. Sie sollen
die Definition von Klassen vereinfachen, die hauptsächlich zum Speichern von
Werten erstellt werden, und auf die dann über die Attributsuche zugegriffen
werden kann. Einige Beispiele sind ``collection.namedtuple``,
``Typing.NamedTuple``, Rezepte zu Records [#]_ und Verschachtelte Dicts [#]_.
Datenklassen ersparen Euch das Schreiben und Verwalten dieser Methoden.

.. seealso::
   * [PEP 557 – Datenklassen](https://www.python.org/dev/peps/pep-0557/)

`attrs <https://www.attrs.org/en/stable/>`_ ist ein Python-Paket, das es schon
viel länger als ``dataclasses`` gibt, umfangreicher ist und auch mit älteren
Versionen von Python verwendet werden kann.

----

.. [#] `Records (Python recipe) <https://code.activestate.com/recipes/576555-records/>`_
.. [#] `Dot-style nested lookups over dictionary based data structures (Python recipe)
       <http://code.activestate.com/recipes/576586-dot-style-nested-lookups-over-dictionary-based-dat/>`_
