.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git-Glossar
===========

.. glossary::

    Blob

        .. _start-blob

        Ein Blob-Objekt enthält den Inhalt einer Datei.

        Bei jedem :term:`Commit` speichert Git den gesamten Inhalt jeder Datei,
        den ihr geändert habt, als Blob. Wenn ihr beispielsweise einen Commit
        habt, der zwei Dateien in einem Repository ändert, erstellt dieser
        Commit zwei neue Blobs, sodass Commits selbst in sehr großen
        Repositories relativ wenig Speicherplatz beanspruchen.

        .. _end-blob

    Branch
    Zweig
        Ein Zweig ist eine Entwicklungslinie. Der letzte :term:`Commit` auf
        einem Zweig wird als Spitze des Zweiges bezeichnet, der durch einen
        :term:`HEAD` referenziert wird und der sich weiterbewegt, wenn weitere
        Entwicklungen auf dem Zweig vorgenommen werden. Ein einzelnes
        Git-Repository kann eine beliebige Anzahl von Zweigen haben, aber ihr
        :term:`Working Tree` ist nur mit einem von ihnen verbunden –  dem
        *aktuellen* oder *ausgecheckten* Zweig – und :term:`HEAD` zeigt auf
        diesen Zweig.

    Cache
        Veraltet für :term:`Index`.

    Clone
    Klon
        Lokale Version eines Repository einschließlich aller :term:`Commits
        <Commit>` und :term:`Branches <Branch>`.

    Commit

        .. _start-commit

        Ein Commit ist ein Snapshot des gesamten Git-Repository, der durch einen
        `SHA <https://de.wikipedia.org/wiki/Secure_Hash_Algorithm>`_-Wert
        eindeutig identifiziert werden kann und mindestens die folgenden
        Angaben enthält:

        * Verzeichnisstruktur aller Dateien dieser Version des Repositorys und
          Inhalt jeder Datei, gespeichert als :term:`Tree`-ID des obersten
          Verzeichnisses des Commits.
        * ID(s) des oder der übergeordneten Commits. Der erste Commit eines
          Repository hat keine übergeordneten Commits, reguläre Commits haben
          einen übergeordneten Commit, Merge-Commits haben zwei oder mehr
          übergeordnete Commits.
        * Autor*in und Zeitpunkt, zu dem der Commit erstellt wurde.
        * Committer und Zeitpunkt, zu dem der Commit committet wurde.
        * Commit-Nachricht

        Beispiel:

        .. code-block:: console

           $ git cat-file -p main
           tree 47cc0283b10bd5e4e8a0d61537d13bba3bfad916
           parent 63825a43e213ef8a7904a8994976ac86284d32bd
           author veit <veit@cusy.io> 1770370977 +0100
           committer veit <veit@cusy.io> 1770370977 +0100

           :memo: Add links to Python speed

        Wie alle anderen Objekte können auch Commits nach ihrer Erstellung nicht
        mehr geändert werden. Wenn ihr also einen Commit mit ``git commit
        --amend`` ändern wollt, wird tatsächlich ein neuer Commit mit demselben
        Parent erstellt. Und auch wenn ihr euch einen Commit mit ``git show``
        anzeigen lasst, so wird das Diff zu diesem Zeitpunkt erst berechnet.

        .. seealso::
           * `Commits are snapshots, not diffs
             <https://github.blog/open-source/git/commits-are-snapshots-not-diffs/>`_

        .. _end-commit

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
        kann mit ``git switch`` in verschiedene :term:`Zweige <Zweig>`,
        :doc:`Tags <tag>` oder :term:`Commits <Commit>` verschoben werden.

    Index
    Staging Area

        .. _start-index

        Liste von Dateien und deren Inhalten, die als :term:`Blob` gespeichert
        sind. Mit ``git add`` könnt ihr Dateien zum Index hinzufügen oder den
        Inhalt einer Datei im Index aktualisieren.

        Im Gegensatz zu einem :term:`Tree` ist der Index eine flache Liste von
        Dateien. Wenn ihr committet, konvertiert Git die Liste der Dateien im
        Index in einen Verzeichnisbaum und verwendet diesen Baum für den neuen
        Commit. Jeder Indexeintrag hat vier Felder:

        #. Einer der folgenden vier Dateitypen:

           * reguläre Datei
           * ausführbare Datei
           * symbolischer Link
           * gitlink (für Submodule)

        #. Blob-ID der Datei oder Commit-ID des Submoduls
        #. Staging-Nummer, normalerweise ``0``. Bei einen Merge-Konflikt kann es
           jedoch auch mehrere Versionen desselben Dateinamens im Index geben.
        #. Dateipfad

        .. _end-index

    Merge-Request
        Ort zum Vergleichen und Diskutieren der in einem Branch eingeführten
        Änderungen mit Bewertungen, Kommentaren, Tests :abbr:`etc. (et cetera)`;

        .. seealso::
           * :doc:`advanced/gitlab/merge-requests`
           * :ref:`Merge- oder Pull-Requests <merge-pull-requests>`

    Objekt

        .. _start-object

        Alle :term:`Commits <Commit>`, :term:`Trees <Tree>`, :term:`Blobs
        <Blob>` und :term:`Tags <Tag-Objekt>` in einem Git-Repository werden als
        Git-Objekte gespeichert, die sich nach ihrer Erstellung nie mehr ändern
        und eine eindeutige ID haben, :abbr:`z. B. (zum Beispiel)`
        ``3a5c279ea2f5d18498b61c229571d2449305a0``. :abbr:`D. h. (Das heißt)`,
        dass ihr mit der ID eines Objekts jederzeit dessen Inhalt
        wiederherstellen könnt, solange das Objekt nicht gelöscht wurde.

        .. seealso::
           * `Git Internals - Git Objects
             <https://git-scm.com/book/en/v2/Git-Internals-Git-Objects>`_

        .. _end-object

    ``origin``
        Das übliche Upstream-Repository. Die meisten Projekte haben mindestens
        ein Upstream-Projekt, das sie verfolgen. Standardmäßig wird ``origin``
        für diesen Zweck verwendet. Neue Upstream-Aktualisierungen werden in
        Zweige mit dem Namen :samp:`origin/{NAME_OF_UPSTREAM_BRANCH}` geholt,
        die ihr mit ``git branch -r`` sehen könnt.

    Packfile

        .. _start-packfile

        Das Format, in dem Git Objekte auf der Festplatte speichert, wird als
        *loose*-Objektformat bezeichnet. Um Platz zu sparen packt Git
        gelegentlich jedoch mehrere dieser Objekte in eine einzige Binärdatei,
        die als Packfile bezeichnet wird, um Platz zu sparen und effizienter
        arbeiten zu können. Ihr könnt das Packen auch manuell mit ``git push``
        oder ``git gc`` ausführen. Dadurch werden in :file:`.git/objects/` die
        meisten eurer Objekte gelöscht und ein neues Dateipaar erstellt:

        .. code-block:: console

           $ find .git/objects -type f
           .git/objects/pack/pack-e9282cda3898f806f7bd108a3675c9e4d236915c.pack
           .git/objects/pack/pack-e9282cda3898f806f7bd108a3675c9e4d236915c.idx

        :file:`*.pack`
            enthält den Inhalt aller Objekte, die aus eurem Dateisystem entfernt
            wurden.
        :file:`.idx`
            enthält die Offsets dieser Packdatei, sodass schnell zu einem
            bestimmten Objekt gespringen werden kann.

        :abbr:`Ggf. (Gegebenenfalls)` verbleibende Objekte sind :term:`Blobs
        <Blob>`, auf die kein Commit verweist, :abbr:`sog. (sogenannte)`
        *dangling references*, :abbr:`z. B. (zum Beispiel)` Dateien im
        Arbeitsverzeichnis, die nie zu einem Commit hinzugefügt wurden.

        Wenn Git Objekte packt, sucht es nach Dateien mit ähnlichen Namen und
        Größen und speichert nur die Deltas von einer Version der Datei zur
        nächsten. Mit ``git verify-pack`` könnt ihr euch das Packfile ansehen
        und erkennen, wie Git Speicherplatz sparte:

        .. code-block:: console

           $ git verify-pack -v .git/objects/pack/pack-e9282cda3898f806f7bd108a3675c9e4d236915c.pack
           ...
           dd1827ebf73b22d9f5828eec005eda4d79520f57 blob   147 140 389838
           0a66f9a9ab72e3a99994803de8337f523b1b93d0 blob   31 43 389978 1 dd1827ebf73b22d9f5828eec005eda4d79520f57
           ...
           .git/objects/pack/pack-e9282cda3898f806f7bd108a3675c9e4d236915c.pack: ok

        * :term:`Blob` ``0a66f9a`` verweist auf den nachfolgenden Blob
          ``dd1827e``.
        * Die dritte Spalte gibt die Größe des Objekts im Packfile an, sodass
          ihr sehen könnt, dass ``dd1827e`` 147 Bytes einnimmt, während
          ``0a66f9a`` nur 31 Bytes einnimmt.
        * Die aktuelle Datei wird also unverändert gespeichert, während die
          ursprüngliche Version als Delta gespeichert ist. Dies erlaubt einen
          schnelleren Zugriff auf die jeweils neueste Version einer Datei.
        * Die allgemeine Syntax von ``git verify-pack -v`` ist:

          :samp:`{OBJECT-ID} {TYPE} {SIZE} {SIZE-IN-PACKFILE} {OFFSET-IN-PACKFILE} [{DEPTH} {BASE-ID}]`

        .. seealso::
           * `Git Internals - Packfiles
             <https://git-scm.com/book/en/v2/Git-Internals-Packfiles>`_
           * `git verify-pack <https://git-scm.com/docs/git-verify-pack>`_

        .. _end-packfile

    Referenz

        .. _start-refs

        Referenzen sind eine Möglichkeit, Commits einen Namen zu geben, der
        einfacher, zu merken ist, :abbr:`z. B. (zum Beispiel)` für :doc:`Zweige
        </productive/git/branch>`, :doc:`Tags </productive/git/tag>`,
        :ref:`remote-branches` :abbr:`u.s.w. (und so weiter)` Git verwendet
        häufig ``ref`` als Abkürzung für solche Referenzen. Die wichtigsten
        Referenzen sind:

        :samp:`.git/refs/heads/{BRANCHNAME}`
            Ein Branch bezieht sich auf die ID des neuesten Commits auf diesem
            Branch. Um die Historie der :term:`Commits <Commit>` auf einem
            :term:`Branch` abzurufen, beginnt Git bei der Commit-ID, auf die der
            Branch verweist, und sieht sich dann die übergeordneten Commits an.
            Referenzen können sich beziehen auf

            * eine Objekt-ID, in der Regel eine Commit-ID
            * eine andere, *symbolische* Referenz

        :samp:`.git/refs/tags/{TAGNAME}`
            Ein Tag bezieht sich auf eine Commit-ID, eine Tag-Objekt-ID oder
            eine andere Objekt-ID.

        ``.git/HEAD``
            :term:`HEAD` ist der Ort, an dem Git euren aktuellen :term:`Branch`
            speichert. ``HEAD`` kann entweder

            * eine symbolische Referenz auf euren aktuellen Branch sein,
              :abbr:`z.B. (zum Beispiel)` ``ref: refs/heads/main``.
            * eine direkte Referenz auf eine Commit-ID wenn es keinen aktuellen
              Branch gibt, also in einem *detached HEAD state*.

        :samp:`.git/refs/remotes/{REMOTE}/{BRANCHNAME}`
            Ein :ref:`Remote-Tracking-Branch <remote-branches>` bezieht sich auf
            eine Commit-ID. Mit ``git fetch`` könnt ihr diese :abbr:`ggf.
            (gegebenenfalls)` aktualisieren und wenn ``git status`` ``Your
            branch is up to date with 'origin/main'`` ausgibt, bezieht es sich
            darauf.

            ``refs/remotes/{REMOTE}/HEAD`` ist eine symbolische Referenz auf den
            Standard-Zweig des Remote-Repositories.

        .. seealso::
           * `Git Internals - Git References
             <https://git-scm.com/book/en/v2/Git-Internals-Git-References>`_

        .. _end-refs:

    Reflog

        .. _start-reflog

        Jedes Mal, wenn ein :term:`Branch`, ein :ref:`Remote-Tracking-Branch
        <remote-branches>` oder :term:`HEAD` aktualisiert wird, aktualisiert Git
        ein Protokoll namens *Reflog* für diese Referenz, :abbr:`z.B. (zum Beispiel)` in :file:`.git/logs/refs/heads/main`:

        .. code-block:: console

           0000000000000000000000000000000000000000 492e16edcf9cdb3371492be59735e517a17cc86c veit <veit@cusy.io> 1739549686 +0100  clone: from github.com:cusyio/Python4DataScience-de.git
           492e16edcf9cdb3371492be59735e517a17cc86c c40bfa2a238e824b619f760494ce5ce0769851c3 veit <veit@cusy.io> 1739549907 +0100  commit: Update git docs
           c40bfa2a238e824b619f760494ce5ce0769851c3 fa39661bb7fa93b420870845cb174529e8d62552 veit <veit@cusy.io> 1739549971 +0100  rebase (finish): refs/heads/main onto b7214df753ecbd01acd90d8f3dcd359e02441249
           ...

        Jeder Eintrag des Reflog enthält:

        * Commit-ID
        * Commit-ID des nachfolgenden Commits
        * Autor*in
        * E-Mail-Adresse
        * Zeitstempel, zu dem die Änderung vorgenommen wurde
        * Protokollmeldung, :abbr:`z. B. (zum Beispiel)`:

          * :samp:`clone: from {REMOTE-URL}`
          * :samp:`commit: {COMMIT-MESSAGE}`
          * :samp:`rebase (finish): refs/heads/main onto {BASIC-COMMIT-ID}`

        Reflogs protokollieren Änderungen, die in eurem lokalen Repository
        vorgenommen wurden. Sie werden jedoch nicht im :term:`Remote Repository`
        geteilt.

        .. seealso::
           * :ref:`reflog`

        .. _end-reflog

    Remote Repository
        Gemeinsames Repository, :abbr:`z.B. (zum Beispiel)` auf :term:`GitLab`,
        zum Austausch von Änderungen in einem Team.

    Tag-Objekt

        .. _start-tag

        Tag-Objekte enthalten mindestens die folgenden Felder:

        * ID des Objekts, auf das es verweist
        * Typ des Objekts, auf das es verweist
        * Tag-Nachricht
        * Tagger und Tag-Datum

        Beispiel:

        .. code-block:: console

           $ git cat-file -p 24.3.0
           object aa366cc9af3497544338482f82bdeb21f1dd3c21
           type commit
           tag 24.3.0
           tagger Veit Schiele <veit@cusy.io> 1732086922 +0100

        .. _end-tag

    Tree

        .. _start-tree

        Darstellung eines Verzeichnisses in Git und kann Dateien oder andere
        Bäume (also Unterverzeichnisse) enthalten. Für jedes Element im Baum
        listet er Folgendes auf:

        * Dateiname
        * Dateityp:

          * normale Datei
          * ausführbare Datei
          * symbolischer Link
          * Verzeichnis
          * Gitlink (für Submodule)

        * Objekt-ID mit dem Inhalt der Datei, des Verzeichnisses oder des
          gitlinks

        Beispiel:

        .. code-block:: console

           $ git cat-file -p main^{tree}
           040000 tree 2f59a223f7dc767f4776e77762d208fa72bfd343 .dvc
           040000 tree 75833fd33271db55b6f1c96915f60f98a60b51a0 .github
           100644 blob 36d2dc5a5228cbf65b8cfe913565c9be49db1a3d .gitignore
           ...
           $ git cat-file -p 2f59a223f7dc767f4776e77762d208fa72bfd343
           100644 blob 669784da1fe0818e9abb795f73b7faf393832f2e .gitignore
           100644 blob 0a66f9a9ab72e3a99994803de8337f523b1b93d0 config
           $ git cat-file -p 36d2dc5a5228cbf65b8cfe913565c9be49db1a3d
           # SPDX-FileCopyrightText: 2019 Veit Schiele
           #
           # SPDX-License-Identifier: BSD-3-Clause
           ...

        .. hint::
           Die erste Spalte eines Baum-Eintrags orientiert sich grob an den
           `Unix-Dateirechten
           <https://de.wikipedia.org/wiki/Unix-Dateirechte>`_, tatsächlich
           können mit Git jedoch keine Unix-Dateirechte verwaltet werden. Hierzu
           sind Erweiterungen, wie :abbr:`z.B. (zum Beispiel)`
           :doc:`/productive/git/advanced/etckeeper` erforderlich.

        .. _end-tree

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
