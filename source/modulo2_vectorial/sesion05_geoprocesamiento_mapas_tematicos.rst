Sesion 5: Geoprocesamiento y Mapas Vectoriales Tematicos
========================================================

.. note::
   **Duracion:** 2 horas.
   **Librerias:** GeoPandas, Mapclassify, Contextily.
   **Tarea 1:** Generacion de un mapa vectorial tematico integrado.

Operaciones de Geoprocesamiento Espacial
----------------------------------------

Las operaciones espaciales permiten responder preguntas ecológicas y de manejo de recursos marinos:

- **Zonas de amortiguamiento (`buffer`):** Delimitar la zona de exclusión de pesca (ej. 5 km o 12 millas náuticas) alrededor de una isla o línea de costa.
- **Unión espacial (`sjoin`):** Vincular atributos según su posición topológica (ej. ¿qué estaciones oceanográficas caen dentro de qué Área Marina Protegida?).
- **Disolución (`dissolve`):** Agregar geometrías complejas basadas en una categoría común (ej. fusionar zonas de zonificación marina).

.. code-block:: python

   import geopandas as gpd

   # Suponiendo gdf_utm con estaciones proyectadas en metros
   # Buffer de 5,000 metros (5 km) de exclusion
   gdf_utm["buffer_5km"] = gdf_utm.geometry.buffer(5000)

   # Spatial Join con areas protegidas (amp_utm)
   # estaciones_en_amp = gpd.sjoin(gdf_utm, amp_utm, predicate="within")

Clasificacion Tematica con Mapclassify
--------------------------------------

Para representar gradientes de variables biogeoquímicas (como biomasa, temperatura o contaminantes) mediante mapas de coropletas o símbolos proporcionales, se utilizan esquemas de clasificación estadística:

- **Cuantiles (`quantiles`):** Distribuye un número idéntico de observaciones en cada categoría.
- **Intervalos naturales de Jenks (`natural_breaks`):** Minimiza la varianza intraclasal y maximiza la interclasal.
- **Intervalos iguales (`equal_interval`):** Divide el rango continuo en pasos idénticos.

.. code-block:: python

   import matplotlib.pyplot as plt

   fig, ax = plt.subplots(figsize=(9, 7))

   # Mapa tematico con esquema de intervalos de Jenks
   gdf.plot(
       column="chlorophyll_a",
       cmap="YlGn",
       scheme="natural_breaks",
       k=5,
       legend=True,
       legend_kwds={"title": "Clorofila-a (mg/m3)", "loc": "lower left"},
       markersize=80,
       edgecolor="black",
       ax=ax
   )
   ax.set_title("Distribucion de Clorofila-a en Estaciones de Monitoreo")
   plt.show()

Exploracion Interactiva con Leaflet (`.explore()`)
--------------------------------------------------

GeoPandas integra visualización web interactiva con un solo comando gracias a Folium:

.. code-block:: python

   # Genera un mapa interactivo con control de capas y mapas base
   gdf.explore(
       column="chlorophyll_a",
       cmap="viridis",
       tooltip=["station_id", "chlorophyll_a"],
       tiles="CartoDB positron"
   )

Tarea Practica 1
----------------

Elabore un mapa vectorial que integre:
1. Las estaciones de monitoreo de su proyecto con tamaño de símbolo proporcional a una variable biológica.
2. Los polígonos oficiales de las Áreas Marinas Protegidas de la región.
3. La línea de costa oficial de alta resolución.
4. Exportación en formato PNG con título y leyenda temática.
