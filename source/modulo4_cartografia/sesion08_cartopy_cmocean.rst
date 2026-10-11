Sesion 8: Cartografia Cientifica con Cartopy y Paletas Oceanograficas
=====================================================================

.. note::
   **Duracion:** 2 horas.
   **Librerias:** Cartopy, Matplotlib, Cmocean.
   **Objetivo:** Crear composiciones cartograficas rigurosas con proyecciones geodésicas y paletas marinas perceptuales.

Introduccion a Cartopy y Proyecciones Geograficas
-------------------------------------------------

**Cartopy** es el estandar de facto para cartografía científica en Python, sustituyendo al antiguo Basemap. Su fortaleza radica en el desacoplamiento entre el **sistema de coordenadas de los datos** (usualmente coordenadas geográficas latitud/longitud) y el **sistema de proyección del mapa visual** (Platea Carrée, Mercator, Lambert Conformal, Polar Estereográfica):

.. code-block:: python

   import matplotlib.pyplot as plt
   import cartopy.crs as ccrs
   import cartopy.feature as cfeature

   # Crear un mapa proyectado en Mercator
   fig = plt.figure(figsize=(9, 7))
   ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())

   # Delimitar la extension espacial del mapa en coordenadas de datos (PlateCarree)
   ax.set_extent([-115, -108, 22, 28], crs=ccrs.PlateCarree())

   # Agregar caracteristicas fisicas de Natural Earth
   ax.add_feature(cfeature.LAND, facecolor="#e8e4c9", edgecolor="black", linewidth=0.5)
   ax.add_feature(cfeature.COASTLINE, linewidth=0.8)
   ax.add_feature(cfeature.RIVERS, edgecolor="lightblue", linewidth=0.5)

   # Reticula de coordenadas geográficas rotulada
   gl = ax.gridlines(draw_labels=True, linestyle="--", alpha=0.5, color="gray")
   gl.top_labels = False
   gl.right_labels = False

Paletas Perceptualmente Uniformes con Cmocean
----------------------------------------------

.. warning::
   El uso de paletas no uniformes (como "jet" o "rainbow") crea falsos gradientes visuales e interpretaciones erróneas de los datos oceanográficos. Además, son inaccesibles para personas con daltonismo.

La librería **`cmocean`** fue desarrollada específicamente por oceanógrafos para garantizar uniformidad perceptual:

- **`cmocean.cm.thermal`:** Diseñada para temperatura del agua (tonos cálidos progresivos).
- **`cmocean.cm.haline`:** Diseñada para salinidad (tonos azul-cian).
- **`cmocean.cm.deep`:** Diseñada para batimetría profunda (azules profundos a claros).
- **`cmocean.cm.algae`:** Diseñada para clorofila y fitoplancton (tonos verdes progresivos).
- **`cmocean.cm.topo`:** Batimetría y topografía combinada con el cero en la costa.

Superposicion de Campos Raster e Isobatas Batimetricas
------------------------------------------------------

.. code-block:: python

   import numpy as np
   import cmocean

   # Suponiendo lons, lats y matriz bathymetry
   # Graficado de campo continuo con pcolormesh e isobatas con contour
   mesh = ax.pcolormesh(
       lons, lats, bathymetry,
       cmap=cmocean.cm.deep,
       transform=ccrs.PlateCarree(),
       shading="auto"
   )

   # Anadir isobatas batimetricas principales (ej. 200m y 1000m)
   contours = ax.contour(
       lons, lats, bathymetry,
       levels=[-1000, -200, -50],
       colors="white",
       linewidths=0.7,
       linestyles="solid",
       transform=ccrs.PlateCarree()
   )
   ax.clabel(contours, inline=True, fontsize=8, fmt="%d m")

   plt.colorbar(mesh, ax=ax, orientation="vertical", shrink=0.7, label="Profundidad (m)")
   plt.title("Mapa Batimetrico Regional con Isobatas", fontsize=12)
   plt.show()

Ejercicios de la Sesion
-----------------------

1. Cree un mapa cartográfico en proyección Mercator centrado en su zona de estudio con líneas de costa de resolución intermedia.
2. Superponga el campo satelital de temperatura superficial usando la paleta `cmocean.cm.thermal` y añada las isobatas de 200 y 1000 metros.
