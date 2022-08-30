Git flow
========

Git Flow war einer der ersten Vorschläge zur Verwendung von Git-Branches. Es
empfahl einen ``main``-Branch und einen separaten ``develop``-Branch sowie
diverse weitere Branches für Features, Releases und Hotfixes. Die verschiedenen
Entwicklungen sollten im ``develop``-Branch zusammengeführt werden, anschließend
in den ``release``-Branch überführt werden und schließlich im ``main``-Branch
landen. So ist Git Flow zwar ein wohldefinierter, aber komplexer Standard, der
praktisch die folgenden beiden Probleme hat:

* Die meisten Entwickler und Werkzeuge gehen von der Annahme aus, dass der
  ``main``-Branch der Hauptzweig ist von dem aus ``branch`` und ``merge``
  ausgeführt wird. Bei Git Flow entsteht nun zusätzlicher Aufwand da immer
  zunächst in den ``develop``-Branch gewechselt werden muss.
* Auch die ``hotfixes``- und ``release``-Branches bringen eine zusätzliche
  Komplexität, die nur in den seltensten Fällen Vorteile bringen dürfte.

Als Reaktion auf die Probleme von Git Flow entwickelten `GitHub
<https://guides.github.com/introduction/flow/>`_ und `Atlassian
<https://www.atlassian.com/de/git/tutorials/comparing-workflows>`_ einfachere
Alternativen, die sich meist auf sog. :doc:`feature-branches` beschränken.

.. seealso::
   `Vincent Driessen: A successful Git branching model
   <https://nvie.com/posts/a-successful-git-branching-model/>`_

Erste Schritte
--------------

Git-flow ist nur eine abstrakte Vorstellung eines Git-Workflows, bei dem die
Zweige und die Zusammenführung vorgegeben werden. Es gibt mit git-flow auch
Software, die bei diesem Workflow unterstützen soll.

Installation
~~~~~~~~~~~~

.. tab:: Windows

    .. code-block:: ps1con

        $ wget -q -O - --no-check-certificate https://github.com/nvie/gitflow/raw/develop/contrib/gitflow-installer.sh | bash

.. tab:: Debian/Ubuntu

   .. code-block:: console

        $ sudo apt install git-flow

.. tab:: macOS

    .. code-block:: console

        $ brew install git-flow

Initialisieren
~~~~~~~~~~~~~~

``git-flow`` ist ein :abbr:`sog. (sogenannter)` Wrapper für Git. Dabei initiiert
der Befehl ``git flow init`` nicht nur ein Verzeichnis, sondern erstellt auch
Verzweigungen für Dich:

.. code-block:: console

    $ git flow init
    Leeres Git-Repository in /home/veit/my_repo/.git/ initialisiert
    No branches exist yet. Base branches must be created now.
    Branch name for production releases: [master] main
    Branch name for "next release" development: [develop]

    How to name your supporting branch prefixes?
    Feature branches? [feature/]
    Bugfix branches? [bugfix/]
    Release branches? [release/]
    Hotfix branches? [hotfix/]
    Support branches? [support/]
    Version tag prefix? []
    Hooks and filters directory? [.git/hooks]

Alternativ hättet ihr auch folgendes eingeben können:

.. code-block:: console

    $ git branch develop
    $ git push -u origin develop

.. graphviz::

    strict digraph Gitflow {
    nodesep=0.5;
    ranksep=0.25;
    splines=line;
    forcelabels=false;

    // general
    node [style=filled, color="black",
        fontcolor="black", font="Consolas", fontsize="8pt" ];
    edge [arrowhead=vee, color="black", penwidth=2];

    // tags
    node [shape=cds, fixedsize=false, fillcolor="#C6C6C6", penwidth=1, margin="0.11,0.055"]
    tag01 [label="0.1"]
    tag02 [label="0.2"]
    tag10 [label="1.0"]

    // graph
    node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

    // branches
    node  [group="main", fillcolor="#27E4F9"];
    main1;
    main2;
    main3;
    main4;
    subgraph {
        rank=source;
        mainstart [label="", width=0, height=0, penwidth=0];
    }
    mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    main1 -> main2 -> main3 -> main4;

    node  [group="develop", fillcolor="#FFE333"];
    develop1;
    develop2;
    develop3;
    develop4;
    develop5;
    develop1 -> develop2 -> develop3 -> develop4 -> develop5;

    // branching and merging
    main1 -> develop1;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> main1;
    }
    subgraph  {
        rank="same";
        tag02 -> main2;
    }
    subgraph  {
        rank="same";
        tag10 -> main3;
    }
    }

Dieser Workflow sieht zwei Zweige vor, um die Historie des Projekts
aufzuzeichnen:

``main``
    enthält den offiziellen Release-Verlauf, wobei alle Commits in diesem Zweig
    mit einer Versionsnummer getaggt sein sollten.
``develop``
    integriert die Features.

Feature-Branches
~~~~~~~~~~~~~~~~

Jedes neue Feature sollte in einem eigenen Branch erstellt werden, der jederzeit
zum entfernten Repository gepusht werden kann. Dabei wird ein Feature-Branch
jedoch nicht aus dem ``main``-Branch erstellt sondern aus dem
``develop``-Branch; und wenn ein Feature fertig ist, wird es auch zurück in den
``develop``-Branch gemergt.

.. graphviz::

    strict digraph Gitflow {
    nodesep=0.5;
    ranksep=0.25;
    splines=line;
    forcelabels=false;

    // general
    node [style=filled, color="black",
        fontcolor="black", font="Consolas", fontsize="8pt" ];
    edge [arrowhead=vee, color="black", penwidth=2];

    // tags
    node [shape=cds, fixedsize=false, fillcolor="#C6C6C6", penwidth=1, margin="0.11,0.055"]
    tag01 [label="0.1"]
    tag02 [label="0.2"]
    tag10 [label="1.0"]

    // graph
    node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

    // branches
    node  [group="main", fillcolor="#27E4F9"];
    main1;
    main2;
    main3;
    main4;
    subgraph {
        rank=source;
        mainstart [label="", width=0, height=0, penwidth=0];
    }
    mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    main1 -> main2 -> main3 -> main4;

    node  [group="develop", fillcolor="#FFE333"];
    develop1;
    develop2;
    develop3;
    develop4;
    develop5;
    develop6;
    develop7;
    develop8;
    develop9;
    develop10;
    develop1 -> develop2 -> develop3 -> develop4 -> develop5 -> develop6 -> develop7 -> develop8 -> develop9 -> develop10;

    node  [group="17-some-feature", fillcolor="#FB3DB5"];
    feature101;
    feature102;
    feature103;
    feature114;
    feature115;
    feature116;
    subgraph features0 {
        feature101 -> feature102 -> feature103;
    }
    subgraph features1 {
        feature114 -> feature115 -> feature116;
    }

    node  [group="42-other-feature", fillcolor="#FB3DB5"];
    feature201;
    feature202;
    feature203;
    feature204;
    subgraph{ rank=same; feature101; feature201; }
    subgraph{ rank=same; feature116; feature204; }
    feature201 -> feature202 -> feature203 -> feature204;

    // branching and merging
    main1 -> develop1;

    develop3 -> feature101;
    feature103 -> develop6;

    develop7 -> feature114;
    feature116 -> develop9;

    develop3 -> feature201;
    feature204 -> develop9;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> main1;
    }
    subgraph  {
        rank="same";
        tag02 -> main2;
    }
    subgraph  {
        rank="same";
        tag10 -> main3;
    }
    }

Ihr könnt solche Feature-Branches erstellen mit ``git flow``

.. code-block:: console

    $ git flow feature start 17-some-feature
    Zu neuem Branch 'feature/17-some-feature' gewechselt

    Summary of actions:
    - A new branch 'feature/17-some-feature' was created, based on 'develop'
    - You are now on branch 'feature/17-some-feature'
    …

… oder mit

.. code-block:: console

    $ git switch -c feature/17-some-feature
    Zu neuem Branch 'feature/17-some-feature' gewechselt

Umgekehrt könnt ihr euren Feature-Branch abschließen mit

.. code-block:: console

    $ git flow feature finish 17-some-feature
    Zu Zweig »develop« gewechselt
    Bereits aktuell.
    Branch feature/17-some-feature entfernt (war 653e88a).
    …

… oder mit

.. code-block:: console

    $ git switch develop
    $ git merge feature/17-some-feature
    $ git branch -d feature/17-some-feature
    Branch feature/17-some-feature entfernt (war 11a9417).

Release-Branches
~~~~~~~~~~~~~~~~

Wenn der ``develop``-Branch genügend Features für ein Release enthält oder ein
festgelegter Release-Termin ansteht, wird vom ``develop``-Branch ein
``release``-Branch erstellt, zu dem ab diesem Zeitpunkt keine neuen Features
mehr hinzukommen sollten, sondern nur noch Bugfixes und auf dieses Release
bezogene Änderungen. Kann das Release ausgeliefert werden, wird der
``release``-Branch einerseits in den ``main``-Branch gemergt und mit einer
Versionsnummer getaggt, andererseits zurück in den ``develop``-Branch gemergt,
der sich seit der Erstellung des ``release``-Branch weiterentwickelt haben
dürfte.

.. code-block:: console

    $ git flow release start 0.1.0
    Zu neuem Branch 'release/0.1.0' gewechselt
    …
    $ git flow release finish '0.1.0'
    Zu Zweig »main« gewechselt
    …
    Branch release/0.1.0 entfernt (war 11a9417).

    Summary of actions:
    - Release branch 'release/0.1.0' has been merged into 'main'
    - The release was tagged '0.1.0'
    - Release tag '0.1.0' has been back-merged into 'develop'
    - Release branch 'release/0.1.0' has been locally deleted
    - You are now on branch 'develop'

… oder

.. code-block:: console

    $ git switch develop
    $ git branch develop/0.1.0
    …
    $ git switch main
    $ git merge release/0.1.0
    $ git tag -a 0.1.0
    $ git switch develop
    $ git merge release/0.1.0
    $ git branch -d release/0.1.0

.. graphviz::

    strict digraph Gitflow {
    nodesep=0.5;
    ranksep=0.25;
    splines=line;
    forcelabels=false;

    // general
    node [style=filled, color="black",
        fontcolor="black", font="Consolas", fontsize="8pt" ];
    edge [arrowhead=vee, color="black", penwidth=2];

    // tags
    node [shape=cds, fixedsize=false, fillcolor="#C6C6C6", penwidth=1, margin="0.11,0.055"]
    tag01 [label="0.1"]
    tag02 [label="0.2"]
    tag10 [label="1.0"]

    // graph
    node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

    // branches
    node  [group="main", fillcolor="#27E4F9"];
    main1;
    main2;
    main3;
    main4;
    subgraph {
        rank=source;
        mainstart [label="", width=0, height=0, penwidth=0];
    }
    mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    main1 -> main2 -> main3 -> main4;

    node  [group="releases", fillcolor="#52C322"];
    release1;
    release2;
    release3;
    release4;
    release5;
    release1 -> release2 -> release3 -> release4;

    node  [group="develop", fillcolor="#FFE333"];
    develop1;
    develop2;
    develop3;
    develop4;
    develop5;
    develop6;
    develop7;
    develop8;
    develop9;
    develop10;
    develop1 -> develop2 -> develop3 -> develop4 -> develop5 -> develop6 -> develop7 -> develop8 -> develop9 -> develop10;

    node  [group="17-some-feature", fillcolor="#FB3DB5"];
    feature101;
    feature102;
    feature103;
    feature114;
    feature115;
    feature116;
    subgraph features0 {
        feature101 -> feature102 -> feature103;
    }
    subgraph features1 {
        feature114 -> feature115 -> feature116;
    }

    node  [group="42-other-feature", fillcolor="#FB3DB5"];
    feature201;
    feature202;
    feature203;
    feature204;
    subgraph{ rank=same; feature101; feature201; }
    subgraph{ rank=same; feature116; feature204; }
    feature201 -> feature202 -> feature203 -> feature204;

    // branching and merging
    main1 -> develop1;

    develop3 -> feature101;
    feature103 -> develop6;
    develop6 -> release1;
    release2 -> develop7;

    release4 -> develop8;
    release4 -> main3;

    develop9 -> release5;
    release5 -> main4;
    release5 -> develop10;

    develop7 -> feature114;
    feature116 -> develop9;

    develop3 -> feature201;
    feature204 -> develop9;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> main1;
    }
    subgraph  {
        rank="same";
        tag02 -> main2;
    }
    subgraph  {
        rank="same";
        tag10 -> main3;
    }
    }

Hotfix-Branches
~~~~~~~~~~~~~~~

Hotfix-Branches eignen sich für schnelle Patches von Produktion-Versionen. Sie
sind Release-Branches und Feature-Branches ähnlich, basieren jedoch auf dem
``main``- statt auf dem ``develop``-Branch. Damit ist er der einzige Branch, der
direkt vom ``main``-Branch geforkt werden sollte. Sobald der Hotfix
abgeschlossen wurde, sollte er sowohl in den ``main``- als auch in den
``develop``-Branch und :abbr:`ggf. (gegebenenfalls)` in den aktuellen
``release``-Branch gemergt werden. Der ``main``-Branch sollte außerdem mit einer
neuen Versionsnummer getaggt werden.

.. code-block:: console

    $ git flow hotfix finish 37-some-bug
    Zu Zweig »develop« gewechselt
    Merge made by the 'recursive' strategy.
     …
    Branch hotfix/37-some-bug entfernt (war ca0814e).

    Summary of actions:
    - Hotfix branch 'hotfix/37-sombe-bug' has been merged into 'main'
    - The hotfix was tagged '0.2.0'
    - Hotfix tag '0.2.0' has been back-merged into 'develop'
    - Hotfix branch 'hotfix/37-some-bug' has been locally deleted
    - You are now on branch 'develop'

… oder

.. code-block:: console

    $ git switch main 
    Zu Zweig »main« gewechselt
    …
    $ git merge hotfix/37-some-bug
    $ git tag -a 0.2.0
    $ git switch develop
    $ git merge hotfix/37-some-bug
    $ git branch -d hotfix/37-some-bug

.. graphviz::

    strict digraph Gitflow {
    nodesep=0.5;
    ranksep=0.25;
    splines=line;
    forcelabels=false;

    // general
    node [style=filled, color="black",
        fontcolor="black", font="Consolas", fontsize="8pt" ];
    edge [arrowhead=vee, color="black", penwidth=2];

    // tags
    node [shape=cds, fixedsize=false, fillcolor="#C6C6C6", penwidth=1, margin="0.11,0.055"]
    tag01 [label="0.1"]
    tag02 [label="0.2"]
    tag10 [label="1.0"]

    // graph
    node [width=0.2, height=0.2, fixedsize=true, label="", margin="0.11,0.055", shape=circle, penwidth=2, fillcolor="#FF0000"]

    // branches
    node  [group="main", fillcolor="#27E4F9"];
    main1;
    main2;
    main3;
    main4;
    subgraph {
        rank=source;
        mainstart [label="", width=0, height=0, penwidth=0];
    }
    mainstart -> main1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    main1 -> main2 -> main3 -> main4;
    main4 -> mainend [color="#b0b0b0", style=dashed, arrowhead=none ];

    node  [group="hotfix", fillcolor="#FD5965"];
    hotfix1;

    node  [group="release", fillcolor="#52C322"];
    release1;
    release2;
    release3;
    release4;
    release5;
    release1 -> release2 -> release3 -> release4;

    node  [group="develop", fillcolor="#FFE333"];
    develop1;
    develop2;
    develop3;
    develop4;
    develop5;
    develop6;
    develop7;
    develop8;
    develop9;
    develop10;
    develop1 -> develop2 -> develop3 -> develop4 -> develop5 -> develop6 -> develop7 -> develop8 -> develop9 -> develop10;
    develop10 -> developend [color="#b0b0b0", style=dashed, arrowhead=none ];

    node  [group="17-some-feature", fillcolor="#FB3DB5"];
    feature101;
    feature102;
    feature103;
    feature114;
    feature115;
    feature116;
    subgraph features0 {
        feature101 -> feature102 -> feature103;
    }
    subgraph features1 {
        feature114 -> feature115 -> feature116;
    }

    node  [group="42-other-feature", fillcolor="#FB3DB5"];
    feature201;
    feature202;
    feature203;
    feature204;
    subgraph{ rank=same; feature101; feature201; }
    subgraph{ rank=same; feature116; feature204; }
    feature201 -> feature202 -> feature203 -> feature204;

    // branching and merging
    main1 -> develop1;

    main1 -> hotfix1;
    hotfix1 -> main2;
    hotfix1 -> develop5;

    develop3 -> feature101;
    feature103 -> develop6;
    develop6 -> release1;
    release2 -> develop7;

    release4 -> develop8;
    release4 -> main3;

    develop9 -> release5;
    release5 -> main4;
    release5 -> develop10;

    develop7 -> feature114;
    feature116 -> develop9;

    develop3 -> feature201;
    feature204 -> develop9;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> main1;
    }
    subgraph  {
        rank="same";
        tag02 -> main2;
    }
    subgraph  {
        rank="same";
        tag10 -> main3;
    }
    }
