.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Zenodo
======

Für den Datenaustausch zwischen ``frictionless-py`` und `Zenodo
<https://zenodo.org/>`_ wird wird die Bibliothek `pyzenodo3
<https://github.com/space-physics/pyzenodo3>`_ verwendet.

#. Früher konnte hierfür einfach die optionale Abhängigkeit ``zenodo``
   mitinstalliert werden:

   .. code-block:: console

      $ uv add 'frictionless[zenodo]'

   Aktuell ist der Datenaustausch nur noch mit einem Fork möglich, der
   installiert werden kann mit:

   .. code-block:: console

      $ uv pip install -U git+https://github.com/coroa/frictionless-py.git@fix/zenodo-no-api-file-access

#. Wir können einzelne oder mehrere Repositories aus Zenodo einlesen und einen
   Katalog erstellen, :abbr:`z. B. (zum Beispiel)` mit:

   .. code-block:: pycon

      >>> from frictionless import portals, Catalog
      >>> control = portals.ZenodoControl(search='notes:"TDWD"')
      >>> catalog = Catalog(control=control)
      >>> print("Total datasets:", len(catalog.datasets))
      Total datasets: 2

#. Ihr könnt Daten aus einem Zenodo-Repository auslesen mit:

   .. code-block:: pycon

      >>> from frictionless import portals, Package
      >>> package = Package("https://zenodo.org/record/7078768")
      >>> print(package)
      {'title': 'Frictionless Data Test Dataset Without Descriptor',
       'resources': [{'name': 'capitals',
                      'type': 'table',
                      'path': 'capitals.csv',
                      'scheme': 'file',
                      'format': 'csv',
                      'mediatype': 'text/csv',
                      'hash': 'md5:154d822b8c2aa259867067f01c0efee5',
                      'bytes': 76},
                     {'name': 'table',
                      'type': 'table',
                      'path': 'table.xls',
                      'scheme': 'file',
                      'format': 'xls',
                      'mediatype': 'application/vnd.ms-excel',
                      'hash': 'md5:3a980d1a559c48978c63c0c1d0d2a8f3',
                      'bytes': 6144}]}

   Wenn das Repo über einen Deskriptor verfügt, gibt es diesen einfach zurück:

   .. code-block:: pycon

      >>> package = Package(
      ...     "https://zenodo.org/record/https://zenodo.org/record/7078760"
      ... )
      >>> print(package)
      {'name': 'testing',
       'title': 'Frictionless Data Test Dataset',
       'resources': [{'name': 'data',
                      'path': 'data.csv',
                      'schema': {'fields': [{'name': 'id',
                                             'type': 'string',
                                             'constraints': {'required': True}},
                                            {'name': 'name', 'type': 'string'},
                                            {'name': 'description', 'type': 'string'},
                                            {'name': 'amount', 'type': 'number'}],
                                 'primaryKey': ['id']}},
                     {'name': 'data2',
                      'path': 'data2.csv',
                      'schema': {'fields': [{'name': 'parent', 'type': 'string'},
                                            {'name': 'comment', 'type': 'string'}],
                                 'foreignKeys': [{'fields': ['parent'],
                                                  'reference': {'resource': 'data',
                                                                'fields': ['id']}}]}}]}

   Sobald ihr das Paket aus dem Repository eingelesen habt, könnt ihr problemlos
   auf die Ressourcen und deren Daten zugreifen, :abbr:`z. B. (zum Beispiel)`:

   .. code-block:: pycon

      >>> print(package.get_resource("data").read_rows())
      [{'amount': Decimal('10000.5'),
        'description': 'Taxes we collect',
        'id': 'A3001',
        'name': 'Taxes'},
       {'amount': Decimal('2000.5'),
        'description': 'Parking fees we collect',
        'id': 'A5032',
        'name': 'Parking Fees'}]

Um Daten in das Zenodo-Repository zu schreiben, verwenden wir die Funktion
:func:`frictionless.Package.publish` wie folgt:

.. code-block:: pycon

   >>> from frictionless import portals, Package
   >>> control = portals.ZenodoControl(metafn="data/zenodo/meta.json", apikey=API_KEY)
   >>> package = Package("MY_PACKAGE/datapackage.json")
   >>> deposition_id = package.publish(control=control)
   >>> print(deposition_id)
   21259741

Wenn das Paket erfolgreich veröffentlicht wurde, wird die ``deposition_id`` wie
im obigen Beispiel gezeigt zurückgegeben.

.. seealso::
   * `Zenodo Portal
     <https://framework.frictionlessdata.io/docs/portals/zenodo.html>`_
