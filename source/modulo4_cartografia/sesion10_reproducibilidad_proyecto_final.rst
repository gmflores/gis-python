Sesion 10: Taller de Reproducibilidad, Revision de Pares y Presentacion
========================================================================

.. note::
   **Duracion:** 2 horas.
   **Producto final del curso:** Repositorio en GitHub con script reproducible `.py` y figura cartográfica de alta resolución del área de tesis.

De Cuaderno Exploratorio a Script `.py` Modular
-----------------------------------------------

Los cuadernos Jupyter son ideales para experimentación interactiva, pero los flujos reproducibles requieren scripts estructurados y ejecutables desde la terminal de forma no interactiva.

Estructura de Carpetas del Repositorio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   tesis-cartografia-marina/
   ├── .gitignore
   ├── README.md
   ├── environment.yml
   ├── data/
   │   ├── raw/           # Datos crudos inmutables
   │   └── processed/     # Capas recortadas o reclasificadas
   ├── src/
   │   ├── __init__.py
   │   ├── procesamiento.py
   │   └── generar_mapa.py
   └── figures/
       ├── figura1_mapa_estudio.pdf
       └── figura1_mapa_estudio.tif

Manejo de Rutas Relativas con `pathlib`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pathlib import Path
   import geopandas as gpd

   # Definir rutas relativas a la ubicacion del script
   BASE_DIR = Path(__file__).resolve().parent.parent
   DATA_DIR = BASE_DIR / "data" / "processed"
   OUT_DIR = BASE_DIR / "figures"
   OUT_DIR.mkdir(exist_ok=True)

   # Cargar capa espacial de forma 100% reproducible
   gdf = gpd.read_file(DATA_DIR / "estaciones.gpkg")

Rubrica de Evaluacion del Proyecto Final
----------------------------------------

El proyecto final representa el **40 %** de la calificacion total del curso:

1. **Rigor y Exactitud Cientifica (30 %):**
   - Sistema de Referencia de Coordenadas (CRS) pertinente para la región marina.
   - Fuentes de datos oficiales citadas explícitamente en el mapa o metadatos (GEBCO, Natural Earth, Copernicus).
2. **Diseno y Calidad Cartografica (30 %):**
   - Jerarquía visual clara: los datos del estudio destacan sobre el mapa base.
   - Elementos presentes: escala gráfica métrica, flecha de norte, cuadrícula rotulada y leyenda legible.
   - Paleta de color perceptualmente uniforme (`cmocean`) y apta para personas con daltonismo.
3. **Calidad Editorial para Publicacion (20 %):**
   - Dimensiones ajustadas a las normas de una revista científica internacional (1 o 2 columnas).
   - Tipografía legible (entre 7 y 10 puntos).
   - Exportación a 300+ DPI en formato vectorial (PDF) y matricial (TIFF).
4. **Reproducibilidad y Codigo en GitHub (20 %):**
   - Repositorio limpio con `README.md`, `environment.yml` y `.gitignore`.
   - Script ejecutable de inicio a fin que genera la figura final sin intervención manual.

Taller de Revision Cruzada entre Pares
--------------------------------------

Durante la última hora de la sesión, los estudiantes intercambian sus mapas y repositorios para verificar:

- [ ] ¿El script se ejecuta sin errores en la máquina del compañero utilizando el entorno ``geo-marinas``?
- [ ] ¿La proyección elegida distorsiona indebidamente las áreas o distancias marítimas?
- [ ] ¿Se leen con facilidad todos los rótulos a escala de impresión del artículo?
