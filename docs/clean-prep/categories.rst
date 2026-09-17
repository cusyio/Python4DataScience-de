.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Kategorien der Datenqualität
============================

Es gibt verschiedene Möglichkeiten, Datenqualitätsprobleme zu kategorisieren –
nach der Ursache des Problems, nach seinen wahrscheinlichen oder potenziellen
Auswirkungen, nach der Art des Datenelements, nach der Ebene einer
Datenhierarchie, auf der der Fehler oder Inkonsistenz sichtbar werden, um nur
einige zu nennen. In diesem Tutorial erfolgt die Kategorisierung im Allgemeinen
implizit, und wir konzentrieren uns auf die Methoden zur Erkennung von Problemen
sowie auf die dafür geeigneten Werkzeuge. Es ist jedoch sinnvoll, zumindest
allgemein auf andere Möglichkeiten der Kategorisierung von Datenproblemen
einzugehen, bevor wir uns mit der Erkennung befassen.

Unmögliche Daten
    wie :abbr:`z. B. (zum Beispiel)` Temperaturen unterhalb des absoluten
    Nullpunkts (0 Kelvin oder −273,15 °C) oder unsinnige Datums- und Zeitangaben
    – in Python können diese zwar nicht im :class:`datetime`-Datentyp auftreten,
    jedoch in :doc:`../data-processing/serialisation-formats/json/index` und
    :doc:`SQLite <python-basics:save-data/sqlite/index>`, in denen meist
    Textfelder zur Speicherung von Datumsangaben verwendet werden.
Sonderwerte
    Der `IEEE-754 <https://de.wikipedia.org/wiki/IEEE_754>`_-Standard zur
    Darstellung von Gleitkommazahlen enthält auch Sonderwerte für positive und
    negative Unendlichkeit (+∞, −∞) sowie *Not-a-Number* -Werte (``NaN``).
Unspezifizierte Werte
    Werte, die einem bestimmten Format entsprechen, können dennoch ungültig
    sein, wie :abbr:`z. B. (zum Beispiel)` E-Mail-Adressen.
Inkonsistenzen
    Gruppen verwandter Feldwerte für jeden Datensatz können sich einschränken.
    Um solche Inkonsistenzen zu vermeiden, empfiehlt das :abbr:`DRY (Don’t
    Repeat Yourself)`-Prinzip, berechenbare Werte zu vernachlässigen. Prüfsummen
    sind jedoch das genaue Gegenteil davon.

    *„Single Source of Truth“* ist ein Beispiel für Datenbanknormalisierung und
    vereinfacht Aktualisierungen; mit denormalisierten Datenspeichern können
    hingegen  wVerknüpfungen und Berechnungen während der Datenanalyse vermieden
    werden.

Anomalien und Data-Drift
    Die bisherigen Überprüfungen erlaubten, Daten ungültig erklären zu können.
    Anomalien und Data-Drift lassen diesen Schluss jedoch nicht zwingend zu und
    erlauben daher nur selten eine automatisierte Bereinigung der Daten.
Malware
    Weder alle Eingabe- noch Ausgabedaten sollen in Analysesystemen verarbeitet
    werden.

    .. figure:: exploits_of_a_mom_2x.png
       :alt: Hi, this is your son’s school. We’re having some  computer trouble.
             Oh, dear - did he break something? In a way –
             Did you really name your son Robert'); DROP TABLE Students; -- ?
             Oh, yes. Little bobby tables, we call him.
             Well, weve lost this year’s student records. I hope you’re happy.
             And I hope, youe’ve learned to sanitize your database inpots.
       :target: https://xkcd.com/327/

       Exploits of a Mom

    Ein offensichtliches Beispiel für versehentlich offengelegte Ausgabedaten
    sind :abbr:`z. B. (zum Beispiel)` aus fortlaufenden Personenkennziffern
    generierte URLs mit personenbezogenen Daten.
