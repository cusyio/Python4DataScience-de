.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Wertebereiche
=============

Die Überprüfung des Wertebereichs der Daten ist nichts Neues; fast jede
Datenvalidierung kann als solche Prüfung betrachtet werden. Neu ist bestenfalls
die automatisierte Festlegung dieser Wertebereiche. Wie beim maschinellen Lernen
wird mit Trainingsdaten begonnen, die dieselbe Struktur aufweisen wie die Daten,
mit denen wir später arbeiten wollen. Idealerweise wurden die Trainingsdaten
bereits überprüft und stellen korrekte Daten dar.

Wertebereiche können mithilfe der Funktion :func:`tdda.discover_df` aus
Trainingsdaten ermittelt werden, :abbr:`s. a. (siehe auch)`
:ref:`/clean-prep/libs-methods/tdda.ipynb#3.-erstellen-eines-constraints-objekt`.
Bei numerischen Feldern werden die Minimal- und Maximalwerte aus den
Trainingsdaten als Wertebereiche verwendet. Bei Texten versucht die Funktion,
:doc:`reguläre Ausdrücke <python-basics:types/strings/built-in-modules/regex>`
zu finden, also konsistente Muster, wie beispielsweise bei Telefonnummern,
Datums- und Zeitangaben, BIC und IBAN.

Manchen dieser Generatoren kann mitgeteilt werden, dass die Daten Ausreißer
enthalten können, die von den meisten Trainingsdaten abweichen. Andere
Generatoren können Beziehungen zwischen Feldern erkennen, wie :abbr:`z. B. (zum
Beispiel)` dass das Startdatum immer vor dem Enddatum liegen muss.

Typischerweise überprüfen und verfeinern wir die generierten Wertebereiche.
Ähnlich wie beim maschinellen Lernen kann es auch hier sinnvoll sein, die
Trainingsdaten in zwei oder mehr Gruppen aufzuteilen, wobei eine Gruppe für das
Training und die anderen für die Validierung verwendet werden. Dies ist
besonders nützlich, wenn die Menge der verfügbaren Trainingsdaten groß ist.
