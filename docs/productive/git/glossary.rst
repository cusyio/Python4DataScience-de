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
        Kopie eines Repository auf :term:`GitHub` oder :term:`GitLab`, das einem
        anderen User oder einer anderen Gruppe gehört. Dies ermöglicht
        :abbr:`sog. (sogenannte)` :term:`Merge-Requests <Merge-Request>`.

    Git
        Git ist eine verteilte Versionsverwaltung.

    GitHub
        Web-Anwendung zur Versionsverwaltung auf Basis von :term:`git`, die die
        Zusammenarbeit auch über :term:`Forks <Fork>` ermöglicht. Zudem gibt es
        mit `GitHub Actions <https://docs.github.com/de/actions>`_ und `GitHub
        Pages <https://pages.github.com>`_ Erweiterungen für kontinuierliche
        Integration und statische Websites.

    GitLab
        Web-Anwendung zur Versionsverwaltung auf Basis von :term:`git`. Später
        kamen :doc:`advanced/gitlab/ci-cd/index`, ein System zur
        kontinuierlichen Integration, GitLab Runner,
        :doc:`advanced/gitlab/package-registry`,
        :doc:`advanced/gitlab/ci-cd/pages` und vieles andere hinzu.

        .. seealso::
           * :doc:`advanced/gitlab/index`

    ``HEAD``
        Der ``HEAD``-Zeiger repräsentiert euer aktuelles Arbeitsverzeichnis und
        kann mit ``git switch`` in verschiedene Zweige, Tags oder Commits
        verschoben werden.

    Index
        Eine Sammlung von Dateien mit Statusinformationen, deren Inhalt als
        Objekte gespeichert wird. Der Index ist eine gespeicherte Version eures
        :term:`Working Tree`.

    Merge-Request
        Ort zum Vergleichen und Diskutieren der in einem Branch eingeführten
        Änderungen mit Bewertungen, Kommentaren, Tests :abbr:`etc. (et cetera)`;

        .. seealso::
           * :doc:`advanced/gitlab/merge-requests`.
           * :ref:`Merge- oder Pull-Requests <merge-pull-requests>`.

    ``origin``
        Das übliche Upstream-Repository. Die meisten Projekte haben mindestens
        ein Upstream-Projekt, das sie verfolgen. Standardmäßig wird ``origin``
        für diesen Zweck verwendet. Neue Upstream-Aktualisierungen werden in
        Zweige mit dem Namen :samp:`origin/{NAME_OF_UPSTREAM_BRANCH}` geholt,
        die ihr mit ``git branch -r`` sehen könnt.

    Remote Repository
        Gemeinsames Repository, :abbr:`z.B. (zum Beispiel)` auf :term:`GitLab`,
        zum Austausch von Änderungen in einem Team.

    Trunk-Based Development
    TBD
        Git-Workflow mit kurzlebigen Themenzweigen, die schnell zum einem
        einzigen ``main``-Zweig zusammengeführt werden.

        .. seealso::
           * :doc:`workflows/tbd`

    Working Tree
        Der Baum der tatsächlich ausgecheckten Dateien. Der Arbeitsbaum enthält
        normalerweise den Inhalt des :term:`HEAD`-Commit-Baums sowie alle
        lokalen Änderungen, die ihr vorgenommen, aber noch nicht übertragen
        habt.
