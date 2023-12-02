.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git-Glossar
===========

.. glossary::

    Branch
    Zweig
        Ein Zweig ist eine Entwicklungslinie. Der letzte Commit auf einem Zweig
        wird als Spitze des Zweiges bezeichnet, der durch einen ``head``
        referenziert wird und der sich weiterbewegt, wenn weitere Entwicklungen
        auf dem Zweig vorgenommen werden. Ein einzelnes Git-Repository kann eine
        beliebige Anzahl von Zweigen haben, aber ihr :term:`Working Tree` ist
        nur mit einem von ihnen verbunden –  dem *aktuellen* oder
        *ausgecheckten* Zweig – und :term:`HEAD` zeigt auf diesen Zweig.

    Cache
        Veraltet für :term:`Index`.

    Clone
    Klon
        Lokale Version eines Repository einschließlich aller Commits und
        Branches.

    Commit
        Ein Snapshot des gesamten Git-Repository, komprimiert in einem `SHA
        <https://de.wikipedia.org/wiki/Secure_Hash_Algorithm>`_.

    Fork
        Kopie eines Repository auf GitLab, die einem anderen User oder einer
        anderen Gruppe gehört.

    Git
        Git ist eine verteilte Versionsverwaltung.

    GitLab
        Web-Anwendung zur Versionsverwaltung auf Basis von :term:`git`. Später
        kamen Gitlab CI, ein System zur kontinuierlichen Integration, GitLab
        Runner, Container-Registry und vieles andere hinzu.

    ``HEAD``
        Der ``HEAD``-Zeiger repräsentiert euer aktuelles Arbeitsverzeichnis und
        kann mit ``git switch`` in verschiedene Zweige, Tags oder Commits
        verschoben werden.

    Index
        Eine Sammlung von Dateien mit Statusinformationen, deren Inhalt als
        Objekte gespeichert wird. Der Index ist eine gespeicherte Version eures
        :term:`Working Tree`.

    Merge request
        Ort zum Vergleichen und Diskutieren der in einem Branch eingeführten
        Änderungen mit Bewertungen, Kommentaren, Tests etc.; siehe auch
        `Merge requests
        <https://docs.gitlab.com/ee/user/project/merge_requests/>`_.

    ``origin``
        Das übliche Upstream-Repository. Die meisten Projekte haben mindestens
        ein Upstream-Projekt, das sie verfolgen. Standardmäßig wird ``origin``
        für diesen Zweck verwendet. Neue Upstream-Aktualisierungen werden in
        Zweige mit dem Namen :samp:`origin/{NAME_OF_UPSTREAM_BRANCH}` geholt,
        die ihr mit ``git branch -r`` sehen könnt.

    Remote Repository
        Ein Repository, das zum Nachverfolgen eines gemeinsamen Projekt
        verwendet wird, sich aber an einem anderen Ort befindet.

    Trunk-Based Development
    TBD
        Git-Workflow mit kurzlebigen Themenzweigen, die schnell zum einem
        einzigen ``main``-Zweig zusammengeführt werden.

        .. seealso::
           * `Trunk Based Development <https://trunkbaseddevelopment.com/>`_

    Working Tree
        Der Baum der tatsächlich ausgecheckten Dateien. Der Arbeitsbaum enthält
        normalerweise den Inhalt des :term:`HEAD`-Commit-Baums sowie alle
        lokalen Änderungen, die ihr vorgenommen, aber noch nicht übertragen
        habt.
