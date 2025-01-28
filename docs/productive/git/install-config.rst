.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git-Installation und -Konfiguration
===================================

Installation
------------

Für ix-Distributionen sollte Git im Standard-Repository vorhanden sein.

.. tab:: Debian/Ubuntu

   Das Paket `git-all <https://packages.debian.org/stable/git-all>`_ stellt euch
   eine vollständige Umgebung für Git bereit. Dieses installiert ihr wie folgt:

   .. code-block:: console

    $ sudo apt install git-all

   Geht es ausschliesslich um Git, genügt das Paket namens
   `git <https://packages.debian.org/stable/git>`_:

   .. code-block:: console

    $ sudo apt install git

   Mit der Bash-Autovervollständigung lässt sich Git auf der Kommandozeile
   einfacher bedienen. Das entsprechende Paket dazu heisst
   `bash-completion <https://packages.debian.org/stable/bash-completion>`_
   und ihr installiert es wie folgt:

   .. code-block:: console

    $ sudo apt install bash-completion

.. tab:: macOS

   Es gibt verschiedene Möglichkeiten, Git auf einem Mac zu installieren. Am
   einfachsten ist es vermutlich, die Xcode Command Line Tools zu installieren.
   Hierfür müsst ihr nur ``git`` das erste Mal vom Terminal aufrufen:

   .. code-block:: console

    $ git --version

   ``git-completion`` könnt ihr mit `Homebrew <https://brew.sh/>`_ installieren:

   Anschließend müsst ihr folgende Zeile in der Datei ``~/.bash_profile`` hinzufügen:

   .. code-block:: bash

    [[ -r "$(brew --prefix)/etc/profile.d/bash_completion.sh" ]] && . "$(brew --prefix)/etc/profile.d/bash_completion.sh"

.. tab:: Windows

   Ruft dazu https://git-scm.com/download/win auf und startet den passenden
   Download dazu.

   .. seealso::
      * `git for windows <https://gitforwindows.org/>`__

.. _git-config:

Konfiguration
-------------

Sichern der globalen Konfiguration in :file:`~/.config/git/`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git nutzt verschiedene Ebenen von Konfigurationsdateien, die in der folgenden
Reihenfolge ausgeführt werden:

``system``
    gilt für alle User auf eurem Computer, aber es ist unwahrscheinlich, dass
    ihr dies jemals benutzen werdet.
``global``
    gilt für alle Repositories eines einzelnen Users und wir werden uns das
    detaillierter anschauen.
``local``
    gilt für ein einzelnes Repository und ist nur für einige wenige
    Repository-spezifische Optionen.

Git such nach einer globalen Konfigurationsdatei an zwei verschiedenen Orten:
:file:`~/.config/git/config` und :file:`~/.gitconfig`. Der erste Ort ist der
Standard für Konfigurationsdateien, der zweite ist der frühere Standard.

.. note::
   Auf Linux-Maschinen kann :file:`~/.config` manchmal ein anderer Pfad sein,
   abhängig von der Umgebungsvariable ``XDG_CONFIG_HOME``. Dieses Verhalten ist
   Teil der `X Desktop Group (XDG) specification
   <https://wiki.archlinux.org/title/XDG_Base_Directory#Specification>`_. Ihr
   erhaltet den Pfad mit:

   .. code-block:: ini

      $ echo $XDG_CONFIG_HOME

   Wenn dies nichts zurückgibt, wird Ihr System :file:`~/.config` verwenden,
   andernfalls wird es den angezeigten Pfad verwenden. Der Einfachheit halber
   werden wir uns von nun an nur noch auf :file:`~/.config` beziehen.

.. seealso::
   * `git config files <https://git-scm.com/docs/git-config#FILES>`_

Da ihr Optionen an mehreren Ebenen festlegen könnt, möchtet ihr vielleicht
nachvollziehen, woher Git einen bestimmten Wert liest. Mit ``git config --list``
[#]_ könnt ihr alle überschriebenen Optionen und Werte auflisten. Dies könnt
ihr kombinieren mit ``--show-scope`` [#]_ um zu sehen, woher Git den Wert
bezieht:

.. code-block:: console

   $ git config --list --show-scope
   system  credential.helper=osxkeychain
   global  user.name=veit
   global  user.email=veit@cusy.io
   …

Ihr könnt auch ``--show-origin`` [#]_ verwenden, um die Namen der
Konfigurationsdateien aufzulisten:

.. code-block:: console

   $ git config --list --show-origin
   file:/opt/homebrew/etc/gitconfig        credential.helper=osxkeychain
   file:/Users/veit/.config/git/config     user.name=veit
   file:/Users/veit/.config/git/config     user.email=veit@cusy.io
   …

.. note::
    Ein umfangreiches Beispiel einer Konfigurationsdatei findet ihr in meinem
    `dotfiles <https://github.com/veit/dotfiles/>`_-Repository: `.gitconfig
    <https://github.com/veit/dotfiles/blob/main/.config/git/config>`_.

.. _migrate-git-config:

Migrieren von :file:`~/.gitconfig` zu :file:`~/.config/git/config`
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Wenn ihr aktuell noch die alte Datei :file:`~/.gitconfig` verwendet, könnt ihr
die Datei mit wenigen Schritten in das :file:`~/.config`-Verzeichnis
verschieben:

#. Stellt sicher, dass das :file:`~/.config`-Verzeichnis existiert.
#. Verschiebt eure bestehende Konfigurationsdate in dieses Verzeichnis:

   .. code-block:: console

      $ mv ~/.gitconfig ~/.config/git/config

#. Überprüft, ob Git weiterhin eure Konfigurationsdatei liest, indem ihr
   ``user.name`` abfragt:

   .. code-block:: console

      $ git config --global user.name
      Veit Schiele

#. Möglicherweise solltet ihr auch noch andere Dateien verschieben, :abbr:`z.B.
   (zum Beispiel)` :file:`~/.gitattributes` und :file:`~/.gitignore`. Ob diese Dateien vorhanden sind, könnt ihr überprüfen mit

   .. code-block:: console

      $ git config --global core.excludesFile
      ~/.gitignore
      $ git config --global core.attributesFile
      ~/.gitattributes

   Dann müsst ihr die Dateien ebenfalls verschieben und die zugehörigen Konfigurationseinträge löschen:

   .. code-block:: console

      $ mv ~/.gitignore_global ~/.config/git/ignore
      $ git config --global --unset core.excludesFile
      $ mv ~/.gitattributes ~/.config/git/attributes
      $ git config --global --unset core.attributesFile

Lesen und Schreiben der Konfigurationseinträge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wie wir bereits oben gesehen haben, können Konfigurationseinträge gelesen werden
mit `git config <https://git-scm.com/docs/git-config>`_, :abbr:`z.B. (zum
Beispiel)`:

.. code-block:: console

   $ git config --global user.name
   Veit Schiele

… und um den Eintrag zu ändern

.. code-block:: console

   $ git config --global user.name 'veit'

Ihr könnt die Konfigurationsdatei auch direkt ändern, indem ihr ``git config``
zusammen mit der ``-e|--edit``-Option aufruft:

.. code-block:: console

   $ git config --global -e

Dies öffnet die :file:`~/.config/git/config`-Datei in eurem Standardeditor.

Git speichert die Konfiguration in `INI
<https://de.wikipedia.org/wiki/Initialisierungsdatei>`_-Dateien.

Der Standardeditor für Git ist definiert in der ``GIT_EDITOR``-Umgebungsvariable
oder in Git’s ``core.editor``-Option oder in der ``VISUAL`` oder
``EDITOR``-Umgebungsvariable. Ihr könnt die Werte abfragen mit

.. code-block:: console

   $ echo $GIT_EDITOR
   $ git config core.editor
   $ echo $VISUAL
   $ echo $EDITOR

Üblicherweise wollt ihr immer denselben Editor verwenden und daher sollte die
``EDITOR``-Umgebungsvariable gesetzt werden. Um dies zu tun, könnt ihr folgendes
in :file:`~/.bash_profile` oder :file:`~/.zprofile` eintragen:

.. code-block:: sh

   export EDITOR='C:\Program Files (x86)\Microsoft VS Code\code.exe --wait'

.. note::
   Auf macOS müsst ihr zunächst Visual Studio Code starten, dann die
   Befehlspalette mit :kbd:`⌘+⇧-p` öffnen und schließlich den Befehl *Install
   'code' command in PATH* ausführen.

oder

.. code-block:: sh

   export EDITOR='vim'

.. _basic-git-config:

Basiskonfiguration
~~~~~~~~~~~~~~~~~~

Git Commits haben zwei Pflichtfelder, die sich auf die Person beziehen: den Namen der Person, die die Code-Änderungen vorgenommen hat und die Person, die den
Code ins Repository übertragen hat. In den meisten Workflows ist dies dieselbe
Person. Mit den Optionen ``user.name`` und ``user.email`` könnt ihr diese
Informationen für ``author`` und ``committer`` konfigurieren.

.. tip::
   Git-Hosts, wie `GitHub <https://github.com>`_ oder
   :doc:`advanced/gitlab/index`, verknüpfen Commits mit eurem Profil über die
   E-Mail-Adresse. Wenn die konfigurierte E-Mail-Adresse nicht mit eurem Profil
   übereinstimmt, werden eure Commits nicht richtig zugewiesen. Dadurch können
   Teammitglieder schwerer bestimmen, dass der Commit von euch kommt. Daher
   solltet ihr den konfigurierten Namen und die E-Mail-Adresse stets überprüfen.

.. _includeif:

Alternative Konfigurationsdatei
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ihr könnt für bestimmte Arbeitsverzeichnisse andere Konfigurationsdateien
verwenden, :abbr:`z.B. (zum Beispiel)` um zwischen privaten und beruflichen
Projekten zu unterscheiden. Dazu könnt ihr eine lokale Konfiguration in eurem
Repository verwenden oder aber `Conditional Includes
<https://git-scm.com/docs/git-config#_conditional_includes>`_ am Ende eurer
globalen Konfiguration:

.. code-block:: ini

   …
   [includeIf "gitdir:~/private"]
   path = ~/.config/git/config-private

Dieses Konstrukt sorgt dafür, dass Git zusätzliche Konfigurationen einbezieht
oder bestehende überschreibt, wenn ihr in :file:`~/private` arbeitet.

Erstellt dazu nun die Datei :file:`~/.config/git/config-private` und legt dort
eure alternative Konfiguration fest, :abbr:`z.B. (zum Beispiel)`:

.. code-block:: ini

   [user]
       email = kontakt@veit-schiele.de

   [core]
       sshCommand = ssh -i ~/.ssh/private_id_rsa

.. seealso::
   * `core.sshCommand
     <https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresshCommand>`_

.. _git-colouring:

Kolorieren
~~~~~~~~~~

Standardmäßig nutzt Git die Fähigkeit eures Terminals, verschiedene Arten von
Text einzufärben und zu formatieren. Eine solche Kolorierung ermöglicht euch,
die Ausgabe schneller zu analysieren. Die Standardfarben sind jedoch suboptimal:
``git status`` beispielsweise markiert geänderte Dateien in Rot, einer Farbe,
die im Allgemeinen mit Fehlern assoziiert wird; das Ändern von Dateien ist
jedoch kein Fehler, sondern völlig normal in jedem Git-Prozess. Ihr könnt die
Optionen ``color.*`` verwenden, um die Farben pro Befehl anzupassen. Ich
verwende die Farben des `cheat sheet colours
<https://web.archive.org/web/20180223152317/https://cheat.errtheblog.com/s/git>`_
schon seit langem:

.. code-block:: ini

   [color "branch"]
       current = yellow reverse
       local = yellow
       remote = green

   [color "status"]
       added = yellow
       changed = green
       untracked = cyan

.. note::
   Später werden wir uns :ref:`git-delta` ansehen, ein Werkzeug zur besseren
   Visualisierung von Unterschieden. Seine Kolorierung würde die Informationen
   aus ``[colour "diff"]`` überschreiben, weshalb wir diesen Abschnitt nicht
   hinzugefügt haben.

.. _git-autocorrect:

Befehle korrigieren
~~~~~~~~~~~~~~~~~~~

Wenn ihr bei der Eingabe eines Git-Befehls einen Fehler macht, werden
standardmäßig ähnliche Befehle aufgelistet und das Programm beendet:

.. code-block:: console

   $ git comit -m ':wrench: Update git config'
   git: 'comit' ist kein Git-Befehl. Siehe 'git --help'.

   Der ähnlichste Befehl ist
       commit

Ihr könnt Git aber auch mit ``git config --global help.autoCorrect immediate``
[#]_ so konfigurieren, dass der erste Treffer automatisch ausgeführt wird:

.. code-block:: console

   $ git comit -m ':wrench: Update git config'
   WARNUNG: Sie haben Git-Befehl 'comit' ausgeführt, welcher nicht existiert.
   Setze fort unter der Annahme, dass Sie 'commit' meinten.
   [main 48cafbf5f] :wrench: Update git config

Git korrigiert jedoch nur dann automatisch, wenn ein Befehl eine ausreichend
große Übereinstimmung aufweist. Wenn es mehrere potenzielle Übereinstimmungen
gibt, werden diese aufgelistet und die Korrektur wird abgebrochen:

.. code-block:: console

   $ git co -m ':wrench: Update git config'
   git: 'co' is not a git command. See 'git --help'.

   The most similar commands are
       commit
       clone
       log

Wenn euch die automatische Korrektur eines Befehls zu viel ist, könnt ihr
stattdessen den *Prompt*-Modus verwenden:

.. code-block:: console

   $ git config --global help.autoCorrect prompt
   $ git comit -m ':wrench: Update git config'
   WARNUNG: Sie haben Git-Befehl 'comit' ausgeführt, welcher nicht existiert.
   Stattdessen 'commit' ausführen (y/N)? y
   [main 48cafbf5f] :wrench: Update git config

.. _git-pagination:

Paginierung
~~~~~~~~~~~

Ihr könnt die Paginierung standardmäßig für einen Befehl aktivieren, indem ihr
die entsprechende Option setzt: :samp:`pager.{CMD} = true`, [#]_ zum Beispiel,
um den Git-Status auf Paginierung umzustellen:

.. code-block:: console

   $ git config --global pager.status true

.. _credential-helper:

Anmeldedaten verwalten
~~~~~~~~~~~~~~~~~~~~~~

Seit der Git-Version 1.7.9 lassen sich die Zugangsdaten zu git-Repositories mit
`gitcredentials <https://git-scm.com/docs/gitcredentials>`_ verwalten. Um diese
zu nutzen, könnt ihr :abbr:`z.B. (zum Beispiel)` folgendes angeben:

.. code-block:: console

    $ git config --global credential.helper Cache

Hiermit wird euer Passwort für 15 Minuten im Cache-Speicher gehalten. Der Timeout
kann :abbr:`ggf. (gegebenenfalls)` erhöht werden, :abbr:`z.B. (zum Beispiel)` mit:

.. code-block:: console

   $ git config --global credential.helper 'cache --timeout=3600'

.. tab:: Debian/Ubuntu

   Unter Linux müsst ihr einen :abbr:`sog: (sogenannten)` `Credential Store
   <https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/credstores.md>`_
   auswählen. In den meisten Fällen werdet ihr euch für die *Secret Service API*
   entscheiden, wie :abbr:`z.B. (zum Beispiel)` ``libsecret`` von Git, den ihr
   auswählen könnt mit:

   .. code-block:: console

      $ git config --global credential.credentialStore secretservice

.. tab:: macOS

   Unter macOS lässt sich mit ``osxkeychain`` die Schlüsselbundverwaltung
   (*Keychain*) nutzen um die Zugangsdaten zu speichern. ``osxkeychain`` setzt
   Git in der Version 1.7.10 oder neuer voraus und kann im selben Verzeichnis
   wie Git installiert werden mit:

   .. code-block:: console

      $ git credential-osxkeychain
      git: 'credential-osxkeychain' is not a git command. See 'git --help'.
      $ curl -s -O http://github-media-downloads.s3.amazonaws.com/osx/git-credential-osxkeychain
      $ chmod u+x git-credential-osxkeychain
      $ sudo mv git-credential-osxkeychain /usr/bin/
      Password:
      git config --global credential.helper osxkeychain

   Dies trägt folgendes in die :file:`~/.gitconfig`-Datei ein:

   .. code-block:: ini

      [credential]
          helper = osxkeychain

   Alternativ könnt ihr auch den `Git Credential Manager
   <https://github.com/git-ecosystem/git-credential-manager>`_ installieren mit

   .. code-block:: console

       brew install --cask git-credential-manager

.. tab:: Windows

   Für Windows steht der `Git Credential Manager (GCM)
   <https://github.com/git-ecosystem/git-credential-manager>`_ zur Verfügung. Er
   ist integriert in `Git for Windows <https://git-scm.com/download/win>`_ und
   wird standardmäßig mitinstalliert. Zusätzlich besteht jedoch auch ein
   eigenständiges Installationsprogramm in
   `Releases <https://github.com/git-ecosystem/git-credential-manager/releases>`_.

   GCM wird mit dem nachfolgenden Aufruf konfiguriert:

   .. code-block:: console

      $ git credential-manager configure
      Configuring component 'Git Credential Manager'...
      Configuring component 'Azure Repos provider'...

   Dies trägt den ``[credential]``-Abschnitt in eure :file:`~/.gitconfig`-Datei
   ein:

   .. code-block:: ini

      [credential]
          helper =
          helper = C:/Program\\ Files/Git/mingw64/bin/git-credential-manager.exe

   Nun öffnet sich beim Clonen eines Repository ein Fenster des GCM und fordert
   euch zur Eingabe eurer Zugangsdaten auf.

   Zudem wird die :file:`~/.gitconfig`-Datei ergänzt, :abbr:`z.B. (zum
   Beispiel)` um die folgenden beiden Zeilen:

   .. code-block:: ini

      [credential "https://ce.cusy.io"]
          provider = generic

.. seealso::
   * `Git Credential Manager: authentication for everyone
     <https://github.blog/security/application-security/git-credential-manager-authentication-for-everyone/>`_

.. _gitignore:

Die :file:`.gitignore`-Datei
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In der :file:`.gitignore`-Datei eines Repository könnt ihr Dateien von der
Versionsverwaltung ausschließen. Eine typische :file:`.gitignore`-Datei kann
:abbr:`z.B. (zum Beispiel)` so aussehen:

.. code-block:: ini

   /logs/*
   !logs/.gitkeep
   /tmp
   *.swp

Dabei verwendet Git `Globbing <https://linux.die.net/man/7/glob>`_-Muster,
:abbr:`u.a. (unter anderem)`:

+-------------------------------+-----------------------------------+-------------------------------+
| Muster                        | Beispiel                          | Erläuterung                   |
+===============================+===================================+===============================+
| .. code-block:: console       | :file:`logs/instance.log`,        | Ihr könnt zwei Sternchen      |
|                               | :file:`logs/instance/error.log`,  | voranstellen um Verzeichnisse |
|     **/logs                   | :file:`prod/logs/instance.log`    | an einer beliebigen Stelle im |
|                               |                                   | Verzeichnisbaum zu finden.    |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs/instance.log`,        | Ihr könnt zwei Sternchen      |
|                               | :file:`prod/logs/instance.log`    | voranstellen um Dateien anhand|
|     **/logs/instance.log      | aber nicht                        | ihres Namens in einem         |
|                               | :file:`logs/prod/instance.log`    | übergeordneten Verzeichnis zu |
|                               |                                   | finden.                       |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance.log`,             | Ein Sternchen ist ein         |
|                               | :file:`error.log`,                | Platzhalter für null oder     |
|     *.log                     | :file:`logs/instance.log`         | mehr Zeichen.                 |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`/logs/instance.log`,       | Ein vor ein Muster gestelltes |
|                               | :file:`/logs/error.log`,          | Anführungszeichen ignoriert   |
|     /logs                     | nicht jedoch                      | dieses. Wenn eine Datei mit   |
|     !/logs/.gitkeep           | :file:`/logs/.gitkeep` oder       | einem Muster übereinstimmt,   |
|                               | :file:`/instance.log`             | aber auch mit einem           |
|                               |                                   | negierenden, das später       |
|                               |                                   | definiert ist, wird sie nicht |
|                               |                                   | ignoriert.                    |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`/instance.log`,            | Mit dem vorangestellten       |
|                               | nicht jedoch                      | Schrägstrich passt das Muster |
|     /instance.log             | :file:`logs/instance.log`         | nur zu Dateien im             |
|                               |                                   | Stammverzeichnis des          |
|                               |                                   | Repository.                   |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance.log`,             | Üblicherweise passen die      |
|                               | :file:`logs/instance.log`         | Muster zu Dateien in jedem    |
|     instance.log              |                                   | Verzeichnis.                  |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance0.log`,            | Ein Fragezeichen passt genau  |
|                               | :file:`instance1.log`,            | zu einem Zeichen.             |
|     instance?.log             | aber nicht                        |                               |
|                               | :file:`instance.log` oder         |                               |
|                               | :file:`instance10.log`            |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance0.log`,            | Eckige Klammern können        |
|                               | :file:`instance1.log`,            | verwendet werden um ein       |
|     instance[0-9].log         | aber nicht                        | einzelnes Zeichen aus einem   |
|                               | :file:`instance.log` oder         | bestimmten Bereich zu finden. |
|                               | :file:`instance10.log`            |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance0.log`,            | Eckige Klammern passen        |
|                               | :file:`instance1.log`,            | auf ein einzelnes Zeichen     |
|     instance[01].log          | aber nicht                        | aus einer bestimmten Menge.   |
|                               | :file:`instance2.log` oder        |                               |
|                               | :file:`instance01.log`            |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance2.log`,            | Ein Ausrufezeichen kann       |
|                               | aber nicht                        | verwendet werden um ein       |
|     instance[!01].log         | :file:`instance0.log`,            | beliebiges Zeichen aus einer  |
|                               | :file:`instance1.log` oder        | angegebenen Menge zu finden.  |
|                               | :file:`instance01.log`            |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs`                      | Wenn kein Schrägstrich        |
|                               | :file:`logs/instance.log`         | anhängt, passt das Muster     |
|     logs                      | :file:`prod/logs/instance.log`    | sowohl auf Dateien als auch   |
|                               |                                   | auf den Inhalt von            |
|                               |                                   | Verzeichnissen mit diesem     |
|                               |                                   | Namen.                        |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs/instance.log`,        | Das Anhängen eines            |
|                               | :file:`logs/prod/instance.log`,   | Schrägstrichs zeigt an, dass  |
|     logs/                     | :file:`prod/logs/instance.log`    | das Muster ein Verzeichnis    |
|                               |                                   | ist. Der gesamte Inhalt jedes |
|                               |                                   | Verzeichnisses im Repository, |
|                               |                                   | das diesem Namen entspricht – |
|                               |                                   | einschließlich all seiner     |
|                               |                                   | Dateien und Unterverzeichnisse|
|                               |                                   | – wird ignoriert.             |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       |:file:`var/instance.log`,          | Zwei Sternchen passen zu null |
|                               |:file:`var/logs/instance.log`,     | oder mehr Verzeichnissen.     |
|                               |nicht jedoch                       |                               |
|     var/**/instance.log       |:file:`var/logs/instance/error.log`|                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs/instance/error.log`,  | Wildcards können auch in      |
|                               | :file:`logs/instance1/error.log`  | Verzeichnisnamen verwendet    |
|     logs/instance*/error.log  |                                   | werden.                       |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs/instance.log`,        | Muster, die eine Datei in     |
|                               | nicht jedoch                      | einem bestimmten Verzeichnis  |
|     logs/instance.log         | :file:`var/logs/instance.log`     | angeben, sind relativ zum     |
|                               | oder                              | Stammverzeichnis des          |
|                               | :file:`instance.log`              | Repository.                   |
+-------------------------------+-----------------------------------+-------------------------------+

Git-commit eines leeren Verzeichnisses
::::::::::::::::::::::::::::::::::::::

In obigem Beispiel seht ihr, dass mit :file:`/logs/*` keine Inhalte des
``logs``-Verzeichnisses mit Git versioniert werden sollen, in der Folgezeile
jedoch eine Ausnahme definiert wird:

:file:`!logs/.gitkeep`

Diese Angabe erlaubt, dass die Datei :file:`.gitkeep` mit Git verwaltet werden
darf. Damit wird dann auch das :file:`logs`-Verzeichnis in das Git-Repository
übernommen. Eine solche Hilfskonstruktion ist erforderlich, da leere
Verzeichnisse nicht mit Git verwaltet werden können.

.. warning::
   Diese Technik hat jedoch mehrere Nachteile:

   * Sowohl :file:`.gitignore` wie auch :file:`log/.gitkeep` müssen bearbeitet
     werden.
   * Beim Umbenennen des Verzeichnis kann leicht vergessen werden, auch die
     :file:`.gitignore`-Datei zu ändern.
   * :file:`.gitkeep` ist für Git eine ganz normale Datei; der Name legt jedoch
     nahe, dass die Datei von Git besonders behandelt würde.

Eine bessere Möglichkeit ist, in einem leeren Verzeichnis eine
:file:`.gitignore`-Datei mit folgendem Inhalt zu erstellen:

.. code-block:: ini

   # ignore everything except .gitignore
   *
   !.gitignore

Dies vermeidet die vorher genannten Probleme.

.. seealso:
   * `Can I add empty directories?
     <https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F>`_

Dateien zentral mit ``excludesfile`` ausschließen
:::::::::::::::::::::::::::::::::::::::::::::::::

Ihr könnt jedoch auch zentral für alle Git-Repositories Dateien ausschließen.
Hierfür wird üblicherweise in der :file:`~/.gitconfig`-Datei folgendes
angegeben:

.. code-block:: ini

   [core]

       # Use custom `.gitignore`
       excludesfile = ~/.gitignore
       …

.. note::
   Hilfreiche Vorlagen findet ihr in meinem `dotfiles
   <https://github.com/veit/dotfiles/tree/main/gitignores>`__-Repository oder
   auf der Website `gitignore.io
   <https://www.toptal.com/developers/gitignore/>`_.

Ignorieren einer Datei aus dem Repository
:::::::::::::::::::::::::::::::::::::::::

Wenn ihr eine Datei ignorieren wollt, die in der Vergangenheit bereits dem Repository hinzugefügt
wurde, müsst ihr die Datei aus eurem Repository löschen und dann eine
``.gitignore``-Regel für sie hinzufügen. Die Verwendung der Option ``--cached``
bei ``git rm`` bedeutet, dass die Datei aus dem Repository gelöscht wird, aber
als ignorierte Datei in eurem Arbeitsverzeichnis verbleibt.

.. code-block:: console

   $ echo *.log >> .gitignore
   $ git rm --cached *.log
   rm 'instance.log'
   $ git commit -m "Remove log files"

.. note::
   Ihr könnt die Option ``--cached`` weglassen, wenn ihr die Datei sowohl aus
   dem Repository als  auch aus eurem lokalen Dateisystem löschen wollt.

Commit einer ignorierten Datei
::::::::::::::::::::::::::::::

Es ist möglich, den Commit einer ignorierten Datei an das Repository mit der
Option ``-f`` (oder ``--force``) bei ``git add`` zu erzwingen:

.. code-block:: console

   $ cat data/.gitignore
   *
   $ git add -f data/iris.csv
   $ git commit -m "Force add iris.csv"

Ihr könnt dies in Erwägung ziehen, wenn ihr ein allgemeines Muster (wie ``*``)
definiert habt, aber eine bestimmte Datei übertragen wollt. Eine bessere Lösung
ist meist jedoch, eine Ausnahme von der allgemeinen Regel zu definieren:

.. code-block:: console

   $ echo '!iris.csv' >> data/.gitignore
   $ cat data/.gitignore
   *
   !iris.csv
   $ git add data/iris.csv
   $ git commit -m "Add iris.csv"

Dieser Ansatz dürfte für euer Team offensichtlicher und weniger verwirrend sein.

Fehlersuche in :file:`.gitignore`-Dateien
:::::::::::::::::::::::::::::::::::::::::

Bei komplizierten :file:`.gitignore`-Mustern oder bei Mustern, die über mehrere
:file:`.gitignore`-Dateien verteilt sind, kann es schwierig sein,
herauszufinden, ob oder warum eine bestimmte Datei ignoriert wird.

Mit dem Aufruf ``git status --ignored=matching`` [#]_ wird der Ausgabe ein
Abschnitt *Ignorierte Dateien* hinzugefügt, der zusätzlich alle von Git
ignorierten Dateien und Verzeichnisse beinhaltet:

.. code-block:: console

   $ git status --ignored=matching
   Auf Branch main
   Ignorierte Dateien:
     (benutzen Sie "git add -f <Datei>...", um die Änderungen zum Commit vorzumerken)
       .DS_Store
       docs/.DS_Store
       docs/_build/doctrees/
       docs/_build/html/
       docs/clean-prep/.ipynb_checkpoints/
       …
       nichts zu committen, Arbeitsverzeichnis unverändert

Ihr könnt den Befehl ``git check-ignore`` [#]_ mit der Option ``-v`` (Langform:
``--verbose``) verwenden, um festzustellen, welches Muster die Ursache für das
Ignorieren einer bestimmten Datei ist:

.. code-block:: console

   $ git check-ignore -v data/iris.csv
   data/.gitignore:2:!iris.csv data/iris.csv

Obige Ausgabe besteht aus vier Feldern (Trennzeichen sind drei Doppelpunkte
und ein Leerzeichen) und beinhaltet:

:samp:`{FILE_CONTAINING_THE_PATTERN}`
    den Namen der Datei, die das Muster enthält.

:samp:`{LINE_NUMBER_OF_THE_PATTERN}`
    die Zeilennummer, in der in der Datei :samp:`{FILE_CONTAINING_THE_PATTERN}`
    das Muster gefunden wurde.

:samp:`{PATTERN}`
    das gefundene Muster.

:samp:`{FILE_NAME}`
    den Namen der Datei inklusive Pfad, die Git ignoriert.

Ihr könnt mehrere Dateinamen an ``git check-ignore`` übergeben, wenn ihr
möchtet, und die Namen selbst müssen nicht einmal den Dateien entsprechen, die
in eurem Repository existieren.

Eine vollständige Liste aller ignorierten Dateien erhaltet ihr mit ``git
ls-files --ignored --exclude-standard --others`` [#]_. Mit
``--exclude-standard`` werden die Standard-:file:`ignore`-Dateien gelesen und
mit ``--others`` werden die nicht-versionierten Dateien statt der versionierten
angezeigt:

.. code-block:: console

   $ git ls-files --ignored --exclude-standard --others
   .DS_Store
   _build/doctrees/clean-prep/bulwark.doctree
   _build/doctrees/clean-prep/dask-pipeline.doctree
   _build/doctrees/clean-prep/deduplicate.doctree
   …

Gelegentlich möchtet ihr vielleicht die globale :file:`~/.gitignore`-Datei
umgehen um zu sehen, welche Dateien Git unabhängig von eurer Konfiguration immer
ignoriert. Ihr könnt dies tun, indem ihr zu einer anderen ``exclude``-Option
wechselt, ``--exclude-per-directory``, die nur die :file:`.gitignore`-Dateien
des Repositorys verwendet:

.. code-block:: console

   $ git ls-files --ignored --exclude-per-directory=.gitignore --others
   docs/_build/doctrees/clean-prep/bulwark.doctree
   docs/_build/doctrees/clean-prep/dask-pipeline.doctree
   docs/_build/doctrees/clean-prep/deduplicate.doctree
   …

Beachtet, dass die Datei :file:`.DS_Store` nicht mehr als ignoriert aufgeführt
wird.

Wenn ihr ``--others`` durch ``--cached`` ersetzt, listet ``git ls-files``
Dateien auf, die ignoriert werden würden, es sei denn, sie wurden bereits
übertragen:

.. code-block:: console

   $ git ls-files --ignored --exclude-per-directory=.gitignore --cached
   data/iris.csv

Möglicherweise habt ihr solche Dateien, weil jemand sie vor den relevanten
Mustern in einer :file:`.gitignore`-Datei hinzugefügt hat, oder weil jemand sie
mit ``git add --force`` hinzugefügt hat. So oder so, wenn ihr die Datei nicht
mehr mit Git verwalten wollt, könnt ihr sie mit dem folgenden Einzeiler aus der
Git-Verwaltung nehmen, sie aber nicht löschen:

.. code-block:: console

   $ git ls-files --ignored --exclude-per-directory=.gitignore --cached | xargs -r git rm --cached
   rm 'data/iris.csv'

----

.. [#] `git config --list
   <https://git-scm.com/docs/git-config#Documentation/git-config.txt---list>`_
.. [#] `git config --show-scope
   <https://git-scm.com/docs/git-config#Documentation/git-config.txt---show-scope>`_
.. [#] `git config --show-origin
   <https://git-scm.com/docs/git-config#Documentation/git-config.txt---show-origin>`_
.. [#] `help.autoCorrect
       <https://git-scm.com/docs/git-config#Documentation/git-config.txt-helpautoCorrect>`_
.. [#] `pager.cmd <https://git-scm.com/docs/git-config#Documentation/git-config.txt-pagerltcmdgt>`_
.. [#] `git status --ignored
   <https://git-scm.com/docs/git-status#Documentation/git-status.txt---ignoredltmodegt>`_
.. [#] `git check-ignore
   <https://git-scm.com/docs/git-check-ignore>`_
.. [#] `git ls-files --ignored
   <https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---ignored>`_
