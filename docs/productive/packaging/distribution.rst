Distribution Package erstellen
==============================

:term:`Distribution Packages <Distribution Package>` sind Archive, die in einen
Paket-Index hochgeladen und mit :term:`Pip` installiert werden können.

Struktur
--------

Ein minimales Distribution Package kann z.B. so aussehen:

.. code-block:: console

    dataprep
    ├── setup.py
    └── src
        └── dataprep
            ├── __init__.py
            └── loaders.py

``setup.py``
------------

Eine minimale und dennoch funktionale :download:`dataprep/setup.py` sieht dann
z.B. so aus:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 2,4-5,9-12,15-21,41-
   :lineno-start: 1

``src``-Package
---------------

`package_dir
<https://docs.python.org/3/distutils/setupscript.html#listing-whole-packages>`_
verweist auf das Verzeichnis ``src``, in dem sich ein oder mehrere Pakete
befinden können. Anschließend könnt ihr mit setuptools’s `find_packages()
<https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html#using-find-or-find-packages>`_
alle Pakete in diesem Verzeichnis finden.

.. note::
    ``find_packages()`` ohne ``src/``-Verzeichnis würde alle Verzeichnisse mit
    einer ``__init__.py``-Datei paketieren, also auch ``tests/``-Verzeichnisse.

``version``
-----------

Für ``version`` gibt es verschiedene Möglichkeiten, die in `PEP 0440
<https://www.python.org/dev/peps/pep-0440/>`_ beschrieben sind.

.. seealso::
    * `Semantic Versioning <https://semver.org>`_
    * `Calendar Versioning <https://calver.org>`_
    * `ZeroVer <https://0ver.org/>`_
    * `bump2version <https://pypi.org/project/bump2version/>`_
    * `Git Tags <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_

``classifiers``
---------------

Mit `classifiers <https://pypi.org/classifiers/>`_ können auf dem
:term:`Python Package Index (PyPI)` passende Filter erstellt werden:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 22-38
   :lineno-start: 16

Außerdem haben eine nützliche Zusatzfunktion: PyPI lehnt unbekannte
*Classifiers* ab, sodass damit auch ein versehentlicher Upload vermieden werden
kann.

.. seealso::
    `Add invalid classifier for non open source license to avoid upload to…
    <https://github.com/veit/cookiecutter-namespace-template/commit/f4fff8ee8595ae2e59e5feb92211c8e3f1252461>`_

Abhängigkeiten
--------------

Abhängigkeiten werden mit ``install_requires`` angegeben:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 40
   :lineno-start: 33

.. note::
   Versionsnummern von Abhängigkeiten sollten üblicherweise nicht in der
    ``setup.py`` festgeschrieben werden sondern in der `requirements.txt
    <https://pip.pypa.io/en/latest/user_guide/#requirements-files>`_-Datei.

.. seealso::
    `setup.py vs requirements.txt
    <https://caremad.io/posts/2013/07/setup-vs-requirement/>`_

Andere Dateien
--------------

``MANIFEST.in``
~~~~~~~~~~~~~~~

Die Datei enthält alle Dateien und Verzeichnisse, die nicht bereits mit
``packages`` oder ``py_module`` erfasst werden. Sie kann z.B. so aussehen:
:download:`dataprep/MANIFEST.in`:

.. literalinclude:: dataprep/MANIFEST.in
   :linenos:

Weitere Anweisungen in `Manifest.in` findet ihr in `Creating a source
distribution
<https://docs.python.org/3/distutils/commandref.html?highlight=manifest#creating-a-source-distribution-the-sdist-command>`_.

.. note::
    Häufig wird die Aktualisierung der ``Manifest.in``-Datei vergessen. Um dies
    zu vermeiden, könnt ihr `check-manifest
    <https://pypi.org/project/check-manifest/>`_ in einem ``pre-commit``-Hook
    verwenden.

.. note::
    Wenn ihr Dateien und Verzeichnisse aus ``MANIFEST.in`` auch installiert
    werden sollen, z.B. wenn es sich um laufzeitrelevante Daten handelt, könnt
    ihr dies mit ``include_package_data=True`` in eurem ``setup()``-Aufruf
    angeben.

``setup.cfg``
~~~~~~~~~~~~~

Diese Datei wird nicht mehr benötigt, zumindest nicht für die Paketierung.
``wheel`` sammelt heutzutage alle erforderlichen Lizenzdateien automatisch und
``setuptools`` kann mit dem ``options``-Keyword-Argument universelle
``wheel``-Pakete bauen, z.B. ``dataprep-0.1.0-py3-none-any.whl``.

``pyproject.toml``
~~~~~~~~~~~~~~~~~~

`PEP 517 <https://www.python.org/dev/peps/pep-0517/>`_ und `PEP 518
<https://www.python.org/dev/peps/pep-0518/>`_ brachten erweiterbare
Build-Backends, isolierte Builds und `pyproject.toml
<https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/>`_. Die
Datei verwendet das
:doc:`../../data-processing/serialisation-formats/toml`-Format und da wir
``setuptools`` verwenden, sollte die Datei so oder so ähnlich aussehen:

.. literalinclude:: dataprep/pyproject.toml
   :language: toml
   :lines: 1-4,6-
   :linenos:

``build-system``
    definiert einen Abschnitt, der das Build-System beschreibt
``requires``
    definiert eine Liste von Abhängigkeiten, die installiert sein müssen, damit
    das Build-System funktioniert. Ein Setuptools-Build-System benötigt
    ``setuptools`` und ``wheel``.
``build-backend``
    identifiziert den Einstiegspunkt für das Build-Backend-Objekt als
    gepunkteten Pfad. Das Setuptools-Backend-Objekt ist unter
    ``setuptools.build_meta`` verfügbar.

``LICENSE``
~~~~~~~~~~~

Ausführliche Informationen hierzu findet ihr im Abschnitt :doc:`../licensing`.

``README.rst``
~~~~~~~~~~~~~~

Diese Datei teilt denjenigen, die sich für das Paket interessieren, in kurzer
Form mit, wie sie es nutzen können. Wenn ihr das Dokument in
:doc:`../documenting/rest` schreibt, könnt ihr die Inhalte auch als ausführliche
Beschreibung in euer Paket übernehmen:

.. literalinclude:: dataprep/setup.py
   :language: python
   :lines: 1,4-9,13-14,41

Zudem könnt ihr sie dann auch in eure :doc:`Sphinx-Dokumentation
<../documenting/start>` mit ``.. include:: ../../README.rst`` übernehmen.

``CHANGELOG.rst``
~~~~~~~~~~~~~~~~~

.. seealso::
   * `Keep a Changelog <https://keepachangelog.com>`_
   * `towncrier <https://pypi.org/project/towncrier/>`_

Build
-----

Wechselt in das Verzeichnis, in dem sich die ``setup.py``-Datei befindet.

.. code-block:: console

    $ pipenv install build
    $ cd /path/to/your/distribution_package
    $ rm -rf build dist
    $ pipenv run pyproject-build .

Die dritte Zeile stellt sicher, dass ein sauberes Build ohne Artefakte
früherer Builds erstellt wird. Die zweite Zeile baut ein ``sdist``-Archiv unter
Linux/Mac als gezippte Tar-Datei (``.tar.gz``) und unter Windows eine ZIP-Datei
sowie ein ``bdist_wheel``-Archiv  mit ``.whl`` im ``dist``-Verzeichnis.

Dieser Befehl sollte für unser Distribution Package die folgenden beiden Dateien
erzeugen::

    dist/
      dataprep-0.1.0-py3-none-any.whl
      dataprep-0.1.0.tar.gz

``sdist``
    mit ``dataprep-0.1.0.tar.gz`` wurden die Quelldateien (engl. *sources*) in
    einem Distributionspaket bereitgestellt.
``wheel``
    ist ein binäres Distributionsformat mit dem Suffix ``.whl``, wobei sich der
    Dateiname folgendermaßen zusammensetzt:

    ``dataprep``
        ist der normalisierte Paketname
    ``0.1.0``
        ist die Version des Distrubitionspakets
    ``py3``
        gibt die Python-Version und ggf. die C-`ABI
        <https://de.wikipedia.org/wiki/Bin%C3%A4rschnittstelle>` an
    ``none``, ``macosx_10_9``
        gibt an, ob das *Wheel*-Paket für jedes oder nur spezifische OS geeignet
        ist
    ``any``,  ``x86_64``
        ``any`` eignet sich für jede Prozessorarchitektur, ``x86_64`` hingegen
            nur für Chips mit dem x86-Befehlssatz und einer 64-Bit-Architektur

.. seealso::
    Die Referenz für die Dateinamen findet ihr in `File name convention
    <https://www.python.org/dev/peps/pep-0427/#file-name-convention>`_.

    Weitere Infos zu ``sdist`` erhaltet ihr in `Creating a Source Distribution
    <https://docs.python.org/2/distutils/sourcedist.html#creating-a-source-distribution>`_.
    und `PEP 376 <https://www.python.org/dev/peps/pep-0376/>`_.

Testen
------

.. code-block:: console

    $ pipenv --rm
    $ pipenv install dist/dataprep-0.1.0-py3-none-any.whl
    Processing ./dist/dataprep-0.1.0-py3-none-any.whl
    Collecting pandas
      Using cached pandas-1.3.4-cp39-cp39-macosx_10_9_x86_64.whl (11.6 MB)
    …
    Successfully installed dataprep-0.1.0 numpy-1.21.4 pandas-1.3.4 python-dateutil-2.8.2 pytz-2021.3 six-1.16.0

Anschließend könnt ihr das Wheel überprüfen mit:

.. code-block:: console

    $ pipenv install check-wheel-contents
    $ pipenv run check-wheel-contents dist/*.whl
    dist/dataprep-0.1.0-py3-none-any.whl: OK

Alternativ könnt ihr das Paket auch installieren:

.. code-block:: console

    $ pipenv install dist/dataprep-0.1.0-py3-none-any.whl
    Processing ./dist/dataprep-0.1-py3-none-any.whl
    Collecting pandas
    …
    Installing collected packages: numpy, pytz, six, python-dateutil, pandas, dataprep
    Successfully installed dataprep-0.1 numpy-1.21.4 pandas-1.3.4 python-dateutil-2.8.2 pytz-2021.3 six-1.16.0

Anschließend könnt ihr Python aufrufen und euer loaders-Modul importieren:

.. code-block:: python

    from dataprep import loaders

.. note::
    Beachtet bitte, dass es immer noch viele Anleitungen gibt, die einen Schritt
    zum Aufruf der ``setup.py`` enthalten, z.B. ``python setup.py sdist``. Dies
    wird jedoch heutzutage von Teilen der `Python Packaging Authority (PyPA)
    <https://github.com/pypa/>`_ als `Anti-Pattern
    <https://twitter.com/pganssle/status/1152695229105000453>`_ angesehen.

.. seealso::
   * `PyPI Release Checklist
     <https://cookiecutter-namespace-template.readthedocs.io/en/latest/pypi-release-checklist.html>`_
