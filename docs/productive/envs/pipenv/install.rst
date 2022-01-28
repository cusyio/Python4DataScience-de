Installation
============

Dieser Abschnitt behandelt die Grundlagen zur Installation von
:term:`Python-Paketen <Distribution Package>`.

Voraussetzungen für die Installation von Paketen
------------------------------------------------

Vor der Installation von Python-Paketen müssen einige Voraussetzungen erfüllt
sein.

#. Stellt sicher, dass ihr die gewünschte Python-Version verwendet:

   .. code-block:: console

    $ python --version
    Python 3.8.12

   .. note::
        In iPython oder einem Jupyter Notebook könnt ihr die Version
        folgendermaßen herausbekommen:

        .. code-block:: ipython

            In [1]: import sys
                    sys.version_info
            sys.version_info(major=3, minor=8, micro=12, releaselevel='final', serial=0)

   .. note::
        Falls ihr das System-Python eurer Linux-Distribution verwendet, solltet
        ihr zunächst eine virtuelle Umgebung mit Python 3 und :term:`Pip <pip>`
        erstellen.

#. Stellt sicher, dass :term:`Pip <pip>` installiert ist:

   .. code-block:: console

    $ pip --version
    pip 21.3.1

   #. Falls Pip noch nicht installiert ist, könnt ihr es installieren (lassen)

      * für Python 2 mit:

        .. code-block:: console

            $ sudo apt install python-pip

      * für Python 3 mit:

        .. code-block:: console

            $ sudo apt install python3-venv python3-pip

Pipenv installieren
-------------------

:term:`pipenv` ist ein Abhängigkeitsmanager für Python-Projekte. Er nutzt
:term:`Pip` zum Installieren von Python-Paketen, er vereinfacht jedoch die
Verwaltung von Abhängigkeiten. Pip kann zum Installieren von Pipenv verwendet
werden, es sollte jedoch das ``--user``-Flag verwendet werden, damit es nur
für diesen Nutzer bereitsteht. Dadurch soll verhindert werden, dass
versehentlich systemweite Pakete überschrieben werden:

.. code-block:: console

    $ python3 -m pip install --user pipenv
    …
    Successfully installed distlib-0.3.4 filelock-3.4.2 pipenv-2022.1.8 platformdirs-2.4.1 virtualenv-20.13.0 virtualenv-clone-0.5.7

.. note::

   Wenn pipenv nach der Installation nicht in der Shell verfügbar ist, muss
   ggf. das ``USER_BASE/bin``-Verzeichnis in ``PATH`` angegeben werden.

   * Unter Linux und MacOS lässt sich ``USER_BASE`` ermitteln mit::

        $ python3 -m site --user-base
        /Users/veit/.local

     Anschließend muss noch das ``bin``-Verzeichnis angehängt und zu ``PATH``
     hinzugefügt werden. Alternativ kann ``PATH`` dauerhaft gesetzt werden, indem
     ``~/.profile`` oder ``~/.bash_profile`` geändert werden, in meinem Fall also::

        export PATH=/Users/veit/.local/bin:$PATH

   * Unter Windows kann das Verzeichnis ermittelt werden mit
     ``py -m site --user-site`` und anschließend ``site-packages`` durch
     ``Scripts`` ersetzt werden. Dies ergibt dann z.B.:

     .. code-block:: console

        C:\Users\veit\AppData\Roaming\Python38\Scripts

     Um dauerhaft zur Verfügung zu stehen, kann dieser Pfad unter ``PATH``
     im Control Panel eingetragen werden.

Weitere Informationen zur nutzerspezifischen Installation findet ihr in `User
Installs <https://pip.readthedocs.io/en/latest/user_guide.html#user-installs>`_.

Virtuelle Umgebungen erstellen
------------------------------

:term:`Virtuelle Python-Umgebungen <Virtuelle Umgebung>` ermöglichen die
Installation von Python-Paketen an einem isolierten Ort für eine bestimmte
Anwendung, anstatt sie global zu installieren. Ihr habt also eure eigenen
Installationsverzeichnisse und teilt keine Bibliotheken mit anderen
virtuellen Umgebungen:

.. code-block:: console

    $ mkdir myproject
    $ cd !$
    cd myproject
    $ pipenv install requests
    Creating a virtualenv for this project..
    …
    Virtualenv location: /srv/jupyter/.local/share/virtualenvs/myproject-CZKj6mqJ
    Creating a Pipfile for this project...
    Installing requests...
    Adding requests to Pipfile's [packages]...
    …
