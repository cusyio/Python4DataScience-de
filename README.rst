.. SPDX-FileCopyrightText: 2020 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Python4DataScience
==================

.. _badges

Status
------

.. image:: https://img.shields.io/github/contributors/cusyio/python4datascience-de.svg
   :alt: Contributors
   :target: https://github.com/cusyio/python4datascience-de/graphs/contributors
.. image:: https://img.shields.io/github/license/cusyio/python4datascience-de.svg
   :alt: License
   :target: https://github.com/cusyio/python4datascience-de/blob/main/LICENSE
.. image:: https://results.pre-commit.ci/badge/github/cusyio/Python4DataScience-de/main.svg
   :target: https://results.pre-commit.ci/run/github/649725482/1726568571.WhuLTrgJT3aZZkF-R0Fd8w
   :alt: pre-commit.ci status
.. image:: https://readthedocs.org/projects/python4datascience-de/badge/?version=latest
   :alt: Docs
   :target: https://python4datascience-de.readthedocs.io/de/latest/
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo..14031392.svg
   :alt: DOI
   :target: https://doi.org/10.5281/zenodo.14031392
.. image:: https://img.shields.io/badge/dynamic/json?label=Mastodon&query=totalItems&url=https%3A%2F%2Fmastodon.social%2F@Python4DataScience%2Ffollowers.json&logo=mastodon
   :alt: Mastodon
   :target: https://mastodon.social/@Python4DataScience

.. _first-steps

Überblick
---------

Dieses Repository enthält ein Tutorium für Datenmanagement und -analyse mit Python.
Die Ordner enthalten:

- ``data/`` - Daten für ein Beispielprojekt
- ``docs/`` - die eigentliche Dokumentation
- ``fastapi/`` - Beispielprojekt eines Servers, der Daten bereitstellt


Installation
------------

#. Herunterladen und Auspacken:

   .. code-block:: console

    $ curl -O https://codeload.github.com/cusyio/python4datascience-de/zip/main
    $ unzip main
    Archive:  main
    …
       creating: python4datascience-de-main/
    …

#. Installieren der Python-Pakete

   .. code-block:: console

    $ cd python4datascience-de-main
    $ python3 -m venv .venv
    $ . .venv/bin/activate
    $ python -m pip install -e ".[dev]"

#. Installieren der `Jupyter Notebook Extensions
   <https://jupyter-contrib-nbextensions.readthedocs.io/>`_:

   .. code-block:: console

      $ jupyter contrib nbextension install --user
      jupyter contrib nbextension install --user
      Installing jupyter_contrib_nbextensions nbextension files to jupyter data directory
      …
      Successfully installed jupyter-contrib-core-0.3.3 jupyter-contrib-nbextensions-0.5.1
      jupyter-highlight-selected-word-0.2.0 jupyter-latex-envs-1.4.6
      jupyter-nbextensions-configurator-0.4.1
      …
      $ jupyter nbextension enable latex_envs --user --py
      Enabling notebook extension latex_envs/latex_envs...
            - Validating: OK

#. HTML-Dokumentation erstellen:

   .. code-block:: console

      $ cd docs
      $ make html

#. PDF erstellen:

   Für die Erstellung von PDFs benötigt ihr weitere Pakete.

   Für Debian/Ubuntu erhaltet ihr diese mit:

   .. code-block:: console

      $ sudo apt install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

   oder für macOS mit:

   .. code-block:: console

      $ brew cask install mactex
      …
      🍺  mactex was successfully installed!
      $ curl --remote-name https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
      $ sudo texlua install-getnonfreefonts
      …
      mktexlsr: Updating /usr/local/texlive/2020/texmf-dist/ls-R...
      mktexlsr: Done.

   Anschließend könnt ihr ein PDF generieren mit:

   .. code-block:: console

      $ make latexpdf
      …
      The LaTeX files are in _build/latex.
      Run 'make' in that directory to run these through (pdf)latex
      …

   Das PDF findet ihr anschließend in ``docs/_build/latex/jupytertutorial.pdf``.


.. _follow-us

Folge uns
---------

* `GitHub <https://github.com/cusyio/Python4DataScience-de>`_
* `Mastodon <https://mastodon.social/@Python4DataScience>`_

Pull-Requests
-------------

Wenn ihr Vorschläge für Verbesserungen und Ergänzungen habt, empfehle ich euch,
einen `Fork <https://github.com/cusyio/Python4DataScience-de/fork>`_ unseres
`GitHub-Repository <https://github.com/cusyio/Python4DataScience-de/>`_ zu
erstellen und darin eure Änderungen vorzunehmen. Gerne dürft ihr auch einen
*Pull Request* stellen. Sofern die darin enthaltenen Änderungen klein und
atomar sind, schauen wir uns eure Vorschläge gerne an.

Da eine englischsprachige Übersetzung gepflegt wird, beachtet folgende
Richtlinien:

* Commit-Nachrichten auf Englisch
* Commit-Nachrichten mit einem `Gitmoji <https://gitmoji.dev/>`__ am Anfang
* Namen von Ordnern und Dateien auf Englisch.
