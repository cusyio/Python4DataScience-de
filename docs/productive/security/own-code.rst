.. SPDX-FileCopyrightText: 2023 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Eigener Code
============

Angriffe auf die Lieferkette gehen nicht nur von :doc:`dependencies` aus, auch
euer eigener Code kann Angriffspunkte liefern. Ein fest im Quellcode
hinterlegtes PyPI-Token liefert, sobald es in ein öffentliches Repository
hochgeladen wurde, alles, was für einem Angriff benötigt wird und euer Konto zu
kompromittieren und bösartige Pakete unter eurem Namen zu veröffentlichen.
Abgesehen von Secrets verbergen sich häufige Sicherheitsfehler in alltäglichen
Codemustern, die bei einem Code-Review zunächst unbedenklich erscheinen und von
Menschen übersehen werden können. Diese mit einem Linter aufzuspüren, ist die
erste Verteidigungsstufe.

.. card-carousel:: 1

   .. card::

      **Das ewige Geheimnis**

      Durchgesickerte Zugangsdaten sind der Ausgangspunkt für viele
      Sicherheitsverletzungen in der Lieferkette. Ein offengelegtes
      :term:`PyPI`-Token ermöglicht, mit Hintertüren versehene Versionen eurer
      Pakete zu veröffentlichen. Eine offengelegte Datenbank-URL ermöglicht,
      Daten  zu entwenden. Und doch ist ein solches Muster weit verbreitet.
      Besser ist die Verwendung von Umgebungsvariablen:

      .. code-block:: python

         import os

         DATABASE_KEY = os.environ["DB_KEY"]
         DATABASE_URL = os.environ["DB_URL"]

      .. warning::
         Git vergisst nie: wenn ihr ein Secret einmal durch Git verwaltet habt,
         bleibt es für immer in der Historie eures Repositories erhalten. Es in
         einem späteren Commit einfach zu löschen, hilft nicht wirklich. Alle,
         die Zugriff auf das Repository haben, können diese Anmeldedaten wieder
         extrahieren. Bei Angriffen wird oft zunächst die Git-Historie nach
         Geheimnissen durchforstet, und ein einmal veröffentlichts PyPI-Token
         oder Cloud-Anmeldedaten sind oft der erste Schritt bei einer
         Kompromittierung der Lieferkette.

   .. card::

      **Kryptografische Schwachstellen**

      Weitere häufige Sicherheitslücken sind kryptografische Schwachstellen wie
      `MD5 <https://de.wikipedia.org/wiki/Message-Digest_Algorithm_5>`_ und
      `SHA-1 <https://de.wikipedia.org/wiki/Secure_Hash_Algorithm#SHA-1>`_.
      MD5-Kollisionen wurden erstmals 2004 nachgewiesen und SHA1-Kollisionen
      2017. Es können also Kollisionen erzeugt werden durch andere Eingaben, die
      denselben Hash-Wert ergeben. Dies ermöglicht die Fälschung von
      Zertifikaten, die Manipulation von Downloads oder die Umgehung von
      Integritätsprüfungen. Verwendet daher keines der beiden Verfahren für
      Sicherheitszwecke sondern stattdessen `SHA256 oder besser
      <https://de.wikipedia.org/wiki/SHA-2>`_:

      .. code-block:: python

         import hashlib

         digest = hashlib.sha256(payload).hexdigest()

   .. card::

      **Hängende Verbindungen**

      Das hier ist zwar subtil, aber dennoch gefährlich, da  ein langsamer
      Server euren Prozess auf unbestimmte Zeit zum Stillstand bringen kann. Ein
      Angriff über einen solchen Server, mit dem eure Anwendung kommuniziert,
      kann jede Anfrage zum Erliegen bringen, euren Thread-Pool erschöpfen und
      einen Denial-of-Service-Angriff auslösen. Eure gesamte Anwendung kommt
      dann zum Stillstand, weil ihr einen Parameter vergessen habt. Daher
      solltet ihr immer einen Timeout angeben:

      .. code-block:: pycon

         >>> import httpx
         >>> r = httpx.get("https://httpbin.org/get", timeout=30)
         httpx.ReadTimeout: The read operation timed out

.. _bandit:

Erkennt Sicherheitslücken mit Ruff
----------------------------------

:doc:`../qa/ruff` ist ein schneller Python-Linter, der umfassende
Sicherheitsregeln von :ref:`Bandit <bandit>` enthält:

.. code-block:: console

   $ uvx ruff check --select S .

.. seealso::
   Weitere Informationen findet ihr in der `Dokumentation zu den
   Ruff-Sicherheitsregeln
   <https://docs.astral.sh/ruff/rules/#flake8-bandit-s>`_.

Für zukünftige Checks könnt ihr ``ruff`` ihn in der :file:`pyproject.toml`-Datei
konfigurieren:

.. code-block:: toml

   [tool.ruff]
   lint.select = ["S"]

Die Sicherheitsregeln ``["S"]`` mit den Bandit-Prüfungen.spüren fest codierte
Geheimnisse, schwache Verschlüsselung und unsichere Deserialisierung auf. Dabei
läuft Ruff in weniger als einer Sekunde, sodass ihr es während der Eingabe in
eurer IDE und vor jedem Commit ausführen könnt. Alle drei oben genannten
Schwachstellen werden erkannt und noch viel mehr, :abbr:`u. a. (unter anderem)`:

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
| `S608`_| SQL-Injection über String-Formatierung                                |
+--------+-----------------------------------------------------------------------+

.. seealso::
   * `flake8-bandit (S) <https://docs.astral.sh/ruff/rules/#flake8-bandit-s>`_
   * `lint.flake8-bandit
     <https://docs.astral.sh/ruff/settings/#lintflake8-bandit>`_

Bandit könnt ihr auch in Jupyter Notebooks, :abbr:`IDEs (Integrated Development
Wnvironments)` und :doc:`../git/advanced/hooks/prek` integrieren.

Zudem könnt ihr :doc:`../qa/pysa` für `Taint
<https://en.wikipedia.org/wiki/Taint_checking>`_-Analysen verwenden.

Für GitHub-Repositories könnt ihr alternativ auch `CodeQL
<https://codeql.github.com>`_ verwenden; :abbr:`s.a. (siehe auch)`
`codeql-action
<https://github.com/github/codeql-action/blob/main/README.md#usage>`_.

Vertrauenswürdige Veröffentlichung
----------------------------------

In einem früheren Abschnitt haben wir schon einige Hinweise gegeben, wie die
Veröffentlichung von Python-Paketen auf :term:`PyPI` abgesichert werden kann:

.. seealso::
   * :ref:`secure-release-workflow`
   * :ref:`add_2fa`

.. seealso::
   * `Publishing package distribution releases using GitHub Actions CI/CD
     workflows
     <https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/>`_

.. _S105: https://docs.astral.sh/ruff/rules/hardcoded-password-string/
.. _S301: https://docs.astral.sh/ruff/rules/suspicious-pickle-usage/
.. _S307: https://docs.astral.sh/ruff/rules/suspicious-eval-usage/
.. _S113: https://docs.astral.sh/ruff/rules/request-without-timeout/
.. _S324: https://docs.astral.sh/ruff/rules/hashlib-insecure-hash-function/
.. _S608: https://docs.astral.sh/ruff/rules/hardcoded-sql-expression/
.. _S608: https://docs.astral.sh/ruff/rules/hardcoded-sql-expression/
