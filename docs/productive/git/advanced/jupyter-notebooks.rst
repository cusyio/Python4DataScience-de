.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Jupyter Notebooks unter Git
===========================

Probleme bei der Versionsverwaltung von Jupyter Notebooks
---------------------------------------------------------

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
  Remote lösen. Wenn :abbr:`z.B. (zum Beispiel)` ein :doc:`Merge-Request
  <gitlab/merge-requests>` eingereicht wird und dann jemand anderes dasselbe
  Notebook überträgt, bevor der Merge-Request zusammengeführt wird, könnte
  dieser einen Konflikt hervorrufen:

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

.. _nbstrip_jq:

``jq``
------

Im Notebook-Dateiformat :ref:`nbformat <was-ist-eine-ipynb-datei>` können auch
die Ergebnisse der Berechnungen gespeichert werden. Dies können auch
Base-64-codierte Blobs für Bilder und andere Binärdaten sein, die üblicherweise
nicht in eine Versionsverwaltung übernommen werden sollen. Diese können zwar
manuell entfernt werden mit :menuselection:`Cell --> All Output --> Clear`, ihr
müsst diese Schritte jedoch vor jedem ``git add`` ausführen, und es löst auch
eine zweite Ursache für das Rauschen in ``git diff`` nicht, nämlich dasjenige
in den `Metadaten
<https://nbformat.readthedocs.io/en/latest/format_description.html#metadata>`_.

Um nun systematisch vergleichbare Versionen von Notebooks in der
Versionsverwaltung zu erhalten, können wir `jq
<https://stedolan.github.io/jq/>`_ verwenden, einen leichtgewichtigen
JSON-Prozessor. Zwar benötigt man einige Zeit um ``jq`` einzurichten da es
eine eigene Abfrage-/Filtersprache mitbringt, aber meist sind
schon die Standardeinstellungen gut gewählt.

Installation
~~~~~~~~~~~~

``jq`` kann installiert werden mit:

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install jq

.. tab:: macOS

   .. code-block:: console

      $ brew install jq

Beispiel
~~~~~~~~

Ein typischer Aufruf ist:

.. code-block:: console

   jq --indent 1  \
     '(.cells [] | select (has ("output")) | .outputs) = []
     | (.cells [] | select (has ("execution_count")) | .execution_count) = null
     | .metadata = {"language_info": {"name": "python", "pygments_lexer": "ipython3"}}
     | .Cells []. Metadaten = {}
     '  example.ipynb

Jede Zeile innerhalb der einfachen Anführungszeichen definiert einen Filter –
die erste wählt alle Einträge aus der Liste *cells* aus und löscht die Ausgaben.
Der nächste Eintrag setzt alle Ausgaben zurück. Der dritte Schritt löscht die
Metadaten des Notebooks und ersetzt sie durch ein Minimum an erforderlichen
Informationen, damit das Notebook noch ohne Beanstandungen ausgeführt werden
kann, folgendes eingeben:wenn es mit nbsphinx formatiert sind. Die vierte Filterzeile,
``.cells []. metadata = {}``, löscht alle Metainformationen. Falls ihr bestimmte
Metainformationen beibehalten wollt, könnt ihr dies hier angeben.

Einrichten
~~~~~~~~~~

#. Um euch die Arbeit zu erleichtern, könnt ihr einen Alias in der
   ``~/.bashrc``-Datei anlegen:

   .. code-block:: console

    alias nbstrip_jq="jq --indent 1 \
        '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
        | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
        | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
        | .cells[].metadata = {} \
        '"

#. Anschließend könnt ihr bequem im Terminal folgendes eingeben:

   .. code-block:: console

    $ nbstrip_jq example.ipynb > stripped.ipynb

#. Wenn ihr von einem bereits vorhandenen Notebook ausgeht, solltet ihr zunächst
   einen ``filter``-Commit hinzufügen, indem ihr einfach die neu gefilterte
   Version eures Notebooks ohne die unerwünschten Metadaten einlest. Nachdem ihr
   mit ``git add`` das Notebook hinzugefügt habt, könnt ihr mit
   ``git diff --cached`` schauen, ob der Filter auch wirklich gewirkt hat bevor
   ihr dann ``git commit -m 'filter'`` angebt.

#. Wenn ihr diesen Filter für alle Git-Repositories verwenden wollt, könnt ihr
   euer Git auch global konfigurieren:

   #. Zunächst fügt ihr in :file:`~/.config/git/config` folgendes hinzu:

      .. code-block:: console

         [core]
         attributesfile = ~/.config/git/attributes

         [filter "nbstrip_jq"]
         clean = "jq --indent 1 \
                 '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
                 | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
                 | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
                 | .cells[].metadata = {} \
                 '"
         smudge = cat
         required = true

      ``clean``
          wird beim Hinzufügen von Änderungen in den Bühnenbereich angewendet.
      ``smudge``
          wird beim Zurücksetzen des Arbeitsbereichs durch Änderungen aus dem
          Bühnenbereich angewendet.

   #. Anschließend müsst ihr in :file:`~/.config/git/attributes` nur noch
      folgendes angeben:

      .. code-block:: ini

         *.ipynb filter=nbstrip_jq


#. Wenn ihr anschließend mit ``git add`` euer Notebook in den Bühnenbereich
   übernehmt, wird der ``nbstrip_jq``-Filter angewendet.

   .. note::
      ``git diff`` zeigt euch jedoch keine Änderungen zwischen Arbeits- und
      Bühnenbereich an. Lediglich mit ``git diff --staged`` könnt ihr erkennen,
      dass nur die gefilterten Änderungen übernommen wurden.

   .. warning::
      ``clean`` und ``smudge``-Filter spielen oft nicht gut mit ``git rebase``
      über solche gefilterten Commits hinweg zusammen. Dann solltet ihr vor dem
      Rebase diese Filter deaktivieren.

#. Und es gibt noch ein weiteres Problem: Wenn ein solches Notebook erneut
   ausgeführt wird, zeigt zwar ``git diff`` keine Änderungen an, ``git status``
   jedoch schon. Daher sollte in der ``~/.bashrc``-Datei folgendes eingetragen
   sein um schnell das jeweilige Arbeitsverzeichnis reinigen zu können:

   .. code-block:: bash

    function nbstrip_all_cwd {
        for nbfile in *.ipynb; do
            echo "$( nbstrip_jq $nbfile )" > $nbfile
        done
        unset nbfile
    }

ReviewNB
--------

`ReviewNB <https://www.reviewnb.com>`_ löst das Problem,
:doc:`gitlab/merge-requests` mit Notebooks durchzuführen. Die Code-Review-GUI
von GitLab funktioniert nur bei zeilenbasierten Dateiformaten, wie :abbr:`z.B.
(zum Beispiel)` Python-Skripten. Meistens bevorzuge ich jedoch, die
Quelltext-Notebooks zu prüfen, weil:

* ich die Dokumentation und die Tests überprüfen möchte, nicht nur die
  Implementierung
* ich die Änderungen an den Zellausgaben sehen möchte, wie Diagrammen und
  Tabellen, nicht nur den Code.

Für diesen Zweck ist ReviewNB perfekt.

``nbdime``
----------

`nbdime <https://nbdime.readthedocs.io/en/latest/>`_ ist ein GUI für `nbformat
<https://nbformat.readthedocs.io/en/latest/>`_-Diffs und ersetzt `nbdiff
<https://github.com/tarmstrong/nbdiff>`_. Es versucht lokal
*Content-Aware*-Diffing sowie das Merging von Notebooks, beschränkt sich nicht
nur auf die Darstellung von Diffs, sondern verhindert auch, dass unnötige
Änderungen eingecheckt werden. Es ist jedoch nicht kompatibel mit ``nbdev2``.

.. _nbstripout_label:

``nbstripout``
--------------

`nbstripout <https://github.com/kynan/nbstripout>`_ automatisiert *Clear all
outputs*. Es nutzt auch `nbformat <https://nbformat.readthedocs.io/en/latest/>`_
und ein paar Automagien um ``git config`` einzurichten. Meines Erachtens hat es
jedoch zwei Nachteile:

* es beschränkt sich auf den problematischen Metadaten-Abschnitt
* es ist langsam.
