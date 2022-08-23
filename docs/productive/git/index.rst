Code verwalten mit Git
======================

Um eine bessere Kontrolle über euren Quellcode zu erhalten, wird dieser
üblicherweise mit `Git <https://git-scm.com/>`_ verwaltet. `Git
<https://github.com/git/git>`__ ist ein ausgereiftes und sehr aktiv gepflegtes
Open-Source-Projekt, das 2005 ursprügnlich von Linus Torvalds, dem Initiator des
Linux-Betriebssystem-Kernels, entwickelt wurde. Git lässt sich gut mit vielen
Betriebssystemen und :abbr:`IDEs (Integrierte Entwciklungsumgebungen)`
kombinieren.

Mit seiner verteilten Architektur ist Git ein Beispiel für ein :abbr:`DVCS
(Distributed Version Control System)` – einem verteilten Versionskontrollsystem.
Somit muss sich nicht mehr die gesamte Versionshistorie an einem einzigen Ort
befinden, wie dies bei früher beliebten Versionskontrollsystemen wie CVS oder
Subversion (SVN) üblich war. In Git kann jedes lokale Repository spezifische
Änderungen enthalten.

Git kann jedoch nicht nur verteilt genutzt werden, sondern ist auch performant,
sicher und flexibel.

Performance
-----------

Git ist im Vergleich zu vielen anderen Versionsverwaltungssystemen sehr schnell
bei Commits von Änderungen, Beim Verzweigen und Zusammenführen und dem Vergleich
mit früheren Versionen. Dies ist auch erforderlich, wenn wir uns das
`Linux-Kernel-Repository <https://github.com/torvalds/linux>`_ mit über einer
Millionen Commits anschaut. Dabei orientiert sich Git nicht an Dateinamen,
sondern konzentriert sich auf inhaltliche Änderungen, sodass Dateien effizient umbenannt, aufgeteilt und neu angeordnet werden können. Dies erreicht Git durch
die Speicherung von Deltas für die inhaltlichen Unterschiede, Metadaten der
Dateien und Komprimierung.

Das verteilte Versionsverwaltungssystem sorgt darüberhinaus dafür, dass
:abbr:`z.B. (zum Beispiel)` für die Implementierung einer neuen Funktion
**kein** Netzwerkzugriff auf einen entfernten Server erforderlich ist und daraus
folgende Verzögerungen ausbleiben. Auch könnt ihr lokal an einer früheren
Version eine Fehlerkorrektur durchführen. Später können mit einem einzigen
Befehl beide Änderungen an einen zentralen Server übermittelt werden.

Sicherheit
----------

Die Integrität des verwalteten Quellcodes hatte hohe Priorität bei der
Konzipierung von Git. So werden die Beziehungen zwischen Dateien und Commits
durch einen Hashing-Algorithmus (SHA1) geschützt, sodass versehentliche oder
vorsätzliche Änderungen erschwert und der tatsächliche Verlauf sichergestellt
werden.

Flexibilität
------------

Git erlaubt nicht nur sehr flexible :doc:`Arbeitsabläufe <workflows/index>`
sondern ist auch für große wie kleine Projekte auf verschiedenen Plattformen
geeignet.

Kritikpunkte
------------

Eine häufige Kritik an Git ist, dass es schwer erlenrnbar sei: entweder sind
große Teile der Git-Terminologie neu oder in anderen Systemen haben
Bezeichnungen eine andere Bedeutung, wie :abbr:`z.B. (zum Beispiel)` ``revert``
in SVN oder CVS. Zudem bietet Git viel Funktionalität, die zum Erlernen jedoch
einige Zeit benötigt.

.. image:: git.png
   :alt: xkcd comic
   :target: https://xkcd.com/1597

Zum Weiterlesen
---------------

.. seealso::

    * :download:`Git Cheat Sheet (PDF) <git-cheatsheet-web.pdf>`
    * `Interactive Git Cheatsheet <http://ndpsoftware.com/git-cheatsheet.html>`_
    * `Software Carpentry Version Control with Git
      <https://swcarpentry.github.io/git-novice/>`_
    * `Flight rules for Git <https://github.com/k88hudson/git-flight-rules>`_
    * `First Aid git <https://firstaidgit.io/>`_
    * `git-tips <https://github.com/git-tips/tips>`_
    * `Pro Git book <https://git-scm.com/book>`_
    * `Git reference <https://git-scm.com/docs>`_

.. toctree::
    :hidden:

    install-config
    pre-commit
    jupyter-config
    tools
    working-areas
    work
    branching
    log
    tagging
    reverting
    best-practices
    workflows/index
    git-big-picture
    git-bisect
    glossary
