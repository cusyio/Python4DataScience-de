Spack-Installation
==================

Anforderungen
-------------

* Interpreter for Spack:

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

Anschließend wird die Shell konfiguriert indem z.B. für die Bash folgendes in
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
    $ git switch releases/v0.19

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
lingo aus vorgefertigten Binärdateien zu installieren, könnt ihr einfach ein
Paket angeben:

.. code-block:: console

    $ spack spec zlib
    ==> Bootstrapping clingo from pre-built binaries
    ==> Fetching https://mirror.spack.io/bootstrap/github-actions/v0.4/build_cache/linux-centos7-x86_64-gcc-10.2.1-clingo-bootstrap-spack-idkenmhnscjlu5gjqhpcqa4h7o2a7aow.spec.json
    ==> Fetching https://mirror.spack.io/bootstrap/github-actions/v0.4/build_cache/linux-centos7-x86_64/gcc-10.2.1/clingo-bootstrap-spack/linux-centos7-x86_64-gcc-10.2.1-clingo-bootstrap-spack-idkenmhnscjlu5gjqhpcqa4h7o2a7aow.spack
    ==> Installing "clingo-bootstrap@spack%gcc@10.2.1~docs~ipo+python+static_libstdcpp build_type=Release arch=linux-centos7-x86_64" from a buildcache
    Input spec
    --------------------------------
    zlib

    Concretized
    --------------------------------
    zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-sandybridge

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
    ==> Warning: `spack find --bootstrap` is deprecated and will be removed in v0.19.
      Use `spack --bootstrap find` instead.
    ==> Showing internal bootstrap store at "/srv/jupyter/.spack/bootstrap/store"
    -- linux-centos7-x86_64 / gcc@10.2.1 ----------------------------
    bison@3.0.4  clingo-bootstrap@spack  python@3.10
    ==> 3 installed packages

Compiler-Konfiguration
----------------------

.. code-block:: console

    $ spack compilers
    ==> Available compilers
    -- gcc ubuntu22.04-x86_64 ---------------------------------------
    gcc@11.3.0

Baut euren eigenen Compiler
---------------------------

.. code-block:: console

    $ spack install gcc
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

    $ spack compiler find /srv/jupyter/spack/opt/spack/linux-ubuntu22.04-sandybridge/gcc-11.3.0/gcc-12.2.0-gbaw464qxjuz6i3uud42cd5mb4xujxia/
    ==> Added 1 new compiler to /srv/jupyter/.spack/linux/compilers.yaml
        gcc@12.2.0
    ==> Compilers are defined in the following files:
        /srv/jupyter/.spack/linux/compilers.yaml

.. code-block:: console

    $ spack compilers
    ==> Available compilers
    -- gcc ubuntu22.04-x86_64 ---------------------------------------
    gcc@12.2.0  gcc@11.3.0

Wenn ihr die Standard- und Site-Einstellungen überschreiben möchtet, könnt ihr
:file:`${HOME}/.spack/packages.yaml` ändern:

.. code-block:: yaml

    packages:
      all:
        compiler: [gcc@12.2.0]

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

Zusätzliche Schlüssel können dem Schlüsselring hinzugefügt werden mit
``spack gpg trust <keyfile>``. Sobald ein Schlüssel vertrauenswürdig ist,
können Pakete, die vom Besitzer dieses Schlüssels signiert wurden, installiert
werden.

Schlüssel erstellen
~~~~~~~~~~~~~~~~~~~

Ihr könnt auch eigene Schlüssel erstellen um eure eigenen Pakete signieren
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
