.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

CKAN
====

`CKAN <https://ckan.org>`_ ist ein Open-Source-Datenmanagementsystem, aus dem
ihr mit Frictionless Pakete laden und veröffentlichen könnt.

#. Zunächst müsst ihr die optionale Abhängigkeit ``ckan`` installieren:

   .. code-block:: console

      $ uv add 'frictionless[ckan]'

#. Anschließend könnt ihr eine Liste der CKAN-Datensätze einer CKAN-Instanz
   herunterladen, :abbr:`z. B. (zum Beispiel)`:

   .. code-block:: pycon

      >>> import frictionless
      >>> from frictionless import portals, Catalog
      >>> ckan_control = portals.CkanControl(baseurl="https://data.gov.au/data")
      >>> c = Catalog(control=ckan_control)
      >>> c
      {'datasets': [{'name': 'native-title-determination-applications-register',
                     'package': {'name': 'native-title-determination-applications-register',
                                 'title': 'Register of Native Title Claims',
                                 'description': 'The Register of Native Title Claims '
      ...

#. Ihr könnt auch die CKAN-Suche verwenden:

   .. code-block:: pycon

      >>> ckan_control = portals.CkanControl(
      ...     baseurl="https://data.gov.au/data", search={"q": "name:ipswich*"}
      ... )
      >>> c = Catalog(control=ckan_control)
      >>> c
      {'datasets': [{'name': 'ipswich-city-drainage-open-drains-inverts',
                     'package': {'name': 'ipswich-city-drainage-open-drains-inverts',
                                 'title': 'Ipswich City Drainage Open Drains Inverts',
                                 'description': 'Location and extents of Drainage '
                                                'Open Drains Inverts within the City '
                                                'of Ipswich',
      ...

#. Um einen bestimmten Datensatz als *Frictionless Package* zu importieren,
   benötigt ihr die :class:`frictionless.Package`-Klasse:

   .. code-block:: pycon

      >>> from frictionless import Package
      >>> package = Package(
      ...     "native-title-determination-applications-register", control=ckan_control
      ... )
      >>> package
      {'name': 'native-title-determination-applications-register',
       'title': 'Register of Native Title Claims',
       'description': 'The Register of Native Title Claims is kept by the Native '
      ...

   Dadurch werden der Datensatz und alle Metadaten zu seinen Ressourcen
   heruntergeladen.

Um ein Paket auf einer CKAN-Instanz zu veröffentlichen, benötigt ihr einen
API-Schlüssel eines CKAN-Users, der Datensätze erstellen darf. Dieser Schlüssel
kann mit dem Parameter ``apikey`` an ``frictionless.portals.CkanControl``
übergeben werden:

.. code-block:: pycon

   >>> from frictionless.portals import CkanControl
   >>> from frictionless import Package
   >>> ckan_control = CkanControl(
   ...     baseurl="https://example.org", apikey="YOUR_API_KEY"
   ... )
   >>> package = Package(
   ...     name="my_package",
   ...     title="My Package",
   ...     description="My Package for the Guide",
   ...     resources=[Resource(path="my_table.csv")],
   ... )
   >>> package.publish(control=ckan_control)

.. seealso::
   * `Ckan Portal
     <https://framework.frictionlessdata.io/docs/portals/ckan.html>`_
