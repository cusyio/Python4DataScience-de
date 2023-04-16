Vim- und IDE-Integration
========================

Vim
---

Um DVC-Dateien in Vim als YAML zu erkennen, solltet ihr Folgendes in
``~/.vimrc`` hinzufügen::

    " DVC
    autocmd! BufNewFile,BufRead Dvcfile,*.dvc setfiletype yaml

Visual Studio Code
------------------

Für `Visual Studio Code <https://code.visualstudio.com>`_ gibt es eine
Erweiterung für `DVC
<https://marketplace.visualstudio.com/items?itemName=Iterative.dvc>`_, die aus
dem `Visual Studio Marketplace <https://marketplace.visualstudio.com>`_
heruntergeladen werden kann.

IntelliJ IDEs
-------------

`intellij-dvc
<https://plugins.jetbrains.com/plugin/11368-data-version-control-dvc-support>`_
ist ein Plugin für IntelliJ IDEs einschließlich PyCharm, IntelliJ IDEA und
CLion. Es kann aus dem `JetBrains Plugins-Repository
<https://plugins.jetbrains.com/plugin/11368-data-version-control-dvc-support/>`_
heruntergeladen werden.
