NumPy
=====

`NumPy <https://numpy.org/>`_ ist die Abkürzung für numerisches Python. Viele
Python-Pakete, die wissenschaftliche Funktionen bereitstellen, verwenden die
Array-Objekte von NumPy als eine der Standardschnittstellen für den
Datenaustausch. Im folgenden möchte ich einen kurzen Überblick über den
wesentlichen Funktionsumfang von NumPy geben:

* :doc:`ndarray <ndarray>`, ein effizientes mehrdimensionales Array, das
  schnelle Array-basierte Operationen bietet, wie das Mischen und Bereinigen von
  Daten, Untergruppenbildung und Filterung, Transformation und alle anderen
  Arten von Berechnungen. Zudem gibt es flexible Funktionen für das
  Broadcasting, also von Auswertungen unterschiedlich großer Arrays.
* Mathematische Funktionen für schnelle Operationen auf ganzen Arrays von Daten,
  wie Sortieren, Eindeutigkeit und Mengenoperationen. Dabei werden die
  Ausdrücke, anstelle von Schleifen mit ``if``-``elif``-``else``-Verzweigungen,
  in bedingter Logik geschrieben.
* Werkzeuge zum Lesen und Schreiben von Array-Daten auf die Festplatte und zur
  Arbeit mit `Memory-Mapped
  <https://de.wikipedia.org/wiki/Memory_Mapped_I/O>`_-Dateien.
* Funktionen für Lineare Algebra, Zufallszahlengenerierung und
  Fourier-Transformation.
* Eine C-API für die Verbindung von NumPy mit Bibliotheken, die in C, C++ oder
  FORTRAN geschrieben sind.

.. note::

    Dieser Avschnitt führt euch in die Grundlagen der Verwendung von
    NumPy-Arrays ein und sollte ausreichen, um dem Rest des Tutorials zu folgen.
    Für viele datenanalytische Anwendungen ist es zwar nicht notwendig, ein
    tiefes Verständnis von NumPy zu haben, aber die Beherrschung der
    array-orientierten Programmierung und Denkweise ist ein wichtiger Schritt
    auf dem Weg zum Data-Scientist.

.. seealso::
    * `Home
      <https://numpy.org/>`_
    * `Docs
      <https://numpy.org/doc/stable/>`_
    * `GitHub
      <https://github.com/numpy/numpy>`_
    * `Tutorials
      <https://numpy.org/numpy-tutorials/>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    intro.ipynb
    ndarray.ipynb
    dtype.ipynb
    arithmetic.ipynb
    indexing-slicing.ipynb
    transpose.ipynb
    where.ipynb