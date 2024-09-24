.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Regressionen finden mit ``git bisect``
======================================

``git bisect`` ermöglicht euch, einen Git-Commit, der eine Regression eingeführt
hat, schnell zu finden. Der Name *bisect* stammt von der `binären Suche
<https://de.wikipedia.org/wiki/Binäre_Suche>`_, den der Befehl anwendet. Dabei
wird die Liste der Commits wiederholt halbiert, bis der zuständige Commit
gefunden ist. So müssen nur log₂(n+1) Commits getestet werden.

#. Hierzu beginnt ihr die Suche mit ``git bisect start``.
   Anschließend könnt ihr den Bereich mit :samp:`git bisect new [{COMMIT}]` und
   :samp:`git bisect old [{COMMIT}]` eingrenzen, in dem ein Fehler eingeführt
   wurde. Alternativ kann auch die Kurzform :samp:`git bisect start [{BAD
   COMMIT}] [{GOOD COMMIT}]` verwendet werden. ``git bisect`` checkt dann einen
   Commit in der Mitte aus und fordert euch auf diesen zu testen, :abbr:`z.B.
   (zum Beispiel)`:

   .. code-block:: console

      $ git bisect start v2.6.27 v2.6.25
      Bisecting: 10928 revisions left to test after this (roughly 14 steps)
      [2ec65f8b89ea003c27ff7723525a2ee335a2b393] x86: clean up using max_low_pfn on 32-bit

#. Die Suche kann nun manuell oder automatisch mit einem Skript fortgesetzt
   werden. Manuell könnt ihr mit ``git bisect new`` und ``git bisect old`` den
   Bereich immer weiter eingrenzen, in dem ein Fehler eingeführt wurde. Wird
   dieser Commit gefunden, kann die Ausgabe :abbr:`z.B. (zum Beispiel)`
   folgendermaßen aussehen:

   .. code-block:: console

      $ git bisect new
      2ddcca36c8bcfa251724fe342c8327451988be0d is the first bad commit
      commit 2ddcca36c8bcfa251724fe342c8327451988be0d
      Author: Linus Torvalds <torvalds@linux-foundation.org>
      Date:   Sat May 3 11:59:44 2008 -0700

          Linux 2.6.26-rc1

      :100644 100644 5cf82581... 4492984e... M      Makefile

#. Anschließend überprüfen wir mit ``git show HEAD``, welche Änderungen in
   diesem Commit vorgenommen wurden:

   .. code-block:: console

      $ git show HEAD
      commit 2ddcca36c8bcfa251724fe342c8327451988be0d
      Autor: Linus Torvalds <torvalds@linux-foundation.org>
      Datum: Sa 3. Mai 11:59:44 2008 -0700

          Linux 2.6.26-rc1

      diff --git a / Makefile b / Makefile
      index 5cf8258 ..4492984 100644
      --- a / Makefile
      +++ b / Makefile
      @@ -1,7 +1,7 @@
       VERSION = 2
       PATCHLEVEL = 6
      -SUBLEVEL = 25
      -EXTRAVERSION =
      + SUBLEVEL = 26
      + EXTRAVERSION = -rc1
       NAME = Funky Weasel is Jiggy with it

       # * DOKUMENTATION *

#. Schließlich könnt ihr mit ``git bisect reset`` in den Branch zurückkehren,
   in dem ihr euch vor der Bisect-Suche befunden habt:

   .. code-block:: console

      $ git bisect reset
      Checking out files: 100% (21549/21549), done.
      Previous HEAD position was 2ddcca3... Linux 2.6.26-rc1
      Switched to branch 'master'

.. seealso::
   * `Fighting regressions with git bisect
     <https://git-scm.com/docs/git-bisect-lk2009>`_
   * `Docs <https://git-scm.com/docs/git-bisect>`_

Nicht-testbare Commits markieren mit ``git bisect skip``
--------------------------------------------------------

Manchmal landet man mit ``git bisect`` bei einem Commit, den man nicht testen
kann, weil es ein anderes Problem gibt. Normalerweise ist dies auf einen Fehler
zurückzuführen, der verhindert, dass ihr euren Code ausführen oder das
Testergebnis sehen könnt, :abbr:`z.B. (zum Beispiel)` ein Syntaxfehler. In
diesem Fall solltet ihr den Commit nicht als ``old`` oder ``new`` markieren, da
ihr aufgrund des Fehlers nicht feststellen könnt, welches Verhalten vorliegt.
Stattdessen solltet ihr den Commit mit `git bisect skip
<https://git-scm.com/docs/git-bisect#_bisect_skip>`_ überspringen. ``git
bisect`` checkt stattdessen einen benachbarten Commit zum Testen aus. Wenn
dieser funktioniert, macht wie gewohnt mit dem Testen und Ausführen von ``new``
oder ``old`` weiter. Wenn nicht, führt ``git bisect skip`` erneut aus. Wenn ihr
wisst, dass es einen Bereich von nicht testbaren Commits gibt, weist ``git
bisect`` an, diesen gesamten Bereich zu überspringen mit :samp:`git bisect skip
{COMMIT1}..{COMMIT2}`.

.. seealso::
   * `Avoiding testing a commit
     <https://git-scm.com/docs/git-bisect#_avoiding_testing_a_commit>`_

Automatisches Testen mit ``git bisect run``
-------------------------------------------

Oft ist es möglich, den Test, ob ein Commit altes oder neues Verhalten zeigt, zu
automatisieren. Dadurch wird die Verwendung von ``git bisect`` massiv
beschleunigt, da ihr nicht mehr bei jedem Schritt eine Eingabe machen müsst.
Außerdem wird der Prozess dadurch weniger fehleranfällig, da ihr nicht aus
Versehen den falschen Unterbefehl ``old`` und ``new`` ausführt. Automatisierte
Tests sind auch dann von Vorteil, wenn euer Testprozess eine Weile dauert,
:abbr:`z.B. (zum Beispiel)` wenn ihr einen langen Kompilierungsschritt habt. Die
Suche wird nicht unterbrochen, um auf eure Eingabe zu warten, und ihr könnt in
der Zwischenzeit an etwas anderem arbeiten.

Um automatische Tests zu starten, verwendet `git bisect run
<https://git-scm.com/docs/git-bisect#_bisect_run>`_ mit eurem Testbefehl und
optionalen Argumenten. Möglicherweise müsst ihr ein kurzes Testskript erstellen,
das den betroffenen Teil eures Codes ausführt und prüft, welches Verhalten
vorhanden ist. ``git bisect`` führt den angegebenen Befehl bei jedem Schritt der
Binärsuchschleife aus und verwendet seine Ergebnisse, um je nach Bedarf ``old``,
``new`` oder ``skip`` aufzurufen.

Ein Beispiel hierfür findet ihr im Issue `fetch_california_housing fails in CI
on master <https://github.com/scikit-learn/scikit-learn/issues/14956>`_ von
scikit-learn:

.. code-block:: console

   $ git bisect run pytest sklearn/utils/tests/test_multiclass.py -k test_unique_labels_non_specific

Automatisiertes Testen von Performance-Regressionen
---------------------------------------------------

Mit ein wenig Mehraufwand könnt ihr mit automatisierten Tests nach
komplizierteren Verhaltensänderungen suchen. Für Performance-Tests benötigen wir
hierfür ein Testprogramm, das mehrere Durchläufe durchführen und die minimale
Zeit ermitteln kann, wobei mögliches Rauschen eliminiert werden soll:

.. code-block:: python

   from subprocess import run
   from time import perf_counter


   times = []
   for _ in range(10):
       start = perf_counter()
       run(
           [./perftest, PARAM],
           check=True,
           capture_output=True,
       )
       elapsed = perf_counter() - start
       times.append(elapsed)
   if min(times) > X.0:
       print("Too slow")
       raise SystemExit(1)
   else:
       print("Fast enough")
       raise SystemExit(0)

Das Programm führt :samp:`python perftest.py {PARAM}` zehnmal aus und misst bei
jeder Ausführung die Zeit. Anschließend vergleicht es die minimale
Ausführungszeit mit einem Grenzwert von ``X`` Sekunden. Liegt die Mindestzeit
über dem Grenzwert, gibt es *Too slow* aus und beendet sich mit dem Exit-Code
``1``, andernfalls gibt es *Fast enough* aus und beendet sich mit dem Exit-Code
``0``:

.. code-block:: console

   $ python perftest.py PARAM
   Fast enough
   $ echo $? 0

Reproduzieren der Binärsuche mit ``git bisect log`` und ``git bisect replay``
-----------------------------------------------------------------------------

Das scikit-learn-Issue zeigt auch, wie ihr anderen die Ergebnisse eurer
Bisect-Suche mit ``git bisect log`` nachvollziehbar mitteilen könnt:

.. code-block::

   $ git bisect log
   81f2d3a0e *   massich/multiclass_type_of_target Merge branch 'master' into multiclass_type_of_target
           |\
   15f24f25d | * bad DOC Cleaning for what's new
   fbb2c7c70 | * good-fbb2c7c7007dc373c462e39ab273a183a8823d58 @ ENH Adds _MultimetricScorer for Optimized Scoring  (#14593)
   …

Mit ``$ git bisect log > bisect_log.txt`` könnt ihr eure Suche auch für andere
reproduzierbar abspeichern:

.. code-block:: console

   $ git bisect replay bisect_log.txt
