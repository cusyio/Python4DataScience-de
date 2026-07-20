.. SPDX-FileCopyrightText: 2023 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Sicherheit
==========

In früheren Kapiteln haben wir schon einige Hinweise gegeben, die einen
sichereren Betrieb ermöglichen sollen.

.. seealso::
   * :ref:`secure-release-workflow`
   * :ref:`zizmorcore`
   * :ref:`add_2fa`

Hier wollen wir die einzelnen Elemente nun nochmal zusammenfassen und erweitern.
Dabei orientieren wir uns an der `OpenSSF Scorecard
<https://securityscorecards.dev/>`_. Alternativ könnt ihr euch auch an
:ref:`open_chain` orientieren.

.. _check-vulnerabilities:

Schwachstellen überprüfen
-------------------------

Risiko: Hoch

Mit dieser Prüfung wird festgestellt, ob das Projekt offene, nicht behobene
Sicherheitslücken in seiner eigenen Codebasis oder in seinen Abhängigkeiten
aufweist. Eine offene Sicherheitslücke kann leicht ausgenutzt werden und sollte
so schnell wie möglich geschlossen werden.

Für eine solche Überprüfung könnt ihr :abbr:`z.B. (zum Beispiel)` ``uv audit``
verwenden. Alternativ könnt ihr auch `osv <https://pypi.org/project/osv/>`_ oder
`pip-audit <https://pypi.org/project/pip-audit/>`_ verwenden.

``uv audit`` ist ein neuer Befehl von uv≥0.11.19, der die Abhängigkeiten in
eurem Projekt auf bekannte Schwachstellen in der `OSV
<https://osv.dev>`_-Datenbank und „nachteilige“ Projektstatus :abbr:`z. B. (zum
Beispiel)` *deprecated* überprüft:

.. code-block:: console

   $ uv audit
   warning: `uv audit` is experimental and may change without warning. Pass `--preview-features audit-command` to disable this warning.
   Resolved 115 packages in 16ms
   Found 12 known vulnerabilities and no adverse project statuses in 114 packages

   Vulnerabilities:

   idna 3.12 has 1 known vulnerability:
   - GHSA-65pc-fj4g-8rjx: Internationalized Domain Names in Applications (IDNA): Specially crafted inputs to idna.encode() can bypass CVE-2024-3651 fix
     Fixed in: 3.15
     Advisory information: https://github.com/kjd/idna/security/advisories/GHSA-65pc-fj4g-8rjx
   …

``uv add``, ``uv sync`` :abbr:`usw. (und so weiter)` können nun bei jedem
Synchronisierungsvorgang nach zuvor identifizierter Malware suchen. Diese
Funktion ist standardmäßig nicht aktiviert, sie kann jedoch mit
``UV_MALWARE_CHECK=1`` in der Shell einfach ermöglicht werden.

.. seealso::
   * `uv audit <https://docs.astral.sh/uv/reference/cli/#uv-audit>`_
   * `uv audit settings <https://docs.astral.sh/uv/reference/settings/#audit>`_

Wenn eine Schwachstelle in einer Abhängigkeit gefunden wird, solltet ihr auf
eine nicht-anfällige Version aktualisieren; wenn kein Update verfügbar ist,
solltet ihr überlegen, die Abhängigkeit zu entfernen.

Wenn ihr glaubt, dass die Sicherheitslücke euer Projekt nicht betrifft, kann für
``uv audit`` in der :file:`pyproject.toml`-Datei Ausnahmen definiert werden,
:abbr:`z.B. (zum Beispiel)`:

.. code-block:: toml
   :caption: pyproject.toml

   [tool.uv.audit]
   ignore = ["PYSEC-2022-43017", "GHSA-5239-wwwm-4pmq"]

oder besser:

.. code-block:: toml
   :caption: pyproject.toml

   [tool.uv.audit]
   ignore-until-fixed = ["PYSEC-2022-43017"]

.. seealso::
   * `ignore <https://docs.astral.sh/uv/reference/settings/#audit_ignore>`_
   * `ignore-until-fixed
     <https://docs.astral.sh/uv/reference/settings/#audit_ignore-until-fixed>`_

Ihr könnt die Schwachstellenanalyse mit ``uv-audit`` auch in eure :doc:`prek
<../git/advanced/hooks/prek>`-Checks übernehmen:

.. code-block:: yaml

   - repo: https://github.com/astral-sh/uv-pre-commit
     rev: d9fca3320346514799461a80b0753eb45d707d46 # 0.11.28
     hooks:
     - id: uv-audit
       files: ^(uv\.lock|pyproject\.toml)$

Wartung
-------

.. _automatic-update:

Werden die Abhängigkeiten automatisch aktualisiert?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Hoch

Veraltete Abhängigkeiten machen ein Projekt anfällig für Angriffe auf bekannte
Schwachstellen. Daher sollte der Prozess der Aktualisierung von Abhängigkeiten
automatisiert werden, indem nach veralteten oder unsicheren Anforderungen
gesucht und :abbr:`ggf. (gegebenenfalls)` aktualisiert werden. Hierfür könnt ihr
:abbr:`z.B. (zum Beispiel)` `dependabot <https://github.com/dependabot>`_ oder
`Safety CLI <https://www.getsafety.com/>`_ verwenden.

Ihr könnt eure :doc:`/productive/envs/uv/index`-Umgebungen auch automatisch
aktualisieren.

.. seealso::
   * :ref:`Update uv.lock <python-basics:update-uv-lock>`

Werden die Abhängigkeiten noch gewartet?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Hoch

Dies weist auf möglicherweise ungepatchte Sicherheitslücken hin. Daher sollte
regelmäßig überprüft werden, ob ein Projekt archiviert wurde. Umgekehrt wird bei
der OSSF-Scorecard davon ausgegangen, dass bei mindestens einem Commit in der
Woche über 90 Tage hinweg das Projekt sehr aktiv gewartet wird. Ein Mangel an
aktiver Wartung ist jedoch nicht unbedingt immer ein Problem: insbesondere
kleinere Dienstprogramme müssen normalerweise nicht oder nur sehr selten
gewartet werden. Fehlende aktive Wartung weist euch also nur darauf hin, dass
ihr die Situation genauer untersuchen solltet.

Ihr könnt euch die Aktivitäten eines Projekts auch mit Badges anzeigen lassen,
:abbr:`z.B. (zum Beispiel)`:

.. image:: https://img.shields.io/github/commit-activity/y/veit/python4datascience
   :alt: Jährliche Commit-Aktivität
.. image:: https://img.shields.io/github/commit-activity/m/veit/python4datascience
   :alt: Monatliche Commit-Aktivität
.. image:: https://img.shields.io/github/commit-activity/w/veit/python4datascience
   :alt: Wöchentliche Commit-Aktivität

Gibt es ein Sicherheitskonzept für das Projekt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Mittel

Idealerweise sollte mit dem Projekt eine :ref:`python-basics:security`-Datei
:abbr:`o.ä. (oder ähnliches)` veröffentlicht worden sein. Diese Datei sollte
Informationen enthalten,

* wie eine Sicherheitslücke gemeldet werden kann ohne dass sie öffentlich
  sichtbar wird,
* über den Ablauf und den Zeitplan für die Offenlegung der Schwachstelle,
* zu Links, :abbr:`z.B. (zum Beispiel)` URLs und E-Mails, unter denen
  Unterstützung angefragt werden kann.

.. seealso::
   * `Guide to implementing a coordinated vulnerability disclosure process for
     open source projects
     <https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md>`_
   * `Adding a security policy to your repository
     <https://docs.github.com/de/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy>`_
   * `Runbook
     <https://github.com/ossf/oss-vulnerability-guide/blob/main/runbook.md>`_

Enthält das Projekt eine verwendbare Lizenz?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Niedrig

Eine :doc:`Lizenz </productive/licensing>` weist darauf hin, wie der Quellcode
verwendet werden darf oder nicht. Das Fehlen einer Lizenz erschwert jede Art von
Sicherheitsüberprüfung oder Audit und stellt ein rechtliches Risiko für die
potenzielle Nutzung dar.

OpenSSF-Scorecard verwendet die `GitHub License API
<https://docs.github.com/en/rest/licenses/licenses?apiVersion=2022-11-28#get-the-license-for-a-repository>`_
für auf GitHub gehostete Projekte, ansonsten eine eigene Heuristik, um eine
veröffentlichte Lizenzdatei zu erkennen. Dateien in einem
:file:`LICENSES`-Verzeichnis sollten mit ihrem :ref:`SPDX
<standard_format_licensing>`-Lizenzbezeichner benannt werden, gefolgt von einer
entsprechenden Dateierweiterung, wie in der :ref:`REUSE <reuse>`-Spezifikation
beschrieben.

OpenSSF Best Practices Badge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Niedrig

Mit dem `OpenSSF Best Practices Badge Programm
<https://www.bestpractices.dev/de>`_ könnt ihr euch auch ein entsprechendes
Badge holen.

Kontinuierliches Testen
-----------------------

Werden im Projekt CI-Tests durchgeführt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Niedrig

Bevor Code in Pull- oder Merge-Requests zusammengeführt wird, sollten Tests
durchgeführt werden, die dabei helfen, Fehler frühzeitig zu erkennen und die
Anzahl der Schwachstellen in einem Projekt zu reduzieren.

.. seealso::
   * :ref:`coverage-github-actions`

Verwendet das Projekt Fuzzing-Tools?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Mittel

Fuzzing oder Fuzz-Testing übergibt unerwartete oder zufällige Daten an euer
Programm, um Fehler zu entdecken. Regelmäßiges Fuzzing ist wichtig, um
Schwachstellen aufzuspüren, die von anderen ausgenutzt werden können, zumal auch
bei einem Angriff Fuzzing genutzt werden kann, um dieselben Schwachstellen zu
finden.

* Verwendet euer Projekt `Fuzzing <https://owasp.org/www-community/Fuzzing>`_?
* Ist der Name des Repository in der `OSS-Fuzz
  <https://github.com/google/oss-fuzz>`_-Projektliste enthalten?
* Wird `ClusterFuzzLite <https://google.github.io/clusterfuzzlite/>`_ im
  Repository eingesetzt?
* Sind benutzerdefinierte sprachenspezifische Fuzzing-Funktionen im Repository
  vorhanden, :abbr:`z.B. (zum Beispiel)` mit `atheris
  <https://pypi.org/project/atheris/>`_?

Verwendet euer Projekt Werkzeuge zur statischen Codeanalyse?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Mittel

:term:`Statische Testverfahren` testen den Quellcode, bevor die Anwendung
ausgeführt wird. Dies kann verhindern, dass bekannte Fehlerklassen versehentlich
in die Codebasis eingeführt werden.

.. _bandit:

Mit `Bandit <https://github.com/PyCQA/bandit>`__, das ihr mit :doc:`../qa/ruff`
verwenden könnt lassen sich :abbr:`u. a. (unter anderem)` folgende
Schwachstellen überprüfen:

+--------+-----------------------------------------------------------------------+
| Regel  | Beschreibung                                                          |
+--------+-----------------------------------------------------------------------+
| `S105`_| fest codierte Geheimnisse                                             |
+--------+-----------------------------------------------------------------------+
| `S301`_| :doc:`/data-processing/serialisation-formats/pickle/index` und andere |
|        | unsichere Deserialisierung                                            |
+--------+-----------------------------------------------------------------------+
| `S307`_| Verwendung von :func:`eval` mit nicht vertrauenswürdigen Eingaben     |
+--------+-----------------------------------------------------------------------+
| `S113`_| fehlende Zeitüberschreitungen                                         |
+--------+-----------------------------------------------------------------------+
| `S324`_| schwache Kryptografie wie :abbr:`z. B. (zum Beispiel)` MD5-Kollisionen|
+--------+-----------------------------------------------------------------------+
| `S608`_| SQL-Injection über Zeichenfolgenformatierung                          |
+--------+-----------------------------------------------------------------------+

.. seealso:
   `flake8-bandit <https://docs.astral.sh/ruff/rules/#flake8-bandit-s>`_

Bandit könnt ihr auch in Jupyter Notebooks, IDEs und
:doc:`../git/advanced/hooks/prek` integrieren.

Zudem könnt ihr :doc:`../qa/pysa` für `Taint
<https://en.wikipedia.org/wiki/Taint_checking>`_-Analysen verwenden.

Für GitHub-Repositories könnt ihr alternativ auch `CodeQL
<https://codeql.github.com>`_ verwenden; :abbr:`s.a. (siehe auch)`
`codeql-action
<https://github.com/github/codeql-action/blob/main/README.md#usage>`_.

Risikobewertung des Quellcodes
------------------------------

Ist das Projekt frei von eingecheckten Binärdateien?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Hoch

Generierte ausführbare Dateien im Quellcode-Repository (:abbr:`z.B. (zum
Beispiel)` Java :file:`.class`-Dateien, Python :file:`.pyc` Dateien) erhöhen das
Risiko, da sie schwer überprüft werden können, so dass sie veraltet oder
böswillig manipuliert sein können. Diesen Problemen kann mit verifizierten,
reproduzierbaren Builds begegnet werden, deren ausführbare Dateien jedoch nicht
wieder im Quellcode-Repository landen sollten.

.. seealso::
   * `Reproducible Builds <https://reproducible-builds.org>`_
   * `Python 3.12.0 from a supply chain security perspective
     <https://sethmlarson.dev/security-developer-in-residence-weekly-report-13>`_
   * `Defending against the PyTorch supply chain attack PoC
     <https://sethmlarson.dev/security-developer-in-residence-weekly-report-25>`_

Ist der Entwicklungsprozess anfällig für das Einschleusen von bösartigem Code?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Hoch

Mit :ref:`geschützten Git-Zweigen <protected_branches>` können Regeln für die
Übernahme von Änderungen in Standard- und Veröffentlichungszweige definiert
werden, :abbr:`z.B. (zum Beispiel)` automatisierte `statische Code-Analysen
<https://de.wikipedia.org/wiki/Statische_Code-Analyse>`_ mit
:doc:`../qa/flake8`, :doc:`../qa/pysa`, :doc:`../qa/wily` und :ref:`Code-Reviews
<code_reviews>` über
:abbr:`sog. (sogenannte)` :doc:`../git/advanced/gitlab/merge-requests`.

.. _code_reviews:

Werden Code-Reviews durchgeführt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Hoch

Mit Code-Reviews lassen sich unbeabsichtigte Schwachstellen oder das mögliche
Einschleusen von bösartigem Code erkennen. :abbr:`Ggf. (Gegebenenfalls)` können
so Angriffe aufgespürt werden, bei denen das Konto eines Teammitglieds
unterwandert wurde.

Wirken an dem Projekt Personen aus mehreren Organisationen mit?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Niedrig

Dies wird als Indiz für eine geringere Anzahl von vertrauenswürdigen
Code-Reviewers gewertet. Hierfür kann in den Profilen nach unterschiedlichen
Einträgen im Feld *Unternehmen* gesucht werden. Wünschenswert sind mindestens
drei verschiedene Unternehmen in den letzten 30 Commits, wobei jedes dieser
Teammitglieder mindestens fünf Commits gemacht haben sollte.

Risikobewertung der Builds
--------------------------

.. _lock-dependencies:

Werden im Projekt Abhängigkeiten deklariert und festgeschrieben?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Mittel

In eurem Projekt sollten Abhängigkeiten, die während des Build- und
Release-Prozesses verwendet werden, festgeschrieben werden. Dabei sollte eine
*gepinnte Abhängigkeit* explizit auf einen bestimmten Hash gesetzt sein und
nicht nur auf eine veränderbare Version oder einen Versionsbereich.

:doc:`../envs/spack/index` schreibt für die jeweilige Umgebung diese Hashes in
:ref:`spack_lock`, :doc:`../envs/uv/index` in :ref:`uv_lock` fest.

.. tip::
   Üblicherweise verwalte ich diese Dateien jedoch nur bei
   :doc:`python-basics:packs/apps` in :doc:`Git <../git/index>`. Bei
   :doc:`python-basics:libs/index` schränke ich üblicherweise lediglich den
   Versionsbereich der Abhängigkeiten in der :file:`pyproject.toml`-Datei ein.

Für :doc:`python-basics:packs/apps` können sich dadurch die folgenden
Sicherheitsrisiken verringern:

* Die Prüfung und Bereitstellung erfolgt mit derselben Software, was die Risiken
  beim Deployment verringert, die Fehlersuche vereinfacht und Reproduzierbarkeit
  ermöglicht.
* Kompromittierte Abhängigkeiten untergraben nicht die Sicherheit des Projekts.
* Substitutionsangriffe, also Angriffe, die auf die Verwechslung von
  Abhängigkeiten abzielen, kann so entgegengewirkt werden.

Das Festschreiben der Abhängigkeiten sollte jedoch Software-Updates nicht
verhindern. Ihr könnt dieses Risiko verringern durch

* automatisierte Werkzeuge, die euch benachrichtigen, wenn Abhängigkeiten in
  eurem Projekt veraltet sind
* Anwendungen, die Abhängigkeiten festhalten, schnell aktualisieren.

.. _S105: https://docs.astral.sh/ruff/rules/hardcoded-password-string/
.. _S301: https://docs.astral.sh/ruff/rules/suspicious-pickle-usage/
.. _S307: https://docs.astral.sh/ruff/rules/suspicious-eval-usage/
.. _S113: https://docs.astral.sh/ruff/rules/request-without-timeout/
.. _S324: https://docs.astral.sh/ruff/rules/hashlib-insecure-hash-function/
.. _S608: https://docs.astral.sh/ruff/rules/hardcoded-sql-expression/
.. _S608: https://docs.astral.sh/ruff/rules/hardcoded-sql-expression/

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    sbom
