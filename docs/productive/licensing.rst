Lizenzieren
===========

Damit andere eure Software verwenden können, sollte sie eine Lizenz erhalten,
die die Nutzungsbedingungen beschreibt. Andernfalls dürfte sie meist
urheberrechtlich geschützt sein. Urheber sind diejenigen, die zur Software
originär beigetragen haben. Wenn eine Software relizenziert werden soll, ist
die Zustimmung aller Personen erforderlich, die Urheberschaft beanspruchen
können.

.. note::
   Dies stellt keine Rechtsberatung dar. Wendet euch im Zweifelsfall bitte an
   eine Rechtsvertretung oder die Rechtsabteilung eures Unternehmens.

.. seealso::
   * `The Whys and Hows of Licensing Scientific Code
     <https://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/>`_
   * `A Quick Guide to Software Licensing for the Scientist-Programmer
     <https://doi.org/10.1371/journal.pcbi.1002598>`_
   * Karl Fogel: `Producing Open Source Software <https://producingoss.com/>`_

Proprietäre Softwarelizenzen
----------------------------

Proprietäre Softwarelizenzen sind selten standardisiert; sie können kommerziell,
Shareware oder Freeware sein.

Freie und Open-Source Software-Lizenzen
---------------------------------------

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

Da die Lizenzgeber nicht selbst an ih eigenes Copyleft gebunden sind, können sie
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

Auswahl einer geeigneten Lizenz
-------------------------------

Übersichten über mögliche Lizenzen findet ihr in `SPDX License List
<https://spdx.org/licenses/>`_ oder `OSI Open Source Licenses by Category
<https://opensource.org/licenses/category>`_. Bei der Wahl einer geeigneten
Lizenz unterstützt Euch die Website `Choose an open source license
<https://choosealicense.com/>`_ und `Comparison of free and open-source
software licenses
<https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses>`_.

Wenn ihr z.B. eine möglichst große Verbreitung eures Pakets erreichen wollt,
sind MIT- oder die BSD-Varianten eine gute Wahl. Die Apache-Lizenz schützt euch
besser vor Patentverletzungen ist jedoch nicht kompatibel mit der GPL v2. Daher
solltet ihr schauen, welche Lizenzen diejenigen Pakete haben, von denen ihr
abhängt und zu denen ihr kompatibel sein solltet. Zur Analyse von Lizenzen könnt
`License compatibility <https://en.wikipedia.org/wiki/License_compatibility>`_
anschauen und den `licensechecker
<https://boyter.org/2018/03/licensechecker-command-line-application-identifies-software-license/>`_,
verwenden, ein Kommandozeilenwerkzeug, das Installationsverzeichnisse nach
Lizenzen durchsucht.

Darüberhinaus kann es auch sinnvoll sein, ein Package unter mehreren Lizenzen
zu veröffentlichen. Ein Beispiel hierfür ist `cryptography/LICENSE
<https://github.com/pyca/cryptography/blob/adf234e/LICENSE>`_.

GitHub
------

Auf `GitHub <https://github.com/>`_ könnt ihr Euch eine Open Source-Lizenz in
eurem Repository erstellen lassen.

#. Geht zur Hauptseite eures Repository.
#. Klickt auf *Create new file* und gebt anschließend als Dateiname ``LICENSE``
   oder ``LICENSE.md`` ein.
#. Anschließend könnt ihr rechts neben dem Feld für den Dateinamen auf *Choose a
   license template* klicken.
#. Nun könnt ihr die für euer Repository passende Open Source-Lizenz auswählen.
#. Ihr werdet nun zu zusätzlichen Angaben aufgefordert, sofern die gewählte
   Lizenz dies erfordert.
#. Nachdem ihr eine Commit-Message angegeben habt, z.B. ``Add license``, könnt
   ihr auf *Commit new file* klicken.

Falls ihr in eurem Repository bereits eine ``/LICENSE``-Datei hinzugefügt habt,
verwendet GitHub `licensee <https://github.com/licensee/licensee>`_ um die Datei
mit einer kurzen `Liste von Open-Source-Lizenzen
<https://choosealicense.com/appendix/>`_ abzugleichen. Falls GitHub die Lizenz
eures Repository nicht erkennen kann, enthält es möglicherweise mehrere
Lizenzen oder ist zu komplex. Überlegt Euch dann, ob ihr die Lizenz vereinfachen
könnt, z.B. indem ihr Komplexität in die ``/README``-Datei auslagert.

Umgekehrt könnt ihr auf GitHub auch nach Repositories mit bestimmten Lizenzen
oder Lizenzfamilien suchen. Eine Übersicht über die Lizenz-Schlüsswlwörter
erhaltet ihr in `Searching GitHub by license type
<https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository#searching-github-by-license-type>`_.

Schließlich könnt ihr euch von `Shields.io <https://shields.io/>`_ ein
License-Badge generieren lassen, das ihr z.B. auf eurer ``README``-Datei
einbinden könnt, z.B.

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

`REUSE <https://reuse.software/>`_ wurde von der Free Software Foundation Europe
(FSFE) initiiert, um die Lizenzierung freier Software-Projekte zu erleichtern.
Das `REUSE tool <https://git.fsfe.org/reuse/tool>`_ überprüft Lizenzen und
unterstützt euch bei der Einhaltung der Lizenzkonformität. Mit der `REUSE API
<https://reuse.software/dev/#api>`_ könnt ihr euch auch ein dynamisches
Compliance-Badge generieren:

.. figure:: reuse-compliant.svg
   :alt: REUSE-compliant Badge

CI-Workflow
~~~~~~~~~~~

Ihr könnt REUSE einfach in euren Continuous Integration-Workflow integrieren,
z.B. für GitLab in der ``.gitlab-ci.yml``-Datei mit:

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
    Urheberrechtssituation eines Software-Projekts an
`OpenChain <https://www.openchainproject.org/>`_
    Es empfiehlt REUSE als eine Komponente, um die Klarheit der Lizenz- und
    Urheberrechtssituation zu verbessern, stellt jedoch höhere Anforderungen, um
    eine vollständige Konformität zu erreichen.
`FOSSology <https://www.fossology.org/>`_
    Toolkit für die Einhaltung freier Software, das Informationen in einer
    Datenbank mit Lizenz-, Copyright- und Exportscanner

.. seealso::
    * `Python License tracker
      <https://wagenrace.github.io/python_dep_frontend/>`_
