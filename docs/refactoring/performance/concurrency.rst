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

Überblick
~~~~~~~~~

+------------------+------------------+------------------+--------------------------------+
| Kriterium        | Multithreading   | Multiprocessing  | asyncio                        |
+==================+==================+==================+================================+
| Trennung         | Threads teilen   | Die Prozesse sind| Mit                            |
|                  | sich einen       | unabhängig       | ``run_coroutine_threadsafe()`` |
|                  | Status.          | voneinander.     | können ``asyncio``-Objekte     |
|                  |                  |                  | auch von anderen Threads       |
|                  | Das Teilen eines | Sollen sie       | verwendet werden.              |
|                  | Status kann      | dennoch          |                                |
|                  | jedoch zu *Race  | miteinander      | Fast alle ``asyncio``-Objekte  |
|                  | Conditions*      | kommunizieren,   | sind nicht threadsicher.       |
|                  | führen, d.h. die | wird             |                                |
|                  | Ergebnisse einer | `Interprocess    |                                |
|                  | Operation können | communication    |                                |
|                  | vom zeitlichen   | (IPC)`_,         |                                |
|                  | Verhalten        | `object          |                                |
|                  | bestimmter       | pickling`_ und   |                                |
|                  | Einzeloperationen| anderer Overhead |                                |
|                  | abhängen.        | nötig.           |                                |
+------------------+------------------+------------------+--------------------------------+
| Wechsel          | Threads wechseln | Sobald Ihr den   | asyncio wechselt `kooperativ`_,|
|                  | `präemptiv`_,    | Prozess erhaltet,| d.h., es muss explizit `yield`_|
|                  | d.h., es muss    | sollten deutliche| oder `await`_ angegeben werden |
|                  | kein expliziter  | Fortschritte     | um einen Wechsel               |
|                  | Code hinzugefügt | gemacht werden.  | herbeizuführen. Ihr könnt daher|
|                  | werdenm um einen | Ihr solltet also | die Aufwände für diese Wechsel |
|                  | Wechsel der Tasks| nicht zu viele   | sehr gering halten.            |
|                  | zu verursachen.  | Roundtrips hin   |                                |
|                  |                  | und her machen.  |                                |
|                  | Ein solcher      |                  |                                |
|                  | Wechsel ist      |                  |                                |
|                  | jedoch jederzeit |                  |                                |
|                  | möglich;         |                  |                                |
|                  | dementsprechend  |                  |                                |
|                  | müssen kritische |                  |                                |
|                  | Bereiche mit     |                  |                                |
|                  | ``lock``         |                  |                                |
|                  | geschützt werden.|                  |                                |
|                  |                  |                  |                                |
|                  |                  |                  |                                |
+------------------+------------------+------------------+--------------------------------+
| Tooling          | Threads erfordern| Einfaches Tooling| Zumindest bei komplexen        |
|                  | sehr wenig       | u.a. mit `map`_  | Systemen führt ``asyncio``     |
|                  | Tooling: `Lock`_ | und              | einfacher zum Ziel als         |
|                  | und `Queue`_.    | `imap_unordered`_| Multithreading Locks.          |
|                  |                  | um einzelne      |                                |
|                  | Locks sind in    | Prozesse in einem| ``asyncio`` benötigt jedoch    |
|                  | nicht-trivialen  | einzelnen Thread | eine große Menge von           |
|                  | Beispielen schwer| zu testen, bevor | Werkzeugen: `futures`_,        |
|                  | zu verstehen.    | zu               | `Event Loops`_ und nicht       |
|                  | Bei komplexen    | Multiprocessing  | blockierende Versionen von fast|
|                  | Anwendungen      | gewechselt wird. | allem.                         |
|                  | sollten daher    |                  |                                |
|                  | besser atomare   | Wird IPC oder    |                                |
|                  | Message Queues   | object pickling  |                                |
|                  | oder asyncio     | verwendet, wird  |                                |
|                  | verwendet werden.| das Tooling      |                                |
|                  |                  | jedoch           |                                |
|                  |                  | aufwändiger.     |                                |
+------------------+------------------+------------------+--------------------------------+
| Performance      | Multithreading   | Die Prozesse     | Der Aufruf einer reinen        |
|                  | führt bei        | können auf       | Python-Funktion erheugt mehr   |
|                  | IO-lastigen      | mehrere CPUs     | Overhead als die erneute       |
|                  | Aufgaben zu den  | verteilt werden  | Anfrage eines ``generator``    |
|                  | besten           | und sollten daher| oder ``awaitable`` – d.h.,     |
|                  | Ergebnissen.     | für CPU-lastige  | ``asyncio`` kann die CPU       |
|                  |                  | Aufgaben         | effizient auslasten.           |
|                  | Die              | verwendet werden.|                                |
|                  | Leistungsgrenze  |                  | Für CPU-intensive Aufgaben ist |
|                  | für Threads ist  | Für die          | jedoch Multiprocessing besser  |
|                  | eine CPU         | Kommunikation und| geeignet.                      |
|                  | abzüglich der    | die              |                                |
|                  | Kosten für       | Synchronisierung |                                |
|                  | Task-Switches    | der Prozesse     |                                |
|                  | und              | entstehen jedoch |                                |
|                  | Aufwänden für die| ggf. zusätzliche |                                |
|                  | Synchronisation. | Aufwände.        |                                |
+------------------+------------------+------------------+--------------------------------+

.. _`Interprocess Communication (IPC)`: https://docs.python.org/3/library/ipc.html
.. _`object pickling`: https://docs.python.org/3/library/pickle.html
.. _`präemptiv`: https://de.wikipedia.org/wiki/Multitasking#Pr%C3%A4emptives_Multitasking
.. _`Lock`: https://docs.python.org/3/library/threading.html#threading.Lock
.. _`Queue`: https://docs.python.org/3/library/queue.html
.. _`kooperativ`: https://de.wikipedia.org/wiki/Multitasking#Kooperatives_Multitasking
.. _`yield`: https://docs.python.org/3/reference/simple_stmts.html#yield
.. _`await`: https://docs.python.org/3/reference/expressions.html#await
.. _`map`: https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map
.. _`imap_unordered`: https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap_unordered
.. _`futures`: https://docs.python.org/3/library/asyncio-task.html#awaitables
.. _`Event Loops`: https://docs.python.org/3/library/asyncio-eventloop.html
