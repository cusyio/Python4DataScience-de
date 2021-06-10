Einführung in die Nebenläufigkeit
=================================

Bei der Entwicklung von Code kann es häufig zu Kompromissen zwischen
verschiedenen Implementierungen kommen. Zu Beginn der Entwicklung eines
Algorithmus ist es jedoch meist kontraproduktiv, sich um die Effizienz des Codes
zu kümmern.

    »Wir sollten kleine Effizienzsteigerungen in sagen wir etwa 97 % der Zeit,
    vergessen: Vorzeitige Optimierung ist die Wurzel allen Übels. Dennoch
    sollten wir unsere Chancen in diesen kritischen 3 % nicht verpassen.«[#]_

.. [#] Donald Knuth, Begründer des `Literate programming
       <http://www.literateprogramming.com/>`_, in Computer Programming as an
       Art (1974)

Martelli’s Modell der Skalierbarkeit
------------------------------------

+--------------+----------------------------------------+
| Anzahl Kerne | Beschreibung                           |
+==============+========================================+
| 1            | Einzelner Thread und einzelner Prozess |
+--------------+----------------------------------------+
| 2–8          | Mehrere Threads und mehrere Prozesse   |
+--------------+----------------------------------------+
| >8           | Verteilte Verarbeitung                 |
+--------------+----------------------------------------+

Martelli’s Beobachtung: Im Laufe der Zeit wird die zweite Kategorie immer
unbedeutender: Einzelne Kerne werden immer leistungsfähiger und große Datensätze
immer größer.

Global Interpreter Lock (GIL)
-----------------------------

CPython verfügt über eine Sperre für seinen intern geteilten globalen Status.
Dies hat zur Folge, dass nicht mehr als ein Thread gleichzeitig laufen kann.

Für I/O-lastige Anwendungen ist das GIL kein großes Problem; bei CPU-lastigen
Anwendungen führt die Verwendung von Threading jedoch zu einer Verlangsamung.
Dementsprechend ist Multi-Processing für uns spannend um mehr CPU-Zyklen zu
erhalten.

*Literate Programming* und *Martelli’s Modell der Skalierbarkeit* bestimmten die
Design-Entscheidungen zur Performance von Python über lange Zeit. An dieser
Einschätzung hat sich bis heute wenig geändert: Entgegen der intuitiven
Erwartungen führen mehr CPUs und Threads in Python zunächst zu weniger
effizienten Anwendungen. Dennoch wünschen sich laut der Umfrage von 2020 zu den
gewünschten Python-Features 20% Performance-Verbesserungen und 15% bessere
Nebenläufigkeit und Parallelisierung. Das `Gilectomy
<https://pythoncapi.readthedocs.io/gilectomy.html>`_-Projekt, das das GIL
ersetzen sollte, stieß jedoch auch noch auf ein weiteres Problem: Die Python
C-API legt sehr viele Implementierungsdetails offen. Damit würden
Leistungsverbesserungen jedoch schnell zu inkompatiblen Änderungen führen, die
dann vor allem bei einer so beliebten Sprache wie Python inakzeptabel
erscheinen. Dennoch gibt jedoch bereits einige Lösungen:

* `Numba <http://numba.pydata.org/>`_ ist ein JIT-Compiler, der vor allem
  wissenschaftlichen Python- und NumPy-Code in schnellen Maschinencode
  übersetzt.
* `PyPy <https://www.pypy.org/>`_ mit einem universelleren JIT-Compiler, der
  jedoch vorhandene C-Erweiterung wie NumPy emulieren muss, was wirklich
  ineffizient ist.

Multithreading, Multiprocessing und asynchrone Kommunikation
------------------------------------------------------------

Multithreading
--------------

Pros
~~~~

* Threads haben den Vorteil, einen gemeinsamen Status zu teilen. Allerdings kann
  dies auch zu *Race Conditions* führen, d.h., die Ergebnisse einer Operation
  können vom zeitlichen Verhalten bestimmter Einzeloperationen abhängen.
* Threads wechseln präemptiv, s. `Präemptives Multitasking
  <https://de.wikipedia.org/wiki/Multitasking#Pr%C3%A4emptives_Multitasking>`_.
  Dies ist praktisch, da Ihr keinen expliziten Code hinzufügen müsst, um einen
  Wechsel der Tasks zu verursachen.
* Threading funktioniert normalerweise mit vorhandenem Code und Werkzeugen,
  solange Locks für kritische Abschnitte hinzugefügt werden.
* Threads erfordern sehr wenig Tooling: `Lock
  <https://docs.python.org/3/library/threading.html#threading.Lock>`_ und
  `Queues <https://docs.python.org/3/library/queue.html>`_.

Cons
~~~~

* Die Kosten für diese Bequemlichkeit sind, dass ihr davon ausgehen müsst, dass
  ein solcher Wechsel jederzeit möglich ist. Dementsprechend müssen kritische
  Bereiche mit Locks geschützt werden.
* Die Leistungsgrenze für Threads ist eine CPU abzüglich der Kosten für
  Task-Switches und Synchronisationsaufwände.

Multiprocessing
---------------

Pros
~~~~

* Die Stärke von Prozessen ist, unabhängig voneinander zu sein.

Cons
~~~~

* Allerdings kommunizieren sie auch nicht miteinander. Daher werden
  `Interprocess Communication (IPC)
  <https://docs.python.org/3/library/ipc.html>`_, `object pickling
  <https://docs.python.org/3/library/pickle.html>`_ und anderer Overhead
  notwendig.

Asynchrone Kommunikation
------------------------

Pros
~~~~

* Async schaltet kooperativ um, daher müsst ihr explizit `yield
  <https://docs.python.org/3/reference/simple_stmts.html#yield>`_ oder `await
  <https://docs.python.org/3/reference/expressions.html#await>`_ hinzufügen, um
  einen Task-Switch herbeizuführen. Damit könnt ihr kontrollieren, wann diese
  Task-Switches und ggf. Locks und Synchronisationen stattfinden sollen. Ihr
  könnt daher die Aufwände für Task-Switches sehr niedrig halten. Zudem hat der
  Aufruf einer reinen Python-Funktion mehr Overhead als die erneute Anfrage
  eines *generator* oder *awaitable* – d.h., Async ist sehr billig.
* Async kann die CPU-Auslastung verbessern, da es die üblichen Aufwände
  reduzieren kann.
* Bei komplexen Systemen kommt man mit async viel einfacher zum Ziel als mit
  Threads mit Locks.

Cons
~~~~

* Async benötigt eine große Menge an Werkzeugen: `futures
  <https://docs.python.org/3/library/asyncio-task.html#future>`_, `Event Loops
  <https://docs.python.org/3/library/asyncio-eventloops.html>`_ und
  nicht-blockierende Versionen von fast allem.
