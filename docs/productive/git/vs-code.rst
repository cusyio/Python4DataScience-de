Visual Studio Code
==================

`Visual Studio Code <https://code.visualstudio.com/>`_ kann eine bereits
vorhandene :doc:`Git-Installation <install-config>` nutzen um die entsprechenden
Funktionalitäten zur Verfügung stellen zu können. 

Klonen
------

.. figure:: vs-code_source-control-icon.png
   :alt: Source-Control-Icon
   :align: left

   Source-Control-Icon

   Wenn ihr noch kein Repository geöffnet habt, habt ihr in der
   :menuselection:`Source Code`-Ansicht die Möglichkeit, :menuselection:`Open
   Folder` oder :menuselection:`Clone Repository` auszuwählen. Bei
   :menuselection:`Clone Repository` werdet ihr nach der URL des Repository
   gefragt.

Zeilenindikator
---------------

Wenn ihr ein Git-Repository öffnet und beginnt, Änderungen vorzunehmen, fügt
VS-Code nützliche Anmerkungen hinzu:

* ein rotes Dreieck zeigt an, wo Zeilen gelöscht worden sind
* ein grüner Balken zeigt neu hinzugefügte Zeilen an
* ein blauer Balken zeigt geänderte Zeilen an

Commit
------

``git add`` und ``git reset`` können entweder im Kontextmenü einer Datei
ausgewählt werden oder per drag & drop. Nach einem ``git commit`` könnt ihr eine
Commit-Nachricht eingeben und mit :kbd:`Ctrl ⏎` oder :kbd:`⌘ ⏎` bestätigen. Wenn
es bereits Änderungen im Bühnenbereich gibt, werden nur diese übernommen;
andernfalls werdet ihr aufgefordert, Änderungen auszuwählen. :abbr:`Ggf.
(gegebenenfalls)` erhaltet ihr spezifischere Commit-Aktionen in
:menuselection:`Views and More Actions…`.

.. note::
    Wenn ihr euren Commit versehentlich im falschen Branch erstellt habt, könnt
    ihr diesen Commit zurücknehmen mit :menuselection:`Git: Undo Last Commit` in
    der :menuselection:`Command Palette` (:kbd:`⇧ ⌘ P`).

Das Source-Control-Icon in der Aktivitätsleiste auf der linken Seite zeigt euch
an, wieviele Änderungen ihr in eurem Repository gemacht habt. Wenn ihr das Icon
auswählt, erhaltet ihr einen detaillierteren Überblick über eure Änderungen. Bei
der Auswahl einer einzelnen Datei werden euch dann die zeilenweisen
Textänderungen angezeigt. Ihr könnt auch den Editor auf der rechten Seite nutzen
um weitere Änderungen vorzunehmen. 

Zweige und Tags
---------------

Ihr könnt Zweige erstellen und in diese wechseln mit :menuselection:`Git: Create
Branch` und :menuselection:`Git: Checkout to` aus der :menuselection:`Command
Palette` (:kbd:`⇧ ⌘ P`). Wenn ihr :menuselection:`Git: Checkout to` aufruft,
erscheint anschließend eine Dropdown-Liste mit allen Zweigen und Tags des
Repository. Ihr könnt hier auch einen neuen Zweig erstellen.

Git-Statuszeile
---------------

.. figure:: vs-code_status-bar.png
   :alt: Statuszeile
   :align: left

   Statuszeile

   In der unteren linken Ecke seht ihr die Statusanzeige mit weiteren
   Indikatoren über den Zustand eures Repository:

   * den aktuellen Zweig mit der Möglichkeit, in einen anderen Zweig zu wechseln
   * ein- und ausgehenden Commits
   * die :menuselection:`Synchronize Changes`-Aktion, die zunächst ``git pull``
     und dann ``git push`` ausführt.

Erweiterungen
-------------

* `Git Blame
  <https://marketplace.visualstudio.com/items?itemName=waderyan.gitblame>`_
* `Git History
  <https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory>`_
* `Git Lens
  <https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens>`_
