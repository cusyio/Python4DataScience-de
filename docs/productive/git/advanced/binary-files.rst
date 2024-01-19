
Git für Binärdateien
====================

``git diff`` lässt sich konfigurieren, sodass es auch bei Binärdateien sinnvolle
Diffs anzeigen kann.

… für Excel-Dateien
-------------------

Hierfür benötigen wir `openpyxl <https://openpyxl.readthedocs.io/en/stable/>`_
und `pandas <https://pandas.pydata.org>`_:

.. code-block:: console

    $ pipenv install openpyxl pandas

Anschließend können wir in :file:`exceltocsv.py`
:doc:`pandas:reference/api/pandas.DataFrame.to_csv` zum Konvertieren der
Excel-Dateien verwenden:

.. literalinclude:: exceltocsv.py
   :caption: exceltocsv.py
   :name: exceltocsv.py
   :language: python
   :lines: 5-

Nun fügt ihr noch in der globalen Git-Konfiguration in der Datei :file:`~/.gitconfig`
den folgenden Abschnitt hinzu:

.. code-block:: ini

    [diff "excel"]
        textconv=python3 /PATH/TO/exceltocsv.py
        binary=true

Schließlich wird in der globalen :file:`~/.gitattributes`-Datei unser
``excel``-Konverter mit :file:`*.xlsx`-Dateien verknüpft:

.. code-block:: ini

    *.xlsx diff=excel

… für PDF-Dateien
-----------------

Hierfür wird zusätzlich ``pdftohtml`` benötigt. Ihr installiert es mit

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install poppler-utils

.. tab:: macOS

   .. code-block:: console

      $ brew install pdftohtml

Anschließend fügt ihr den folgenden Abschnitt der globalen Git-Konfiguration in der
Datei :file:`~/.gitconfig` hinzu:

.. code-block:: ini

    [diff "pdf"]
        textconv=pdftohtml -stdout

Schließlich wird in der globalen :file:`~/.gitattributes`-Datei unser
``pdf``-Konverter mit :file:`*.pdf`-Dateien verknüpft:

.. code-block:: ini

    *.pdf diff=pdf

Nun wird beim Aufruf von ``git diff`` die PDF-Datei zunächst konvertiert und
dann ein Diff über den Ausgaben des Konverters durchgeführt.

… für Word-Dokumente
--------------------

Auch Unterschiede in Word-Dokumenten lassen sich anzeigen. Hierfür kann `Pandoc
<https://pandoc.org/>`_ verwendet werden, das einfach installiert werden kann
mit

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install pandoc

.. tab:: macOS

   .. code-block:: console

      $ brew install pandoc

.. tab:: Windows

   Herunterladen und Installieren der aktuellen :file:`.msi`-Datei von `GitHub
   <https://github.com/jgm/pandoc/releases/>`_.

Anschließend wird der globalen Git-Konfiguration :file:`~/.gitconfig` folgender
Abschnitt hinzugefügt:

.. code-block:: ini

   [diff "word"]
           textconv=pandoc --to=markdown
           binary=true
           prompt=false

Schließlich wird in der globalen :file:`~/.gitattributes`-Datei unser
``word``-Konverter mit :file:`*.docx`-Dateien verknüpft:

.. code-block:: ini

   *.docx diff=word

Die gleiche Vorgehensweise kann auch angewandt werden, um nützliche Diffs von
anderen Binärdateien zu erhalten, :abbr:`z.B. (zum Beispiel)` ``*.zip``,
``*.jar`` und andere Archive mit ``unzip`` oder für Änderungen in den
Metainformationen von Bildern mit ``exiv2``. Zudem gibt es
Konvertierungswerkzeuge für die Umwandlung von :file:`*.odt`, :file:`*.doc` und
anderen Dokumentenformaten in einfachen Text. Für Binärdateien, für die es
keinen Konverter gibt, reichen oft auch Strings aus.
