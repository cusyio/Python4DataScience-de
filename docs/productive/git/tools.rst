Git-Tools für Notebooks
=======================

``nbdev2``
----------

`nbdev2 <https://nbdev.fast.ai>`_ bietet eine Reihe von Git-Hooks, die saubere
Git-Diffs bereitstellen, die meisten Git-Konflikte automatisch lösen und
sicherstellen, dass alle verbleibenden Konflikte vollständig innerhalb der
Standard-Jupyter-Notebook-Umgebung aufgelöst werden können. Um loszulegen, folgt
den Anweisungen in `Git-Friendly Jupyter
<https://nbdev.fast.ai/tutorials/git_friendly_jupyter.html>`_.

``nbdime``
----------

`nbdime <https://nbdime.readthedocs.io/>`_ ist ein GUI für `nbformat
<https://nbformat.readthedocs.io/>`_-Diffs und ersetzt `nbdiff
<https://github.com/tarmstrong/nbdiff>`_. Es versucht *Content-Aware*-Diffing
sowie das Merging von Notebooks, beschränkt sich nicht nur auf die Darstellung
von Diffs, sondern verhindert auch, dass unnötige Änderungen eingecheckt werden.

.. _nbstripout_label:

``nbstripout``
--------------

`nbstripout <https://github.com/kynan/nbstripout>`_ automatisiert *Clear all
outputs*. Es nutzt auch `nbformat <https://nbformat.readthedocs.io/>`_ und ein
paar Automagien um ``git config`` einzurichten. Meines Erachtens hat es jedoch
zwei Nachteile:

* es beschränkt sich auf den problematischen Metadaten-Abschnitt
* es ist langsam.
