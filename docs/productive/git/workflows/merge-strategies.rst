.. SPDX-FileCopyrightText: 2023 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Merge-Strategien: Merge vs. Squash vs. Rebase
=============================================

Ich verwende :samp:`git merge`, :samp:`git merge squash` und :samp:`git rebase`
situationsabhängig. Sie haben alle ihre Vorzüge, aber ihre Verwendung hängt sehr
stark vom Kontext ab.

:samp:`git merge`
    fügt einen neuen Commit hinzu, wenn die Zweige zusammengeführt werden.

    Dies hat den Vorteil, dass es die wahre Geschichte am besten darstellt. Ihr
    könnt den Merge und alle :abbr:`WIP (work in progress)`-Commits sehen, die
    beim Entwickeln durchlaufen wurden. :abbr:`Ggf. (Gegebenenfalls)` könnt ihr
    den Merge einfach rückgängig machen mit :samp:`git revert {-m|--mainline}
    {1|2} {MERGE-COMMIT_SHA}`.

    ``-m 1``
        führt zurück zu dem Verhalten des Elternelements aus dem Zweig, in den
        ihr die Änderungen übernommen habt.
    ``-m 2``
        führt zurück zu dem Verhalten des Elternelements aus dem Zweig, aus dem
        ihr die Änderungen übernommen habt.

    .. tip::
       Mehr Commits machen auch :doc:`git bisect <../advanced/bisect>` besser,
       solange für jeden Commit ein Build erstellt werden kann. Bei hundert oder
       maximal tausend Zeilen, die sich geändert haben, habe ich noch eine
       Chance, den Bug in angemessener Zeit zu finden.

    .. seealso::
       * `Advanced Merging
         <https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging>`_

:samp:`git merge --squash`
    ermöglicht euch, alle Änderungen aus einem Zweig in einen einzigen Commit
    über dem aktuellen Zweig zusammenzufassen.

    Dies ist sinnvoll, wenn ihr viele kleine :abbr:`WIP (work in
    progress)`-Commits habt, die wirklich alle auf ein Feature abzielen. Dabei
    achte ich beim Squash darauf, die Commit-Nachricht so umzuschreiben, dass
    sie möglichst aussagekräftig ist. Die übliche Squash-Commit-Nachricht, die
    von Git, :doc:`../advanced/gitlab/index` :abbr:`etc. (et cetera)` erstellt
    wird, ist meist nicht hinreichend und fügt einfach alle
    Squash-Commit-Nachrichten zusammen, :abbr:`ggf. (gegebenenfalls)` eine Reihe
    von :abbr:`WIP (work in progress)`-Commit-Nachrichten.

:samp:`git rebase`
    verschiebt eine Folge von Commits zu einem neuen Basis-Commit. Damit bleibt
    der Vorteil erhalten, mittels :doc:`git bisect <../advanced/bisect>` schnell
    einen Bug finden zu können. Darüberhinaus wird es nun jedoch einfacher, den
    Kontext, in dem der Bug entstanden ist, zu erkennen.

    .. tip::
       Bei einem großen Diff und vielen :abbr:`WIP (work in progress)`-Commits
       kann :samp:`git rebase -i` interaktiv angewendet werden, um selektiv
       Commits für die ``squash``-Option auszuwählen und die Commits neu
       anzuordnen. Macht jedoch immer nur eine Sache:

       * Commits mit der ``squash``-Option zusammenfassen oder
       * die Reihenfolge der Commits ändern oder
       * die Commits bearbeiten.

       Versucht nicht, alle Änderungen auf einmal zu machen.

    .. tip::
       Wenn ihr euch bei :samp:`git rebase` nicht sicher fühlt, dann lasst es
       einfach sein! Ihr könnt stattdessen :samp:`git merge` oder :samp:`git
       commit --amend` verwenden.

    .. seealso::
       * :doc:`../rebase`
       * `Rewriting History: Squashing Commits
         <https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#_squashing>`_
       * `Rewriting History: Reordering Commits
         <https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#_reordering_commits>`_
