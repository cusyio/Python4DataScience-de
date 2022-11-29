Schnelleinstieg
===============

.. _badges:

Status
------

.. image:: https://img.shields.io/github/contributors/veit/jupyter-tutorial.svg
   :alt: Contributors
   :target: https://github.com/veit/jupyter-tutorial/graphs/contributors
.. image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
   :alt: License
   :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE
.. image:: https://readthedocs.org/projects/jupyter-tutorial-de/badge/?version=latest
   :alt: Docs
   :target: https://jupyter-tutorial.readthedocs.io/de/latest/
.. image:: https://pyup.io/repos/github/veit/jupyter-tutorial/shield.svg
   :alt: Pyup
   :target: https://pyup.io/repos/github/veit/jupyter-tutorial/
.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.4147287.svg
   :alt: DOI
   :target: https://zenodo.org/badge/latestdoi/199994535
.. image:: https://img.shields.io/badge/dynamic/json?label=Mastodon&query=totalItems&url=https%3A%2F%2Fmastodon.social%2F@JupyterTutorial%2Ffollowers.json&logo=mastodon
   :alt: Mastodon
   :target: https://mastodon.social/@JupyterTutorial

.. _first-steps:

Installation
------------

#. Herunterladen und Auspacken:

   .. code-block:: console

    $ curl -O https://codeload.github.com/veit/jupyter-tutorial-de/zip/main
    $ unzip main
    Archive:  main
    …
       creating: jupyter-tutorial-de-main/
    …

#. Installieren der Python-Pakete

   .. code-block:: console

    $ cd jupyter-tutorial-main
    $ pipenv install
    Creating a virtualenv for this project…
    …

#. Installieren der `Jupyter Notebook Extensions
   <https://jupyter-contrib-nbextensions.readthedocs.io/>`_:

   .. code-block:: console

    $ pipenv run jupyter contrib nbextension install --user
    jupyter contrib nbextension install --user
    Installing jupyter_contrib_nbextensions nbextension files to jupyter data directory
    …
    Successfully installed jupyter-contrib-core-0.3.3 jupyter-contrib-nbextensions-0.5.1
    jupyter-highlight-selected-word-0.2.0 jupyter-latex-envs-1.4.6
    jupyter-nbextensions-configurator-0.4.1
    …
    $ pipenv run jupyter nbextension enable latex_envs --user --py
    Enabling notebook extension latex_envs/latex_envs...
          - Validating: OK

#. HTML-Dokumentation erstellen:

   .. code-block:: console

    $ python3 -m venv .
    $ bin/python -m pip install --upgrade pip
    $ bin/python -m pip install -r docs/constraints.txt
    $ bin/sphinx-build -ab html docs/ docs/_build/

#. PDF erstellen:

   Für die Erstellung von PDFs benötigt ihr weitere Pakete.

   Für Debian/Ubuntu erhaltet ihr diese mit:

   .. code-block:: console

    $ sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

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

    $ cd docs/
    $ pipenv run make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   Das PDF findet ihr anschließend in ``docs/_build/latex/jupytertutorial.pdf``.

.. _follow-us:

Folge uns
---------

* `GitHub <https://github.com/veit/jupyter-tutorial>`_
* `Twitter <https://twitter.com/JupyterTutorial>`_
* `Mastodon <https://mastodon.social/@JupyterTutorial>`_

Pull-Requests
-------------

Wenn ihr Vorschläge für Verbesserungen und Ergänzungen habt, empfehle ich euch,
einen `Fork <https://github.com/veit/jupyter-tutorial-de/fork>`_ meines
`GitHub-Repository <https://github.com/veit/jupyter-tutorial-de/>`_ zu erstellen
und darin eure Änderungen vorzunehmen. Gerne dürft ihr auch einen *Pull Request*
stellen. Sofern die darin enthaltenen Änderungen klein und atomar sind, schaue ich
mir eure Vorschläge gerne an.
