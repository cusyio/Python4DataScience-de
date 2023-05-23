Sicherheit
==========

In den vorherigen Kapiteln haben wir schon einige Hinweise gegeben, die einen
sichereren Betrieb ermöglichen. Hier wollen wir die einzelnen Elemente nun
nochmal zusammenfassen und erweitern. Dabei orientieren wir uns an der `OpenSSF
Scorecard <https://securityscorecards.dev/>`_. Alternativ könnt ihr euch auch an
:ref:`open_chain` orientieren.

Schwachstellen überprüfen
-------------------------

Risiko: Hoch

Mit dieser Prüfung wird festgestellt, ob das Projekt offene, nicht behobene
Sicherheitslücken in seiner eigenen Codebasis oder in seinen Abhängigkeiten
aufweist. Eine offene Sicherheitslücke kann leicht ausgenutzt werden und sollte
so schnell wie möglich geschlossen werden.

Für eine solche Überprüfung könnt ihr :abbr:`z.B. (zum Beispiel)` :ref:`pipenv
check <pipenv_check>` verwenden, das die Python-Bibliothek `safety
<https://github.com/pyupio/safety>`_ verwendet. Alternativ könnt ihr auch `osv
<https://pypi.org/project/osv/>`_ oder `pip-audit
<https://pypi.org/project/pip-audit/>`_ verwenden, das auf die `Open Source
Vulnerability Database <https://osv.dev>`_ zurückgreift.

Wenn eine Schwachstelle in einer Abhängigkeit gefunden wird, solltet ihr auf
eine Version nicht-anfällige Version aktualisieren; wenn kein Update verfügbar
ist, solltet ihr überlegen, die Abhängigkeit zu entfernen.

Wenn ihr glaubt, dass die Sicherheitslücke euer Projekt nicht betrifft, kann für
``osv`` eine :file:`osv-scanner.toml`-Datei erstellt werden, :abbr:`u.a. (unter
anderem)` mit der zu ignorierenden ID und einer Begründung, :abbr:`z.B. (zum
Beispiel)`:

.. code-block:: toml

   [[IgnoredVulns]]
   id = "GO-2022-1059"
   # ignoreUntil = 2022-11-09 # Optional exception expiry date
   reason = "No external http servers are written in Go lang."

Wartung
-------

Werden die Abhängigkeiten automatisch aktualisiert?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Hoch

Veraltete Abhängigkeiten machen ein Projekt anfällig für Angriffe auf bekannte
Schwachstellen. Daher sollte der Prozess der Aktualisierung von Abhängigkeiten
automatisiert werden, indem nach veralteten oder unsicheren Anforderungen
gesucht und :abbr:`ggf. (gegebenenfalls)` aktualisiert werden. Hierfür könnt ihr
:abbr:`z.B. (zum Beispiel)` `dependabot <https://github.com/dependabot>`_ oder
`PyUp <https://pyup.io>`_ verwenden.

Ihr könnt eure :doc:`/productive/envs/pipenv/index`-Umgebungen auch automatisch
mit :ref:`pipenv update <pipenv_update>` aktualisieren.

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

.. image:: https://img.shields.io/github/commit-activity/y/veit/jupyter-tutorial
   :alt: Jährliche Commit-Aktivität
.. image:: https://img.shields.io/github/commit-activity/m/veit/jupyter-tutorial
   :alt: Monatliche Commit-Aktivität
.. image:: https://img.shields.io/github/commit-activity/w/veit/jupyter-tutorial
   :alt: Wöchentliche Commit-Aktivität

Gibt es ein Sicherheitskonzept für das Projekt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Mittel

Idealerweise sollte mit dem Projekt eine Datei :file:`SECURITY.md` :abbr:`o.ä.
(oder ähnliches)` veröffentlicht worden sein. Diese Datei sollte Informationen
enthalten,

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
     <https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository>`_
   * `Runbook
     <https://github.com/ossf/oss-vulnerability-guide/blob/main/runbook.md>`_

Enthält das Projekt eine verwendbare Lizenz?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Niedrig

Eine :doc:`Lizenz </productive/licensing>` weist darauf hin, wie der Quellcode
verwendet werden darf oder nicht. Das Fehlen einer Lizenz erschwert jede Art von
Sicherheitsüberprüfung oder Audit und stellt ein rechtliches Risiko für die
potenzielle Nutzung dar.

OSSF-Scorecard verwendet die `GitHub License API
<https://docs.github.com/en/rest/licenses#get-the-license-for-a-repository>`_
für auf GitHub gehostete Projekte, ansonsten eine eigene Heuristik, um eine
veröffentlichte Lizenzdatei zu erkennen. Dateien in einem
:file:`LICENSES`-Verzeichnis sollten mit mit ihrem :ref:`SPDX
<standard_format_licensing>`-Lizenzbezeichner benannt werden, gefolgt
von einer entsprechenden Dateierweiterung, wie in der :ref:`REUSE
<reuse>`-Spezifikation beschrieben.

Wird nach den Best Practices der Core Infrastructure Initiative (CII) gehandelt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Niedrig

Das `Core Infrastructure Initiative (CII) Best Practices Program
<https://www.coreinfrastructure.org/programs/best-practices-program/>`_ umfasst
eine Reihe von sicherheitsorientierten Best Practices für die Entwicklung von
Open-Source-Software:

* das Verfahren zur Meldung von Schwachstellen ist auf der Projektseite
  veröffentlicht
* ein funktionierendes Build-System  erstellt die Software automatisch aus dem
  Quellcode neu
* eine allgemeine Richtlinie, dass Tests zu einer automatisierten Testsuite
  hinzugefügt werden, wenn wichtige neue Funktionen hinzukommen
* :abbr:`ggf. (gegebenenfalls)` verschiedene Kryptographie-Kriterien werden
  erfüllt
* mindestens ein statisches Code-Analyse-Tool, das auf jede geplante größere
  Produktionsversion angewendet wird

Mit dem `OpenSSF Best Practices Badge Programm
<https://bestpractices.coreinfrastructure.org/de>`_ könnt ihr euch auch ein
entsprechendes Badge holen.

Kontinuierliches Testen
-----------------------

Werden im Projekt CI-Tests durchgeführt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Niedrig

Bevor Code in Pull- oder Merge-Requests zusammengeführt wird, sollten Tests
durchgeführt werden, die dabei helfen, Fehler frühzeitig zu erkennen und die
Anzahl der Schwachstellen in einem Projekt zu reduzieren.

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
  <https://pypi.org/project/atheris/>`_ oder `OneFuzz
  <https://github.com/microsoft/onefuzz>`_?

Verwendet euer Projekt Werkzeuge zur statischen Codeanalyse?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Mittel

`Statische Codeanalysen <https://de.wikipedia.org/wiki/Statische_Code-Analyse>`_
testen den Quellcode, bevor die Anwendung ausgeführt wird. Dies kann verhindern,
dass bekannte Fehlerklassen versehentlich in die Codebasis eingeführt werden.

Um Schwachstellen zu überprüfen, könnt ihr `bandit
<https://github.com/PyCQA/bandit>`_ verwenden, das ihr auch in eure
:file:`.pre-commit-hooks.yaml` integrieren könnt:

.. code-block:: yaml

    repos:
    - repo: https://github.com/PyCQA/bandit
      rev: '1.7.5'
      hooks:
      - id: bandit

Zudem könnt ihr :doc:`/productive/qa/pysa` für `Taint
<https://en.wikipedia.org/wiki/Taint_checking>`_-Analysen verwenden.

Für GitHub-Repositories könnt ihr alternativ auch `CodeQL
<https://codeql.github.com>`_ verwenden; :abbr:`s.a. (siehe auch)`
`codeql-action <https://github.com/github/codeql-action#usage>`_.

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

Ist der Entwicklungsprozess anfällig für das Einschleusen von bösartigem Code?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Hoch

Mit :ref:`geschützten Git-Zweigen <protected_branches>` können Regeln für
die Übernahme von Änderungen in Standard- und Veröffentlichungszweige definiert
werden, :abbr:`z.B. (zum Beispiel)` automatisierte `statische Code-Analysen
<https://de.wikipedia.org/wiki/Statische_Code-Analyse>`_ mit :doc:`qa/flake8`,
:doc:`qa/pysa`, :doc:`qa/wily` und :ref:`Code-Reviews <code_reviews>` über
:abbr:`sog. (sogenannte)` :doc:`git/gitlab/merge-requests`.

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

Werden im Projekt Abhängigkeiten deklariert und festgeschrieben?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risiko: Mittel

In eurem Projekt sollten Abhängigkeiten, die während des Build- und
Release-Prozesses verwendet werden, festgeschrieben werden. Dabei sollte eine
*gepinnte Abhängigkeit* explizit auf einen bestimmten Hash gesetzt sein und
nicht nur auf eine veränderbare Version oder einen Versionsbereich.

:doc:`envs/spack/index` schreibt für die jeweilige Umgebung diese Hashes in
:ref:`spack_lock`, :doc:`envs/pipenv/index` in :ref:`Pipfile.lock <pipenv_lock>`
fest. Diese Dateien sollten daher ebenfalls mit dem Quellcode eingecheckt
werden.

Hierdurch können die folgenden Sicherheitsrisiken verringert werden:

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
