``git-big-picture``
===================

``git-big-picture`` visualisiert Git-Repositories als DAGs. Das Tool kommt mit
einigen Filtern um sich nur die interessanten Bereiche anzeigen zu lassen, z.B.
nur die Hierarchie von Tags und Branches.

Beispiel
--------

Hier ist ein Beispiel des Jupyter-Tutorial mit Merges aber ohne Tags:

.. image:: git-big-picture7r6bxfcw.svg
   :alt: Git-Graph mit Merges aber ohne Tags
   :width: 171 px
   :height: 1374 px

Installation
------------

Ihr könnt ``git-big-picture`` einfach installieren mit:

.. code-block:: console

    $ pipenv install git-big-picture
    Installing git-big-picture…
    Adding git-big-picture to Pipfile's [packages]…
    ✔ Installation Succeeded
    …

Git-Integration
---------------

Ihr könnt das Tool einfach in Git integrieren indem Ihr das Skript
``git-big-picture`` einfach ``$PATH`` hinzufügt. Anschließend könnt Ihr es
verwenden z.B. mit:

.. code-block:: console

    $ git big-picture -h
    Usage: git-big-picture OPTIONS [<repo-directory>]

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      --pstats=FILE         run cProfile profiler writing pstats output to FILE
      -d, --debug           activate debug output

      Output Options:
        Options to control output and format

        -f FMT, --format=FMT
                            set output format [svg, png, ps, pdf, ...]
        -g, --graphviz      output lines suitable as input for dot/graphviz
        -G, --no-graphviz   disable dot/graphviz output
        -p, --processed     output the dot processed, binary data
        -P, --no-processed  disable binary output
        -v CMD, --viewer=CMD
                            write image to tempfile and start specified viewer
        -V, --no-viewer     disable starting viewer
        -o FILE, --outfile=FILE
                            write image to specified file
        -O, --no-outfile    disable writing image to file

      Filter Options:
        Options to control commit/ref selection

        -a, --all           include all commits
        -b, --branches      show commits pointed to by branches
        -B, --no-branches   do not show commits pointed to by branches
        -t, --tags          show commits pointed to by tags
        -T, --no-tags       do not show commits pointed to by tags
        -r, --roots         show root commits
        -R, --no-roots      do not show root commits
        -m, --merges        include merge commits
        -M, --no-merges     do not include merge commits
        -i, --bifurcations  include bifurcation commits
        -I, --no-bifurcations
                            do not include bifurcation commits

Konfiguration
-------------

Die Standard-``git config``-Infrastruktur kann verwendet werden um auch
``git-big-picture`` zu konfigurieren. Die meisten Kommandozeilen-Argumente
können konfiguriert werden im  ``[big-picture]``-Abschnitt, z.B. um Firefox als
Viewer zu konfigurieren

.. code-block:: console

    $ git config --global big-picture.viewer firefox

erstellt den folgenden Abschnitt in Eurer ``~/.gitconfig``-Datei:

.. code-block:: ini

    [big-picture]
        viewer = firefox

.. note::
  Bitte beachtet jedoch, dass Ihr dann keine  anderen Optionen mehr auswählen
  könnt. So könnt Ihr nun den Graph nicht mehr als Graphviz ausgeben lassen:

  .. code-block:: console

    $ git-big-picture -g
    fatal: Options '-g | --graphviz' and '-p | --processed' are incompatible with other output options.

  In diesem Fall müsst Ihr dann die ``-V`` oder ``--no-viewer``-Option wählen:

  .. code-block:: console

    $ git-big-picture -g -V
    digraph {
        "c509669a01b156900eed9f1c9f927b6d2f7bb95b"[label="origin/pyup-scheduled-update-2020-11-16", color="/pastel13/2", style=filled];
    …
