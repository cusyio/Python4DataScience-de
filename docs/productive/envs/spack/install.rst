Spack-Installation
==================

Anforderungen
-------------

* Interpreter für Spack:

* Software erstellen

  * C/C++ Compiler
  * ``make``,  ``patch`` und ``bash``

* Archive erstellen und extrahieren

  * ``tar``, ``gzip`` und ``bzip``

* Verwalten von Software-Repositories

  * ``git``

* Signieren und Verifizieren von Build-Caches

  * ``gnupg2`` für ``gpg``-Subcommand

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install build-essential patch tar gzip bzip2 git gnupg2

.. tab:: macOS

   .. code-block:: console

      $ xcode-select --install
      $ brew install make bash gzip bzip2 git gnupg
      $ brew link gnupg

Anschließend wird die Shell konfiguriert, indem z.B. für die Bash folgendes in
die Bash-Konfiguration eingetragen wird:

.. code-block:: console

    $ source /usr/local/opt/modules/init/bash

Installation
------------

.. code-block:: console

    $ git clone https://github.com/spack/spack.git
    Cloning into 'spack'...
    ...
    $ cd spack
    $ git switch releases/v0.17

Shell konfigurieren
-------------------

#. Zur Konfiguration des Bash-Environment wird folgendes in ``~/.bashrc``
   eingetragen:

   .. code-block:: bash

    export SPACK_ROOT=~/spack
    . $SPACK_ROOT/share/spack/setup-env.sh

#. Die geänderte Konfiguration wird nun übernommen mit

   .. code-block:: console

    $ source ~/.bashrc

Bootstrapping ``clingo``
------------------------

Spack uses `clingo <https://potassco.org/clingo/>`_ to resolve optimal versions
and variants of dependencies when installing packages. To install clingo from
pre-built binaries you can simply specify a package:

Spack benutzt `clingo <https://potassco.org/clingo/>`_ um optimale Versionen und
Varianten von Abhängigkeiten bei der Installation von Paketen aufzulösen. Um
clingo aus vorgefertigten Binärdateien zu installieren, könnt ihr einfach ein
Paket angeben:

.. code-block:: console

    $ spack spec zlib
    Input spec
    --------------------------------
    zlib

    Concretized
    --------------------------------
    ==> Bootstrapping clingo from pre-built binaries
    ==> Fetching https://mirror.spack.io/bootstrap/github-actions/v0.1/build_cache/darwin-catalina-x86_64/apple-clang-12.0.0/clingo-bootstrap-spack/darwin-catalina-x86_64-apple-clang-12.0.0-clingo-bootstrap-spack-omsvlh5v6fi2saw5qyqvzsbvqpvrf5yw.spack
    ==> Installing "clingo-bootstrap@spack%apple-clang@12.0.0~docs~ipo+python build_type=Release arch=darwin-catalina-x86_64" from a buildcache
    zlib@1.2.11%apple-clang@13.0.0+optimize+pic+shared arch=darwin-bigsur-cannonlake

.. note::
   Um von vorgefertigten Binärdateien zu booten, benötigt Spack ``patchelf``
   unter Linux oder ``otool`` unter macOS. Ansonsten baut Spack sie aus den
   Quellen und mit einem C++ Compiler.


Bootstrap store
---------------

Alle Werkzeuge, die Spack benötigt, werden in einem separaten Speicher
installiert, der sich im Verzeichnis :file:`${HOME}/.spack` befindet. Die dort
installierte Software kann abgefragt werden mit:

.. code-block:: console

    $ spack find --bootstrap
    ==> Showing internal bootstrap store at "/Users/veit/.spack/bootstrap/store"
    ==> 2 installed packages
    -- darwin-catalina-x86_64 / apple-clang@12.0.0 ------------------
    clingo-bootstrap@spack  python@3.9

Compiler-Konfiguration
----------------------

.. code-block:: console

    $ $ spack compilers
    ==> Available compilers
    -- apple-clang bigsur-x86_64 ------------------------------------
    apple-clang@13.0.0

Baut euren eigenen Compiler
---------------------------

.. code-block:: console

    $ spack install gcc@11.2.0
    ...
    ==> gcc: Successfully installed gcc-11.2.0-azhiay4ugfrs634hqlez7u3f2li3wvzd
      Fetch: 12.09s.  Build: 2h 8m 13.92s.  Total: 2h 8m 26.01s.
    [+] /Users/veit/spack/opt/spack/darwin-bigsur-cannonlake/apple-clang-13.0.0/gcc-11.2.0-azhiay4ugfrs634hqlez7u3f2li3wvzd

Allerdings findet Spack den Compiler zunächst nicht:

.. code-block:: console

    $ $ spack compilers
    ==> Available compilers
    -- apple-clang bigsur-x86_64 ------------------------------------
    apple-clang@13.0.0

Ihr könnt ihn jedoch mit ``spack compiler find`` hinzufügen:

.. code-block:: console

    spack compiler find /Users/veit/spack/opt/spack/darwin-bigsur-cannonlake/apple-clang-13.0.0/gcc-11.2.0-azhiay4ugfrs634hqlez7u3f2li3wvzd
    ==> Added 1 new compiler to /Users/veit/.spack/darwin/compilers.yaml
        gcc@11.2.0
    ==> Compilers are defined in the following files:
        /Users/veit/.spack/darwin/compilers.yaml

.. code-block:: console

    $ spack compilers
    ==> Available compilers
    -- apple-clang bigsur-x86_64 ------------------------------------
    apple-clang@13.0.0

    -- gcc bigsur-x86_64 --------------------------------------------
    gcc@11.2.0

Wenn ihr die Standard- und Site-Einstellungen überschreiben möchtet, könnt ihr
:file:`${HOME}/.spack/packages.yaml` ändern:

.. code-block:: yaml

    packages:
      all:
        compiler: [gcc@11.2.0]

GPG Signing
-----------

Spack unterstützt das Signieren und Verifizieren von Paketen mit
GPG-Schlüsseln. Für Spack wird ein separater Schlüsselring verwendet, weswegen
keine Schlüssel aus dem Home-Verzeichnis von Nutzern verfügbar sind.

Wenn Spack zum ersten Mal installiert wird, ist dieser Schlüsselring leer.
Die in ``/var/spack/gpg`` gespeicherten Schlüssel sind die Standardschlüssel
für eine Spack-Installation. Diese Schlüssel werden durch ``spack gpg init``
importiert. Dadurch werden die Standardschlüssel als vertrauenswürdige Schlüssel
in den Schlüsselbund importiert.

Schlüsseln vertrauen
~~~~~~~~~~~~~~~~~~~~

Zusätzliche Schlüssel können mit ``spack gpg trust <keyfile>`` dem 
Schlüsselring hinzugefügt werden. Sobald ein Schlüssel vertrauenswürdig ist,
können Pakete, die vom Besitzer dieses Schlüssels signiert wurden, installiert
werden.

Schlüssel erstellen
~~~~~~~~~~~~~~~~~~~

Ihr könnt auch eigene Schlüssel erstellen, um eure eigenen Pakete signieren
zu können mit

.. code-block:: console

    $ spack gpg export <location> [<key>…]

Schlüssel auflisten
~~~~~~~~~~~~~~~~~~~

Die im Schlüsselbund verfügbaren Schlüssel können aufgelistet werden mit

.. code-block:: console

    $ spack gpg list

Schlüssel entfernen
~~~~~~~~~~~~~~~~~~~

Schlüssel können entfernt werden mit

.. code-block:: console

    $ spack gpg untrust <keyid>

Schlüssel-IDs können E-Mail-Adressen, Namen oder Fingerprints sein.
