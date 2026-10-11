Sesion 9: Elementos Cartograficos de Publicacion y Exportacion Editorial
========================================================================

.. note::
   **Duracion:** 2 horas.
   **Librerias:** Cartopy, Matplotlib-scalebar, Matplotlib.
   **Normas:** Directrices editoriales de revistas científicas internacionales (Elsevier, Springer, Nature).

Elementos Cartograficos Imprescindibles
---------------------------------------

Un mapa con calidad de publicación para un artículo o tesis debe contener una jerarquía visual equilibrada y los siguientes elementos:

1. **Escala gráfica métrica:** Proporciona escala proporcional exacta, adaptable a reescalados (`matplotlib_scalebar`).
2. **Flecha de norte (indicador de orientación):** Indispensable cuando el mapa utiliza proyecciones donde el norte no es paralelo al borde superior.
3. **Barra de color estructurada:** Con unidades del SI legibles y rangos físicos apropiados.
4. **Minimapa de localización contextual (*Inset map*):** Proporciona referencia geográfica continental o global del área de estudio.

.. code-block:: python

   import matplotlib.pyplot as plt
   from matplotlib_scalebar.scalebar import ScaleBar
   import cartopy.crs as ccrs

   fig, ax = plt.subplots(figsize=(8, 7), subplot_kw={"projection": ccrs.Mercator()})
   ax.set_extent([-112, -109, 23, 26], crs=ccrs.PlateCarree())

   # Agregar escala grafica metrica
   # Requiere que el mapa este proyectado (unidades en metros)
   scalebar = ScaleBar(1.0, "m", length_fraction=0.25, location="lower right")
   ax.add_artist(scalebar)

Insercion de Minimapas de Ubicacion (Inset Maps)
------------------------------------------------

.. code-block:: python

   # Crear un eje secundario dentro de la figura principal
   # Coordenadas relativas de la caja: [x_inicio, y_inicio, ancho, alto]
   inset_ax = fig.add_axes([0.15, 0.58, 0.25, 0.25], projection=ccrs.PlateCarree())
   inset_ax.set_extent([-125, -95, 14, 34], crs=ccrs.PlateCarree())

   # Caracteristicas del minimapa
   inset_ax.add_feature(cfeature.LAND, facecolor="lightgray")
   inset_ax.add_feature(cfeature.COASTLINE, linewidth=0.4)

   # Dibujar rectangulo rojo indicando la zona de estudio detallada
   import matplotlib.patches as mpatches
   rect = mpatches.Rectangle(
       (-112, 23), 3, 3,
       fill=False, edgecolor="red", linewidth=1.5,
       transform=ccrs.PlateCarree()
   )
   inset_ax.add_patch(rect)

Directrices de Revistas Cientificas y Exportacion
-------------------------------------------------

Para someter a revistas indexadas (Deep Sea Research, Progress in Oceanography, Limnology and Oceanography):

- **Dimensiones físicas:** 1 columna (80-90 mm), 1.5 columnas (120-140 mm) o 2 columnas (180-190 mm).
- **Tipografía:** Sans-serif accesible (Helvetica, Arial) en tamaños entre 7 pt (mínimo) y 10 pt (título).
- **Resolución:** Mínimo **300 DPI** para imágenes compuestas y **600 DPI** para arte lineal.
- **Formatos:** Vectoriales para texto y polígonos (PDF, SVG) o matriciales de compresión sin pérdida (TIFF con compresión LZW).

.. code-block:: python

   # Exportacion para revista cientifica (2 columnas = 180 mm ~ 7.08 pulgadas)
   plt.tight_layout()
   plt.savefig("figura1_area_estudio.pdf", format="pdf", bbox_inches="tight", dpi=300)
   plt.savefig("figura1_area_estudio.tif", format="tiff", dpi=300, pil_kwargs={"compression": "tiff_lzw"})

Ejercicios de la Sesion
-----------------------

1. Configure las dimensiones de su figura en pulgadas exactamente iguales al ancho de 2 columnas de la revista elegida para su tesis.
2. Incorpore un minimapa de localización contextual con caja delimitadora roja y exporte la figura en PDF vectorial y TIFF a 300 DPI.
