.. SPDX-FileCopyrightText: 2025 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

GitLab Pages
============

Mit GitLab Pages lassen sich statische Websites direkt aus einem Repository in
GitLab veröffentlichen.

Diese Websites werden automatisch mit :doc:`index`-Pipelines bereitgestellt und
unterstützen Generatoren für statische Websites wie :abbr:`z.B. (zum
Beispiel)` :doc:`python-basics:document/sphinx/index` `Hugo
<https://gohugo.io>`_, `Jekyll <https://jekyllrb.com>`_ oder `Gatsby
<https://www.gatsbyjs.com>`_. Sie können mit benutzerdefinierten Domains und
SSL/TLS-Zertifikaten verbunden werden.

Erste Schritte
--------------

#. zunächst erstellt ihr eine :file:`.gitlab-ci.yml`-Datei, für
   :doc:`python-basics:document/sphinx/index` :abbr:`z.B. (zum Beispiel)` mit
   folgendem Inhalt:

   .. code-block:: yaml
      :caption: gitlab-ci.yml
      :linenos:
      :emphasize-lines: 6, 15, 18

      image: python:latest

      stages:
        - deploy

      pages:
        stage: deploy
        rules:
          - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
        before_script:
          - python -m pip install furo sphinxext-opengraph sphinx-copybutton sphinx_inline_tabs
        script:
          - cd docs && make html
        after_script:
          - mv docs/_build/html/ ./public/
        artifacts:
          paths:
            - public

   Zeile 6
       Am Job-Namen ``pages`` erkennt GitLab, dass ihr eine GitLab Pages-Website
       bereitstellen wollt.
   Zeilen 15, 18
       GitLab stellt eure Website immer aus einem bestimmten Ordner namens
       :file:`public` in eurem Repository zur Verfügung.

#. GitLab Pages bietet Standard-Domänennamen, die auf eurem Account oder
   Gruppennamen und Projekt basieren. Daraus werden vorhersehbare URLs erzeugt.
   Für die cusy-GitLab-Instanz ist dies ``pages.cusy.io``. Wenn euer Projekt
   erreichbar ist unter :samp:`https://ce.cusy.io/{GROUPNAME}/{PROJECTNAME}`,
   dann sind die zugehörigen GitLab-Pages erreichbar unter
   :samp:`https://{GROUPNAME}.pages.cusy.io/{PROJECTNAME}`.

   .. seealso::
      GitLab Pages unterstützt auch benutzerdefinierte Domains. Weitere
      Informationen findet ihr unter `GitLab Pages custom domains
      <https://docs.gitlab.com/user/project/pages/custom_domains_ssl_tls_certification/>`_.
