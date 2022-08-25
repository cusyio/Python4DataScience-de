================
Feature-Branches
================

`GitHub Flow <https://docs.github.com/en/get-started/quickstart/github-flow>`_
war als stark vereinfachte Alternative zu :doc:`git-flow` gedacht, wobei es
neben dem ``main``-Branch nur verschiedene Feature-Branches geben sollte. Auch
Atlassian empfiehlt eine `ähnliche Strategie
<https://www.atlassian.com/blog/git/simple-git-workflow-is-simple>`_, wobei sie
jedoch ein ``rebase`` der Feature-Branches vornehmen. Diese Strategien bieten
dabei zwei Vorteile:

* Das zu verwaltende Code-Inventar bleibt relativ klein da die Feature-Branches
  üblicherweise schnell in den ``main`` übernommen werden.
* Die Workflows entsprechen den üblichen Methoden von *Continuous Delivery*.

Diese Workflows können jedoch nicht beantworten, wie Deployments in
unterschiedliche Umgebungen oder die Aufteilung in verschiedene Releases
erfolgen können. Möglichkeiten hierfür werden in :doc:`deploy-branches`
beschrieben.

.. seealso::
   * `Feature Driven Development
     <https://de.wikipedia.org/wiki/Feature_Driven_Development>`_
   * Martin Fowler: `Feature Branch
     <https://martinfowler.com/bliki/FeatureBranch.html>`_
