.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Geodaten
========

Dateiformate
------------

.. _pmtiles:

PMTiles
~~~~~~~

`PMTiles <https://docs.protomaps.com>`_ ist ein allgemeines Format für
Kacheldaten, die durch Z/X/Y-Koordinaten adressiert werden. Dabei kann es sich
um kartografische Vektorkacheln, :ref:`Fernerkundungsdaten <remote-sensing>`,
JPEG-Bilder oder ähnliches handeln.

Zum Lesen werden `HTTP Range Requests
<https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests>`_ verwendet,
um nur die relevanten Kacheln oder Metadaten innerhalb eines PMTiles-Archivs
abzurufen. Die Anordnung der Kacheln und Verzeichnisse ist so konzipiert, dass
die Anzahl der Anfragen beim Verschieben und Zoomen minimiert wird.

PMTiles ist jedoch ein schreibgeschütztes Format: Es ist nicht möglich, einen
Teil des Archivs zu aktualisieren, ohne die gesamte Datei neu zu schreiben. Wenn
ihr transaktionale Aktualisierungen benötigt, solltet ihr eine Datenbank wie
SQLite oder :doc:`postgresql/postgis/index` und `ST_asMVT
<https://postgis.net/docs/ST_AsMVT.html>`_ verwenden.

.. seealso::
   * `GitHub Repository <https://github.com/protomaps/PMTiles>`_
   * `PMTiles Version 3 Specification
     <https://github.com/protomaps/PMTiles/blob/main/spec/v3/spec.md>`_
   * `pmtiles Python package
     <https://github.com/protomaps/PMTiles/tree/main/python/pmtiles>`_

Mapbox Vector Tiles (MVT)
~~~~~~~~~~~~~~~~~~~~~~~~~

Das `Mapbox Vector Tiles
<https://docs.mapbox.com/data/tilesets/guides/vector-tiles-standards/>`_-Dateiformat
speichert jede Kachel in einem Verzeichnisbaum wie :file:`/Z/X/Y.mvt`. Dies
funktioniert gut für kleine Kachelsätze, aber das Aktualisieren einer kompletten
globalen Pyramide mit ~300 Millionen Kacheln ist sehr ineffizient.
:ref:`pmtiles` ist dagegen eine einzige Datei, in deren Kacheln de-dupliziert
sind, wodurch die Größe globaler Vektor-Basiskarten um ~70% reduziert werden.

Zum Schreiben muss die :ref:`gdal`-Bibliothek mit `SQLite
<https://www.sqlite.org>`_ und `GEOS <https://libgeos.org>`_-Unterstützung
installiert sein. Dabei werden die Mapbox Vector Tiles in SQLite wie
:ref:`mbtiles` gespeichert und können mit dem MBTiles-Treiber verarbeitet
werden.

.. seealso::
   * `Mapbox Vector Tile specification
     <https://github.com/mapbox/vector-tile-spec>`_
   * `MVT: Mapbox Vector Tiles
     <https://gdal.org/en/stable/drivers/vector/mvt.html>`_

.. _mbtiles:

MBTiles
~~~~~~~

`MBTiles <https://docs.mapbox.com/help/glossary/mbtiles/>`_ ist ein
Containerformat für Kacheldaten auf der Grundlage von SQLite. Es ist für den
lokalen Zugriff optimiert, nicht wie :ref:`pmtiles` auf den Zugriff via HTTP.

.. seealso::
   * `MBTiles specification <https://github.com/mapbox/mbtiles-spec>`_

.. _geodata-repositories:

Cloud Optimized GeoTIFF (COG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Cloud Optimized GeoTIFF <https://cogeo.org>`_ ist eine Raster-TIFF-Datei, die
ähnlich wie :ref:`pmtiles` für das Lesen aus einem Cloud-Speicher optimiert ist.
:ref:`pmtiles` kann jedoch auch andere Kacheldaten, :abbr:`z.B. (zum Beispiel)`
Vektor-Kacheln ausliefern. COG ist jedoch mit den meisten GIS-Programmen, die
mit GeoTIFF arbeiten, abwärtskompatibel.

.. seealso::
   * `OGC Cloud Optimized GeoTIFF Standard
     <https://docs.ogc.org/is/21-026/21-026.html>`_

.. _geoparquet:

GeoParquet
~~~~~~~~~~

`Parquet <https://parquet.apache.org>`_ ist ein quelloffenes,
spaltenorientiertes Datendateiformat, das für die effiziente Speicherung und
Abfrage von Daten entwickelt wurde. Es bietet effiziente
Datenkomprimierungs- und -kodierungsverfahren mit optimierter Verarbeitung
großer, komplexer Daten. `GeoParquet <https://geoparquet.org>`_ erweitert
Parquet um interoperable Geodatentypen (Punkt, Linie, Polygon).

* :doc:`pyviz:matplotlib/geopandas/index`  unterstützt das `Lesen
  <https://geopandas.org/en/stable/docs/reference/api/geopandas.read_parquet.html>`_
  und `Schreiben
  <https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_parquet.html>`_
  von GeoParquet.
* `GeoParquet Downloader Plugin
  <https://plugins.qgis.org/plugins/qgis_plugin_gpq_downloader/>`_ für `QGIS
  <https://qgis.org>`_ ermöglicht Streaming-Downloads von großen
  GeoParquet-Datensätzen.
* `DuckDB <https://duckdb.org>`_ erlaubt mit der `Spatial Extension
  <https://duckdb.org/docs/stable/extensions/spatial/overview.html>`_ das Lesen
  und Schreiben von GeoParquet-Dateien.

.. seealso::
   * `GeoParquet specification <https://github.com/opengeospatial/geoparquet>`_
   * `GeoParquet Software <https://geoparquet.org/#implementations>`_
   * `validate_geoparquet.py
     <https://github.com/OSGeo/gdal/blob/master/swig/python/gdal-utils/osgeo_utils/samples/validate_geoparquet.py>`_

Daten-Repositorien
------------------

`Norwegian Polar Data Centre: Datasets <https://data.npolar.no/dataset>`_
    Antarktis, Arktischer Ozean und Svalbard
`Common Metadata Repository (CMR) <https://cmr.earthdata.nasa.gov/search>`_
    Such-API für die Metadaten der NASA zu fernerkundeten Geowissenschaften
`UC Irvine Machine Learning Repository <https://archive.ics.uci.edu>`_
    Datensätze zum maschinellen Lernen mit Daten zur Luftqualität, zur Erkennung
    von Ozonwerten, zur Konzentration von Treibhausgasen, zur aquatischen
    Toxizität und mehr
`National Data Buoy Center <https://www.ndbc.noaa.gov>`_
    Meteorologische und ozeanografische Messungen für die Meeresumwelt.

.. seealso::
   `List of GIS data sources
   <https://en.wikipedia.org/wiki/List_of_GIS_data_sources>`_

Software
--------

Lesen und Schreiben
~~~~~~~~~~~~~~~~~~~

.. _gdal:

`Geospatial Data Abstraction Library (GDAL) <https://gdal.org/en/latest/>`_
    bietet eine einfache, aber leistungsfähige API zum Lesen und Schreiben von
    Hunderten von Datenformaten.

    .. image::
       https://raster.shields.io/github/stars/OSGeo/gdal
    .. image::
       https://raster.shields.io/github/contributors/OSGeo/gdal
    .. image::
       https://raster.shields.io/github/commit-activity/y/OSGeo/gdal
    .. image::
       https://raster.shields.io/github/license/OSGeo/gdal

`pyogrio <https://pyogrio.readthedocs.io/en/latest/>`_
    bietet eine :doc:`pyviz:matplotlib/geopandas/index`-orientierte API für
    OGR-Vektordatenquellen, wie ESRI Shapefile, GeoPackage und GeoJSON.

    .. image::
       https://raster.shields.io/github/stars/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/contributors/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/commit-activity/y/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/license/geopandas/geopandas

`Rasterio <https://rasterio.readthedocs.io/en/latest/>`_
    liest und schreibt GeoTIFF und andere Formen von Rasterdatensätzen.

    .. image::
       https://raster.shields.io/github/stars/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/contributors/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/commit-activity/y/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/license/rasterio/rasterio

`Zarr-Python <https://zarr.readthedocs.io/en/stable/>`_
    `Zarr <https://zarr.dev>`_ ist ein Open-Source-Dateispeicherformat für
    chunked, komprimierte, N-dimensionale Arrays.

    .. image::
       https://raster.shields.io/github/stars/zarr-developers/zarr-python
    .. image::
       https://raster.shields.io/github/contributors/zarr-developers/zarr-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/zarr-developers/zarr-python
    .. image::
       https://raster.shields.io/github/license/zarr-developers/zarr-python

`Fiona <https://fiona.readthedocs.io/en/latest/>`_
    liest und schreibt :file:`*.shp`- und :file:`*.json`-Daten und viele andere
    Formate.

    .. image::
       https://raster.shields.io/github/stars/Toblerity/Fiona
    .. image::
       https://raster.shields.io/github/contributors/Toblerity/Fiona
    .. image::
       https://raster.shields.io/github/commit-activity/y/Toblerity/Fiona
    .. image::
       https://raster.shields.io/github/license/Toblerity/Fiona

`netCDF4 <https://unidata.github.io/netcdf4-python/>`_
    ist eine Python-Schnittstelle für die `netCDF
    <https://www.unidata.ucar.edu/software/netcdf/>`_-C-Bibliothek.

    .. image::
       https://raster.shields.io/github/stars/Unidata/netcdf4-python
    .. image::
       https://raster.shields.io/github/contributors/Unidata/netcdf4-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/Unidata/netcdf4-python
    .. image::
       https://raster.shields.io/github/license/Unidata/netcdf4-python

`pyModis <http://www.pymodis.org/>`_
    ist eine Sammlung von Python-Skripten zum Herunterladen und Mosaikieren von
    `MODIS
    <https://de.wikipedia.org/wiki/Moderate-resolution_Imaging_Spectroradiometer>`__-Daten.

    .. image::
       https://raster.shields.io/github/stars/lucadelu/pyModis
    .. image::
       https://raster.shields.io/github/contributors/lucadelu/pyModis
    .. image::
       https://raster.shields.io/github/commit-activity/y/lucadelu/pyModis
    .. image::
       https://raster.shields.io/github/license/lucadelu/pyModis

`xmitgcm <https://xmitgcm.readthedocs.io/en/latest/>`_
    liest `MITgcm <https://mitgcm.org>`_-Binär-MDS-Dateien in
    Xarray-Datenstrukturen.

    .. image::
       https://raster.shields.io/github/stars/MITgcm/xmitgcm
    .. image::
       https://raster.shields.io/github/contributors/MITgcm/xmitgcm
    .. image::
       https://raster.shields.io/github/commit-activity/y/MITgcm/xmitgcm
    .. image::
       https://raster.shields.io/github/license/MITgcm/xmitgcm

.. seealso::
   :ref:`geo-wrappers`

.. _remote-sensing:

Fernerkundung
~~~~~~~~~~~~~

`Satpy <https://satpy.readthedocs.io/en/stable/>`_
    Einfach zu verwendende API für Sensoren von Satellitenbildern wie `MODIS
    <https://modis.gsfc.nasa.gov/data/>`_, `Sentinel-2
    <https://sentiwiki.copernicus.eu/web/s2-mission>`_ :abbr:`usw (und so
    weiter)`.

    .. image::
       https://raster.shields.io/github/stars/pytroll/satpy
    .. image::
       https://raster.shields.io/github/contributors/pytroll/satpy
    .. image::
       https://raster.shields.io/github/commit-activity/y/pytroll/satpy
    .. image::
       https://raster.shields.io/github/license/pytroll/satpy

`sentinelsat <https://github.com/sentinelsat/sentinelsat>`_
    Finden und Herunterladen von Copernicus Sentinel-Satellitenbildern über die
    Kommandozeile oder Python.

    .. image::
       https://raster.shields.io/github/stars/sentinelsat/sentinelsat
    .. image::
       https://raster.shields.io/github/contributors/sentinelsat/sentinelsat
    .. image::
       https://raster.shields.io/github/commit-activity/y/sentinelsat/sentinelsat
    .. image::
       https://raster.shields.io/github/license/sentinelsat/sentinelsat

`Open Data Cube <https://www.opendatacube.org>`_
    Open-Source-Software zur Verwaltung und Analyse von Geodaten.

    .. image::
       https://raster.shields.io/github/stars/opendatacube/datacube-core
    .. image::
       https://raster.shields.io/github/contributors/opendatacube/datacube-core
    .. image::
       https://raster.shields.io/github/commit-activity/y/opendatacube/datacube-core
    .. image::
       https://raster.shields.io/github/license/opendatacube/datacube-core

`RSGISLib <http://rsgislib.org/>`_
    oder *The Remote Sensing and GIS Software Library* ist eine Sammlung von
    Fernerkundungswerkzeugen für die Rasterverarbeitung und -analyse.

    .. image::
       https://raster.shields.io/github/stars/remotesensinginfo/rsgislib
    .. image::
       https://raster.shields.io/github/contributors/remotesensinginfo/rsgislib
    .. image::
       https://raster.shields.io/github/commit-activity/y/remotesensinginfo/rsgislib
    .. image::
       https://raster.shields.io/github/license/remotesensinginfo/rsgislib

.. seealso::
   :doc:`/clean-prep/dask-pipeline`

Allgemeine Zwecke
~~~~~~~~~~~~~~~~~

`pyproj <https://github.com/pyproj4/pyproj>`_
    Python-Schnittstelle zu `PROJ <https://proj.org/>`_, einer Bibliothek für
    kartographische Projektionen und Koordinatentransformationen.

    .. image::
       https://raster.shields.io/github/stars/pyproj4/pyproj
    .. image::
       https://raster.shields.io/github/contributors/pyproj4/pyproj
    .. image::
       https://raster.shields.io/github/commit-activity/y/pyproj4/pyproj
    .. image::
       https://raster.shields.io/github/license/pyproj4/pyproj

`pgeocode <https://pypi.org/project/pgeocode/>`_
    Abfrage von GPS-Koordinaten und Gemeindenamen aus Postleitzahlen,
    Entfernungen zwischen Postleitzahlen sowie allgemeine Entfernungen.

    .. image::
       https://raster.shields.io/github/stars/symerio/pgeocode
    .. image::
       https://raster.shields.io/github/contributors/symerio/pgeocode
    .. image::
       https://raster.shields.io/github/commit-activity/y/symerio/pgeocode
    .. image::
       https://raster.shields.io/github/license/symerio/pgeocode

`Arcpy <https://pro.arcgis.com/de/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm>`_
    wird von `Esri ArcGIS <https://en.wikipedia.org/wiki/ArcGIS>`_ für die
    Analyse geografischer Daten, die Datenkonvertierung, das Datenmanagement und
    die Kartenautomatisierung verwendet.

GIS
~~~

`QGIS <https://qgis.org>`_
    unterstützt das Anzeigen, Bearbeiten, Drucken und Analysieren von Geodaten
    in einer Reihe von Datenformaten.

    .. image::
       https://raster.shields.io/github/stars/qgis/QGIS
    .. image::
       https://raster.shields.io/github/contributors/qgis/QGIS
    .. image::
       https://raster.shields.io/github/commit-activity/y/qgis/QGIS
    .. image::
       https://raster.shields.io/github/license/qgis/QGIS

`GeoPandas <https://geopandas.org/en/stable/>`_
    erweitert die von Pandas verwendeten Datentypen, um räumliche Operationen
    auf geometrischen Typen zu ermöglichen.

    .. image::
       https://raster.shields.io/github/stars/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/contributors/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/commit-activity/y/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/license/geopandas/geopandas

`regionmask <https://regionmask.readthedocs.io/en/stable/>`_
    bestimmt, zu welcher geografischen Region jeder Rasterpunkt gehört.

    .. image::
       https://raster.shields.io/github/stars/regionmask/regionmask
    .. image::
       https://raster.shields.io/github/contributors/regionmask/regionmask
    .. image::
       https://raster.shields.io/github/commit-activity/y/regionmask/regionmask
    .. image::
       https://raster.shields.io/github/license/regionmask/regionmask

`Salem <https://salem.readthedocs.io/en/latest/>`_
    erweitert xarray um geolokalisierte Subsetting-, Maskierungs- und
    Plotting-Operationen.

    .. image::
       https://raster.shields.io/github/stars/fmaussion/salem
    .. image::
       https://raster.shields.io/github/contributors/fmaussion/salem
    .. image::
       https://raster.shields.io/github/commit-activity/y/fmaussion/salem
    .. image::
       https://raster.shields.io/github/license/fmaussion/salem

Räumlich-zeitliche Statistik
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`rasterstats <https://pythonhosted.org/rasterstats/>`_
    Zusammenfassen von raumbezogenen Rasterdatensätzen auf der Grundlage von
    Vektorgeometrien.

    .. image::
       https://raster.shields.io/github/stars/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/contributors/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/commit-activity/y/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/license/rasterio/rasterio

`eofs <https://ajdawson.github.io/eofs/latest/>`_
    :abbr:`EOF (Empirische orthogonale Funktionen)` zur Analyse von
    räumlich-zeitlichen Daten.

    .. image::
       https://raster.shields.io/github/stars/ajdawson/eofs
    .. image::
       https://raster.shields.io/github/contributors/ajdawson/eofs
    .. image::
       https://raster.shields.io/github/commit-activity/y/ajdawson/eofs
    .. image::
       https://raster.shields.io/github/license/ajdawson/eofs

Re-Gridding
~~~~~~~~~~~

`Pyresample <https://pyresample.readthedocs.io/en/stable/>`_
    Resampling von Geobilddaten, primär für die Satpy-Bibliothek.

    .. image::
       https://raster.shields.io/github/stars/pytroll/pyresample
    .. image::
       https://raster.shields.io/github/contributors/pytroll/pyresample
    .. image::
       https://raster.shields.io/github/commit-activity/y/pytroll/pyresample
    .. image::
       https://raster.shields.io/github/license/pytroll/pyresample

`xESMF <https://xesmf.readthedocs.io/en/latest/>`_
    Universal Regridder für Geodaten.

    .. image::
       https://raster.shields.io/github/stars/pangeo-data/xESMF
    .. image::
       https://raster.shields.io/github/contributors/pangeo-data/xESMF
    .. image::
       https://raster.shields.io/github/commit-activity/y/pangeo-data/xESMF
    .. image::
       https://raster.shields.io/github/license/pangeo-data/xESMF

Simulation
~~~~~~~~~~

`xarray-simlab <https://xarray-simlab.readthedocs.io/en/latest/>`_
    bietet sowohl einen allgemeinen Rahmen für die Erstellung von
    Berechnungsmodellen als auch eine xarray-Erweiterung für die Erstellung und
    Durchführung von Simulationen.

    .. image::
       https://raster.shields.io/github/stars/xarray-contrib/xarray-simlab
    .. image::
       https://raster.shields.io/github/contributors/xarray-contrib/xarray-simlab
    .. image::
       https://raster.shields.io/github/commit-activity/y/xarray-contrib/xarray-simlab
    .. image::
       https://raster.shields.io/github/license/xarray-contrib/xarray-simlab

`Fastscape <https://fastscape.readthedocs.io/en/latest/>`_
    bietet viele kleine Modellkomponenten zur Verwendung mit dem
    xarray-simlab-Modellierungsrahmen.

    .. image::
       https://raster.shields.io/github/stars/fastscape-lem/fastscape
    .. image::
       https://raster.shields.io/github/contributors/fastscape-lem/fastscape
    .. image::
       https://raster.shields.io/github/commit-activity/y/fastscape-lem/fastscape
    .. image::
       https://raster.shields.io/github/license/fastscape-lem/fastscape

`EarthSim <https://earthsim.holoviz.org>`_
    Werkzeuge für die Umweltsimulation.

    .. image::
       https://raster.shields.io/github/stars/holoviz-topics/EarthSim
    .. image::
       https://raster.shields.io/github/contributors/holoviz-topics/EarthSim
    .. image::
       https://raster.shields.io/github/commit-activity/y/holoviz-topics/EarthSim
    .. image::
       https://raster.shields.io/github/license/holoviz-topics/EarthSim

Visualisierung
~~~~~~~~~~~~~~

:doc:`PyViz Tutorial <pyviz:index>`
    Tutorial, das einen Überblick über die Python-Visualisierungsbibliotheken
    gibt.

    :doc:`pyviz:matplotlib/cartopy/index`
        erstellt Karten auf Basis von :doc:`pyviz:matplotlib/index` und
        konvertiert Punkte, Linien und Vektoren zwischen den verschiedenen
        Projektionen.
    :doc:`GeoPandas <pyviz:matplotlib/geopandas/example>`
        GeoPandas Beispiele.
    :doc:`pyviz:matplotlib/iris`
        implementiert ein auf :abbr:`CF (Climate and Forecast)`-Konventionen
        basierendes Datenmodell, dessen Visualisierung auf
        :doc:`pyviz:matplotlib/index` und :doc:`pyviz:matplotlib/cartopy/index`
        basiert.
    :doc:`pyviz:bokeh/integration/holoviews/geoviews`
        Erforschen und visualisieren geographischer, meteorologischer und
        ozeanographischer Datensätze.
    :doc:`pyviz:js/ipyleaflet`
        ist ein Jupyter-Widget für `Leaflet.js <https://leafletjs.com>`_.
    :doc:`pyviz:js/xarray-leaflet`
        ist eine xarray-Erweiterung für das Plotten von Kachelkarten.

Meteorologie
~~~~~~~~~~~~

`MetPy <https://unidata.github.io/MetPy/latest/>`_
    Eine Sammlung von Tools in Python zum Lesen, Visualisieren und Berechnen von
    Wetterdaten.

    .. image::
       https://raster.shields.io/github/stars/Unidata/MetPy
    .. image::
       https://raster.shields.io/github/contributors/Unidata/MetPy
    .. image::
       https://raster.shields.io/github/commit-activity/y/Unidata/MetPy
    .. image::
       https://raster.shields.io/github/license/Unidata/MetPy

`wrf-python <https://wrf-python.readthedocs.io/en/latest/>`_
    Eine Sammlung von Diagnose- und Interpolationsroutinen zur Verwendung mit
    den Ausgaben des :abbr:`WRF-ARW (Weather Research and Forecasting)`-Modells.

    .. image::
       https://raster.shields.io/github/stars/NCAR/wrf-python
    .. image::
       https://raster.shields.io/github/contributors/NCAR/wrf-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/NCAR/wrf-python
    .. image::
       https://raster.shields.io/github/license/NCAR/wrf-python

`windspharm <https://ajdawson.github.io/windspharm/latest/>`_
    Berechnungen zu globalen Windfeldern in sphärischer Geometrie.

    .. image::
       https://raster.shields.io/github/stars/ajdawson/windspharm
    .. image::
       https://raster.shields.io/github/contributors/ajdawson/windspharm
    .. image::
       https://raster.shields.io/github/commit-activity/y/ajdawson/windspharm
    .. image::
       https://raster.shields.io/github/license/ajdawson/windspharm

Ozeanographie
~~~~~~~~~~~~~

`GSW-Python <https://github.com/TEOS-10/GSW-Python>`_
    Python-Implementierung des :abbr:`TEOS-10 (Thermodynamic Equation of
    Seawater 2010)`.

    .. image::
       https://raster.shields.io/github/stars/TEOS-10/GSW-Python
    .. image::
       https://raster.shields.io/github/contributors/TEOS-10/GSW-Python
    .. image::
       https://raster.shields.io/github/commit-activity/y/TEOS-10/GSW-Python
    .. image::
       https://raster.shields.io/github/license/TEOS-10/GSW-Python

`PyCO2SYS <https://pyco2sys.readthedocs.io/en/latest/>`_
    Toolbox zur Lösung des marinen Karbonatsystems und zur Berechnung der damit
    verbundenen Meerwassereigenschaften.

    .. image::
       https://raster.shields.io/github/stars/mvdh7/PyCO2SYS
    .. image::
       https://raster.shields.io/github/contributors/mvdh7/PyCO2SYS
    .. image::
       https://raster.shields.io/github/commit-activity/y/mvdh7/PyCO2SYS
    .. image::
       https://raster.shields.io/github/license/mvdh7/PyCO2SYS

`pyoos <https://pypi.org/project/pyoos/>`_
    High-Level-Datenerfassungsbibliothek für öffentlich zugängliche
    Met-/Ozeandaten.

    .. image::
       https://raster.shields.io/github/stars/ioos/pyoos
    .. image::
       https://raster.shields.io/github/contributors/ioos/pyoos
    .. image::
       https://raster.shields.io/github/commit-activity/y/ioos/pyoos
    .. image::
       https://raster.shields.io/github/license/ioos/pyoos

`UMWM <https://github.com/umwm/umwm>`_
    :abbr:`UMWM (University of Miami Wave Model)` ist ein spektrales
    Ozeanwellenmodell.

    .. image::
       https://raster.shields.io/github/stars/umwm/umwm
    .. image::
       https://raster.shields.io/github/contributors/umwm/umwm
    .. image::
       https://raster.shields.io/github/commit-activity/y/umwm/umwm
    .. image::
       https://raster.shields.io/github/license/umwm/umwm

Klima
~~~~~

`PyOWM <https://github.com/csparpa/pyowm>`_
    Ein Python-Wrapper um die OpenWeatherMap-Web-APIs.

    .. image::
       https://raster.shields.io/github/stars/csparpa/pyowm
    .. image::
       https://raster.shields.io/github/contributors/csparpa/pyowm
    .. image::
       https://raster.shields.io/github/commit-activity/y/csparpa/pyowm
    .. image::
       https://raster.shields.io/github/license/csparpa/pyowm

`climpred <https://climpred.readthedocs.io/en/stable/>`_
    Überprüfung von Wetter- und Klimavorhersagen.

    .. image::
       https://raster.shields.io/github/stars/pangeo-data/climpred
    .. image::
       https://raster.shields.io/github/contributors/pangeo-data/climpred
    .. image::
       https://raster.shields.io/github/commit-activity/y/pangeo-data/climpred
    .. image::
       https://raster.shields.io/github/license/pangeo-data/climpred

`xgcm <https://xgcm.readthedocs.io/en/latest/>`_
    Postprocessing des `General Circulation Model
    <https://en.wikipedia.org/wiki/General_circulation_model>`_ mit xarray.

    .. image::
       https://raster.shields.io/github/stars/xgcm/xgcm
    .. image::
       https://raster.shields.io/github/contributors/xgcm/xgcm
    .. image::
       https://raster.shields.io/github/commit-activity/y/xgcm/xgcm
    .. image::
       https://raster.shields.io/github/license/xgcm/xgcm

`climlab <https://climlab.readthedocs.io/en/latest/>`_
    Prozessorientierte Klimamodellierung.

    .. image::
       https://raster.shields.io/github/stars/climlab/climlab
    .. image::
       https://raster.shields.io/github/contributors/climlab/climlab
    .. image::
       https://raster.shields.io/github/commit-activity/y/climlab/climlab
    .. image::
       https://raster.shields.io/github/license/climlab/climlab

`aospy <https://aospy.readthedocs.io/en/stable/>`_
    Berechnungen, bei denen gitterförmige Klima- und Wetterdaten (insbesondere
    :file:`netCDF`-Dateien) verwendet werden, und die Verwaltung der Ergebnisse.

    .. image::
       https://raster.shields.io/github/stars/spencerahill/aospy
    .. image::
       https://raster.shields.io/github/contributors/spencerahill/aospy
    .. image::
       https://raster.shields.io/github/commit-activity/y/spencerahill/aospy
    .. image::
       https://raster.shields.io/github/license/spencerahill/aospy

`OpenClimateGIS <https://ocgis.readthedocs.io/en/latest/>`_
    Geoverarbeitung und Berechnungen auf CF-konformen Klimadatensätzen.

    .. image::
       https://raster.shields.io/github/stars/NCPP/ocgis
    .. image::
       https://raster.shields.io/github/contributors/NCPP/ocgis
    .. image::
       https://raster.shields.io/github/commit-activity/y/NCPP/ocgis
    .. image::
       https://raster.shields.io/github/license/NCPP/ocgis

`oocgcm <https://oocgcm.readthedocs.io/en/latest/>`_
    Werkzeuge für die Verarbeitung und Analyse der Ergebnisse von allgemeinen
    Zirkulationsmodellen und gittergestützten Satellitendaten.

    .. image::
       https://raster.shields.io/github/stars/lesommer/oocgcm
    .. image::
       https://raster.shields.io/github/contributors/lesommer/oocgcm
    .. image::
       https://raster.shields.io/github/commit-activity/y/lesommer/oocgcm
    .. image::
       https://raster.shields.io/github/license/lesommer/oocgcm

`pangaea <https://pangaea.readthedocs.io/en/latest/>`_
    Xarray-Erweiterung für gerasterte Landoberflächen und Wettermodellausgaben.

    .. image::
       https://raster.shields.io/github/stars/erdc/pangaea
    .. image::
       https://raster.shields.io/github/contributors/erdc/pangaea
    .. image::
       https://raster.shields.io/github/commit-activity/y/erdc/pangaea
    .. image::
       https://raster.shields.io/github/license/erdc/pangaea

Glaziologie
~~~~~~~~~~~

`OGGM <https://oggm.org>`_
    Open-Source-Modellierungsrahmen für Gletscher.

    .. image::
       https://raster.shields.io/github/stars/OGGM/oggm
    .. image::
       https://raster.shields.io/github/contributors/OGGM/oggm
    .. image::
       https://raster.shields.io/github/commit-activity/y/OGGM/oggm
    .. image::
       https://raster.shields.io/github/license/OGGM/oggm
