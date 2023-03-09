pre-commit in CI-Pipelines
==========================

Pre-Commit kann auch für kontinuierliche Integration (:abbr:`CI (Continuous
Integration)`) verwendet werden.

.. _gh-action-pre-commit-example:

Beispiele für GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pre-commit ci <https://pre-commit.ci>`_
    Service, der eurem GitHub-Repository die *pre-commit ci*-App in eurem
    Repository unter
    :samp:`https://github.com/{PROFILE}/{REPOSITORY}/installations` hinzufügt.

    Neben der automatischen Änderung von Pull-Requests führt die App auch
    `autoupdate <https://pre-commit.com/#pre-commit-autoupdate>`_ aus, um eure
    Konfiguration aktuell zu halten.

    Weitere Installationen könnt ihr hinzufügen unter `Install pre-commit ci
    <https://github.com/apps/pre-commit-ci/installations/new>`_.

:samp:`.github/workflows/pre-commit.yml`
    Alternative Konfiguration als GitHub-Workflow, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: yaml

        name: pre-commit

        on:
          pull_request:
          push:
            branches: [main]

        jobs:
          pre-commit:
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v3
            - uses: actions/setup-python@v3
            - uses: actions/cache@v3
              with:
                path: ~/.cache/pre-commit
                key: pre-commit|${{ env.pythonLocation }}|${{ hashFiles('.pre-commit-config.yaml') }}
            - uses: pre-commit/action@v3.0.0

    .. seealso::

        * `pre-commit/action <https://github.com/pre-commit/action>`_

Beispiel für GitLab Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    stages:
      - validate

    pre-commit:
      stage: validate
      image:
        name: python:3.10
      variables:
        PRE_COMMIT_HOME: ${CI_PROJECT_DIR}/.cache/pre-commit
      only:
        refs:
          - merge_requests
          - tags
          - main
      cache:
        paths:
          - ${PRE_COMMIT_HOME}
      before_script:
        - pip install pre-commit
      script:
        - pre-commit run --all-files

.. seealso::

    Weitere Informationen zur Feinabstimmung des Caching findet ihr in `Good
    caching practices
    <https://docs.gitlab.com/ee/ci/caching/#good-caching-practices>`_.

.. toctree::
    :hidden:

    hooks
    advanced
