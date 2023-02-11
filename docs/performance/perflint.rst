perflint
========

`perflint <https://github.com/tonybaloney/perflint>`_ ist eine Erweiterung für
`pylint <https://pylint.org/>`_ für Performance-Anti-Patterns, :abbr:`u.a.
(unter anderem)`:

W8101: ``unnecessary-list-cast``
    Unnötige Verwendung von ``list()`` bei einem bereits iterierbarem Typ.
W8102: ``incorrect-dictionary-iterator``
    Falsche Iterator-Methode für ``dict``: Python-Dictionaries speichern
    Schlüssel und Werte in zwei separaten Tabellen. Sie können einzeln
    iteriert werden. Die Verwendung von ``.items()`` und das Verwerfen
    entweder des Schlüssels oder des Wertes mit ``_`` ist ineffizient, wenn
    stattdessen ``.keys()`` oder ``.values()`` verwendet werden können.
W8201: ``loop-invariant-statement``
    Die Schleife wird untersucht, um Anweisungen oder Ausdrücke zu
    ermitteln, deren Ergebnis bei jeder Iteration einer Schleife konstant
    ist, da sie auf benannten Variablen basieren, die während der Iteration
    nicht verändert werden.
W8202: ``loop-global-usage``
    Globale Namensverwendung in einer Schleife: Das Laden globaler Variablen ist
    langsamer als das Laden lokaler Variablen. Der Unterschied ist marginal,
    aber wenn er in einer Schleife weitergegeben wird, kann es zu einer
    spürbaren Geschwindigkeitsverbesserung kommen.
R8203: ``loop-try-except-usage``
    Bis Python 3.10 sind ``try``…``except``-Blöcke im Vergleich zu
    ``if``-Anweisungen sehr rechenintensiv.

    Vermeidet es, sie in einer Schleife zu verwenden, da sie erhebliche
    Overheads verursachen können. Refaktoriert euren Code so, dass keine
    iterationsspezifischen Details erforderlich sind und legt die gesamte
    Schleife in den ``try``-Block.

W8204: ``memoryview-over-bytes``
    Das Slicing von Byte-Objekten in Schleifen ist ineffizient, da eine Kopie
    der Daten erstellt wird. Verwendet stattdessen ``memoryview()``.

    .. seealso::
        * `Zero-copy interactions
          <https://effectivepython.com/2019/10/22/memoryview-bytearray-zero-copy-interactions>`_
        * `Memoryview Benchmarks
          <https://jakevdp.github.io/blog/2012/08/08/memoryview-benchmarks/>`_
        * `Memoryview Benchmarks 2
          <https://jakevdp.github.io/blog/2012/08/16/memoryview-benchmarks-2/>`_

W8205: ``dotted-import-in-loop``
    Der direkte Import des Namens ``%s`` ist in einer Schleife effizienter. In
    Python könnt ihr ein Modul importieren und dann auf Untermodule als
    Attribute zugreifen. Ihr könnt auch auf Funktionen als Attribute dieses
    Moduls zugreifen. Dadurch werden die Importanweisungen minimal gehalten.
    Wenn ihr diese Methode jedoch in einer Schleife verwendet, ist sie
    ineffizient, da bei jedem Schleifendurchlauf erst global, dann das Attribut
    und dann die Methode geladen wird.
W8301: ``use-tuple-over-list``
    Verwendet ein Tupel anstelle einer Liste für eine unveränderliche Sequenz:
    Sowohl die Konstruktion als aoch die Indizierung eines Tupels ist schneller
    als die einer Liste.
W8401: ``use-list-comprehension``
    Verwendet List Comprehensions mit oder ohne ``if``-Anweisung anstelle einer
    ``for``-Schleife.
W8402: ``use-list-copy``
    Verwendet eine Listenkopie mit ``list.copy()`` anstelle einer
    ``for``-Schleife.
W8403: ``use-dict-comprehension``
    Verwendet ein Dictionary Comprehensions anstelle einer einfachen
    ``for``-Schleife.
