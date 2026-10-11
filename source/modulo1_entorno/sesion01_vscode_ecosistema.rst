Sesion 1: Configuracion de VS Code y el Ecosistema Geoespacial
==============================================================

.. note::
   **Duracion:** 2 horas (40 min exposicion teorica, 80 min practica guiada).
   **Audiencia:** Estudiantes de posgrado en Ciencias Marinas sin experiencia previa en programacion.

Objetivos de Aprendizaje
------------------------

- Comprender la arquitectura de bibliotecas de codigo abierto en Python (GDAL, PROJ, GEOS).
- Instalar y configurar Miniforge y Mamba utilizando canales comunitarios (`conda-forge`).
- Configurar Visual Studio Code con las extensiones cientificas indispensables.
- Crear y verificar un entorno virtual aislado para analisis marino.

El Ecosistema Geoespacial de Python
-----------------------------------

A diferencia de los paquetes tradicionales de analisis numerico puro, las bibliotecas geoespaciales dependen de librerias binarias de bajo nivel escritas en C y C++:

- **GDAL/OGR:** Abstraccion universal para lectura y escritura de formatos raster y vectoriales.
- **PROJ:** Motor matematico para transformaciones y conversiones de coordenadas geodesicas.
- **GEOS:** Implementacion en C++ de la especificacion OpenGIS Simple Features para operaciones topologicas.

.. tip::
   El gestor de paquetes recomendado es **Miniforge** con canal por defecto ``conda-forge``. Esto garantiza que las librerias compiladas en C++ (como GDAL y GEOS) sean binariamente compatibles entre si, evitando errores criticos comunes en Windows y macOS.

Configuracion del Entorno con Mamba
-----------------------------------

El entorno del curso se define mediante un archivo ``environment.yml``:

.. code-block:: yaml

   name: geo-marinas
   channels:
     - conda-forge
     - nodefaults
   dependencies:
     - python=3.12
     - geopandas>=1.0
     - rasterio>=1.4
     - xarray>=2024.1
     - cartopy>=0.23
     - cmocean>=3.0

Para crear y activar el entorno desde la terminal integrada:

.. code-block:: bash

   # Crear el entorno virtual
   mamba env create -f environment.yml

   # Activar el entorno
   mamba activate geo-marinas

Extensiones Esenciales en VS Code
---------------------------------

Para un flujo de trabajo optimo en VS Code, se requieren las siguientes extensiones:

1. **Python (`ms-python.python`):** Proporciona IntelliSense, resaltado de sintaxis y depuracion.
2. **Jupyter (`ms-toolsai.jupyter`):** Permite ejecutar cuadernos interactivos `.ipynb` y la ventana interactiva.
3. **Ruff (`charliermarsh.ruff`):** Linter y formateador ultrarrapido para codigo limpio.

Verificacion del Entorno
------------------------

Cree un script llamado ``test_env.py`` o un cuaderno interactivo para validar la instalacion:

.. code-block:: python

   import geopandas as gpd
   import rasterio
   import xarray as xr
   import cartopy.crs as ccrs
   import cmocean

   print(f"GeoPandas version: {gpd.__version__}")
   print(f"Rasterio version:  {rasterio.__version__}")
   print(f"Xarray version:    {xr.__version__}")
   print("Exito: Todas las bibliotecas oceanograficas fueron importadas correctamente.")

Ejercicios de la Sesion
-----------------------

1. Verifique en la terminal de VS Code que el interprete activo apunte a la ruta de ``geo-marinas``.
2. Ejecute el script de prueba y registre en su cuaderno de notas las versiones exactas instaladas.
