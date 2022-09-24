Merge-Requests
==============

Mit Merge-Requests könnt ihr Quellcodeänderungen in einen Zweig einchecken. Wenn
ihr eine Zusammenführungsanforderung öffnet, könnt ihr die Codeänderungen vor
der Zusammenführung visualisieren und gemeinsam daran arbeiten.
Zusammenführungsanfragen enthalten:

* eine Beschreibung der Anfrage
* Codeänderungen und Codeüberprüfungen
* Informationen über :doc:`CI/CD-Pipelines <ci-cd>`
* Diskussionsbeiträge
* die Liste der Commits

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
   :doc:`GitLab CI/CD <ci-cd>`.
#. Ihr vermeidet die Verwendung von Abhängigkeiten, deren Lizenz nicht mit eurem
   Projekt kompatibel ist, mit :ref:`Berichten zur Lizenzkonformität
   <gitlab-ci-workflow>`.
#. Ihr beantragt die `Genehmigung
   <https://docs.gitlab.com/ee/user/project/merge_requests/approvals/index.html>`_
   eurer Änderungen.
#. Wenn die Zusammenführungsanforderung genehmigt wurde, wird die :doc:`GitLab
   CI/CD <ci-cd>` die Änderungen in der ``production``-Umgebung bereitstellen.
