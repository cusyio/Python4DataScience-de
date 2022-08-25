Regressionen finden mit ``git bisect``
======================================

``git bisect`` ermöglicht Euch, den Git-Commit zu finden, der eine Regression
eingeführt hat.

#. Hierzu beginnt ihr die Suche mit ``git bisect start``.
   Anschließend könnt ihr den Bereich mit ``git bisect bad [COMMIT]`` und ``git
   bisect good [COMMIT]`` eingrenzen, in dem ein Fehler eingeführt wurde.
   Alternativ kann auch die Kurzform ``git bisect start [BAD COMMIT] [GOOD
   COMMIT]`` verwendet werden. ``git bisect`` checkt dann einen Commit in der
   Mitte aus und fordert Euch auf diesen zu testen, z.B.:

   .. code-block:: console

    $ git bisect start v2.6.27 v2.6.25
    Bisecting: 10928 revisions left to test after this (roughly 14 steps)
    [2ec65f8b89ea003c27ff7723525a2ee335a2b393] x86: clean up using max_low_pfn on 32-bit

#. Die Suche kann nun manuell oder automatisch mit einem Skript fortgesetzt
   werden. Manuell könnt ihr mit ``git bisect bad`` und ``git bisect good`` den
   Bereich immer weiter eingrenzen, in dem ein Fehler eingeführt wurde. Wird
   dieser Commit gefunden, kann die Ausgabe z.B. folgendermaßen aussehen:

   .. code-block:: console

    $ git bisect bad
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
     NAME = Funky Weasel ist Jiggy wit it

     # * DOKUMENTATION *

   Die Überprüfung, ob mit einem Commit fehlerhafter Code eingeführt wurde, kann
   auch automatisiert erfolgen. Ein Beispiel hierfür findet ihr im Issue
   `fetch_california_housing fails in CI on master
   <https://github.com/scikit-learn/scikit-learn/issues/14956>`_ von scikit-learn:

   .. code-block:: console

    git bisect run pytest sklearn/utils/tests/test_multiclass.py -k test_unique_labels_non_specific

#. Das scikit-learn-Issue zeigt auch, wie ihr anderen die Ergebnisse eurer
   Bisect-Suche mit ``$ git bisect log`` nachvollziehbar mitteilen könnt:

   .. code-block::

    $ git bisect log
    81f2d3a0e *   massich/multiclass_type_of_target Merge branch 'master' into multiclass_type_of_target
              |\
    15f24f25d | * bad DOC Cleaning for what's new
    fbb2c7c70 | * good-fbb2c7c7007dc373c462e39ab273a183a8823d58 @ ENH Adds _MultimetricScorer for Optimized Scoring  (#14593)
    …

   Mit ``$ git bisect log > bisect_log.txt`` könnt ihr eure Suche auch für
   andere reproduzierbar abspeichern:

   .. code-block:: console

    $ git bisect replay bisect_log.txt

#. Schließlich könnt ihr mit ``git bisect reset`` in den Branch zurückkehren,
   in dem ihr Euch vor der Bisect-Suche befunden habt:

   .. code-block:: console

    $ git bisect reset
    Checking out files: 100% (21549/21549), done.
    Previous HEAD position was 2ddcca3... Linux 2.6.26-rc1
    Switched to branch 'master'

.. seealso::
   * `Fighting regressions with git bisect
     <https://git-scm.com/docs/git-bisect-lk2009>`_
   * `Docs <https://git-scm.com/docs/git-bisect>`_
