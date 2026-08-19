.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Umgebungen trennen
==================

Aktuelle Best-Practices trennen zwischen verschiedenen Umgebungen, je nachdem,
was in dieser Umgebung gemacht werden soll. So wird :abbr:`z. B. (zum Beispiel)`
in unserer `cusy.tasks <https://github.com/cusyio/cusy.tasks>`_-Anwendungen
folgende Umgebungen unterschieden:

.. code-block:: toml
   :caption: pyproject.toml

   [project]

   dependencies = [
     "rich",
     "tinydb",
     "typer",
   ]

   [dependency-groups]
   dev = [
     "pre-commit",
     "reuse",
     "tox-uv",
     "watchgha",
     { include-group = "docs" },
     { include-group = "tests" },
   ]
   docs = [
     "furo",
     "interrogate",
     "matplotlib",
     "sphinx-copybutton",
     "sphinx-inline-tabs",
     "sphinxcontrib-napoleon",
     "sphinxext-opengraph",
   ]
   tests = [
     "coverage[toml]",
     "faker",
     "pytest",
     "pytest-cov",
   ]

So können beim Betrieb der Anwendung nur die dafür benötigten Abhängigkeiten
installiert werden, Nur beim Testen oder beim Deployment der Dokumentation
werden jeweils dort benötigte Abhängigkeiten zusätzlich installiert. Lediglich
die Entwicklungsumgebung enthält alle Abhängigkeiten.

So wie eure Python-Umgebung mit unveränderbaren Referenzen aktuell gehalten
werden sollte, sollten auch eure
:doc:`../git/advanced/hooks/checks` und GitHub Actions regelmäßig aktualisiert
werden.

In der :file:`.pre-commit-config.yaml` sollten die Versionen der Checks mit
ihren Hashes regelmäßig aktualisiert werden, :abbr:`z. B. (zum Beispiel)` mit:

.. code-block:: console

   $ uv run prek update --freeze --cooldown-days 7
   https://github.com/pre-commit/pre-commit-hooks
     updating rev `v6.0.0` -> `3e8a8703264a2f4a69428a0aa4dcb512790b2c8c` (frozen: v6.0.0)

.. seealso::
   :doc:`../git/advanced/hooks/prek`

.. _pinact:

Überprüft eure GitHub-Actions
-----------------------------

Für GitHub Actions könnt ihr `pinact
<https://github.com/suzuki-shunsuke/pinact>`_ verwenden, :abbr:`z. B. (zum
Beispiel)` mit:

.. code-block:: console

   $ pinact run -u --min-age 7

`zizmor <https://docs.zizmor.sh>`_ ist ein Tool zur statischen Analyse, das
Sicherheitslücken in GitHub-Actions-Workflows aufspürt – darunter
Template-Injection, nicht fixierte Aktionen, übermäßige Berechtigungen, das
Offenlegen von Anmeldedaten sowie `mehr als 30 weitere Prüfregeln
<https://docs.zizmor.sh/audits/>`_. ``zizmor`` erkennt Schwachstellen wie
diejenigen, die durch :ref:`token-exfiltration` ausgenutzt wurden.

.. seealso::
   * :ref:`zizmorcore`
