.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

GitLab
======

`GitLab <https://about.gitlab.com>`_ ist eine Webanwendung zur
Versionsverwaltung auf Basis von Git. Später kamen weitere Funktionen hinzu wie
ein Issue-Tracking-System mit Kanban-Board, ein System für `Continuous
Integration und Continuous Delivery (CI/CD)
<https://about.gitlab.com/solutions/continuous-integration/>`_ sowie ein Wiki
und Snippets. Die GitLab Community Edition (CE) wird als Open-Source-Software
unter der MIT-Lizenz entwickelt und kann On-Premises, also in den eigenen
Räumlichkeiten, installiert werden.

Die GitLab CI Tools ermöglichen automatisierte Builds und Deployments ohne dass
externe Integrationen erforderlich wären, :abbr:`z.B. (zum Beispiel)` das
:doc:`Bauen eines Docker-Containers mit der Python-Version des Projekts
<ci-cd/docker>`.

Wenn bereits eine PaaS-Lösung wie `Kubernetes
<https://de.wikipedia.org/wiki/Kubernetes>`_ verwendet wird, können mit
GitLab-CI/CD Apps automatisch bereitgestellt, getestet und skaliert werden.
Zudem kann automatisch die :doc:`/productive/security` eures Projekts
überprüft werden.

GitLab ist eine komplett paketierte Plattform, während GitHub mit Apps aus dem
Marketplace erweitert werden kann. Das bedeutet aber nicht, dass GitLab nicht
integriert werden kann, :abbr:`z.B. (zum Beispiel)` mit Asana, Jira, Microsoft
Teams, Slack etc.

.. seealso::
    `Visual Studio Code: GitLab Workflow
    <https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow>`_

.. toctree::
   :hidden:

   roles-permissions
   merge-requests
   ci-cd/index
   package-registry
