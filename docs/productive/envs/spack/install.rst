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

    $ brew install libc++ make bash gzip bzip2 git gnupg
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

Überprüfen der Installation
---------------------------

.. code-block:: console

    $ spack spec python
    Input spec
    --------------------------------
    python

    Concretized
    --------------------------------
    python@3.8.12%apple-clang@13.0.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87,4c2457325f2b608b1b6a2c63087df8c26e07db3e3d493caf36a56f0ecf6fb768,f2fd060afc4b4618fe8104c4c5d771f36dc55b1db5a4623785a4ea707ec72fb4 arch=darwin-bigsur-cannonlake
        ^apple-libuuid@1353.100.2%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
        ^bzip2@1.0.8%apple-clang@13.0.0~debug~pic+shared arch=darwin-bigsur-cannonlake
            ^diffutils@3.8%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
                ^libiconv@1.16%apple-clang@13.0.0 libs=shared,static arch=darwin-bigsur-cannonlake
        ^expat@2.4.1%apple-clang@13.0.0~libbsd arch=darwin-bigsur-cannonlake
        ^gdbm@1.19%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
            ^readline@8.1%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
                ^ncurses@6.2%apple-clang@13.0.0~symlinks+termlib abi=none arch=darwin-bigsur-cannonlake
                    ^pkgconf@1.8.0%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
        ^gettext@0.21%apple-clang@13.0.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=darwin-bigsur-cannonlake
            ^libxml2@2.9.12%apple-clang@13.0.0~python arch=darwin-bigsur-cannonlake
                ^xz@5.2.5%apple-clang@13.0.0~pic libs=shared,static arch=darwin-bigsur-cannonlake
                ^zlib@1.2.11%apple-clang@13.0.0+optimize+pic+shared arch=darwin-bigsur-cannonlake
            ^tar@1.34%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
        ^libffi@3.3%apple-clang@13.0.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=darwin-bigsur-cannonlake
        ^openssl@1.1.1l%apple-clang@13.0.0~docs certs=system arch=darwin-bigsur-cannonlake
            ^perl@5.34.0%apple-clang@13.0.0+cpanm+shared+threads arch=darwin-bigsur-cannonlake
                ^berkeley-db@18.1.40%apple-clang@13.0.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=darwin-bigsur-cannonlake
        ^sqlite@3.36.0%apple-clang@13.0.0+column_metadata+fts~functions~rtree arch=darwin-bigsur-cannonlake

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
