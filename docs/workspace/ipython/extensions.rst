.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

IPython-Erweiterungen
=====================

IPython-Erweterungen sind Python-Module, die das Verhalten der Shell ändern. Sie
werden mit einem importierbaren Modulnamen bezeichnet und befinden sich
üblicherweise in :file:`.ipython/extensions/`.

Einige wichtige Erweiterungen sind bereits in IPython enthalten:
:label:`extensions_autoreload` und :label:`extensions_storemagic`. Andere
Erweiterungen findet ihr im  `Extensions Index
<https://github.com/ipython/ipython/wiki/Extensions-Index>`_ oder auf PyPI unter
dem `IPython tag <https://pypi.org/search/?c=Framework+%3A%3A+IPython>`_.

.. seealso::
    * `IPython extensions docs
      <https://ipython.readthedocs.io/en/stable/config/extensions/index.html>`_

Erweiterungen verwenden
-----------------------

Die ``%load_ext``-Magie kann verwendet werden um Erweiterungen zu laden während
IPython ausgeführt wird, :abbr:`z.B. (zum Beispiel)` :samp:` %load_ext
{MYEXTENSION}`.

Alternativ kann eine Erweiterung auch bei jedem Start von IPython geladen
werden, indem sie in der IPython-Konfigurationsdate aufgelistet wird,
:abbr:`z.B. (zum Beispiel)` :samp:`c.InteractiveShellApp.extensions =
["{MYEXTENSION}"]`.

Falls ihr noch keine IPython-Konfigurationsdatei erstellt habt, könnt ihr dies
mit :samp:`$ ipython profile create [{PROFILENAME}]`,

Falls kein Profilname angegeben wird, wird ``default`` verwendet. Üblicherweise
wird die Datei dann in :file:`~/.ipython/profile_default/` erstellt und je nach
Verwendungszweck benannt: :file:`ipython_config.py` wird für alle
IPython-Befehle verwendet, während :file:`ipython_notebook_config.py` nur für
Befehle in IPython-Notebooks Verwendung findet.

IPython-Erweiterungen schreiben
-------------------------------

Eine IPython-Erweiterung ist ein importierbares Python-Modul, das über spezielle
Funktionen zum Laden und Entladen verfügt:

.. code-block:: python

    def load_ipython_extension(ipython):
        # The `ipython` argument is the currently active `InteractiveShell`
        # instance, which can be used in any way. This allows you to register
        # new magics or aliases, for example.

    def unload_ipython_extension(ipython):
        # If you want your extension to be unloadable, put that logic here.

.. seealso::
    * :label:`defining_magics`
