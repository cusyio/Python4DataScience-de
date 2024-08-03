.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Repos aufteilen und zusammenführen
==================================

Repos aufteilen
---------------

Häufig ist es sinnvoll, ein großes Git-Repository in mehrere kleinere
aufzuteilen. Das kann in einem Projekt nötig sein, das stark angewachsen ist,
oder wenn wir ein Teilprojekt als eigenständiges Repo auslagern möchten.
Natürlich könnten wir einfach ein neues Repository erstellen und die Dateien für
das Teilprojekt hineinkopieren. Allerdings würden wir dabei die gesamte
Versionsgeschichte verlieren.

Hier beschreibe ich, wie ihr ein Git-Repository aufteilen könnt, ohne die
jeweils zugehörige Historie zu verlieren.

Szenario und Ziele
~~~~~~~~~~~~~~~~~~

Wir wollen aus dem Jupyter-Tutorial-Repository denjenigen Teil herauslösen, der
sich mit der Visualisierung der Daten befasst: ``docs/viz/``. Die
Herausforderung besteht darin, dass die Historie für das
``docs/viz/``-Verzeichnis mit anderen Änderungen vermischt ist. Daher klonen wir
zunächst zweimal dasselbe Repository:

.. code-block:: console

    $ git clone git@github.com:veit/jupyter-tutorial.git
    Klone nach 'jupyter-tutorial'...
    $ git clone git@github.com:veit/jupyter-tutorial.git pyviz-tutorial
    Klone nach 'pyviz-tutorial' ...

Der nächste Schritt besteht darin, die unerwünschten Historien aus jedem der
beiden Repos herauszufiltern. Um die Historie umzuschreiben und nur diejenigen
Commits zu behalten, die tatsächlich dein Inhalt eines bestimmten Unterordners
betreffen, verwenden wir `git-filter-repo
<https://github.com/newren/git-filter-repo>`_:

.. code-block:: console

    $ curl https://raw.githubusercontent.com/newren/git-filter-repo/main/git-filter-repo -o git-filter-repo
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  161k  100  161k    0     0   578k      0 --:--:-- --:--:-- --:--:--  584k

    $ cd pyviz-tutorial
    $ python3 ../git-filter-repo --path docs/viz

Das Einzige, was jetzt noch zu tun ist, ist die Anpassung der Remote-URL:

.. code-block:: console

    $ git remote add origin git@github.com:veit/pyviz-tutorial.git
    $ git push -u origin main

Für unser Jupyter-Tutorial-Repository invertieren wir jetzt den ausgewählten
Pfad:

.. code-block::

    $ cd jupyter-tutorial
    $ python3 ../git-filter-repo --invert-paths --path docs/viz
    $ git remote add origin git@github.com:veit/jupyter-tutorial.git
    $ git push -f -u origin main

Repos zusammenführen
--------------------

Repos mit unterschiedlicher Historie können auch zusammengeführt werden. Dies
kann :abbr:`z.B. (zum Beispiel)` wünschenswert sein, wenn ein Projekt lokal
begonnen wurde, auf dem Git-Server jedoch ein Projekt mit einem initialen Commit
angelegt wurde. In diesem Fall könnt ihr dann einfach ``git pull
--allow-unrelated-histories`` verwenden; dabei wird dann die Option an das
darunterliegende ``git merge`` weitergereicht.

Wollt ihr zwei größere Projekte zusammenführen, könnt ihr dies folgendermaßen:

.. code-block:: console

    $ git remote add -f pyviz git@github.com:veit/pyviz-tutorial.git docs/viz/
    $ git merge -s ours --no-commit --allow-unrelated-histories pyviz/main
    $ git read-tree --prefix=docs/pyviz -u pyviz/main
    $ git commit -m "Merge pyviz tutorial as subdirectory"
    $ git push

.. seealso::
   `merge-options
   <https://git-scm.com/docs/merge-options#Documentation/merge-options.txt---allow-unrelated-histories>`_
