.. SPDX-FileCopyrightText: 2023 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Abhängigkeiten
==============

Genau hier finden Angriffe auf die Software-Lieferkette statt. Das `OpenSSF
Secure Supply Chain Consumption Framework (S2C2F)
<https://github.com/ossf/s2c2f>`_ bietet ein strukturiertes Reifegradmodell
dafür, wie Unternehmen Open-Source-Software nutzen sollten. Bedauerlicherweise
ist das :abbr:`S2C2F (Secure Supply Chain Consumption Framework)` jedoch
beschränkt auf GitHub-Projekte. Daher suchten wir nach vergleichbaren Lösungen
für unsere Python-Projekte, die ohne GitHub auskommen.

.. seealso::
   * `OpenSSF Scorecard <https://securityscorecards.dev/>`_
   * :ref:`open_chain`
   * `CNCF Software Supply Chain Security Whitepaper
     <https://tag-security.cncf.io/community/working-groups/supply-chain-security/supply-chain-security-paper-v2/Software_Supply_Chain_Practices_whitepaper_v2.pdf>`_

Wählt eure Abhängigkeiten sorgfältig aus
----------------------------------------

Bevor ihr eine Abhängigkeit hinzufügt, solltet ihr prüfen, ob ihr diese
überhaupt benötigt, denn jede Abhängigkeit vergrößert eure Angriffsfläche.
Weniger oder kleinere Abhängigkeiten bedeuten weniger Angriffsmöglichkeiten.
Wenn ihr eine Abhängigkeit hinzufügt, könnt ihr die Sicherheitslage mithilfe der
`OpenSSF-Scorecard <https://securityscorecards.dev>`_ bewerten:

Eine niedrige Punktzahl gibt euch Aufschluss darüber, wie viel Vertrauen ihr in
ein Projekt mit eingeschränkter Sicherheitshygiene setzen solltet.

Gibt es ein Sicherheitskonzept?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Idealerweise sollte mit der Abhängigkeit eine
:ref:`python-basics:security`-Datei :abbr:`o. ä. (oder ähnliches)`
veröffentlicht worden sein. Diese Datei sollte Informationen enthalten,

* wie eine Sicherheitslücke gemeldet werden kann ohne dass sie öffentlich
  sichtbar wird,
* über den Ablauf und den Zeitplan für die Offenlegung der Schwachstelle,
* zu Links, :abbr:`z. B. (zum Beispiel)` URLs und E-Mails, unter denen
  Unterstützung angefragt werden kann.

.. seealso::
   * `Guide to implementing a coordinated vulnerability disclosure process for
     open source projects
     <https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md>`_
   * `Adding a security policy to your repository
     <https://docs.github.com/de/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy>`_
   * `Runbook
     <https://github.com/ossf/oss-vulnerability-guide/blob/main/runbook.md>`_

Werden CI-Tests durchgeführt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bevor Code in Pull- oder Merge-Requests zusammengeführt wird, sollten Tests
durchgeführt werden, die dabei helfen, Fehler frühzeitig zu erkennen und die
Anzahl der Schwachstellen in einem Projekt zu reduzieren.

.. seealso::
   * :ref:`coverage-github-actions`

Werden Fuzzing-Tools verwendet?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
  vorhanden, :abbr:`z. B. (zum Beispiel)` mit `atheris
  <https://pypi.org/project/atheris/>`_?

Werden Werkzeuge zur statischen Codeanalyse verwendet?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:term:`Statische Testverfahren` testen den Quellcode, bevor die Anwendung
ausgeführt wird. Dies kann verhindern, dass bekannte Fehlerklassen versehentlich
in die Codebasis eingeführt werden.

Ist der Quellcode frei von eingecheckten Binärdateien?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generierte ausführbare Dateien im Quellcode-Repository (:abbr:`z. B. (zum
Beispiel)` Python :file:`.pyc` Dateien) erhöhen das Risiko, da sie schwer
überprüft werden können, so dass sie veraltet oder böswillig manipuliert sein
können. Diesen Problemen kann mit verifizierten, reproduzierbaren Builds
begegnet werden, deren ausführbare Dateien jedoch nicht wieder im
Quellcode-Repository landen sollten.

.. seealso::
   * `Reproducible Builds <https://reproducible-builds.org>`_
   * `Python 3.12.0 from a supply chain security perspective
     <https://sethmlarson.dev/security-developer-in-residence-weekly-report-13>`_
   * `Defending against the PyTorch supply chain attack PoC
     <https://sethmlarson.dev/security-developer-in-residence-weekly-report-25>`_

Kann bösartigem Code eingeschleust werden?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit :ref:`geschützten Git-Zweigen <protected_branches>` können Regeln für die
Übernahme von Änderungen in Standard- und Veröffentlichungszweige definiert
werden, :abbr:`z. B. (zum Beispiel)` automatisierte `statische Code-Analysen
<https://de.wikipedia.org/wiki/Statische_Code-Analyse>`_ mit
:doc:`../qa/ruff`, :doc:`../qa/pysa`, :doc:`../qa/wily` und :ref:`Code-Reviews
<code_reviews>` über :abbr:`sog. (sogenannte)`
:doc:`../git/advanced/gitlab/merge-requests`.

.. _code_reviews:

Werden Code-Reviews durchgeführt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit Code-Reviews lassen sich unbeabsichtigte Schwachstellen oder das mögliche
Einschleusen von bösartigem Code erkennen. :abbr:`Ggf. (Gegebenenfalls)` können
so Angriffe aufgespürt werden, bei denen das Konto eines Teammitglieds
unterwandert wurde.

Wirken Personen aus mehreren Organisationen mit?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dies wird als Indiz für eine geringere Anzahl von vertrauenswürdigen
Code-Reviewers gewertet. Hierfür kann in den Profilen nach unterschiedlichen
Einträgen im Feld *Unternehmen* gesucht werden. Wünschenswert sind mindestens
drei verschiedene Unternehmen in den letzten 30 Commits, wobei jedes dieser
Teammitglieder mindestens fünf Commits gemacht haben sollte.

.. _lock-dependencies:

Werden Abhängigkeiten deklariert und festgeschrieben?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
wird. Alternativ könnt ihr auch ``pip-compile --generate-hashes`` der `pip-tools
<https://pip-tools.readthedocs.io/en/stable/>`_ verwenden:

.. code-block:: console

   $ python -m pip install pip-tools
   $ pip-compile --generate-hashes pyproject.toml -o requirements.txt

.. seealso::
   * `Secure installs <https://pip.pypa.io/en/stable/topics/secure-installs/>`_

Ihr solltet jedoch nicht nur für eure Python-Abhängigkeiten Hash-Pinning
verwenden, sondern :abbr:`z. B. (zum Beispiel)` auch für eure :doc:`pre-commit
Checks <../git/advanced/hooks/checks>` und :ref:`GitHub Actions <pinact>`.

Hash-Pinning schützt jedoch nicht davor, ein schädliches Paket zum ersten Mal zu
installieren; in diesem Fall würdet ihr nur den Hash des schädlichen Pakets
festlegen. Daher solltet ihr das Hash-Pinning mit Schwachstellen-Scans und
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

Alternativ könnt ihr euch auch von :doc:`../envs/uv/dependency-bot` unterstützen
lassen.

.. _vulnerability_scans:

Schwachstellen-Scans
--------------------

*Dependency Pinning* verhindert unbefugte Änderungen – doch was passiert, wenn
ihr eine Version festgeschrieben habt, die eine bekannte Sicherheitslücke
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

Ihr könnt die Schwachstellen-Analyse mit ``uv-audit`` auch in eure :doc:`prek
<../git/advanced/hooks/prek>`-Checks übernehmen:

.. code-block:: yaml

   - repo: https://github.com/astral-sh/uv-pre-commit
     rev: d9fca3320346514799461a80b0753eb45d707d46 # 0.11.28
     hooks:
     - id: uv-audit
       files: ^(uv\.lock|pyproject\.toml)$

Sicherheitsprüfungen sollten automatisiert durchgeführt werden. Hierzu könnt ihr
``uv audit`` :abbr:`z. B. (zum Beispiel)` in einer GitHub Action verwenden:

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
<https://pypi.org/project/pip-audit/>`_ verwenden. Es gibt auch eine
entsprechende GitHub-Action: `pypa/gh-action-pip-audit
<https://github.com/pypa/gh-action-pip-audit>`_.

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
#. ``pip`` schaut jedoch in allen Indexen nach und wählt die höchste Version
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

:term:`uv` verwendet hingegen üblicherweise die ``first-index``-Strategie, nimmt
also den erstgenannten Index, in dem ein Paket gefunden wird. Dadurch werden die
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

Überprüft Package Attestations
------------------------------

:term:`PyPI` :ref:`Package Attestations <package-attestations>` liefern mithilfe
von `Sigstore <https://www.sigstore.dev>`_ einen kryptografischen Nachweis über
die Herkunft eines Pakets gemäß :pep:`740`. Seit `gh-action-pypi-publish v1.11.0
<https://github.com/pypa/gh-action-pypi-publish/discussions/281>`_ werden
die Bescheinigungen auch automatisch generiert. Bis Ende 2025 nutzten mehr als
50-Tsd. Projekte *Trusted Publishing*, und 17 % der Uploads enthielten
Attestations. *Trusted Publishing* wurde zudem auf Organisationen und
selbstverwaltete GitLab-Instanzen ausgeweitet.

.. seealso::
   * `PyPI in 2025: A Year in Review
     <https://blog.pypi.org/posts/2025-12-31-pypi-2025-in-review/>`_
   * `Are we PEP 740 yet? 🔏
     <https://trailofbits.github.io/are-we-pep740-yet/>`_

:pep:`740` definiert neben *Package Attestations* auch :abbr:`SLSA (Supply-chain
Levels for Software Artifacts)`-Provenance-Attestations. Für Anwendungsfälle
außerhalb von :term:`PyPI` kann `actions/attest
<https://github.com/actions/attest>`_ diese SLSA-Provenienz- und
:doc:`SBOM <sbom>`-Bescheinigungen für jedes Artefakt generieren.

Im Fall des Angriffs auf :ref:`Ultralytics <ultralytics>` hätte mit den
Attestations erkannt werden können, welche Versionen aus einem kompromittierten
Workflow stammten und welche legitim waren – ganz ohne manuelle forensische
Analyse. Die Transparency-Logs von Sigstore bieten einen unabhängigen Prüfpfad
mit exakten Zeitstempeln und Angaben zur Herkunft jedes veröffentlichten
Artefakts.

Fügt zeitbasierte Abwehrmaßnahmen hinzu
---------------------------------------

Wenn ein bösartiges Paket auf :term:`PyPI` veröffentlicht wird, ist es sofort
weltweit verfügbar. Die Erkennungszeiten variieren – manche Angriffe werden
innerhalb weniger Stunden entdeckt, während andere wochen- oder monatelang
unbemerkt bleiben. 2025 gab es über 2.000 Malware-Meldungen, wovon 66 %
innerhalb von vier Stunden bearbeitet wurden.

Mit dem Abwarten vor der Verwendung neu veröffentlichter Pakete erhaltet ihr
zwar keine Garantie, aber das Risiko wird vermindert, da die Community
vermutlich innerhalb kurzer Zeit offensichtliche Bedrohungen aufdeckt.

Moderne Paketmanager unterstützen zeitbasierte Filterung. :term:`uv` verfügt
über die Option ``--exclude-newer``, und pip ≥ v26 hat die Option
``--uploaded-prior-to`` mit demselben Zweck eingeführt wobei beide sich gemäß
:pep:`700` auf Metadaten zur Upload-Zeit stützen.

Verwendet interne Paket-Repositories in euren Organisationen
------------------------------------------------------------

In kleineren Organisationen kann ein einfacher Spiegel des :term:`PyPI`, der
Pakete um eine Woche verzögert bereitstellt, bereits das Sicherheitsrisiko für
die Organisation vermindern. Ihr solltet dann jedoch darauf achten, dass ihr für
kritische Sicherheits-Patches die Verzögerung aufheben könnt. Sofern ihr in
eurer Organisation interne Paket-Repositories verwendet, könnt ihr darüberhinaus
noch weitere Sicherheitsmaßnahmen treffen:

#. Automatisierte Security-Scans der Pakete
#. Automatisiertes Bauen der Pakete mit `fromager
   <https://fromager.readthedocs.io/en/latest/>`_

Reagiert schnell, wenn ihr ein schädliches Paket entdeckt
---------------------------------------------------------

Wenn ihr ein kompromittiertes Paket bei euch entdeckt, könnt ihr mit schnellem
Handeln häufig größeren Schaden vermeiden.

#. Isoliert das Paket unverzüglich

   Stoppt alle Deployments, die diese Abhängigkeit nutzen, und sperrt die
   Paketversion in eurem internen Mirror, falls ihr einen solchen betreibt. Ziel
   ist es, weitere Installationen zu verhindern, während ihr die Ursache weiter
   untersuchen könnt.

#. Bewertet den Schaden

   Überprüft anhand von Logs und Prozessdaten, ob der Schadcode ausgeführt
   wurde. Ermittelt, auf welche vertraulichen Daten das Paket möglicherweise
   zugegriffen hat: Umgebungsvariablen, Anmeldedaten, Cloud-Token :abbr:`etc.
   (et cetera)`. Nutzt eure :doc:`SBOM <sbom>`, um alle betroffenen Projekte bei
   euch im Unternehmen zu identifizieren.

#. Begrenzt den Schaden

   Ändert alle Anmeldedaten, auf die das Paket möglicherweise zugegriffen hat:
   API-Schlüssel, Datenbankpasswörter, Cloud-Anmeldedaten. Scannt Systeme auf
   Anzeichen einer Kompromittierung und überprüft ausgehende
   Netzwerkverbindungen auf Anzeichen von Datenexfiltration.

#. Entfernt die Abhängigkeit vollständig

   Fixiert eine bekanntermaßen fehlerfreie Version und entfernt die Abhängigkeit
   vollständig. Führt ``pip-audit`` aus, um sicherzustellen, dass keine weiteren
   Schwachstellen eingeführt wurden. Aktualisiert anschließend eure Lockfiles
   mit der korrigierten Version.

#. Meldet das schädliche Paket

   Über `PyPI’s security reporting system <https://pypi.org/security/>`_ könnt
   ihr das schädliche Paket melden. Benachrichtigt auch Verantwortliche eurer
   Organisation und potenziell betroffene Kunden. Dokumentiert den Vorfall: Was
   ist passiert? Wie wurde das Paket entdeckt? Welche Änderungen habt ihr
   vorgenommen, um eine Wiederholung zu verhindern?

Überprüft, ob eure Abhängigkeiten noch gewartet werden?
-------------------------------------------------------

Es sollte regelmäßig überprüft werden, ob eine Abhängigkeit archiviert wurde.
Die Checks der OSSF-Scorecard sind jedoch nur erfolgreich, wenn das Projekt
älter als 90 Tage ist. Ein Mangel an aktiver Wartung ist jedoch nicht unbedingt
immer ein Problem: insbesondere kleinere Dienstprogramme müssen normalerweise
nur sehr selten gewartet werden. Fehlende aktive Wartung weist euch also nur
darauf hin, dass ihr die Situation genauer untersuchen solltet.

Mit `pypi-changes <https://github.com/gaborbernat/pypi-changes>`_ gibt es ein
CLI-Tool, das die für einem Python-Interpreter installierten Pakete überprüft
und mit den neuesten Versionen auf :term:`PyPI` vergleicht. Es zeigt an, welche
Pakete veraltet sind, wie lange die Veröffentlichung der jeweiligen Version
zurückliegt, und hebt wichtige Versionssprünge hervor, damit ihr fundierte
Entscheidungen bezüglich Upgrades treffen können, :abbr:`z. B. (zum Beispiel)`:

.. figure:: pypi-changes.png
   :alt: Kommandozeilenaufruf uvx pypi-changes mit der Auflistung aller in einem
         Projekt verwendeten Python-Bibliotheken, deren Version und
         Veröffentlichungsdatum

..
    $ uvx pypi-changes
    Installed 26 packages in 18ms
    🐍 Distributions within
    /Users/veit/.cache/uv/archive-v0/soguBMAn2UOVYxDU/bin/python
    ├── annotated-types 0.8.0 7 days
    ├── certifi 2026.7.22 9 days
    ├── soupsieve 2.9.1 9 days
    ├── pypi-changes 1.6.0 9 days
    ├── platformdirs 4.11.0 9 days
    ├── charset-normalizer 3.4.9 a month
    ├── requests-cache 1.3.3 a month
    ├── typing_extensions 4.16.0 a month
    ├── humanize 4.16.0 a month
    ├── beautifulsoup4 4.15.0 2 months
    ├── idna 3.18 2 months
    ├── pydantic_core 2.46.4 3 months remote 2.47.0 2 months
    ├── requests 2.34.2 3 months
    ├── urllib3 2.7.0 3 months
    ├── markdown-it-py 4.2.0 3 months
    ├── pydantic 2.13.4 3 months
    ├── url-normalize 3.0.0 3 months
    ├── packaging 26.2 3 months
    ├── rich 15.0.0 4 months
    ├── Pygments 2.20.0 4 months
    ├── attrs 26.1.0 4 months
    ├── cattrs 26.1.0 5 months
    ├── mailbits 0.2.3 8 months
    ├── typing-inspection 0.4.2 10 months
    ├── pypi-simple 1.8.0 11 months
    └── mdurl 0.1.2 3 years

Alternativ könnt ihr euch auch die PyPI-Versionen eines Projekts mit Badges
anzeigen lassen, :abbr:`z. B. (zum Beispiel)`:

+---------------+-------------------------------------------------------+
| Paketname     | aktuelle PyPI-Version                                 |
+===============+=======================================================+
| pypi-simple   | .. image:: https://img.shields.io/pypi/v/pypi-simple  |
|               |    :alt: PyPI Version                                 |
|               |    :target: https://pypi.org/project/pypi-simple      |
+---------------+-------------------------------------------------------+
| mdurl         | .. image:: https://img.shields.io/pypi/v/mdurl        |
|               |    :alt: PyPI Version                                 |
|               |    :target: https://pypi.org/project/mdurl            |
+---------------+-------------------------------------------------------+

.. tab:: reST

   .. code-block:: rst

      +---------------+-------------------------------------------------------+
      | Paketname     | aktuelle PyPI-Version                                 |
      +===============+=======================================================+
      | pypi-simple   | .. image:: https://img.shields.io/pypi/v/pypi-simple  |
      |               |    :alt: PyPI Version                                 |
      |               |    :target: https://pypi.org/project/pypi-simple      |
      +---------------+-------------------------------------------------------+
      | mdurl         | .. image:: https://img.shields.io/pypi/v/mdurl        |
      |               |    :alt: PyPI Version                                 |
      |               |    :target: https://pypi.org/project/mdurl            |
      +---------------+-------------------------------------------------------+

.. seealso::
   * `Is it maintained? <https://isitmaintained.com/>`_
