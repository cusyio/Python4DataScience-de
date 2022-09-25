Rollen, Gruppen und Berechtigungen
==================================

Je nach der Rolle, die eine Person in einer bestimmten Gruppe oder einem Projekt
innehat, verfügt sie über unterschiedliche Berechtigungen. Wenn sie sowohl in
einer Projektgruppe als auch im Projekt ist, wird die höchste Rolle verwendet.

.. seealso::
   * `Permissions and roles <https://docs.gitlab.com/ee/user/permissions.html>`_

Mitglieder eines Projekts
-------------------------

Mitglieder sind die Personen und Gruppen, die Zugang zu eurem Projekt haben.
Jedes Mitglied erhält eine Rolle, die bestimmt, was es im Projekt tun kann.
Projektmitglieder können:

* direkte Mitglieder des Projekts sein
* die Mitgliedschaft im Projekt von der Projektgruppe erben
* Mitglied einer Gruppe sein, die mit dem Projekt geteilt wurde
* Mitglied einer Gruppe sein, die mit der Gruppe des Projekts geteilt wurde

Berechtigungen in GitLab
------------------------

Gäste
    sind keine aktiven Mitwirkenden in privaten Projekten; sie können nur sehen
    und Kommentare und Issues hinterlassen.
Reporter*innen
    nehmen lesend teil. sie können nicht in das Repository schreiben, aber sie
    können an Issues mitarbeiten.
Entwickler*innen
    wirken direkt mit und haben Zugang zu allem, um von der Idee bis zur
    Produktion, es sei denn, etwas wurde ausdrücklich eingeschränkt, :abbr:`z.B.
    (zum Beispiel)` durch den Schutz von Zweigen.
Maintainer
    können zu ``main`` pushen und den Code in die ``production``-Umgebung
    überführen.
Eigentümer*innen
    administrieren im Wesentlichen die Gruppen und Workflows. Sie können Zugang
    zu Gruppen gewähren und dürfen löschen.

Geschützte Zweige
-----------------

In GitLab werden Berechtigungen grundsätzlich so definiert, dass Lese- oder
Schreibrechte für das Repository und die Zweige vergeben werden. Um bestimmten
Zweigen weitere Einschränkungen aufzuerlegen, können sie geschützt werden. Der
Standardzweig für euer Projektarchiv ist standardmäßig geschützt. Wenn ein Zweig
geschützt ist, werden standardmäßig üblicherweise die folgenden Einschränkungen
für den Zweig erzwungen:

+---------------------------------------+---------------------------------------+
| Aktion                                | Rolle                                 |
+=======================================+=======================================+
| Einen Zweig schützen                  | Maintainer                            |
+---------------------------------------+---------------------------------------+
| Push in diesen Zweig                  | GitLab-Admins und alle, denen dies    |
|                                       | explizit erlaubt wurde.               |
+---------------------------------------+---------------------------------------+
| Force push in diesen Zweig            | Niemand                               |
+---------------------------------------+---------------------------------------+
| Löschen der Verzweigung               | Mit einem Git-Kommando niemand;       |
|                                       | mit GitLab-UI oder API zumindest      |
|                                       | Maintainer                            |
+---------------------------------------+---------------------------------------+

.. seealso::
   * `Protected branches
     <https://docs.gitlab.com/ee/user/project/protected_branches.html>`_
   * `Pipeline security on protected branches
     <https://docs.gitlab.com/ee/ci/pipelines/index.html#pipeline-security-on-protected-branches>`_

Geschützte Zweige konfigurieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Voraussetzung ist, dass ihr mindestens die *Maintainer*-Rolle habt.

#. Wählt in der oberen Leiste :menuselection:`Menü --> Projekte` und sucht euer
   Projekt.
#. Wählt in der linken Seitenleiste :menuselection:`Einstellungen -->
   Repository`.
#. Erweitert * Protected branches*.
#. Wählt in der Dropdown-Liste :menuselection:`Protect branch…` den Zweig aus,
   den ihr schützen möchtet. Alternativ könnt ihr auch Wildcards verwenden:

   +-----------------------+-----------------------------------------------+
   | Wildcard              | Beispiele                                     |
   +=======================+===============================================+
   | ``*-stage``           | ``#17-some-feature-stage``,                   |
   |                       | ``#42-other-feature-stage``                   |
   +-----------------------+-----------------------------------------------+
   | ``production/*``      | ``production/app-server``,                    |
   |                       | ``production/load-balancer``                  |
   +-----------------------+-----------------------------------------------+
   | ``*app-server*``      | ``app-server``,                               |
   |                       | ``production/app-server``                     |
   +-----------------------+-----------------------------------------------+

#. Wählt in der Dropdown-Liste :menuselection:`Allowed to merge:` eine Rolle aus,
   die in diesen Zweig zusammenführen darf.
#. Wählt in der Dropdown-Liste :menuselection:`Allowed to push:` eine Rolle aus,
   der in diesen Zweig pushen darf.
#. Wählt :menuselection:`Schützen`.
#. Der geschützte Zweig wird nun in der Liste der geschützten Zweige angezeigt.
