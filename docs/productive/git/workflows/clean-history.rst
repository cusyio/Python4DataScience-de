Commits für ein sauberes Log ändern
===================================

Mit ``git commit --fixup`` und ``git rebase --autosquash`` könnt ihr relativ
einfach eine Reihe von Commits korrigieren. Um dies an einem Beispiel zu
demonstrieren, stelle ich euch folgendes Szenario vor:

#. Wir haben in unserem ``my-feature``-Branch zwei Commits: den einen für die
   eigentliche Funktion, den anderen für die zugehörigen Tests:

   .. code-block:: console

      $ git log --oneline my-feature ^origin/main
      a4587fa (my-feature) Add test for my new feature
      56e34e9 Add new feature

#. Beim *Merge-* oder *Pull-Request* erhalten wir sowohl zu unserer Funktion wie
   auch zu unseren Tests Feedback, das wir gerne in unsere bestehenden Commits
   integrieren würden. Hierfür erstellen wir nun zunächst temporäre Commits:

   .. code-block:: console

      $ git commit -m "Feedback on the tests from my function"
      $ git commit -m "Feedback on my function"
      $ git log --oneline my-feature ^origin/main
      556c1e8 (my-feature) Feedback on my function
      8780db6 Feedback on the tests from my function
      a4587fa Add test for my new feature
      56e34e9 Add new feature

… mit ``git rebase``
--------------------

3. Mit ``git rebase -i`` können wir interaktiv die ``pick``-Zeilen neu
   anordnen:

   .. code-block:: console

      $ git rebase -i origin/main

   Dies öffnet unseren Editor:

   .. code-block:: console

      pick 56e34e9 Add new feature
      pick a4587fa Add test for my new feature
      pick 8780db6 Feedback on the tests from my function
      pick 556c1e8 Feedback on my function

   Anschließend können wir die Zeilen umändern, :abbr:`z.B. (zum Beispiel)` in:

   .. code-block:: console

      pick 56e34e9 Add new feature
      squash 556c1e8 Feedback on my function
      pick a4587fa Add test for my new feature
      squash 8780db6 Feedback on the tests from my function

   Nun haben wir erneut zwei Commits:

   .. code-block:: console

      $ git log --oneline my-feature ^origin/main
      31a140a (my-feature) Add test for my new feature
      132ae9b Add new feature

#. Die Änderungen können nun mit ``git push -f`` an unseren entfernten Zweig
   gesendet werden.

…mit ``git commit --fixup``  und ``git rebase --autosquash``
------------------------------------------------------------

In Git gibt es jedoch noch einen einfacheren Weg, einen vorherigen Commit zu
korrigieren: mit ``git commit--fixup`` und ``git rebase --autosquash``.

5. Wir erstellen erneut zwei temporäre Commits, diesmal jedoch mit ``git
   commit--fixup``:

   .. code-block:: console

      # Further changes to the tests
      $ git commit --fixup=31a140a
      [my-feature dd0c0d1] fixup! Add test for my new feature
       1 file changed, 1 insertion(+)
      # Further changes to my function
      $ git commit --fixup=132ae9b
      [my-function bc2298a] fixup! Add new feature
       1 file changed, 1 insertion(+)
      $ git log --oneline my-feature ^origin/main
      bc2298a (my-feature) fixup! Add new feature
      dd0c0d1 fixup! Add test for my new feature
      31a140a Add test for my new feature
      132ae9b Add new feature

   Bei Commits mit der Option :samp:`--fixup={SHA}` schreibt Git eine speziell
   formatierte Commit-Nachricht, die als *dieser Commit korrigiert jenen*
   gelesen werden kann.

#. Anstatt nun mit ``git rebase -i`` die ``Pick``/``Squash``-Zeilen manuell
   festzulegen, können wir nun einfach ``git rebase --autosquash`` ausführen:

   .. code-block:: console

      $ git rebase --autosquash origin/main
      Successfully rebased and updated refs/heads/my-feature.
      $ git log --oneline my-feature ^origin/main
      694cb48 (my-feature) Add test for my new feature
      55cbe9b Add new feature

   ``git rebase --autosquash`` automatisiert das, was wir gerade manuell mit
   ``git rebase -i`` getan haben – es öffnete sich jedoch kein Editor, in dem
   wir die Commits manuell verschieben mussten.

   .. tip::
      Die Option ``--fixup`` enthält auch die Optionen ``amend`` und ``reword``,
      um die Commit-Nachricht umzuformulieren, :abbr:`z.B. (tum Beispiel)`
      :samp:`git commit --fixup:amend={SHA}`.

      Weitere Optionen findet ihr in der `Git Commit-Dokumentation
      <https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---fixupamendrewordltcommitgt>`_.
