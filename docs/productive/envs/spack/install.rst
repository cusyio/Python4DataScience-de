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

  * ``gnupg2``

… for Debian/Ubuntu:

.. code-block:: console

    $ sudo apt install build-essential patch tar gzip bzip2 git gnupg2

… oder für macOS:

.. code-block:: console

    $ xcode-select --install
    $ brew install make bash gzip bzip2 git gnupg
    $ brew link gnupg

Anschließend wird die Shell konfiguriert indem z.B. für die Bash folgendes in
die Bash-Konfiguration eingetragen wird:

.. code-block:: console

    $ source /usr/local/opt/modules/init/bash

* ``gnupg2`` für ``gpg``-Subcommand

Installation
------------

.. code-block:: console

    $ git clone https://github.com/spack/spack.git
    Cloning into 'spack'...
    ...
    $ cd spack
    $ $ git checkout releases/v0.17

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
