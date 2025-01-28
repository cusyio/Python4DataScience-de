Git für Binärdateien
====================

``git diff`` lässt sich konfigurieren, sodass es auch bei Binärdateien sinnvolle
Diffs anzeigen kann.

… für Excel-Dateien
-------------------

Hierfür benötigen wir `openpyxl <https://openpyxl.readthedocs.io/en/stable/>`_
und `pandas <https://pandas.pydata.org>`_:

.. code-block:: console

    $ uv add openpyxl pandas

Anschließend können wir in :file:`exceltocsv.py`
:doc:`pandas:reference/api/pandas.DataFrame.to_csv` zum Konvertieren der
Excel-Dateien verwenden:

.. literalinclude:: exceltocsv.py
   :caption: exceltocsv.py
   :name: exceltocsv.py
   :language: python
   :lines: 5-

Nun fügt ihr noch in der globalen Git-Konfiguration in der Datei
:file:`~/.config/git/config` den folgenden Abschnitt hinzu:

.. code-block:: ini

    [diff "excel"]
        textconv=python3 /PATH/TO/exceltocsv.py
        binary=true

Schließlich wird in der globalen :file:`~/.config/git/attributes`-Datei unser
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

Anschließend fügt ihr den folgenden Abschnitt der globalen Git-Konfiguration in
der Datei :file:`~/.config/git/config` hinzu:

.. code-block:: ini

    [diff "pdf"]
        textconv=pdftohtml -stdout

Schließlich wird in der globalen :file:`~/.config/git/attributes`-Datei unser
``pdf``-Konverter mit :file:`*.pdf`-Dateien verknüpft:

.. code-block:: ini

    *.pdf diff=pdf

Nun wird beim Aufruf von ``git diff`` die PDF-Datei zunächst konvertiert und
dann ein Diff über den Ausgaben des Konverters durchgeführt.

… für Dokumente
---------------

Auch Unterschiede in Dokumenten lassen sich anzeigen. Hierfür kann `Pandoc
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

Anschließend wird der globalen Git-Konfiguration :file:`~/.config/git/config`
folgender Abschnitt hinzugefügt:

.. code-block:: ini

   [diff "pandoc-to-markdown"]
       textconv = pandoc --to markdown
       cachetextconv = true

Schließlich wird in der globalen :file:`~/.config/git/attributes`-Datei unser
``pandoc-to-markdown``-Konverter mit :file:`*.docx`, :file:`*.odt` und
:file:`*.rtf`-Dateien verknüpft:

.. code-block:: ini

   *.docx diff=pandoc-to-markdown
   *.odt diff=pandoc-to-markdown
   *.rtf diff=pandoc-to-markdown

.. tip::
   :doc:`Jupyter Notebooks <jupyter-tutorial:notebook/index>` schreiben in eine
   JSON-Datei :ref:`*.ipynb <jupyter-tutorial:was-ist-eine-ipynb-datei>`, die
   ziemlich dicht und insbesondere bei Diffs schwer zu lesen ist. Die
   Markdown-Darstellung von Pandoc vereinfact dies:

   .. code-block:: ini

      *.ipynb diff=pandoc-to-markdown

Die gleiche Vorgehensweise kann auch angewandt werden, um nützliche Diffs von
anderen Binärdateien zu erhalten, :abbr:`z.B. (zum Beispiel)` ``*.zip``,
``*.jar`` und andere Archive mit ``unzip`` oder für Änderungen in den
Metainformationen von Bildern mit ``exiv2``. Zudem gibt es
Konvertierungswerkzeuge für die Umwandlung von :file:`*.odt`, :file:`*.doc` und
anderen Dokumentenformaten in einfachen Text. Für Binärdateien, für die es
keinen Konverter gibt, reichen oft auch Strings aus.

.. _exiftool:

… für Medien-Dateien
--------------------

`ExifTool <https://exiftool.org>`_ kann verwendet werden um die Metadaten der
Medien-Dateien in Text zu konvertieren.

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install libimage-exiftool-perl

.. tab:: macOS

   .. code-block:: console

      $ brew install exiftool

.. tab:: Windows

   .. code-block:: ps1

      > choco install exiftool

.. seealso::
   * `Installing ExifTool <https://exiftool.org/install.html>`_

Anschließend könnt ihr in der globalen Git-Konfigurationsdatei
:file:`~/.config/git/config` folgenden Abschnitt hinzufügen:

.. code-block:: ini

   [diff "exiftool"]
   textconv = exiftool --composite -x 'Exiftool:*'
   cachetextconv = true
   xfuncname =
   "^-.*$"

Schließlich wird in der :file:`~/.config/git/attributes` der
``exiftool``-Konverter mit Datei-Endungen von Medien-Dateien verknüpft:

.. code-block:: ini

   *.avif diff=exiftool
   *.bmp diff=exiftool
   *.gif diff=exiftool
   *.jpeg diff=exiftool
   *.jpg diff=exiftool
   *.png diff=exiftool
   *.webp diff=exiftool

.. seealso::
   ``exiftool`` kann noch viele weitere Medien-Dateien verarbeiten. Eine
   vollständige Liste erhaltet ihr in `Supported File Types
   <https://exiftool.org/#supported>`_.
