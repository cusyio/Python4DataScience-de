.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

GitHub
======

Frictionless-Daten können auch über `GitHub <https://github.com>`_ ausgetauscht
werden. Alle Lese- und Schreibfunktionen basieren auf der `PyGithub
<https://pygithub.readthedocs.io/en/stable/>`_-Bibliothek, die verwendet wird,
um eine Verbindung zur GitHub-API herzustellen.

#. Um GitHub als Datenportal nutzen zu können, müssen zusätzliche Abhängigkeiten
   installiert werden:

   .. code-block:: console

      $ uv add "frictionless[github]"

#. Ihr könnt einzelne oder mehreren Repositories von GitHub einlesen und einen
   Katalog erstellen:

   .. code-block:: console

      >>> from frictionless import portals, Catalog
      ...
      ... control = portals.GithubControl(search="'TestAction: Read' in:readme")
      ... catalog = Catalog(
      ...         "https://github.com/fdtester", control=control
      ...     )
      >>> print("Total datasets:", len(catalog.datasets))
      Total datasets: 3
      >>> print(catalog.datasets[0])
      {'name': 'test-package',
       'package': 'https://raw.githubusercontent.com/fdtester/test-repo-with-datapackage-json/master/datapackage.json'}
      >>> print(catalog.datasets[1])
      {'name': 'test-repo-with-datapackage-yaml',
       'package': {'name': 'test-repo-with-datapackage-yaml',
                   'resources': [{'name': 'capitals',
                                  'type': 'table',
                                  'path': 'data/capitals.csv',
                                  'scheme': 'file',
                                  'format': 'csv',
                                  'mediatype': 'text/csv'}]}}

   Um :abbr:`ggf. (gegebenenfalls)` das Zugriffslimit zu erhöhen, könnt ihr
   einen API-Schlüssel übergeben:

   .. code-block:: pycon

      >>> control = portals.GithubControl(apikey=MY_API_KEY)
      >>> package = Package(
      ...     "https://github.com/fdtester/test-repo-with-datapackage-json",
      ...     control=control,
      ... )

#. Anschließend können Daten aus einem GitHub-Repository auslgeesen werden mit:

   .. code-block:: pycon

      >>> from frictionless import Package
      >>> package = Package(
      ...     "https://github.com/fdtester/test-repo-with-datapackage-json"
      ... )
      >>> print(package)
      {'name': 'test-package',
       'resources': [{'name': 'first-resource',
                      'type': 'table',
                      'path': 'table.xls',
                      'scheme': 'file',
                      'format': 'xls',
                      'mediatype': 'application/vnd.ms-excel',
                      'schema': {'fields': [{'name': 'id', 'type': 'number'},
                                            {'name': 'name', 'type': 'string'}]}}]}

#. Die :func:`reader`-Funktion kann Pakete aus Repos einlesen. Verfügt das Repo
   nicht über eine Beschreibung, wird eine Beschreibung mit demselben Namen wie
   der Repo-Name erstellt. Standardmäßig liest die Funktion Dateien der Typen
   ``CSV``, ``XLSX`` und ``XLS`` ein:

   .. code-block:: console

      $ uv pip install 'frictionless[excel]'

   .. code-block:: pycon

      >>> print(package.get_resource("first-resource").read_rows())
      [{'id': 1, 'name': 'english'}, {'id': 2, 'name': '中国人'}]

Um Daten in das GitHub-Repository zu schreiben, kann die Funktion
:func:`Package.publish` verwendet werden:

.. code-block:: pycon

   >>> from frictionless import portals, Package
   >>> package = Package("MY_PACKAGE.json")
   >>> control = portals.GithubControl(
   ...     repo="MY_PACKAGE", name="GITHUB_ACCOUNT_NAME", email=EMAIL, apikey=API_KEY
   ... )
   >>> response = package.publish(control=control)
   >>> print(response)
   Repository(full_name="GITHUB_ACCOUNT_NAME/MY_PACKAGE")

.. seealso::
   * `Github Portal
     <https://framework.frictionlessdata.io/docs/portals/github.html>`_
