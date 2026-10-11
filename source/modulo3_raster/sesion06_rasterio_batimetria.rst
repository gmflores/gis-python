Sesion 6: Modelo Raster y Analisis de Batimetria con Rasterio
============================================================

.. note::
   **Duracion:** 2 horas.
   **Librerias:** Rasterio, Rioxarray, Matplotlib.
   **Conjunto de datos:** Malla batimetrica global GEBCO (General Bathymetric Chart of the Oceans).

Estructura Matricial de los Datos Raster
----------------------------------------

A diferencia de los vectores, el modelo ráster discretiza el espacio continuo en una cuadrícula regular de celdas o píxeles:

- **Resolución espacial:** Dimensiones físicas del píxel en unidades del CRS (metros o grados).
- **Transformación afín (`Affine Transform`):** Matriz que mapea las coordenadas fila/columna de la matriz con las coordenadas geográficas reales del mundo:

.. math::

   \begin{bmatrix} x \\ y \\ 1 \end{bmatrix} = 
   \begin{bmatrix} a & b & c \\ d & e & f \\ 0 & 0 & 1 \end{bmatrix}
   \begin{bmatrix} \text{col} \\ \text{fila} \\ 1 \end{bmatrix}

- **Valores NoData:** Valor numérico reservado que designa píxeles sin observación o fuera de los límites de estudio.

Lectura e Inspeccion de Metadatos con Rasterio
----------------------------------------------

.. code-block:: python

   import rasterio
   from rasterio.plot import show

   # Apertura de la malla batimetrica
   with rasterio.open("gebco_regional.tif") as src:
       print(f"Dimensiones: {src.height} filas x {src.width} columnas")
       print(f"Numero de bandas: {src.count}")
       print(f"CRS: {src.crs}")
       print(f"Resolucion espacial: {src.res}")
       print(f"Caja delimitadora (bounds): {src.bounds}")
       print(f"Transformacion afin: \n{src.transform}")
       
       # Lectura de la banda 1 (profundidad en metros)
       bathymetry = src.read(1)

Recorte Espacial (Mask / Clip) con Limites Vectoriales
------------------------------------------------------

En ciencias marinas es común disponer de archivos globales de batimetría de varios gigabytes y requerir únicamente el golfo o fiordo de estudio delimitado por un polígono vectorial:

.. code-block:: python

   import rioxarray
   import geopandas as gpd

   # Cargar el raster con rioxarray
   rds = rioxarray.open_rasterio("gebco_regional.tif")

   # Cargar el poligono del area de estudio
   area_estudio = gpd.read_file("area_estudio.gpkg")

   # Asegurar que ambos compartan el mismo CRS
   area_estudio = area_estudio.to_crs(rds.rio.crs)

   # Recortar el raster exactamente al contorno poligonal
   clipped_rds = rds.rio.clip(area_estudio.geometry, area_estudio.crs)

   # Guardar el recorte optimizado en GeoTIFF
   clipped_rds.rio.to_raster("batimetria_recortada.tif", compress="DEFLATE")

Visualizacion de la Batimetria
------------------------------

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np

   bathy_data = clipped_rds.squeeze().values

   fig, ax = plt.subplots(figsize=(8, 6))
   im = ax.imshow(
       bathy_data, 
       cmap="Blues_r", 
       vmin=-3000, 
       vmax=0, 
       extent=[rds.x.min(), rds.x.max(), rds.y.min(), rds.y.max()]
   )
   plt.colorbar(im, ax=ax, label="Profundidad (m)")
   ax.set_title("Malla Batimetrica Recortada - Area de Estudio")
   plt.show()

Ejercicios de la Sesion
-----------------------

1. Abra una escena ráster de batimetría e imprima el valor mínimo y máximo de profundidad en el área.
2. Genere una máscara booleana con NumPy para aislar la plataforma continental (profundidades menores a 200 m).
