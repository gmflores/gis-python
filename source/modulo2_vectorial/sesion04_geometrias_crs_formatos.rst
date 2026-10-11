Sesion 4: Geometrias Espaciales, CRS y Formatos Vectoriales
===========================================================

.. note::
   **Duracion:** 2 horas.
   **Librerias:** GeoPandas, Shapely, Pyogrio.
   **Conceptos clave:** Puntos, Lineas, Poligonos, Sistemas de Referencia de Coordenadas (CRS), EPSG.

El Modelo Vectorial con Shapely y GeoPandas
-------------------------------------------

El modelo vectorial representa el mundo discretizando el espacio en geometrías geométricas euclidianas mediante la biblioteca **Shapely**:

- **`Point` / `MultiPoint`:** Boyas oceanográficas, sitios de anclaje, estaciones oceanográficas o avistamientos biológicos.
- **`LineString` / `MultiLineString`:** Transectos de navegación oceanográfica, rutas marítimas, cables submarinos o líneas de costa.
- **`Polygon` / `MultiPolygon`:** Polígonos de Áreas Marinas Protegidas (AMP), Zonas Económicas Exclusivas (ZEE) o cuencas sedimentarias.

.. code-block:: python

   from shapely.geometry import Point, LineString, Polygon

   # Construccion de geometrias basicas
   station_pt = Point(-110.312, 24.142)
   transect_line = LineString([(-110.31, 24.14), (-110.50, 24.30), (-110.75, 24.55)])
   marine_reserve = Polygon([
       (-110.40, 24.20), (-110.20, 24.20), 
       (-110.20, 24.40), (-110.40, 24.40), 
       (-110.40, 24.20)
   ])

Construccion de GeoDataFrames desde Coordenadas
-----------------------------------------------

Un ``GeoDataFrame`` es una tabla de Pandas con una columna espacial especial llamada ``geometry``:

.. code-block:: python

   import pandas as pd
   import geopandas as gpd

   # Datos de muestreo de estaciones costeras
   stations_df = pd.DataFrame({
       "station_id": ["E01", "E02", "E03", "E04"],
       "lon": [-110.32, -110.45, -110.60, -110.15],
       "lat": [24.15, 24.35, 24.50, 24.05],
       "chlorophyll_a": [1.45, 0.82, 0.35, 2.10]
   })

   # Conversion a GeoDataFrame vectorizado
   gdf = gpd.GeoDataFrame(
       stations_df,
       geometry=gpd.points_from_xy(stations_df["lon"], stations_df["lat"]),
       crs="EPSG:4326"  # WGS84 Coordenadas Geograficas
   )

Sistemas de Referencia de Coordenadas (CRS)
-------------------------------------------

.. warning::
   Nunca realice cálculos métricos (como distancias en metros o áreas en km²) en grados geográficos (EPSG:4326). Los grados son unidades angulares cuya longitud física varía drásticamente con la latitud.

Para mediciones métricas exactas, reproyecte al sistema proyectado local (por ejemplo, Universal Transverse Mercator - UTM):

.. code-block:: python

   # Reproyeccion de WGS84 a UTM Zona 12N (Baja California Sur)
   gdf_utm = gdf.to_crs(epsg=32612)
   print(f"CRS proyectado: {gdf_utm.crs.name}")

Formatos de Almacenamiento Vectorial
------------------------------------

1. **Shapefile (`.shp`):** Formato heredado con limitaciones severas (nombres truncados a 10 caracteres, límite de 2 GB, múltiples archivos).
2. **GeoPackage (`.gpkg`):** Estándar abierto SQLite moderno, autocontenido, rápido y sin límites arbitrarios de atributos.
3. **GeoParquet (`.parquet`):** Formato columnar optimizado para análisis masivo de datos en la nube y computación distribuida.

.. code-block:: python

   # Guardar y leer en GeoPackage con el motor pyogrio
   gdf.to_file("estaciones_muestreo.gpkg", layer="ctd_2026", driver="GPKG", engine="pyogrio")
   gdf_leido = gpd.read_file("estaciones_muestreo.gpkg", engine="pyogrio")

Ejercicios de la Sesion
-----------------------

1. Importe una tabla CSV de lances de pesca con coordenadas geográficas y conviértala a GeoDataFrame.
2. Identifique el código EPSG de la zona UTM correspondiente a su área de estudio y reproyecte sus capas.
