Sesion 7: Arreglos Multidimensionales (NetCDF) e Integracion Vector-Raster
========================================================================

.. note::
   **Duracion:** 2 horas.
   **Librerias:** Xarray, NetCDF4, Exactextract / Rasterstats.
   **Conjunto de datos:** Series de tiempo de Temperatura Superficial del Mar (NOAA OISST / Copernicus Marine).
   **Tarea 2:** Analisis espacial integrado vector + raster.

El Modelo de Datos Multidimensional de Xarray
---------------------------------------------

Muchos productos oceanográficos y climáticos no son simples imágenes de 2 dimensiones, sino arreglos multidimensionales almacenados en formato **NetCDF** (Network Common Data Form) o **Zarr**:

- **Dimensiones:** Ejes físicos del arreglo (tiempo, profundidad/nivel, latitud, longitud).
- **Coordenadas:** Arreglos numéricos que dan nombre físico y ubicación a los índices de las dimensiones.
- **Variables de datos (`DataArray`):** Campos oceanográficos medidos (ej. `analysed_sst`, `salinity`, `sea_level_anomaly`).
- **Atributos:** Metadatos globales y por variable (unidades, convenciones CF, proveedor).

.. code-block:: python

   import xarray as xr

   # Cargar un conjunto de datos NetCDF de temperatura marina
   ds = xr.open_dataset("oisst_monthly_2020_2025.nc")
   print(ds)

Seleccion Basada en Etiquetas y Climatologias
--------------------------------------------

Xarray permite indexar utilizando valores geográficos y temporales naturales mediante `.sel()`:

.. code-block:: python

   # Seleccionar una estacion especifica y un intervalo de fechas
   punto_serie = ds["sst"].sel(
       lon=-110.5, 
       lat=24.5, 
       method="nearest"
   ).sel(time=slice("2021-01-01", "2024-12-31"))

   # Calculo de la climatologia mensual (ciclo estacional medio)
   climatologia_mensual = ds["sst"].groupby("time.month").mean(dim="time")

   # Calculo de anomalias termicas marinas
   anomalia_sst = ds["sst"].groupby("time.month") - climatologia_mensual

Integracion Vector-Raster: Extraccion en Puntos y Poligonos
-----------------------------------------------------------

Uno de los mayores desafios en la ecologia marina es combinar registros discretos de muestreo con capas ambientales continuas:

1. **Extraccion puntual:** Asignar la temperatura de fondo o superficial del mar a cada estacion de lance oceanografico.
2. **Estadisticas zonales:** Calcular el promedio, maximo y desviacion estandar de la clorofila dentro de los limites de un Area Marina Protegida.

.. code-block:: python

   import geopandas as gpd
   from rasterstats import zonal_stats

   # Poligonos de Areas Marinas Protegidas
   amp_gdf = gpd.read_file("areas_protegidas.gpkg")

   # Calculo de estadisticas zonales sobre una capa raster de batimetria o temperatura
   stats = zonal_stats(
       amp_gdf, 
       "batimetria_recortada.tif", 
       stats=["mean", "min", "max", "std"]
   )

   # Anadir las estadisticas calculadas al GeoDataFrame
   amp_gdf["profundidad_media"] = [s["mean"] for s in stats]
   print(amp_gdf[["nombre_amp", "profundidad_media"]])

Tarea Practica 2
----------------

1. Extraiga la serie temporal de temperatura para tres estaciones oceanográficas de su estudio.
2. Calcule la media batimétrica y la temperatura máxima superficial para cada polígono de conservación de su región.
3. Exporte la tabla resultante con atributos ambientales integrados en formato GeoPackage.
