Multi-Arch-Images mit Buildah
=============================

`Buildah <https://buildah.io>`_ erlaubt euch, Container-Images zu erstellen ohne
dass ihr eine vollständige Container-Runtime benötigt. Buildah ist ein
Open-Source-Tool auf Linux-Basis, das `Docker <https://www.docker.com>`_- und
`Kubernetes <https://kubernetes.io>`_-kompatible Images erstellen kann. Zudem kann Buildah nicht nur funktionierende Container von Grund auf neu erstellen,
sondern auch aus einer bereits vorhandenen Dockerdatei. Schließlich lässt es
sich leicht in Skripte und Build-Pipelines einbinden.

Installation
------------

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install buildah

.. seealso::
   * `Installation Instructions
     <https://github.com/containers/buildah/blob/main/install.md>`_

Grundlegende Befehle
--------------------

``buildah --version``
    gibt die aktuelle Version unserer Buildah-Installation aus.
``buildah --help``
    gibt die Buildah-Hilfe aus, wenn ihr nicht weiterkommt.
``buildah from``
    erzeugt einen neuen Arbeitscontainer, entweder von Grund auf oder unter
    Verwendung eines angegebenen Image als Ausgangspunkt, :abbr:`z.B. (zum
    Beispiel)`:

    .. code-block:: console

       $ buildah from centos

``buildah images``
    listet unsere aktuellen Images auf.
``buildah run``
    führt einen Befehl innerhalb des Containers aus, :abbr:`z.B. (zum
    Beispiel)`:

    .. code-block:: console

       $ buildah run centos-working-container yum install python3

``buildah copy``
    kopiert den Inhalt einer Datei, einer URL oder eines Verzeichnisses in das
    Arbeitsverzeichnis eures Containers.
``buildah config``
    aktualisiert die Einstellungen der Bildkonfiguration, :abbr:`z.B. (zum
    Beispiel)` um den Einstiegspunkt für euren Container zu definieren mit

    .. code-block:: console

       $ buildah config --entrypoint

``buildah commit``
    erstellt ein Abbild von einem Arbeitscontainer, um es in die Registry eurer
    Wahl zu pushen.
``buildah containers``
    listet unsere laufenden Container auf, :abbr:`z.B. (zum Beispiel)`:

    .. code-block:: console

       $ buildah containers
       CONTAINER ID  BUILDER  IMAGE ID     IMAGE NAME                      CONTAINER NAME
       d5fe553d344a  *        831691599b88 docker.io/library/centos:latest centos-working-container

``buildah rm -all``
    räumt laufende Container auf und entfernt sie.

Build mit einem Dockerfile
--------------------------

Buildah bietet euch auch die Möglichkeit, Images aus einem Dockerfile zu
erstellen mit dem Befehl ``build-using-dockerfile`` oder ``bud``. ``buildah
images`` sollte anschließend unser Image im Repository anzeigen.
