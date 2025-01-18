Git LFS entfernen
=================

Dienste wie GitHub bieten zwar `Git LFS <https://git-lfs.com>`_ für ihre
Repositories an, diese dürfen jedoch nicht den zusätzlichen Storage von 1 GiB
überschreiten. Zusätzliche Kontingente bei GitHub einzukaufen ist dann ziemlich
teuer.

.. seealso::
   * `Informationen zur Speicher- und Bandbreitennutzung
     <https://docs.github.com/de/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage>`_

Nur wie wird man Git LFS in einem solchen Repository wieder los?

Die folgenden Schritte ermöglichen, Git LFS wieder loszuwerden:

#. Mit ``git lfs ls-files`` erhaltet ihr eine Liste aller Dateien, die von Git
   LFS verwaltet werden.

#. Als Nächstes sollten wir sicherstellen, dass alle großen Dateien ausgecheckt
   sind mit

   .. code-block:: console

      $ git lfs fetch --all
      $ git lfs checkout

#. Entfernt die Git LFS-Filter:

   #. Hierzu müssen zunächst Einträge, wie :abbr:`z.B. (zum Beispiel)`
         ::samp:`*.{png} filter=lfs diff=lfs merge=lfs -text` aus eurer
         :file:`.gitattributes`-Datei entfernt werden.
   #. Anschließend könnt ihr für jeden gelöschten Eintrag in der
      :file:`.gitattributes`-Datei :abbr:`z.B. (zum Beispiel)` mit :samp:`git
      lfs untrack '*.{png}'` auch die Nachverfolgung durch Git beenden.

      Alternativ könnt ihr auch ``cut -f 1 < .gitattributes | xargs "git lfs
      untrack {}"`` für alle mit Git LFS verwalteten Dateien verwenden.

   #. Schließlich sollten noch die Zeilenenden normalisiert werden mit ``git add
      --renormalize .``.

#. Nun kann Git LFS deinstalliert werden mit ``git lfs uninstall``.
#. Schließlich müssen die Änderungen noch auf den Server übertragen werden.

Nun könnt ihr :abbr:`z.B. (zum Beispiel)` zu :doc:`DVC <../../dvc/index>`
wechseln, um damit große Dateien versioniert zu verwalten.
