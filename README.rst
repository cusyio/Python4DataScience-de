Schnelleinstieg
===============

|Contributors| |License| |Docs| |Pyup| |DOI|

.. |Contributors| image:: https://img.shields.io/github/contributors/veit/jupyter-tutorial-de.svg
   :target: https://github.com/veit/jupyter-tutorial-de/graphs/contributors
.. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial-de.svg
   :target: https://github.com/veit/jupyter-tutorial-de/blob/master/LICENSE
.. |Docs| image:: https://readthedocs.org/projects/jupyter-tutorial-de/badge/?version=latest
   :target: https://jupyter-tutorial.readthedocs.io/de/latest/
.. |Pyup| image:: https://pyup.io/repos/github/veit/jupyter-tutorial-de/shield.svg
   :target: https://pyup.io/repos/github/veit/jupyter-tutorial-de/
.. |DOI| image:: https://zenodo.org/badge/307380211.svg
   :target: https://zenodo.org/badge/latestdoi/307380211

.. first-steps::

Installation
------------

#. Herunterladen und Auspacken:

   .. code-block:: console

    $ curl -O https://codeload.github.com/veit/jupyter-tutorial-de/zip/master
    $ unzip master
    Archive:  master
    …
       creating: jupyter-tutorial-de-master/
    …

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

    $ apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

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

Folge uns
---------

* `GitHub <https://github.com/veit/jupyter-tutorial>`_
* `Twitter <https://twitter.com/JupyterTutorial>`_
* `Mastodon <https://mastodon.social/web/accounts/1089854>`_

Pull-Requests
-------------

Wenn ihr Vorschläge für Verbesserungen und Ergänzungen habt, empfehle ich euch,
einen `Fork <https://github.com/veit/jupyter-tutorial-de/fork>`_ meines
`GitHub-Repository <https://github.com/veit/jupyter-tutorial-de/>`_ zu erstellen
und darin eure Änderungen vorzunehmen. Gerne dürft ihr auch einen *Pull Request*
stellen. Sofern die darin enthaltenen Änderungen klein und atomar sind, schaue ich
mir eure Vorschläge gerne an.
