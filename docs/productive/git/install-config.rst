.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git-Installation und -Konfiguration
===================================

Installation
------------

Für iX-Distributionen sollte Git im Standard-Repository vorhanden sein.

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

Für jede Änderung muss ersichtlich sein, wer diese verursacht hat. Dazu hinterlegt
ihr euren Namen und eure E-Mail-Adresse wie folgt:

:samp:`$ git config --global user.name "{NAME}"`
    legt den Namen :samp:`{NAME}` fest, der mit euren Commit-Transaktionen verknüpft wird.
:samp:`$ git config --global user.email "{EMAIL-ADDRESS}"`
    legt die E-Mail-Adresse :samp:`{EMAIL-ADDRESS}` fest, die mit euren Commit-Transaktionen
    verknüpft wird.

Für eine bessere Lesbarkeit der Ausgabe sorgt die Kolorierung der Befehlszeilenausgabe.
Diese schaltet ihr mit Hilfe dieses Aufrufs ein:

:samp:`$ git config --global color.ui auto`
    aktiviert die Kolorierung der Befehlszeilenausgabe.

Die :file:`~/.gitconfig`-Datei
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit den oben angegebenen Befehlen wird dir folgende :file:`~/.gitconfig`-Datei
erstellt:

.. code-block:: ini

    [user]
        name = veit
        email = veit@cusy.io

    [color]
        ui = auto

In der :file:`~/.gitconfig`-Datei können jedoch auch Aliase festgelegt werden:

.. code-block:: ini

    [alias]
        st = status
        ci = commit
        br = branch
        co = checkout
        df = diff
        dfs = diff --staged

.. seealso::
   Shell-Konfiguration:

   * `oh-my-zsh <https://ohmyz.sh>`_

     * `Git plugin aliases
       <https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git#aliases>`_
     * `zsh-you-should-use
       <https://github.com/MichaelAquilina/zsh-you-should-use>`_

   * `Starship <https://starship.rs>`_

     * `git_branch-Modul <https://starship.rs/config/#git-branch>`_
     * `git_commit-Modul <https://starship.rs/config/#git-commit>`_
     * `git_state <https://starship.rs/config/#git-state>`_
     * `git_status-Modul <https://starship.rs/config/#git-status>`_

Sowohl der Editor lässt sich angeben, als auch die Hervorhebung von Leerzeichenfehlern
in ``git diff``:

.. code-block:: ini

    [core]
        editor = vim

        # Highlight whitespace errors in git diff:
        whitespace = tabwidth=4,tab-in-indent,cr-at-eol,trailing-space

.. note::
   Neben :file:`~/.gitconfig` sucht Git seit Version 1.17.12 auch in
   :file:`~/.config/git/config` nach einer globalen Konfigurationsdatei.

   Unter Linux kann :file:`~/.config` manchmal ein anderer Pfad sein, der durch
   die Umgebungsvariable ``XDG_CONFIG_HOME`` festgelegt wird. Dieses
   Verhalten ist Teil der `Spezifikation der X Desktop Group (XDG)
   <https://wiki.archlinux.org/title/XDG_Base_Directory#Specification>`_. Den
   anderen Pfad erhaltet ihr mit:

   .. code-block:: ini

      $ echo $XDG_CONFIG_HOME

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

``git diff``
~~~~~~~~~~~~

``git diff`` lässt sich konfigurieren, sodass es auch bei Binärdateien sinnvolle
Diffs anzeigen kann.

… für Excel-Dateien
:::::::::::::::::::

Hierfür benötigen wir `openpyxl <https://openpyxl.readthedocs.io/en/stable/>`_
und `pandas <https://pandas.pydata.org>`_:

.. code-block:: console

    $ pipenv install openpyxl pandas

Anschließend können wir in :file:`exceltocsv.py`
:doc:`pandas:reference/api/pandas.DataFrame.to_csv` zum Konvertieren der
Excel-Dateien verwenden:

.. literalinclude:: exceltocsv.py
   :caption: exceltocsv.py
   :name: exceltocsv.py
   :language: python
   :lines: 5-

Nun fügt ihr noch in der globalen Git-Konfiguration in der Datei :file:`~/.gitconfig`
den folgenden Abschnitt hinzu:

.. code-block:: ini

    [diff "excel"]
        textconv=python3 /PATH/TO/exceltocsv.py
        binary=true

Schließlich wird in der globalen :file:`~/.gitattributes`-Datei unser
``excel``-Konverter mit :file:`*.xlsx`-Dateien verknüpft:

.. code-block:: ini

    *.xlsx diff=excel

… für PDF-Dateien
:::::::::::::::::

Hierfür wird zusätzlich das Werkzeug ``pdftohtml`` benötigt. Ihr installiert es
mit

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install poppler-utils

.. tab:: macOS

   .. code-block:: console

      $ brew install pdftohtml

Anschließend fügt ihr den folgenden Abschnitt der globalen Git-Konfiguration in der
Datei :file:`~/.gitconfig` hinzu:

.. code-block:: ini

    [diff "pdf"]
        textconv=pdftohtml -stdout

Schließlich wird in der globalen :file:`~/.gitattributes`-Datei unser
``pdf``-Konverter mit :file:`*.pdf`-Dateien verknüpft:

.. code-block:: ini

    *.pdf diff=pdf

Nun wird beim Aufruf von ``git diff`` die PDF-Datei zunächst konvertiert und
dann ein Diff über den Ausgaben des Konverters durchgeführt.

… für Word-Dokumente
::::::::::::::::::::

Auch Unterschiede in Word-Dokumenten lassen sich anzeigen. Hier kommt `Pandoc
<https://pandoc.org/>`__ ins Spiel.

.. tab:: Debian/Ubuntu

   Das Paket heisst `pandoc <https://packages.debian.org/stable/pandoc>`_.
   Dieses installiert ihr wie folgt:

   .. code-block:: console

      $ sudo apt install pandoc

.. tab:: macOS

   Das Paket heisst ``pandoc``. Dieses installiert ihr mittels ``brew`` wie
   folgt:

   .. code-block:: console

      $ brew install pandoc

.. tab:: Windows

   Dazu ladet ihr zunächst die aktuelle :file:`.msi`-Datei von `GitHub
   <https://github.com/jgm/pandoc/releases/>`_ herunter und installiert diese.

Anschließend wird der globalen Git-Konfiguration :file:`~/.gitconfig` folgender
Abschnitt hinzugefügt:

.. code-block:: ini

   [diff "word"]
           textconv=pandoc --to=markdown
           binary=true
           prompt=false

Schließlich wird in der globalen :file:`~/.gitattributes`-Datei unser
``word``-Konverter mit :file:`*.docx`-Dateien verknüpft:

.. code-block:: ini

   *.docx diff=word

Die gleiche Vorgehensweise kann auch angewandt werden, um nützliche Diffs von
anderen Binärdateien zu erhalten, :abbr:`z.B. (zum Beispiel)` ``*.zip``,
``*.jar`` und andere Archive mit ``unzip`` oder für Änderungen in den
Metainformationen von Bildern mit ``exiv2``. Zudem gibt es
Konvertierungswerkzeuge für die Umwandlung von :file:`*.odt`, :file:`.*doc` und
anderen Dokumentenformaten in einfachen Text. Für Binärdateien, für die es
keinen Konverter gibt, reichen oft auch Strings aus.

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

.. tab:: Windows

    Für Windows steht der `Git Credential Manager (GCM)
    <https://github.com/GitCredentialManager/git-credential-manager>`_ zur
    Verfügung. Er ist integriert in `Git for Windows
    <https://git-scm.com/download/win>`_ und wird standardmäßig mitinstalliert.
    Zusätzlich besteht jedoch auch ein eigenständiges Installationsprogramm in
    `Releases <https://github.com/GitCredentialManager/git-credential-manager/releases/>`_.

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

.. note::
    Ein umfangreiches Beispiel einer Konfigurationsdatei findet ihr in meinem
    `dotfiles <https://github.com/veit/dotfiles/>`_-Repository: `.gitconfig
    <https://github.com/veit/dotfiles/blob/main/.config/git/config>`_.

.. seealso::
    * `Git Credential Manager: authentication for everyone
      <https://github.blog/2022-04-07-git-credential-manager-authentication-for-everyone/>`_

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
übernommen. Diese Hilfskonstruktion ist erforderlich, da leere Verzeichnisse
nicht mit Git verwaltet werden können.

Eine andere Möglichkeit besteht darin, in einem leeren Verzeichnis eine
:file:`.gitignore`-Datei mit folgendem Inhalt zu erstellen:

.. code-block:: ini

    # ignore everything except .gitignore
    *
    !.gitignore


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
    auf der Website `gitignore.io <https://gitignore.io/>`_.

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
    data/.gitignore:2:!iris.csv	data/iris.csv

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
.. [#] `git status --ignored
   <https://git-scm.com/docs/git-status#Documentation/git-status.txt---ignoredltmodegt>`_
.. [#] `git check-ignore
   <https://git-scm.com/docs/git-check-ignore>`_
.. [#] `git ls-files --ignored
   <https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---ignored>`_
