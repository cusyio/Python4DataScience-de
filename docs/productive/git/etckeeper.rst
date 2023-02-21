etckeeper
=========

`etckeeper <https://etckeeper.branchable.com>`_ ist eine Sammlung von
Werkzeugen, mit denen das ``/etc``-Verzeichnis in einem Git-Repository verwaltet
werden kann. So können Änderungen überprüft und :abbr:`ggf. (gegebenenfalls)`
rückgängig gemacht werden. Zudem verbindet es sich mit Paketmanagern wie `apt
<https://de.wikipedia.org/wiki/Advanced_Packaging_Tool>`_, um Änderungen, die
während eines Paket-Upgrades an ``/etc`` vorgenommen werden, automatisch zu
übertragen. Schließlich werden auch Metadaten von Dateien berücksichtigt, die
Git normalerweise nicht verwaltet, die aber für ``/etc`` wichtig sind, wie
:abbr:`z.B. (zum Beispiel) die Berechtigungen von` ``/etc/shadow``.

Installation
------------

.. tab:: Debian/Ubuntu

    etckeeper kann einfach installiert werden mit

    .. code-block:: console

        $ sudo apt install git etckeeper

Konfiguration
-------------

#. Die Konfiguration von etckeeper erfolgt in der ``etckeeper.conf``-Datei:

   .. code-block:: console

    $ sudo vi /etc/etckeeper/etckeeper.conf
    # The VCS to use.
    #VCS="hg"
    VCS="git"
    #VCS="bzr"
    #VCS="darcs"
    …

#. Außerdem sollten die folgenden beiden automatischen Commits vermieden werden:

   .. code-block:: console

    # Uncomment to avoid etckeeper committing existing changes
    # to /etc automatically once per day.
    AVOID_DAILY_AUTOCOMMITS=1
    …
    # Uncomment to avoid etckeeper committing existing changes to
    # /etc before installation. It will cancel the installation,
    # so you can commit the changes by hand.
    AVOID_COMMIT_BEFORE_INSTALL=1

#. Nun sollte noch git selbst konfiguriert werden, :abbr:`s. (siehe)`
   :ref:`git-config`.

#. Schließlich kann das ``/etc``-Verzeichnis unter die Git-Versionsverwaltung
   genommen werden mit:

   .. code-block:: console

    $ cd /etc/
    $ sudo etckeeper init
    Initialized empty Git repository in /etc/.git/
    $ sudo etckeeper commit "Initial commit"

Verwendung
----------

Wird nun eine Konfigurationsdatei editiert, so können die Änderungen nun einfach
mit Git protokolliert werden.

Metadaten verwalten
-------------------

Da Git an sich keine vollständigen Metadaten aufzeichnet, wurde von etckeeper
ein :doc:`pre-commit Hook <hooks/index>` in :file:`/etc/.git/hooks/pre-commit`
eingerichtet. Dieser protokolliert in der Datei :file:`/etc/.etckeeper` die
``chmod``- und ``chgrp``-Angaben für alle Dateien die nicht den Standardrechten
entsprechen:

.. code-block::

    maybe chmod 0755 '.'
    maybe chmod 0700 './.etckeeper'
    maybe chmod 0644 './.gitignore'
    …
    . gitignore

Dateien, die nicht mit Git im ``/etc``-Verzeichnis versioniert werden sollen,
können in der Datei :file:`/etc/.gitignore` hinzugefügt werden. Diese Datei wird
beim Initiieren von etckeeper erzeugt und kann :abbr:`ggf. (gegebenenfalls)`
ergänzt werden nach dem Kommentar

.. code-block::

    # end section managed by etckeeper
