Monorepos und große Repositories
================================

Git ist ein sehr flexibles Versionskontrollsystem. Insbesondere ``branch`` und
``merge`` sind mächtige Werkzeuge in verteilten Entwicklungsumgebungen. Manchmal
schafft dies jedoch auch eine unnötige Komplexität. In diesen Fällen kann es
sinnvoll sein, mit einem monolithischen Repository oder *Monorepo* zu arbeiten.

Definition
----------

* Das Repository enthält mehr als ein logisches Projekt (:abbr:`z.B. (zum
  Beispiel)` einen iOS-Client und eine Webanwendung).
* Diese Projekte sind meist nur lose miteinander verbunden oder können auf
  andere Weise miteinander verbunden werden, :abbr:`z.B. (zum Beispiel)` über
  Tools zur Verwaltung von Abhängigkeiten.
* Das Repository enthält viele Commits, Zweige und/oder Tags. Oder es enthält
  viele und/oder große Dateien.

Mit Tausenden von Commits von hunderten Autoren in tausenden von Dateien pro
Monat ist das `Linux-Kernel-Repository <https://github.com/torvalds/linux/>`_
riesig.

Vor- und Nachteile
------------------

Ein Vorteil von Monorepos kann sein, dass die Aufwände um zu bestimmen, welche
Versionen des einen Projekts mit welchen Versionen des anderen Projekts
kompatibel sind, deutlich verringert sein könnten. Dies ist zumindest immer
dan der Fall, wenn alle Projekte eines Repository von nur einem Entwicklerteam
bearbeitet werden. Dann empfiehlt sich, mit jedem *Merge* wieder eine lauffähige
Version zu erhalten auch wenn die API zwischen den beiden Projekten geändert
wurde.

Als Nachteil können sich jedoch Performance-Einbußen erweisen. Diese können
:abbr:`z.B. (zum Beispiel)` entstehen durch:

eine große Anzahl an Commits
    Da Git DAGs (*directed acyclic graphs*) verwendet, um die Historie eines
    Projekts darzustellen, werden alle Operationen, die diesen Graphen
    durchlaufen, also :abbr:`z.B. (zum Beispiel)` ``git log`` oder
    ``git blame``, langsam werden.

eine große Anzahl von Git-Referenzen
    Eine große Anzahl von Branches und Tags verlangsamen Git ebenfalls.
    Mit ``git ls-remote`` könnt ihr euch die Referenzen eines Repository
    anzeigen lassen und mit ``git gc`` werden lose Referenzen in einer einzigen
    Datei zusammengefasst.

    Jede Operation, die den Commit-Verlauf eines Repositories durchlaufen und
    die einzelnen Referenzen berücksichtigen muss, wie :abbr:`z.B. (zum
    Beispiel)` bei ``git branch --contains <commit>``, werden bei einem Repo mit
    vielen Referenzen langsam.

eine große Anzahl an versionierten Dateien
    Der Index des Directory Cache (``.git/index``) wird von Git verwendet um
    zu ermitteln, ob die Datei verändert wurde. Dabei verlangsamen sich mit
    zunehmender Anzahl an Dateien viele Vorgänge, wie :abbr:`z.B. (zum
    Beispiel)` ``git status`` und ``git commit``.

große Dateien
    Große Dateien in einem Teilbaum oder einem Projekt verringern die Leistung
    des gesamten Repository.

Strategien für große Repositories
---------------------------------

Die Designziele von Git, die es so erfolgreich und beliebt gemacht haben, stehen
manchmal im Widerspruch zu dem Wunsch, es auf eine Weise zu verwenden, für die
es nicht konzipiert wurde. Dennoch gibt es eine Reihe von Strategien, die bei
der Arbeit mit großen Repositories hilfreich sein können:

``git clone --depth``
~~~~~~~~~~~~~~~~~~~~~

Auch wenn die Schwelle, ab der eine Historie als *riesig* eingestuft wird,
ziemlich hoch ist, kann es immer noch mühsam sein, sie zu klonen. Dennoch können
wir lange Historien nicht immer vermeiden, wenn sie aus rechtlichen oder
regulatorischen Gründen beibehalten werden müssen.

Die Lösung für einen schnellen Clone eines solchen Repositories  besteht darin,
nur die jüngsten Revisionen zu kopieren. Mit der *Shallow*-Option von ``git
clone`` könnt ihr nur die letzten :samp:`{N}` Commits der Historie abrufen,
:abbr:`z.B. (zum Beispiel)` :samp:`git clone --depth {N} {REMOTE-URL}`.

.. tip::
   Auch Build-Systeme, die mit eurem Git-Repository verbunden sind, profitieren
   von solchen Shallow Clones!

Shallow Clones waren in Git bisher eher selten, da einige Operationen Anfangs
kaum unterstützt wurden. Seit einiger Zeit (in den Versionen 1.9 und höher)
könnt ihr jetzt sogar von einem Shallow Clone aus Pull- und Push-Vorgänge in
Repositories durchführen.

``git filter-branch``
~~~~~~~~~~~~~~~~~~~~~

Für große Repositories, in denen viele Binärdateien versehentlich übertragen
wurden, oder alte Assets, die nicht mehr benötigt werden, ist ``git
filter-branch`` eine gute Lösung um die gesamte Historie durchzugehen und
Dateien nach vordefinierten Mustern herauszufiltern, zu ändern oder zu
überspringen.

Es ist ein sehr leistungsfähiges Werkzeug, sobald ihr herausgefunden habt, wo
euer Projektarchiv *schwer* ist. Es gibt auch Hilfsskripte, um große Objekte zu
identifizieren: :samp:`git filter-branch --tree-filter 'rm -rf
{/PATH/TO/BIG/ASSETS}'`.

.. warning::
   ``git filter-branch`` schreibt allerdings die gesamte Historie eures Projekts
   um, :abbr:`d.h. (das heißt)`, dass sich einerseits alle Commit-Hashes ändern
   und andererseits, dass jedes Teammitglied das aktualisierte Repository neu
   klonen muss.

.. seealso::
   * `How to tear apart a repository: the Git way
     <https://www.atlassian.com/blog/git/tear-apart-repository-git-way?>`_

``git clone --branch``
~~~~~~~~~~~~~~~~~~~~~~

Ihr könnt den Umfang der geklonten Historie auch begrenzen, indem ihr einen
einzelnen Zweig klont, etwa mit :samp:`git clone {REMOTE-URL} --branch
{BRANCH-NAME} --single-branch {FOLDER}`.

Dies kann nützlich sein, wenn ihr mit langlaufenden und abweichenden Zweigen
arbeitet, oder wenn ihr viele Zweige habt und nur mit einigen davon arbeiten
müsst. Wenn ihr jedoch nur eine wenige Zweige mit wenigen Unterschieden habt,
werdet ihr damit jedoch wahrscheinlich keinen großen Unterschied feststellen.

Git LFS
~~~~~~~

`Git LFS <https://git-lfs.github.com/>`_ ist eine Erweiterung, die Pointer auf
große Dateien in eurem Repository speichert, anstatt die Dateien selbst; diese
werden auf einem entfernten Server gespeichert, wodurch die Zeit für das Klonen
eures Projektarchivs drastisch verkürzt wird. Git LFS greift dabei auf die
nativen Push-, Pull-, Checkout- und Fetch-Operationen von Git zu, um die Objekte
zu übertragen und zu ersetzen, :abbr:`d.h. (das heißt)`, dass ihr mit großen
Dateien in eurem Repository wie gewohnt arbeiten könnt.

Git file system monitor (FSMonitor)
-----------------------------------

``git status`` und ``git add`` sind langsam, weil sie den gesamten Arbeitsbaum
nach Änderungen durchsuchen müssen. Mit der Funktion ``git fsmonitor--daemon``,
die ab Git-Version 2.36 zur Verfügung steht, wwerden diese Befehle beschleunigt,
indem der Umfang der Suche reduziert wird:

.. code-block::

    $ time git status
    Auf Branch master
    Ihr Branch ist auf demselben Stand wie 'origin/master'.
    real    0m1,969s
    user    0m0,237s
    sys     0m1,257s
    $ git config core.fsmonitor true
    $ git config core.untrackedcache true
    $ time git status
    Auf Branch master
    Ihr Branch ist auf demselben Stand wie 'origin/master'.
    real    0m0,415s
    user    0m0,171s
    sys     0m0,675s
    $ git fsmonitor--daemon status
    fsmonitor-daemon beobachtet '/srv/jupyter/linux'

.. seealso::
   * `Improve Git monorepo performance with a file system monitor
     <https://github.blog/2022-06-29-improve-git-monorepo-performance-with-a-file-system-monitor/>`_
    * `Scaling monorepo maintenance
      <https://github.blog/2021-04-29-scaling-monorepo-maintenance/>`_
