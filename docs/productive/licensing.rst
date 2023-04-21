Lizenzieren
===========

Damit andere eure Software verwenden können, sollte sie eine oder mehrere
Lizenzen erhalten, die die Nutzungsbedingungen beschreiben. Andernfalls dürfte
sie meist urheberrechtlich geschützt sein. Urheber sind diejenigen, die zur
Software originär beigetragen haben. Wenn eine Software relizenziert werden
soll, ist die Zustimmung aller Personen erforderlich, die Urheberschaft
beanspruchen können.

.. note::
   Dies stellt keine Rechtsberatung dar. Wendet euch im Zweifelsfall bitte an
   eine Rechtsvertretung oder die Rechtsabteilung eures Unternehmens.

.. seealso::
   * `The Whys and Hows of Licensing Scientific Code
     <https://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/>`_
   * `A Quick Guide to Software Licensing for the Scientist-Programmer
     <https://doi.org/10.1371/journal.pcbi.1002598>`_
   * Karl Fogel: `Producing Open Source Software <https://producingoss.com/>`_
   * `Forschungsdaten veröffentlichen
     <https://forschungsdaten.info/themen/rechte-und-pflichten/forschungsdaten-veroeffentlichen/>`_

Proprietäre Softwarelizenzen
----------------------------

Proprietäre Softwarelizenzen sind selten standardisiert; sie können kommerziell,
Shareware oder Freeware sein.

Freie und Open-Source Softwarelizenzen
--------------------------------------

Sie werden von der `Free Software Foundation (FSF)
<https://www.fsf.org/de/?set_language=de>`_ und der `Open Source Initiative
(OSI) <https://opensource.org/>`_ definiert. Dabei kann im Wesentlichen
unterschieden werden zwischen Copyleft-, freizügigen- und gemeinfreien Lizenzen.

Copyleft-Lizenzen
~~~~~~~~~~~~~~~~~

Copyleft-Lizenzen verpflichten die Lizenznehmer, jegliche Bearbeitung der
Software unter die Lizenz des ursprünglichen Werks zu stellen. Dies soll
Nutzungseinschränkungen der Software verhindern. Die bekannteste Copyleft-Lizenz
ist die GNU General Public License (GPL). Dabei wird das Copyleft der GPL als
sehr stark, das der Mozilla Public License hingegen als sehr schwach angesehen.

Da die Lizenzgeber nicht selbst an ihr eigenes Copyleft gebunden sind, können sie
neue Versionen auch unter proprietärer Lizenz veröffentlichen oder Dritten dies
erlauben (Mehrfachlizenzierung).

Durch Copyleft-Lizenzen können jedoch schnell Inkompatibilitäten auch zu freien
Lizenzen ohne Copyleft entstehen. So ist beispielsweise die 3-Clause-BSD-Lizenz
mit der GPL inkompatibel.

Freizügige Open-Source-Lizenzen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Freizügige oder permissive Open-Source-Lizenzen erlauben eine breitere
Wiederverwendung als die Copyleft-Lizenzen. Ableitungen und Kopien des
Quellcodes können unter Bedingungen verbreitet werden, die grundlegend andere
Eigenschaften haben als die der Originallizenz. Die bekanntesten Beispiele
solcher Lizenzen sind die MIT-Lizenz und die BSD-Lizenz.

Gemeinfreie Lizenzen
~~~~~~~~~~~~~~~~~~~~

Bei gemeinfreien oder Public Domain-Lizenzen gehen die Urheberrechte an die
Allgemeinheit über. Zur Kennzeichnung der Freigabe weitest möglicher
Nutzungsrechte wurde die Creative Commons Zero-Lizenz erstellt.

Nicht-Software-Lizenzen
-----------------------

Open-Source-Software-Lizenzen können auch für Werke verwendet werden, die nicht
Software sind. Oft sind sie auch die beste Wahl, insbesondere wenn die
betreffenden Werke als Quelltext bearbeitet und versioniert werden.

Daten, Medien, etc.
~~~~~~~~~~~~~~~~~~~

`CC0-1.0 <https://creativecommons.org/publicdomain/zero/1.0/deed.de>`_,
`CC-BY-4.0 <https://creativecommons.org/licenses/by/4.0/deed.de>`_ und
`CC-BY-SA-4.0 <https://creativecommons.org/licenses/by-sa/4.0/deed.de>`_ sind
offene Lizenzen, die für Nicht-Software-Material verwendet werden, von
Datensätzen bis zu Videos. Sie sind jedoch `nicht für Software empfohlen
<https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software>`_.

Die `Open Knowledge Foundation <https://okfn.org>`_ hat ebenfalls eine Reihe von
`Open Data Commons <https://opendatacommons.org>`_-Lizenzen für
Daten/Datenbanken veröffentlicht:

`Open Data Commons Open Database License (ODbL) v1.0 <https://opendatacommons.org/licenses/odbl/1-0/>`_
    Namensnennung und Weitergabe unter gleichen Bedingungen.
`Open Data Commons Attribution License (ODC-By) v1.0 <https://opendatacommons.org/licenses/by/1-0/>`_
    Namensnennung.
`Open Data Commons Public Domain Dedication and License (PDDL) v1.0 <https://opendatacommons.org/licenses/pddl/1-0/>`_
    Die PDDL stellt die Daten in den öffentlichen Bereich und verzichtet auf
    alle Rechte.

`GovData <https://www.govdata.de>`_ hat die *Datenlizenz Deutschland* in zwei
Varianten vorgelegt:

* `Datenlizenz Deutschland – Namensnennung – Version 2.0
  <https://www.govdata.de/dl-de/by-2-0>`_
* `Datenlizenz Deutschland – Zero – Version 2.0
  <https://www.govdata.de/dl-de/zero-2-0>`_

Bei der Verwendung des `Community Data License Agreement – Permissive, Version 2.0 <https://cdla.dev/permissive-2-0/>`_ müssen die Urheberrechtshinweise
beibehalten werden.

Eine weitere mögliche Lizenz für künstlerische Werke ist die `Free Art License
1.3 <https://artlibre.org/licence/lal/en/>`_.

Dokumentation
~~~~~~~~~~~~~

Jede Open-Source-Softwarelizenz oder offene Lizenz für Medien gilt auch für
Software-Dokumentation. Wenn ihr unterschiedliche Lizenzen für eure Software und
deren Dokumentation verwendet, solltet ihr darauf achten, dass die
Quellcode-Beispiele in der Dokumentation auch unter der Software-Lizenz
lizenziert sind. Neben den oben bereits genannten Creative Commons-Lizenzen gibt
es speziell für freie Dokumentationen folgende Lizenzen.

`GNU Free Documentation License (FDL) <https://www.gnu.org/licenses/fdl-1.3.txt>`_
    Copyleft-Lizenz für Dokumentationen, die für alle GNU-Handbücher verwendet
    werden soll. Ihre Anwendbarkeit ist auf textuelle Werke (Bücher) beschränkt.
`FreeBSD Documentation License <https://www.freebsd.org/copyright/freebsd-doc-license/>`_
    Freizügige Dokumentationslizenz mit Copyleft, die mit der GNU FDL vereinbar
    ist.
`Open Publication License, Version 1.0 <https://opencontent.org/openpub/>`_
    freie Dokumentationslizenz mit Copyleft, sofern keine der Lizenzoptionen
    aus Abschnitt VI der Lizenz wahrgenommen werden. In jedem Fall ist sie mit
    der GNU FDL unvereinbar.

Schriftarten
~~~~~~~~~~~~

`SIL Open Font License 1.1 <https://opensource.org/licenses/OFL-1.1>`_
    Schriftlizenz, die in anderen Werken frei verwendet werden kann.
`GNU General Public License 3 <https://www.gnu.org/licenses/gpl-3.0>`_
    Sie kann auch für Schriften verwendet werden, sie darf jedoch nur mit der
    `Schriftausnahme <https://www.gnu.org/licenses/gpl-faq.html#FontException>`_
    in Dokumente eingebunden werden.

    .. seealso::
       * `Font Licensing <https://www.fsf.org/blogs/licensing/20050425novalis>`_

`LaTeX ec fonts <https://dante.ctan.org/tex-archive/fonts/ec/src/copyrite.txt>`_
    Freie *European Computer Modern- und Text Companion*-Schriften, die
    üblicherweise mit Latex verwendet werden.
`Arphic Public License <https://spdx.org/licenses/Arphic-1999>`_
    Freie Lizenz mit Copyleft.
`IPA Font license <https://spdx.org/licenses/IPA.html>`_
    Freie Lizenz mit Copyleft, deren abgeleitete Werte jedoch nicht den Namen
    des Originals verwenden oder beinhalten dürfen.

Hardware
~~~~~~~~

Entwürfe für `Open-Source-Hardware <https://www.oshwa.org/definition/>`_ werden
von den CERN Open Hardware Lizenzen abgedeckt:

`CERN-OHL-P-2.0 <https://ohwr.org/cern_ohl_p_v2.txt>`_
    permissiv
`CERN-OHL-W-2.0 <https://ohwr.org/cern_ohl_w_v2.txt>`_
    schwach reziprok
`CERN-OHL-S-2.0 <https://ohwr.org/cern_ohl_s_v2.txt>`_
    stark reziprok

Auswahl geeigneter Lizenzen
---------------------------

Übersichten über mögliche Lizenzen findet ihr in `SPDX License List
<https://spdx.org/licenses/>`_ oder `OSI Open Source Licenses by Category
<https://opensource.org/licenses/category>`_. Bei der Wahl geeigneter
Lizenzen unterstützt euch die Website `Choose an open source license
<https://choosealicense.com/>`_ und `Comparison of free and open-source
software licenses
<https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses>`_.

Wenn ihr :abbr:`z.B. (zum Beispiel)` eine möglichst große Verbreitung eures
Pakets erreichen wollt, sind MIT- oder die BSD-Varianten eine gute Wahl. Die
Apache-Lizenz schützt euch besser vor Patentverletzungen, ist jedoch nicht
kompatibel mit der GPL v2.

Abhängigkeiten überprüfen
~~~~~~~~~~~~~~~~~~~~~~~~~

Daher solltet ihr schauen, welche Lizenzen diejenigen Pakete haben, von denen
ihr abhängt und zu denen ihr kompatibel sein solltet. Zur Analyse von Lizenzen
könnt ihr euch `License compatibility
<https://en.wikipedia.org/wiki/License_compatibility>`_ anschauen und den
`licensechecker
<https://boyter.org/2018/03/licensechecker-command-line-application-identifies-software-license/>`_,
verwenden, ein Kommandozeilenwerkzeug, das Installationsverzeichnisse nach
Lizenzen durchsucht.

Darüberhinaus kann es auch sinnvoll sein, ein Package unter mehreren Lizenzen
zu veröffentlichen. Ein Beispiel hierfür ist `cryptography/LICENSE
<https://github.com/pyca/cryptography/blob/adf234e/LICENSE>`_.

GitHub
------

Auf `GitHub <https://github.com/>`_ könnt ihr euch eine Open Source-Lizenz in
eurem Repository erstellen lassen.

#. Geht zur Hauptseite eures Repository.
#. Klickt auf *Create new file* und gebt anschließend als Dateiname ``LICENSE``
   oder ``LICENSE.md`` ein.
#. Anschließend könnt ihr rechts neben dem Feld für den Dateinamen auf *Choose a
   license template* klicken.
#. Nun könnt ihr die für euer Repository passende Open Source-Lizenz auswählen.
#. Ihr werdet nun zu zusätzlichen Angaben aufgefordert, sofern die gewählte
   Lizenz dies erfordert.
#. Nachdem ihr eine Commit-Message angegeben habt, :abbr:`z.B. (zum Beispiel)`
   ``Add license``, könnt ihr auf *Commit new file* klicken.

Falls ihr in eurem Repository bereits eine ``/LICENSE``-Datei hinzugefügt habt,
verwendet GitHub `licensee <https://github.com/licensee/licensee>`_ um die Datei
mit einer kurzen `Liste von Open-Source-Lizenzen
<https://choosealicense.com/appendix/>`_ abzugleichen. Falls GitHub die Lizenz
eures Repository nicht erkennen kann, enthält es möglicherweise mehrere
Lizenzen oder ist zu komplex. Überlegt Euch dann, ob ihr die Lizenz vereinfachen
könnt, :abbr:`z.B. (zum Beispiel)` indem ihr Komplexität in die
``/README``-Datei auslagert.

Umgekehrt könnt ihr auf GitHub auch nach Repositories mit bestimmten Lizenzen
oder Lizenzfamilien suchen. Eine Übersicht über die Lizenz-Schlüsselwörter
erhaltet ihr in `Searching GitHub by license type
<https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository#searching-github-by-license-type>`_.

Schließlich könnt ihr euch von `Shields.io <https://shields.io/>`_ ein
License-Badge generieren lassen, das ihr :abbr:`z.B. (zum Beispiel)` auf eurer
``README``-Datei einbinden könnt:

.. code-block:: rst

    |License|

    .. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
       :target: https://github.com/veit/jupyter-tutorial/blob/main/LICENSE

|License|

.. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
   :target: https://github.com/veit/jupyter-tutorial/blob/main/LICENSE

Standardformat für die Lizenzierung
-----------------------------------

`SPDX <https://spdx.dev/>`_ steht für *Software Package Data Exchange* und
definiert eine standardisierte Methode zum Austausch von Urheberrechts- und
Lizenzinformationen zwischen Projekten und Personen. Die passenden
SPDX-Identifier könnt ihr aus der `SPDX License List
<https://spdx.org/licenses/>`_ auswählen und dann in den Kopf eurer
Lizenzdateien eintragen:

.. code-block::

    # SPDX-FileCopyrightText: [year] [copyright holder] <[email address]>
    #
    # SPDX-License-Identifier: [identifier]

Konformität überprüfen
----------------------

`REUSE <https://reuse.software/de/>`_ wurde von der :abbr:`FSFE (Free Software
Foundation Europe)` initiiert, um die Lizenzierung freier Software-Projekte zu
erleichtern. Das `REUSE tool <https://git.fsfe.org/reuse/tool>`_ überprüft
Lizenzen und unterstützt euch bei der Einhaltung der Lizenzkonformität. Mit der
`REUSE API <https://reuse.software/dev/#api>`_ könnt ihr euch auch ein
dynamisches Compliance-Badge generieren:

.. figure:: reuse-compliant.svg
   :alt: REUSE-compliant Badge

.. _gitlab-ci-workflow:

GitLab-CI-Workflow
~~~~~~~~~~~~~~~~~~

Ihr könnt REUSE einfach in euren Continuous Integration-Workflow integrieren,
:abbr:`z.B. (zum Beispiel)` für GitLab in der ``.gitlab-ci.yml``-Datei mit:

.. code-block:: yaml

    reuse:
      image:
        name: fsfe/reuse:latest
        entrypoint: [""]
      script:
        - reuse lint

Alternativen
~~~~~~~~~~~~

`ClearlyDefined <https://clearlydefined.io/>`_
    Es sammelt und zeigt Informationen über die Lizenzierungs- und
    Urheberrechtssituation eines Software-Projekts an.
`OpenChain <https://www.openchainproject.org/>`_
    Es empfiehlt REUSE als eine Komponente, um die Klarheit der Lizenz- und
    Urheberrechtssituation zu verbessern, stellt jedoch höhere Anforderungen, um
    eine vollständige Konformität zu erreichen.
`FOSSology <https://www.fossology.org/>`_
    Toolkit für die Einhaltung freier Software, das Informationen in einer
    Datenbank mit Lizenz-, Copyright- und Exportscanner speichert.

Python-Paket-Metadaten
----------------------

In Python-Paketen gibt es noch weitere Felder, in denen Lizenzinformationen
gespeichert werden, wie die `Core metadata specifications
<https://packaging.python.org/en/latest/specifications/core-metadata/>`_, die
zudem limitiert sind. Dies führt nicht nur zu Problemen für die Autoren, die
richtige Lizenz angeben zu können, sondern auch zu Problemen beim Re-Paketieren
für diverse Linux-Distributionen.

Aktuell werden zwar einige häufige Fälle abgedeckt und die Lizenzklassifizierung
kann auch erweitert werden, es gibt jedoch einige beliebte Klassifizierungen wie
:samp:`License :: OSI Approved :: BSD License`, die abgeschafft werden. Damit
ist dann jedoch die Abwärtskompatibilität nicht mehr gewährleistet und die
Pakete müssen relizensiert werden. Immerhin habt ihr mit `trove-classifiers
<https://github.com/pypa/trove-classifiers>`_ auch eine Möglichkeit, eure
Trove-Klassifizierungen zu überprüfen.

.. seealso::
   * `PEP 639 – Improving License Clarity with Better Package Metadata
     <https://peps.python.org/pep-0639/>`_
   * `PEP 621 – Storing project metadata in pyproject.toml
     <https://peps.python.org/pep-0621/>`_
   * `PEP 643 – Metadata for Package Source Distributions
     <https://peps.python.org/pep-0643/>`_
