.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Merge-Requests
==============

Mit Merge-Requests könnt ihr Quellcodeänderungen in einen Zweig einchecken. Wenn
ihr eine Zusammenführungsanforderung öffnet, könnt ihr euch die Codeänderungen
vor dem Zusammenführen anschauen und gemeinsam daran arbeiten.
Zusammenführungsanfragen enthalten:

* eine Beschreibung der Anfrage
* Codeänderungen und Codeüberprüfungen
* Informationen über :doc:`CI/CD-Pipelines <ci-cd/index>`
* Diskussionsbeiträge
* die Liste der Commits

.. tip::
   Wenn ihr einen Fork erstellt habt, stellt die Merge-Requests dennoch nicht
   vom ``main``-Branch aus. Damit vermeidet ihr folgende Schwierigkeiten:

   * Ihr könnt dann an nicht nur an einem sondern an mehreren Merge-Requests
     arbeiten.
   * Wenn euer Merge-Request akzeptiert wurde, könnt ihr kein ``git pull`` mehr
     machen, da ihr widersprüchliche Commits habt.
   * Wenn der ``main``-Branch des Ziel-Repository geschützt ist, können Personen
     mit *Maintainer*-Rolle den Merge-Request nicht mehr bearbeiten. Alle
     Änderungen müssten dann über euch laufen.

.. seealso::
   * `Merge requests <https://docs.gitlab.com/ee/user/project/merge_requests/>`_

Merge-Request-Arbeitsabläufe
----------------------------

#. Ihr checkt einen neuen Zweig aus und übermittelt eure Änderungen durch eine
   Zusammenführungsanforderung.
#. Ihr holt Feedback von eurem Team ein.
#. Ihr arbeitet an der Implementierung und optimiert den Code mit
   `Codequalitätsberichten
   <https://docs.gitlab.com/ee/ci/testing/code_quality.html>`_.
#. Ihr verifiziert eure Änderungen mit `Berichten von Unit-Tests
   <https://docs.gitlab.com/ee/ci/testing/unit_test_reports.html>`_ in
   :doc:`GitLab CI/CD <ci-cd/index>`.
#. Ihr vermeidet die Verwendung von Abhängigkeiten, deren Lizenz nicht mit eurem
   Projekt kompatibel ist, mit :ref:`Berichten zur Lizenzkonformität
   <reuse-in-gitlab-ci>`.
#. Ihr beantragt die `Genehmigung
   <https://docs.gitlab.com/ee/user/project/merge_requests/approvals/index.html>`_
   eurer Änderungen.
#. Wenn die Zusammenführungsanforderung genehmigt wurde, wird die :doc:`GitLab
   CI/CD <ci-cd/index>` die Änderungen in der ``production``-Umgebung
   bereitstellen.
