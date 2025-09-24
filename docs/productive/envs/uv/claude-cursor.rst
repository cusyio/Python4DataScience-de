Claude Code oder Cursor für uv konfigurieren
============================================

Wie konfigurieren wir `Claude Code <https://claude.com/product/claude-code>`_
oder `Cursor <https://cursor.com>`_, damit automatisch uv anstelle von pip für
die Python-Paketverwaltung verwendet wird?

.. tab:: Claude Code

   Claude Code verwendet :file:`CLAUDE.md`-Dateien, um Speicher und Kontext
   eures Projekts zu konfigurieren, wodurch eine einheitliche Tooling-Umgebung
   für euren gesamten Entwicklungs-Workflow gewährleistet wird.

   Vorausgesetzt, Claude Code und uv sind bereits auf eurem System installiert
   und ihr habt bereits ein uv-basiertes Python-Projekt :abbr:`z. B. (zum
   Beispiel)` erstellt mit :ref:`uv init <uv-package-structure>`.

   .. tip::
      Ihr könnt den ``/init``-Befehl in Claude Code verwenden um euch
      automatisch eine :file:`CLAUDE.md`-Datei erstellen zu lassen und sie
      anschließend mit uv-spezifischen Instruktionen zu ergänzen.

   .. code-block:: md
      :caption: CLAUDE.md

      # Python environment with uv
      Exclusively use uv for the Python environment in this project.

      ## Environment commands
      - Use uv to install, sync, and lock Python dependencies
      - Never use pip, pip-tools, poetry, or conda for dependency management

      Use these commands:
      - Install dependencies: `uv add <package>`
      - Remove dependencies: `uv remove <package>`
      - Sync dependencies: `uv sync`

      ## Running Python Code
      - Run a Python script with `uv run <script-name>.py`
      - Run Python tools like pytest with `uv run pytest`

   .. tip::
      Denkt daran, eure projektspezifische :file:`CLAUDE.md`-Datei mit :doc:`Git
      </productive/git/index>` zu verwalten, damit alle im Team, die mit Claude
      Code arbeiten, automatisch die gleiche Konfiguration erhalten.

   .. seealso::
      * `Claude Docs <https://docs.claude.com/en/home>`_
      * `Manage Claude's memory
        <https://docs.claude.com/en/docs/claude-code/memory>`_

.. tab:: Cursor

   `Cursor Rules <https://cursor.com/docs/context/rules>`_ können verwendet
   werden, um uv anstelle von pip zu verwenden.

   Vorausgesetzt, Cursor und uv sind bereits auf eurem System installiert und
   ihr habt bereits ein uv-basiertes Python-Projekt :abbr:`z. B. (zum Beispiel)`
   erstellt mit :ref:`uv init <uv-package-structure>`.

   Anschließend könnt ihr für eure Cursor Rules eine *Cursor Markdown
   Context*-Datei :file:`uv.mdc` in :samp:`{PROJECT}/.cursor/rules/` erstellen
   in :menuselection:`View Menu --> Command Palette --> New Cursor Rule` mit

   * Name: ``uv``
   * Rule Type: *Agent Requested*
   * Description: *Exclusively use uv for the Python environment in this project.*

   Anschließend könnt ihr folgende Regeln hinzufügen:

   .. code-block:: md
      :caption: .cursor/rules/uv.mdc

      # Python environment with uv
      Exclusively use uv for the Python environment in this project.

      ## Environment commands
      - Use uv to install, sync, and lock Python dependencies
      - Never use pip, pip-tools, poetry, or conda for dependency management

      Use these commands:
      - Install dependencies: `uv add <package>`
      - Remove dependencies: `uv remove <package>`
      - Sync dependencies: `uv sync`

      ## Running Python Code
      - Run a Python script with `uv run <script-name>.py`
      - Run Python tools like pytest with `uv run pytest`
