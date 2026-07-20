.. SPDX-FileCopyrightText: 2023 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Abhängigkeiten verwalten
========================

Genau hier finden Angriffe auf die Software-Lieferkette statt. Das `OpenSSF
Secure Supply Chain Consumption Framework (S2C2F)
<https://github.com/ossf/s2c2f>`_ bietet ein strukturiertes Reifegradmodell
dafür, wie Unternehmen Open-Source-Software nutzen sollten.

.. seealso::
   Für ein umfassenderes Bedrohungsmodell über alle Ökosysteme hinweg ist das
   `CNCF Software Supply Chain Security Whitepaper
   <https://tag-security.cncf.io/community/working-groups/supply-chain-security/supply-chain-security-paper-v2/Software_Supply_Chain_Practices_whitepaper_v2.pdf>`_
   eine gute Einführung.

Wählt eure Abhängigkeiten sorgfältig aus
----------------------------------------

Bevor ihr eine Abhängigkeit hinzufügt, solltet ihr prüfen, ob ihr diese
überhaupt benötigt, denn jede Abhängigkeit vergrößert eure Angriffsfläche.
Weniger oder kleinere Abhängigkeiten bedeuten weniger Angriffsmöglichkeiten.
Wenn ihr eine Abhängigkeit hinzufügt, bewertet die Sicherheitslage mithilfe der
`OpenSSF-Scorecard <https://securityscorecards.dev>`_, die Projekte bewertet
hinsichtlich

* :doc:`Branch<../git/branch>`-Protection
* signierte Releases
* Tools zur Aktualisierung von Abhängigkeiten
* Vulnerability Disclosure

Eine niedrige Punktzahl gibt euch Aufschluss darüber, wie viel Vertrauen ihr in
ein Projekt mit eingeschränkter Sicherheitshygiene setzen solltet.

Schreibt die Abhängigkeiten fest
--------------------------------

.. warning::
   Wenn ihr eine Bibliothek auf :term:`PyPI` veröffentlicht, solltet ihr im
   ``dependencies``-Abschnitt eurer :file:`pyproject.toml`-Datei möglichst
   breite Versionsbereiche verwenden, um Konflikte zu vermeiden, wenn andere
   eure Bibliothek zusammen mit weiteren Bibliotheken installieren wollen. Die
   Hinweise in diesem Abschnitt gelten ausschließlich für die Bereitstellung von
   Anwendungen.

Denkt euch folgendes Szenario: ``uv add`` schreibt in eure
:file:`pyproject.toml`-Datei die ungefähre Version eurer Abhängigkeit,
:abbr:`z. B. (zum Beispiel)` :samp:`"{MYDEP}>=3.0.5"`. Wenn das Projekt neu
aufgesetzt wird, kann ``uv sync`` dazu führen, dass :samp:`{MYDEP}` in der
Version ``3.0.6`` installiert wird. So könnte unbemerkt eine bösartige Version
heruntergeladen werden ohne dass auch nur eine einzige Zeile Code geändert
wurde.

Eine festgelegte Version :samp:`"{MYDEP}==3.0.5"` ist besser, da wir zumindest
keine neuere Version als die getestete im Projekt erhalten. Dennoch erhaltet ihr
somit immer noch keine Integritätsprüfung: Sollte bei einem Angriff das Konto
des Maintainer kompromittiert werden und ein neues, mit einer Hintertür
versehenes Release für dieselbe Version, aber für eine andere Plattform
veröffentlicht werden, könnte auch dieses unwissentlich installiert werden. Um
dieses Angriffsszenario zu reduzieren, sind zukünftig auf :term:`PyPI` `nur noch
Releases für eine Version innerhalb von 14 Tagen erlaubt
<https://blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days/>`_.

Hash-Pinning ist sicherer – es erstellt einen kryptografischen Fingerabdruck der
Paketdatei, der mit :term:`uv` in der :file:`uv.lock`-Datei festgeschrieben
wird. Alternativ könnt ihr auch die ``--require-hashes``-Option von :term:`pip`
verwenden. Ihr solltet jedoch nicht nur für eure Python-Abhängigkeiten
Hash-Pinning verwenden, sondern :abbr:`z. B. (zum Beispiel)` auch für eure
:doc:`pre-commit Checks <../git/advanced/hooks/checks>` und GitHub Actions.

Hash-Pinning schützt jedoch nicht davor, ein schädliches Paket zum ersten Mal zu
installieren; in diesem Fall würdet ihr nur den Hash des schädlichen Pakets
festlegen. Daher solltet ihr das Hash-Pinning mit Schwachstellenscans und
verzögerter Übernahme kombinieren.

.. seealso::
   `The lockfile
   <https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile>`_

.. _automatic-update:

Aktualisiert die Abhängigkeiten automatisch
-------------------------------------------

Abhängigkeiten sollten regelmäßig aktualisiert  werden, um Schwachstellen zu
vermeiden, Inkompatibilitäten zwischen Abhängigkeiten einzuschränken und
komplexe Upgrades zu vermeiden, wenn von einer zu alten Version aktualisiert
wird. Eine Vielzahl von Werkzeugen kann dabei helfen, auf dem neuesten Stand zu
bleiben.

Veraltete Abhängigkeiten machen ein Projekt anfällig für Angriffe auf bekannte
Schwachstellen. Daher sollte die Aktualisierung von Abhängigkeiten automatisiert
werden, indem nach veralteten Anforderungen gesucht wird und diese :abbr:`ggf.
(gegebenenfalls)` aktualisiert werden. Mit :doc:`../git/advanced/hooks/prek`
könnt ihr regelmäßig eure :file:`uv.lock`-Datei aktualisieren:

.. code-block:: yaml
   :caption: .pre-commit-config.yaml

   - repo: https://github.com/astral-sh/uv-pre-commit
     rev: 6a280ba12b7901e47757c868c8c13c6a624c9ecb # 0.11.7
     hooks:
       - id: uv-lock
         args: ["--exclude-newer = 'P3D'", "--quiet"]

``--exclude-newer``
    *Dependency Cooldown*, das Pakete ausschließt, die erst seit einigen Tagen,
    mit ``P3D`` erst seit drei Tagen, auf :term:`PyPI` veröffentlicht sind. Dies
    gibt den PyPI-Administrator*innen die Möglichkeit, in dieser Zeit auf
    Malware zu reagieren.

.. seealso::
   * :ref:`Update uv.lock <python-basics:update-uv-lock>`

Alternativ könnt ihr euch auch von :doc:`../envs/uv/renovate>` unterstützen
lassen.

.. _vulnerability_scans:

Schwachstellen-Scans
--------------------

*Dependency Pinning* verhindert unbefugte Änderungen – doch was passiert, wenn
ihr eine Version gestgeschrieben habt, die eine bekannte Sicherheitslücke
aufweist? Forschende entdecken immer wieder neue :abbr:`CVEs (Common
Vulnerabilities and Exposures)` in Paketen. Ein Paket, das gestern noch
problemlos war, könnte heute schon eine kritische Sicherheitslücke aufweisen.
Offene Sicherheitslücken in euren Abhängigkeiten können leicht ausgenutzt
werden, und sie sollten daher so schnell wie möglich geschlossen werden. Hierfür
könnt ihr ``uv audit`` verwenden und überprüfen, ob euer Projekt bekannte
Sicherheitslücken in den Abhängigkeiten aufweist:

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

Wenn in einer Abhängigkeit eine Schwachstelle gefunden wird, solltet ihr auf
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

Sicherheitsprüfungen sollten automatisiert durchgeführt werden. Hierzu könnt ihr
``uv audit`` :abbr:`z.B . (zum Beispiel)` in einer GitHub Action verwenden:

.. code-block:: yaml

   name: Security Scan
   jobs:
     security:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
         - uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
         - run: uv audit

oder in einer GitLb CI/CD-Pipeline:

.. code-block:: yaml

   security-scan:
     image: ghcr.io/astral-sh/uv:python3.14
     script:
       - uv audit

Alternativ zu ``uv audit`` könnt ihr hierfür auch `osv
<https://pypi.org/project/osv/>`_ oder `pip-audit
<https://pypi.org/project/pip-audit/>`_ verwenden.

Vermeidet Abhängigkeitskonflikte
--------------------------------

Abhängigkeitskonflikte können durch die Art und Weise entstehen, wie
Paketmanager Namen auflösen, wenn sowohl öffentliche als auch private
Paketverzeichnisse verwendet werden. Ein bösartiges Paket, das auf :term:`PyPI`
veröffentlicht wurde und denselben Namen wie euer internes Paket trägt, kann vom
Build-System stattdessen installiert werden. Bei :term:`pip` funktioniert der
Angriff wie folgt:

#. Beim Aufruf von :samp:`python -m pip install --extra-index-url
   {https://EXAPMPLE.COM/simple MYPACKAGE}` :abbr:`o. ä. (oder ähnlichem)`
   würdet ihr vermutlich erwarten, dass :samp:`{MYPACKAGE}` von eurem Index
   :samp:`https://{EXAPMPLE.COM}/simple` geladen würde.
#. ``pip`` schaut jeddoch in allen Indexen nach und wählt die höchste Version
   aus.
#. Liegt also auf :term:`PyPI` eine höhere Version von :samp:`{MYPACKAGE}` mit
   bösartigem Code, wird diese installiert.

Mit ``--index-url`` für einen einzelnen Index könnt ihr dieses Problem umgehen.
Dabei geht ``pip`` davon aus, dass euer interner Index als Proxy für den
öffentlichen :term:`PyPI` fungiert; falls er jedoch nur interne Pakete hostet,
könnt ihr ihn zunächst als PyPI-Proxy konfigurieren:

.. code-block:: ini
   :caption: pip.conf

   [install]
   index-url = https://EXAPMPLE.COM/simple
   trusted-host = EXAPMPLE.COM

:doc:`SBOMs <sbom>` können dabei helfen, potenzielle Namenskonflikte
aufzudecken, indem sie eine Bestandsliste zur Überprüfung bereitstellen; es
handelt sich dabei jedoch um nachträgliche Kontrollmaßnahmen – sie zeigen euch
also erst im Nachhinein, was ihr installiert habt.

:term:`uv` verwendet hingegen üblicherweise die ``first-index``-Strategie, nimmtalso den erstgenannten Index, in dem ein Paket gefunden wird. Dadurch werden die
oben beschriebenen Abhängigkeitskonflikte vermieden:

.. code-block:: toml
   :caption: pyoroject.toml
   :linenos:

   [[tool.uv.index]]
   name = "internal"
   url = "https://EXAPMPLE.COM/simple"
   explicit = true

   [tool.uv.sources]
   mypackage = { index = "internal" }

Zeile 4:
    Diesen Index wird nur für explizit angeheftete Pakete verwendet.

.. seealso::
   `Searching across multiple indexes
   <https://docs.astral.sh/uv/concepts/indexes/#searching-across-multiple-indexes>`_

----

Im folgenden schauen wir uns nun an, wie die Abhängigkeiten in unseren
Python-Projekten abgesichert werden kann. Dabei orientieren wir uns an der
`OpenSSF Scorecard <https://securityscorecards.dev/>`_. Alternativ könnt ihr
euch auch an :ref:`open_chain` orientieren.

In einem früheren Abschnitt haben wir schon einige Hinweise gegeben, wie die
Veröffentlichung von Python-Paketen auf :term:`PyPI` abgesichert werden kann:

.. seealso::
   * :ref:`secure-release-workflow`
   * :ref:`add_2fa`

.. seealso::
   Für ein umfassenderes Bedrohungsmodell über alle Ökosysteme hinweg ist das
   `CNCF Software Supply Chain Security Whitepaper
   <https://tag-security.cncf.io/community/working-groups/supply-chain-security/supply-chain-security-paper-v2/Software_Supply_Chain_Practices_whitepaper_v2.pdf>`_
   eine gute Einführung.

Nun wollen wir uns anschauen, wie Python-Projekte weiter abgesichert werden
können. Dabei orientieren wir uns an der `OpenSSF Scorecard
<https://securityscorecards.dev/>`_. Alternativ könnt ihr euch auch an
:ref:`open_chain` orientieren.

Wartung
-------

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
