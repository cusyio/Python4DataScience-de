Environments, ``spack.yaml`` und ``spack.lock``
===============================================

#. Erstellen einer virtuellen Umgebung:

   .. code-block:: console

    ==> Created environment 'python-311' in /srv/jupyter/spack/var/spack/environments/python-311
    ==> You can activate this environment with:
    ==>   spack env activate python-311

   Alternativ kann sie auch an beliebigen anderen Orten gespeichert werden,
   z.B.:

   .. code-block:: console

    $ cd spackenvs/
    $ spack env create -d python-311
    ==> Created environment in /srv/jupyter/jupyter-tutorial/spackenvs/python-311
    ==> You can activate this environment with:
    ==>   spack env activate /srv/jupyter/jupyter-tutorial/spackenvs/python-311

#. Überprüfen der virtuellen Umgebung:

   .. code-block:: console

    $ spack env list
    ==> 1 environments
        python-311

#. Aktivieren der virtuellen Umgebung:

   .. code-block:: console

    $ spack env activate python-311

#. Überprüfen der Aktivierung:

   Wenn ihr eine Umgebung aktiviern habt, wird euch nur das angezeigt, was sich
   in der aktuellen Umgebung befindet. Das sollte unmittelbar nach der
   Aktivierung nichts sein:

   .. code-block:: console

    $ spack find
    ==> In environment python-311
    ==> No root specs
    ==> 0 installed packages

   Und wenn ihr überprüfen möchtet, in welcher Umgebung ihr euch befindet, dann
   könnt ihr dies abfragen mit:

   .. code-block:: console

    $ spack env status
    ==> In environment python-311

#. Schließlich könnt ihr die aktivierte Umgebung verlassen mit ``spack env
   deactivate`` oder kurz ``despacktivate``.

   .. code-block:: console

    $ despacktivate
    $ spack env status
    ==> No active environment

Pakete installieren
-------------------

.. code-block:: console

    $ spack env activate python-311
    $ spack add python@3.11.0
    $ spack install
    ==> Concretized python@3.11.0
     -   4nvposf  python@3.11.0%gcc@11.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib build_system=generic patches=13fa8bf,b0615b2,f2fd060 arch=linux-ubuntu22.04-sandybridge
     -   6fefzf3      ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-sandybridge
     -   27f7g74          ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
    …
    ==> python: Successfully installed python-3.11.0-4nvposf6bicf5ogp6nqacfo4dfvwm7zv
      Fetch: 5.19s.  Build: 3m 48.84s.  Total: 3m 54.03s.
    [+] /srv/jupyter/spack/opt/spack/linux-ubuntu22.04-sandybridge/gcc-11.3.0/python-3.11.0-4nvposf6bicf5ogp6nqacfo4dfvwm7zv
    ==> Updating view at /srv/jupyter/python-311/.spack-env/view
    $ spack find
    ==> In environment /home/veit/python-311
    ==> Root specs
    python@3.11.0

    ==> Installed packages
    -- linux-ubuntu22.04-sandybridge / gcc@11.3.0 -------------------
    berkeley-db@18.1.40                 libiconv@1.16   readline@8.1.2
    bzip2@1.0.8                         libmd@1.0.4     sqlite@3.39.4
    ca-certificates-mozilla@2022-10-11  libxml2@2.10.1  tar@1.34
    diffutils@3.8                       ncurses@6.3     util-linux-uuid@2.38.1
    expat@2.4.8                         openssl@1.1.1s  xz@5.2.7
    gdbm@1.23                           perl@5.36.0     zlib@1.2.13
    gettext@0.21.1                      pigz@2.7        zstd@1.5.2
    libbsd@0.11.5                       pkgconf@1.8.0
    libffi@3.4.2                        python@3.11.0
    ==> 25 installed packages

Mit ``spack cd -e python-311`` könnt ihr in dieses Verzeichnis wechseln,
:abbr:`z.B. (zum Beispiel)`:

.. code-block:: console

    $ spack cd -e python-311
    $ pwd
    /srv/jupyter/spack/var/spack/environments/python-311

Dort befinden sich die beiden Dateien ``spack.yaml`` und ``spack.lock``.

``spack.yaml``
    ist die Konfigurationsdatei für die virtuelle Umgebung. Sie wird in
    ``~/spack/var/spack/environments/`` beim Aufruf von ``spack env create``
    erstellt.

    Alternativ zu ``spack install`` können in ``spack.yaml`` auch der
    ``specs``-Liste ``python@3.11.0``, ``py-numpy`` etc. hinzugefügt werden:

    .. code-block:: yaml

        specs: [python@3.11.0, …]

``spack.lock``
    Mit ``spack install`` werden die Specs konkretisiert, in ``spack.lock`` geschrieben und  installiert.
    Im Gegensatz zu ``spack.yaml`` ist ``spack.lock`` im ``json``-Format geschrieben und enthält die
    notwendigen Informationen um reproduzierbare Builds der Umgebung erstellen zu können:

    .. code-block:: javascript

        {
          "_meta": {
            "file-type": "spack-lockfile",
            "lockfile-version": 4,
            "specfile-version": 3
          },
          "roots": [
            {
              "hash": "4nvposf6bicf5ogp6nqacfo4dfvwm7zv",
              "spec": "python@3.11.0"
            }
          ],
          "concrete_specs": {
            "4nvposf6bicf5ogp6nqacfo4dfvwm7zv": {
              "name": "python",
              "version": "3.11.0",
              "arch": {
                "platform": "linux",
                "platform_os": "ubuntu22.04",
                "target": {
                  "name": "sandybridge",
                  "vendor": "GenuineIntel",
                  "features": [
                    "aes",
                    "avx",
                    ...
                  ]
                }
              }
            }
          }
        }

Installation zusätzlicher Pakete
--------------------------------

Zusätzliche Pakete können in der virtuellen Umgebung installiert werden mit
``spack add`` und ``spack install``. Für `Matplotlib <https://matplotlib.org/>`_
sieht dies z.B. folgendermaßen aus:

.. code-block:: console

    $ spack add py-numpy
    ==> Adding py-numpy to environment /srv/jupyter/jupyter-tutorial/spackenvs/python-311
    $ spack install
    ==> Concretized python@3.11.0
    [+]  4nvposf  python@3.11.0%gcc@11.3.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib build_system=generic patches=13fa8bf,b0615b2,f2fd060 arch=linux-ubuntu22.04-sandybridge
    [+]  6fefzf3      ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-sandybridge
    [+]  27f7g74          ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
    …
    ==> Installing environment /srv/jupyter/jupyter-tutorial/spackenvs/python-311
    …
    ==> Successfully installed py-numpy

.. note::
   Falls von diesem Spack-Environment bereits ein :doc:`Pipenv-Environment
   <../pipenv/env>` abgeleitet wurde, muss dieses neu gebaut werden um das
   zusätzliche Spack-Paket zu erhalten:
   
   .. code-block:: console

    $ pipenv install --python=/srv/jupyter/spack/var/spack/environments/python-311/.spack-env/view/bin/python
    Creating a virtualenv for this project...
    Pipfile: /srv/jupyter/jupyter-tutorial/pipenvs/python-311/Pipfile
    Using /srv/jupyter/spack/var/spack/environments/python-311/.spack-env/view/bin/python (3.11.0) to create virtualenv...
    ⠹ Creating virtual environment...Using base prefix '/srv/jupyter/jupyterhub/spackenvs/python-374/.spack-env/view'
      creator Venv(dest=/srv/jupyter/.local/share/virtualenvs/python-311-aGnPz55z, clear=False, no_vcs_ignore=False, global=False, describe=CPython3Posix)
      seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/srv/jupyter/.local/share/virtualenv)
        added seed packages: pip==22.3.1, setuptools==65.5.1, wheel==0.38.4
      activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

    ✔ Successfully created virtual environment!
    Virtualenv location: /srv/jupyter/.local/share/virtualenvs/python-311-aGnPz55z
    Creating a Pipfile for this project...
    Pipfile.lock not found, creating...
    Locking [packages] dependencies...
    Locking [dev-packages] dependencies...
    Updated Pipfile.lock (a3aa656db1de341c375390e74afd03f09eb681fe6881c58a71a85d6e08d77619)!
    Installing dependencies from Pipfile.lock (d77619)...
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.

   Anschließend kann die Installation überprüft werden mit:

   .. code-block:: console

    $ pipenv run python
    Python 3.11.0 (main, Nov 19 2022, 11:29:15) [GCC 12.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import matplotlib.pyplot as plt

Konfiguration
-------------

``spack spec`` spezifiziert die Abhängigkeiten bestimmter Pakete, z.B.:

.. code-block:: console

    $ spack spec py-matplotlib

    Input spec
    --------------------------------
    py-matplotlib

    Concretized
    --------------------------------
    py-matplotlib@3.6.2%gcc@11.3.0~animation~fonts~latex~movies backend=agg build_system=python_pip arch=linux-ubuntu22.04-sandybridge
        ^freetype@2.11.1%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
            ^bzip2@1.0.8%gcc@11.3.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-sandybridge
                ^diffutils@3.8%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
        ^libpng@1.6.37%gcc@11.3.0 build_system=autotools arch=linux-ubuntu22.04-sandybridge
        …

Mit ``spack config get`` könnt ihr euch die Konfiguration einer bestimmten
Umgebung anschauen:

.. code-block:: console

    $ spack config get 
    # This is a Spack Environment file.
    #
    # It describes a set of packages to be installed, along with
    # configuration settings.
    spack:
      # add package specs to the `specs` list
      specs: [python@3.11.0, py-numpy]
      view: true
      concretizer:
        unify: true

Mit ``spack config edit`` kann die Konfigurationsdatei ``spack.yaml`` editiert werden.

.. note::
   Wenn in der Umgebung bereits Pakete installiert sind, sollten mit ``spack
   concretize -f`` alle Abhängigkeiten erneut spezifiziert werden.

Laden der Module
----------------

Mit ``spack env loads -r <env>`` werden alle Module mit ihren Abhängigkeiten
geladen.

.. note::
   Aktuell funktioniert dies jedoch nicht beim Laden der Module aus
   Environments, die nicht in ``$SPACK_ROOT/var/environments`` liegen.

   Daher ersetzen wir das Verzeichnis ``$SPACK_ROOT/var/environments`` durch
   einen symbolischen Link:

   .. code-block:: console

    $ rm $SPACK_ROOT/var/environments
    $ cd $SPACK_ROOT/var/
    $ ln -s /srv/jupyter/jupyter-tutorial/spackenvs environments

.. seealso::

   * :doc:`spack:tutorial_environments`
