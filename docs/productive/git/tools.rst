Git-Tools für Notebooks
=======================

Es gibt mehrere Probleme, um Jupyter Notebooks mit Git zu verwalten:

* Die Metadaten von Zellen der Jupyter Notebooks ändern sich auch, wenn keine
  inhaltlichen Änderungen an den Zellen vorgenommen wurden. Damit werden
  Git-Diffs unnötig kompliziert.
* Die Zeilen, die Git bei :ref:`Merge-Konflikten <merge-conflicts>` in die
  ``*.ipynb``-Dateien schreibt, führen dazu, dass die Notebooks nicht mehr
  gültiges JSON sind und von Jupyter deswegen nicht geöffnet werden kann: ihr
  erhaltet dann beim Öffnen die Fehlermeldung *Error loading notebook*.

  Konflikte treten besonders häufig in Notebooks auf, da Jupyter bei jeder
  Ausführung eines Notizbuchs Folgendes ändert:

  * Jede Zelle enthält eine Nummer, die angibt, in welcher Reihenfolge sie
    ausgeführt wurde. Wenn Team-Mitglieder die Zellen in unterschiedlicher
    Reihenfolge ausführen, hat jede einzelne Zelle einen Konflikt! Dies manuell
    zu beheben, würde sehr lange dauern.
  * Für jede Abbildung, :abbr:`z.B. (zum Beispiel)` einen Plot, nimmt Jupyter
    nicht nur das Bild selbst in das Notizbuch auf, sondern auch eine einfache
    Textbeschreibung, die die ID des Objekts enthält, :abbr:`z.B. (zum
    Beispiel)`
    :samp:`{<matplotlib.axes._subplots.AxesSubplot at 0x7fbc113dbe90>}`. Dies
    ändert sich jedes Mal, wenn ihr ein Notizbuch ausführt, und führt daher
    jedes Mal zu einem Konflikt, wenn zwei Personen diese Zelle ausführen.
  * Einige Ausgaben können nicht-deterministisch sein, :abbr:`z.B. (zum
    Beispiel)` ein Notebook, das Zufallszahlen verwendet oder mit einem Dienst
    interagiert, der im Laufe der Zeit unterschiedliche Ausgaben liefert.
  * Jupyter fügt dem Notizbuch Metadaten hinzu, die die Umgebung beschreiben, in
    der es zuletzt ausgeführt wurde, wie :abbr:`z.B. (zum Beispiel)` den Namen
    des Kernels. Dies variiert oft zwischen verschiedenen Installationen, und
    daher werden zwei Personen, die ein Notizbuch speichern (auch ohne andere
    Änderungen), oft einen Konflikt in den Metadaten haben.

``nbdev2``
----------

`nbdev2 <https://nbdev.fast.ai>`_ bietet eine Reihe von Git-Hooks, die saubere
Git-Diffs bereitstellen, die die meisten Git-Konflikte automatisch lösen und
sicherstellen, dass alle verbleibenden Konflikte vollständig innerhalb der
Standard-Jupyter-Notebook-Umgebung aufgelöst werden können:

* Ein neuer ``git merge``-Treiber bietet *notebook-native* Konfliktmarkierungen,
  die dazu führen, dass Notebooks direkt in Jupyter geöffnet werden können, auch
  wenn es Git-Konflikte gibt. Lokale und entfernte Änderung werden jeweils als
  separate Zellen im Notizbuch angezeigt, so dass ihr die Version, die ihr nicht
  behalten möchtet, einfach löschen oder die beiden Zellen nach Bedarf
  kombinieren könnt.

  .. seealso::
     `nbdev.merge docs <https://nbdev.fast.ai/api/merge.html>`_

* Git-Merges lokal zu lösen ist äußerst hilfreich, aber wir müssen sie auch
  Remote lösen. Wenn :abbr:`z.B. (zum Beispiel)` eine Pull-Anfrage (PR)
  eingereicht wird und dann jemand anderes dasselbe Notebook überträgt, bevor
  der Merge Request zusammengeführt wird, könnte dieser einen Konflikt
  hervorrufen:

  .. code-block:: javascript

        "outputs": [
         {
     <<<<<< HEAD
          "execution_count": 8,
     ======
          "execution_count": 5,
     >>>>>> 83e94d58314ea43ccd136e6d53b8989ccf9aab1b
          "metadata": {},

  Der *save hook* von nbdev2 entfernt automatisch alle unnötigen Metadaten
  (einschließlich :samp:`execution_count`) und nicht-deterministischen
  Zellausgaben; :abbr:`d.h. (das heißt)`, dass es keine sinnlosen Konflikte wie
  den obigen gibt, da diese Informationen gar nicht erst in den Commits
  gespeichert werden.

Um loszulegen, folgt den Anweisungen in `Git-Friendly Jupyter
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
