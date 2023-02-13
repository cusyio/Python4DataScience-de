pre-commit-Skripte
==================

`pre-commit-hooks <https://github.com/pre-commit/pre-commit-hooks>`_
    Das pre-commit-Framework bringt bereits eine ganze Reihe von Skripten mit,
    :abbr:`u.a. (unter anderem)`:

    ``check-added-large-files``
        verhindert, dass große Dateien übertragen werden
    ``check-case-conflict``
        sucht nach Dateien, die in Dateisystemen, die Groß- und Kleinschreibung
        nicht berücksichtigen, in Konflikt geraten würden
    ``check-executables-have-shebangs``
        stellt sicher, dass (nicht-binäre) ausführbare Dateien eine
        Shebang-Zeile haben
    ``check-shebang-scripts-are-executable``
        stellt sicher, dass (nicht-binäre) Dateien mit einer Shebang-Zeile
        ausführbar sind
    ``check-symlinks``
        prüft auf Symlinks, die auf nichts verweisen
    ``destroyed-symlinks``
        erkennt Symlinks, die in reguläre Dateien mit dem Inhalt des Pfades, auf
        den der Symlink verweist, geändert wurden.

`pygrep-hooks <https://github.com/pre-commit/pygrep-hooks>`_
    stellt reguläre Ausdrücke für Python und reStructuredText bereit,
    :abbr:`u.a. (unter anderem)`:

    ``python-no-log-warn``
        such nach der veralteten ``.warn()``-Methode von Python-Loggern
    ``python-use-type-annotations``
        erzwingt, dass Type-Annotations anstelle von Type-Comments verwendet
        werden
    ``rst-backticks``
        erkennt die Verwendung einzelner Backticks beim Schreiben von
        reStructuredText
    ``rst-directive-colons``
        erkennt, dass reStructuredText-Direktiven nicht mit einem Doppelpunkt
        oder einem Leerzeichen vor dem Doppelpunkt enden
    ``rst-inline-touching-normal``
        erkennt, dass Inline-Code in normalem Text in reStructuredText verwendet
        wird
    ``text-unicode-replacement-char``
        verhindert Dateien, die UTF-8-Unicode-Replacement-Character enthalten

Linter und Formatierer
    Sie werden in eigenen Repositories bereitgestellt, :abbr:`u.a. (unter
    anderem)`:

    `autopep8 <https://github.com/pre-commit/mirrors-autopep8>`_
        stellt `autopep8 <https://github.com/hhatto/autopep8>`__ für das
        pre-commit-Framework bereit
    `mypy <https://github.com/pre-commit/mirrors-mypy>`_
        stellt `mypy <https://github.com/python/mypy>`__ bereit
    `clang-format <https://github.com/pre-commit/mirrors-clang-format>`_
        stellt `clang-format-wheel
        <https://github.com/ssciwr/clang-format-wheel>`__ bereit
    `csslint <https://github.com/pre-commit/mirrors-csslint>`_
        stellt `csslint <https://github.com/CSSLint/csslint>`__ bereit
    `scss-lint <https://github.com/pre-commit/mirrors-scss-lint>`_
        stellt `scss-lint <https://github.com/sds/scss-lint>`__ bereit
    `eslint <https://github.com/pre-commit/mirrors-eslint>`_
        stellt `eslint <https://github.com/eslint/eslint>`__ bereit
    `fixmyjs <https://github.com/pre-commit/mirrors-fixmyjs>`_
        stellt `fixmyjs <https://github.com/jshint/fixmyjs>`__ bereit
    `prettier <https://github.com/pre-commit/mirrors-prettier>`_
        stellt `prettier <https://github.com/prettier/prettier>`__ bereit

`black <https://github.com/psf/black>`_
    für die Formatierung von Python-Code

    ``black``
        Python-Code-Formattierer
    ``black-jupyter``
        Python-Code-Formattierer für Jupyter-Notebooks

Python Code Quality Authority
    Codequalitätswerkzeuge (und Plugins) für die Programmiersprache Python:

    `flake8 <https://github.com/PyCQA/flake8>`_
        fördert die Durchsetzung eines konsistenten Python-Stils
    `autoflake <https://github.com/PyCQA/autoflake>`_
        entfernt unbenutzte Importe und unbenutzte Variablen aus Python-Code
    `bandit <https://github.com/PyCQA/bandit>`_
        Werkzeug zum Auffinden von Sicherheitslücken in Python-Code
    `pydocstyle <https://github.com/PyCQA/pydocstyle>`_
        statisches Analysewerkzeug zur Überprüfung der Einhaltung von
        Python-Docstring-Konventionen.
    `docformatter <https://github.com/PyCQA/docformatter>`_
        formatiert docstrings gemäß `PEP 257
        <https://peps.python.org/pep-0257/>`_
    `pylint <https://github.com/PyCQA/pylint>`_
        Python-Linter
    `doc8 <https://github.com/PyCQA/doc8>`_
        führt doc8 zum Linting von Dokumenten aus
    `prospector <https://github.com/PyCQA/prospector>`_
        analysiert Python-Code mit Prospector
    `isort <https://github.com/PyCQA/isort>`_
        sortiert Python-Importe

`nbQA <https://github.com/nbQA-dev/nbQA>`_
    führt isort, pyupgrade, mypy, pylint, flake8 und mehr auf Jupyter Notebooks
    aus:

    ``nbqa``
        führt jedes Standard-Python-Codequalitätswerkzeug auf einem
        Jupyter-Notebook aus
    ``nbqa-black``
        führt ``black`` auf einem Jupyter-Notebook aus
    ``nbqa-check-ast``
        führt ``check-ast`` auf einem Jupyter-Notebook aus
    ``nbqa-flake8``
        führt ``flake8`` auf einem Jupyter-Notebook aus
    ``nbqa-isort``
        führt ``isort`` auf einem Jupyter-Notebook aus
    ``nbqa-mypy``
        führt ``mypy`` auf einem Jupyter-Notebook aus
    ``nbqa-pylint``
        führt ``pylint`` auf einem Jupyter-Notebook aus
    ``nbqa-pyupgrade``
        führt ``ppyupgrade`` auf einem Jupyter-Notebook aus
    ``nbqa-yapf``
        führt ``yapf`` auf einem Jupyter-Notebook aus
    ``nbqa-autopep8``
        führt ``autopep8`` auf einem Jupyter-Notebook aus
    ``nbqa-pydocstyle``
        führt ``pydocstyle`` auf einem Jupyter-Notebook aus
    ``nbqa-ruff``
        führt ``ruff`` auf einem Jupyter-Notebook aus

`blacken-docs <https://github.com/adamchainz/blacken-docs>`_
    wendet ``black`` auf Python-Codeblöcke in Dokumentationsdateien an

Misc

`pyupgrade <https://github.com/asottile/pyupgrade>`_
    aktualisiert automatisch die Syntax für neuere Versionen
`reorder-python-imports <https://github.com/asottile/reorder_python_imports>`_
    ordnet Importe in Python-Dateien neu an
`dead <https://github.com/asottile/dead>`_
    erkkent toten Python-Code
`python-safety-dependencies-check <https://github.com/Lucas-C/pre-commit-hooks-safety>`_
    analysiert Python-Requirements auf bekannte Sicherheitsschwachstellen
`gitlint <https://github.com/jorisroovers/gitlint>`_
    Git commit message Linter
`nbstripout <https://github.com/kynan/nbstripout>`_
    entfernt die Ausgabe von Jupyter Notebooks
`detect-secrets <https://github.com/Yelp/detect-secrets>`_
    erkennt Zeichenfolgen mit hoher Entropie, bei denen es sich wahrscheinlich
    um Passwörter handelt
`pip-compile <https://github.com/jazzband/pip-tools>`_
    kompiliert automatisch Anforderungen
`kontrolilo <https://github.com/kontrolilo/kontrolilo>`_
    Werkzeug zur Kontrolle der Lizenzen für OSS-Abhängigkeiten

.. seealso::
    * `Supported hooks <https://pre-commit.com/hooks.html>`_
