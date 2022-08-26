===========================
Git flow und seine Probleme
===========================

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
    node  [group="master", fillcolor="#27E4F9"];
    master1;
    master2;
    master3;
    master4;
    subgraph {
        rank=source;
        masterstart [label="", width=0, height=0, penwidth=0];
    }
    masterstart -> master1 [color="#b0b0b0", style=dashed, arrowhead=none ];
    master1 -> master2 -> master3 -> master4;
    master4 -> masterend [color="#b0b0b0", style=dashed, arrowhead=none ];

    node  [group="hotfixes", fillcolor="#FD5965"];
    hotfix1;

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
    develop10 -> developend [color="#b0b0b0", style=dashed, arrowhead=none ];

    node  [group="feature #17", fillcolor="#FB3DB5"];
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

    node  [group="feature #42", fillcolor="#FB3DB5"];
    feature201;
    feature202;
    feature203;
    feature204;
    subgraph{ rank=same; feature101; feature201; }
    subgraph{ rank=same; feature116; feature204; }
    feature201 -> feature202 -> feature203 -> feature204;

    // branching and merging
    master1 -> develop1;

    master1 -> hotfix1;
    hotfix1 -> master2;
    hotfix1 -> develop5;

    develop3 -> feature101;
    feature103 -> develop6;
    develop6 -> release1;
    release2 -> develop7;

    release4 -> develop8;
    release4 -> master3;

    develop9 -> release5;
    release5 -> master4;
    release5 -> develop10;

    develop7 -> feature114;
    feature116 -> develop9;

    develop3 -> feature201;
    feature204 -> develop9;

    // tags connections
    edge [color="#b0b0b0", style=dotted, len=0.3, arrowhead=none, penwidth=1];
    subgraph  {
        rank="same";
        tag01 -> master1;
    }
    subgraph  {
        rank="same";
        tag02 -> master2;
    }
    subgraph  {
        rank="same";
        tag10 -> master3;
    }
    }

Git Flow war einer der ersten Vorschläge zur Verwendung von Git-Branches. Es
empfahl einen ``master``-Branch und einen separaten ``develop``-Branch sowie
diverse weitere Branches für Features, Releases und Hotfixes. Die verschiedenen
Entwicklungen sollten im ``develop``-Branch zusammengeführt werden, anschließend
in den ``release``-Branch überführt werden und schließlich im ``master``-Branch
landen. So ist Git Flow zwar ein wohldefinierter, aber komplexer Standard, der
praktisch die folgenden beiden Probleme hat:

* Die meisten Entwickler und Werkzeuge gehen von der Annahme aus, dass der
  ``master``-Branch der Hauptzweig ist von dem aus ``branch`` und ``merge``
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
