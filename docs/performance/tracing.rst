.. SPDX-FileCopyrightText: 2026 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

cProfile/profiling.tracing
==========================

Üblicherweise wird in der Kommandozeile mit `cProfile
<https://docs.python.org/3.14/library/profile.html#module-cProfile>`_ oder ab
Python 3.15 mit :mod:`profiling.tracing` ein Profil erstellt, das anschließend
dessen Profilstatistiken anzeigt. Dies kann jedoch schnell sehr mühsam sein,
insbesondere beim Lesen umfangreicher Profile oder beim Sortieren der Daten.
Flexibler ist, die Profildaten stattdessen in einer Datei zu speichern, die dann
mit dem :mod:`pstats`-Modul gelesen werden kann:

#. :samp:`uv run python -m cProfile -o {PROFILE} ({SCRIPT} | {-m {MODULE})`
   führt `cProfile
   <https://docs.python.org/3.14/library/profile.html#module-cProfile>`_ zum
   Profilerstellung eures Script oder eures Moduls aus und speichert die
   Ergebnisse in einer Datei, die durch die Option ``-o`` angegeben wird.

#. :samp:`uv run python -m (cProfile | profiling.tracing) -o profile ({SCRIPT} |
   -m {MODULE}) <<< $'sort cumtime\nstats 100' | less` übergibt die folgenden
   beiden Befehle an das :mod:`pstats`-Modul, wobei die ``$``-Syntax verwendet
   wird.

   ``sort cumtime``
       sortiert die Ausgabe nach kumulativer Zeit, beginnend mit der größten.

       Um nach anderen Metriken zu sortieren, könnt ihr ``cumtime`` einfach
       durch einen Wert aus :meth:`pstats.Stats.sort_stats` ersetzen.

   ``stats 100``
       zeigt die ersten 100 Zeilen des Profils an.

   Die Ausgabe wird an ``less`` übergeben, sodass ihr euch die Ergebnisse
   anschauen könnt. Drückt :kbd:`q`, um den Vorgang zu beenden, wenn ihr fertig
   seid.

#. Vor und nach der Optimierung lassen sich einfach vergleichen, :abbr:`z. B.
   (zum Beispiel)` mit:

   .. code-block:: console

      $ uv run python -m cProfile -o before.profile main.py
      $ git switch -c main_optimisation
      ...
      $ uv run python -m cProfile -o after.profile main.py
