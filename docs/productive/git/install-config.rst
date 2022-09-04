Git-Installation und -Konfiguration
===================================

Installation
------------

Für iX-Distributionen sollte Git im Standard-Repository vorhanden sein.

.. tab:: Debian/Ubuntu

   .. code-block:: console

    $ sudo apt install git-all

   Mit der Bash-Autovervollständigung lässt sich Git auf der Kommandozeile
   einfacher bedienen:

   .. code-block:: console

    $ sudo apt install bash-completion

.. tab:: macOS

   Es gibt verschiedene Möglichkeiten, Git auf einem Mac zu installieren. Am
   einfachsten ist es vermutlich, die Xcode Command Line Tools zu installieren.
   Hierfür müsst ihr nur ``git`` das erste Mal vom Terminal aufrufen:

   .. code-block:: console

    $ git --version

   ``git-completion`` könnt ihr mit `Homebrew <https://brew.sh/>`_ installieren:

   Anschließend müsst ihr folgende Zeile in ``~/.bash_profile`` hinzufügen:

   .. code-block:: bash

    [[ -r "$(brew --prefix)/etc/profile.d/bash_completion.sh" ]] && . "$(brew --prefix)/etc/profile.d/bash_completion.sh"

.. tab:: Windows

   Ihr könnt einfach https://git-scm.com/download/win aufrufen und den passenden
   Download starten.

   .. seealso::
      * `git for windows <https://gitforwindows.org/>`_

Konfiguration
-------------

``$ git config --global user.name "[name]"``
    legt den Namen fest, den mit euren Commit-Transaktionen verknüpft wird.
``$ git config --global user.email "[email address]"``
    legt die E-Mail fest, die mit euren Commit-Transaktionen verknüpft wird.
``$ git config --global color.ui auto``
    aktiviert die Kolorierung der Befehlszeilenausgabe.

Die ``~/.gitconfig``-Datei
~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit den oben angegebenen Befehle kann z.B. folgende Datei erstellt werden:

.. code-block:: ini

    [user]
        name = veit
        email = veit@cusy.io

    [color]
        diff = auto
        status = auto
        branch = auto

In der ``~/.gitconfig``-Datei können jedoch auch Aliase festgelegt werden:

.. code-block:: ini

    [alias]
        st = status
        ci = commit
        br = branch
        co = checkout
        df = diff
        dfs = diff --staged

Auch der Editor lässt sich angeben und die Hervorhebung von Leerzeichenfehlern
in ``git diff``:

.. code-block:: ini

    [core]

        editor = vim

        # Highlight whitespace errors in git diff:
        whitespace = tabwidth=4,tab-in-indent,cr-at-eol,trailing-space

Anmeldedaten verwalten
::::::::::::::::::::::

Seit der Git-Version 1.7.9 lassen sich die Zugangsdaten zu git-Repositories mit
`gitcredentials <https://git-scm.com/docs/gitcredentials>`_ verwalten. Um diese
zu nutzen, könnt ihr z.B. folgendes angeben:

.. code-block:: console

    $ git config --global credential.helper Cache

Hiermit wird ihr Passwort für 15 Minuten im Cache-Speicher gehalten. Der Timeout
kann ggf. erhöht werden, z.B. mit:

.. code-block:: console

    $ git config --global credential.helper 'cache --timeout=3600'

.. tab:: macOS

    Unter macOS lässt sich mit `osxkeychain` die Schlüsselbundverwaltung
    (*Keychain*) nutzen um die Zugangsdaten zu speichern. `osxkeychain` setzt
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

    Dies trägt folgendes in die ~/.gitconfig ein:

    .. code-block:: ini

        [credential]
            helper = osxkeychain

.. tab:: Windows

    Für Windows steht `Git Credential Manager for Windows
    <https://github.com/Microsoft/Git-Credential-Manager-for-Windows>`_ zur
    Verfügung. Für das Programm muss der `Installer
    <https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/latest>`_
    heruntergeladen werden. Nach dem Doppelklick führt er Euch durch die
    weitere Installation. Als Terminal-Emulator für Git Bash solltet ihr das
    Standardkonsolenfenster von Windows auswählen.

.. note::
    Ein umfangreiches Beispiel einer `Konfigurationsdatei findet ihr in meinem
    `dotfiles <https://github.com/veit/dotfiles/>`__-Repository: `.gitconfig
    <https://github.com/veit/dotfiles/blob/main/.config/git/config>`_.

.. seealso::
    * `Git Credential Manager: authentication for everyone
      <https://github.blog/2022-04-07-git-credential-manager-authentication-for-everyone/>`_

Die ``.gitignore``-Datei
~~~~~~~~~~~~~~~~~~~~~~~~

In der ``.gitignore``-Datei eines Repository könnt ihr Dateien von der
Versionsverwaltung ausschließen. Eine typische ``.gitignore``-Datei kann z.B. so
aussehen:

.. code-block:: ini

    /logs/*
    !logs/.gitkeep
    /tmp
    *.swp

Dabei verwendet Git `Globbing <https://linux.die.net/man/7/glob>`_-Muster,
:abbr:`u.a. (unter anderem)`:

+-------------------------------+-------------------------------+-------------------------------+ 
| Muster                        | Beispiel                      | Erläuterung                   |
+===============================+===============================+===============================+ 
| .. code-block:: console       | ``logs/instance.log``,        | Ihr könnt zwei Sternchen      |
|                               | ``logs/instance/error.log``,  | voranstellen um Verzeichnisse |
|     **/logs                   | ``prod/logs/instance.log``    | an einer beliebigen Stelle im |
|                               |                               | zu finden.                    |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``logs/instance.log``,        | Ihr könnt zwei Sternchen      |
|                               | ``prod/logs/instance.log``    | voranstellen um Dateien anhand|
|     **/logs/instance.log      | aber nicht                    | ihres Namens in einem         |
|                               | ``logs/prod/instance.log``    | übergeordneten Verzeichnis zu |
|                               |                               | finden.                       |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``instance.log``,             | Ein Sternchen ist ein         |
|                               | ``error.log``,                | Platzhalter für null oder     |
|     *.log                     | ``logs/instance.log``         | mehr Zeichen.                 |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``/logs/instance.log``,       | Ein vor ein Muster gestelltes |
|                               | ``/logs/error.log``,          | Anführungszeichen ignoriert   |
|     /logs                     | nicht jedoch                  | dieses. Wenn eine Datei mit   |
|     !/logs/.gitkeep           | ``/logs/.gitkeep`` oder       | einem Muster übereinstimmt,   |
|                               | ``/instance.log``             | aber auch mit einem           |
|                               |                               | negierenden, das später       |
|                               |                               | definiert ist, wird sie nicht |
|                               |                               | ignoriert.                    |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``/instance.log``,            | Mit dem vorangestellten       |
|                               | nicht jedoch                  | Schrägstrich passt das Muster |
|     /instance.log             | ``logs/instance.log``         | nur zu Dateien im             |
|                               |                               | Stammverzeichnis des          |
|                               |                               | Repository.                   |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``instance.log``,             | Üblicherweise passen die      |
|                               | ``logs/instance.log``         | Muster zu Dateien in jedem    |
|     instance.log              |                               | Verzeichnis.                  |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``instance0.log``,            | Ein Fragezeichen passt genau  |
|                               | ``instance1.log``,            | zu einem Zeichen.             |
|     instance?.log             | aber nicht                    |                               |
|                               | ``instance.log`` oder         |                               |
|                               | ``instance10.log``            |                               |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``instance0.log``,            | Eckige Klammern können        |
|                               | ``instance1.log``,            | verwendet werden um ein       |
|     instance[0-9].log         | aber nicht                    | einzelnes Zeichen aus einem   |
|                               | ``instance.log`` oder         | bestimmten Bereich zu finden. |
|                               | ``instance10.log``            |                               |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``instance0.log``,            | Eckige Klammern passen        |
|                               | ``instance1.log``,            | auf ein einzelnes Zeichen     |
|     instance[01].log          | aber nicht                    | aus einer bestimmten Menge.   |
|                               | ``instance2.log`` oder        |                               |
|                               | ``instance01.log``            |                               |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``instance2.log``,            | Ein Ausrufezeichen kann       |
|                               | aber nicht                    | verwendet werden um ein       |
|     instance[!01].log         | ``instance0.log``,            | beliebiges Zeichen aus einer  |
|                               | ``instance1.log`` oder        | angegebenen Menge zu finden.  |
|                               | ``instance01.log``            |                               |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``logs``                      | Wenn kein Schrägstrich        |
|                               | ``logs/instance.log``         | anhängt, passt das Muster     |
|     logs                      | ``prod/logs/instance.log``    | sowohl auf Dateien als auch   |
|                               |                               | auf den Inhalt von            |
|                               |                               | Verzeichnissen mit diesem     |
|                               |                               | Namen.                        |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``logs/instance.log``,        | Das Anhängen eines            |
|                               | ``logs/prod/instance.log``,   | Schrägstrichs zeigt an, dass  |
|     logs/                     | ``prod/logs/instance.log``    | das Muster ein Verzeichnis    |
|                               |                               | ist. Der gesamte Inhalt jedes |
|                               |                               | Verzeichnisses im Repository, |
|                               |                               | das diesem Namen entspricht – |
|                               |                               | einschließlich all seiner     |
|                               |                               | Dateien und Unterverzeichnisse|
|                               |                               | – wird ignoriert.             |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       |``var/instance.log``,          | Zwei Sternchen passen zu null |
|                               |``var/logs/instance.log``,     | oder mehr Verzeichnissen.     |
|     var/**/instance.log       |``var/logs/instance/error.log``|                               |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``logs/instance/error.log``,  | Wildcards können auch in      |
|                               | ``logs/instance1/error.log``  | Verzeichnisnamen verwendet    |
|     logs/instance*/error.log  |                               | werden.                       |
+-------------------------------+-------------------------------+-------------------------------+ 
| .. code-block:: console       | ``logs/instance.log``,        | Muster, die eine Datei in     |
|                               | nicht jedoch                  | einem bestimmten Verzeichnis  |
|     logs/instance.log         | ``var/logs/instance.log``     | angeben, sind relativ zum     |
|                               | oder                          | Stammverzeichnis des          |
|                               | ``instance.log``              | Repository.                   |
+-------------------------------+-------------------------------+-------------------------------+ 

Git-commit leerer Ordner
::::::::::::::::::::::::

In obigem Beispiel seht ihr, dass mit ``/logs/*`` keine Inhalte des
``logs``-Verzeichnis mit Git versioniert werden soll, in der Folgezeile jedoch
eine Ausnahme definiert wird: ``!logs/.gitkeep`` erlaubt, dass die Datei
``.gitkeep`` mit Git verwaltet werden darf. Damit wird dann auch das
``logs``-Verzeichnis in das Git-Repository übernommen. Diese Hilfskonstruktion
ist erforderlich, da leere Ordner nicht mit Git verwaltet werden können.

Eine andere Möglichkeit besteht darin, in einem leeren Ordner eine
``.gitignore``-Datei mit folgendem Inahlt zu erstellen:

.. code-block:: ini

    # ignore everything except .gitignore
    *
    !.gitignore


.. seealso:
    * `Can I add empty directories?
      <https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F>`_

``excludesfile``
::::::::::::::::

Ih könnt jedoch auch zentral für alle Git-Repositories Dateien ausschließen.
Hierfür wird üblicherweise in der ``~/.gitconfig``-Datei folgendes angegeben:

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

Wenn ihr eine Datei ignorieren wollen, die in der Vergangenheit bereits dem Repository hinzugefügt
wurde, müsst ihr die Datei aus eurem Repository löschen und dann eine
``.gitignore``-Regel für sie hinzufügen. Die Verwendung der Option ``--cached`` bei ``git rm``
bedeutet, dass die Datei aus dem Repository gelöscht wird, aber als ignorierte Datei in eurem
Arbeitsverzeichnis verbleibt.

.. code-block:: console

    $ echo *.log >> .gitignore
    $ git rm --cached *.log
    rm 'instance.log'
    $ git commit -m "Remove log files"

.. note::
    Ihr könnt die Option ``--cached`` weglassen, wenn ihr die Datei sowohl aus dem Repository als
    auch aus Ihrem lokalen Dateisystem löschen wollt.

Commit einer ignorierten Datei
::::::::::::::::::::::::::::::

Es ist möglich, den Commit einer ignorierten Datei an das Repository mit der Option ``-f`` (oder
``--force``) bei ``git add`` zu erzwingen:

.. code-block:: console

    $ cat data/.gitignore
    *
    $ git add -f data/iris.csv
    $ git commit -m "Force add iris.csv"

Ihr könnt dies in Erwägung ziehen, wenn ihr ein allgemeines Muster (wie ``*``) definiert habt, aber
eine bestimmte Datei übertragen wollt. Eine bessere Lösung ist meist jedoch, eine Ausnahme von
der allgemeinen Regel zu definieren:

.. code-block:: console

    $ echo '!iris.csv' >> data/.gitignore
    $ cat data/.gitignore
    *
    !iris.csv
    $ git add data/iris.csv
    $ git commit -m "Add iris.csv"

Dieser Ansatz dürfte für euer Team offensichtlicher und weniger verwirrend sein.

Fehlersuche in ``.gitignore``-Dateien
:::::::::::::::::::::::::::::::::::::

Bei komplizierten ``.gitignore``-Mustern oder bei Mustern, die über mehrere ``.gitignore``-Dateien
verteilt sind, kann es schwierig sein, herauszufinden, warum eine bestimmte Datei ignoriert wird.
Ihr könnt den Befehl ``git check-ignore`` mit der Option ``-v`` (oder ``--verbose``) verwenden, um
festzustellen, welches Muster die Ursache für das Ignorieren einer bestimmten Datei ist:

.. code-block:: console

    $ git check-ignore -v data/iris.csv
    data/.gitignore:2:!iris.csv	data/iris.csv

Die Ausgabe zeigt :samp:`{FILE_CONTAINING_THE_PATTERN}:{LINE_NUMBER_OF_THE_PATTERN}:{PATTERN}
{FILE_NAME}`

Ihr könnt mehrere Dateinamen an ``git check-ignore`` übergeben, wenn ihr möchtet, und die Namen
selbst müssen nicht einmal den Dateien entsprechen, die in eurem Repository existieren.
