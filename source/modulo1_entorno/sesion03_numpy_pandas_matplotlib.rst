Sesion 3: Computacion Numerica y Visualizacion Cientifica Base
==============================================================

.. note::
   **Duracion:** 2 horas.
   **Librerias:** NumPy, Pandas, Matplotlib.
   **Conjunto de datos:** Perfiles de lances CTD oceanograficos en formato CSV.

Arreglos de NumPy: Calculo Vectorizado
--------------------------------------

NumPy proporciona arreglos multidimensionales (``ndarray``) optimizados en memoria, fundamentales para operar sobre miles de registros oceanograficos simultaneamente sin usar bucles lentos:

.. code-block:: python

   import numpy as np

   # Mediciones de temperatura in situ y salinidad practica
   depth = np.array([0.0, 10.0, 25.0, 50.0, 100.0, 200.0, 400.0])
   temp = np.array([25.4, 25.1, 23.8, 19.5, 14.2, 10.8, 7.5])
   sal = np.array([35.2, 35.2, 35.1, 34.8, 34.5, 34.4, 34.5])

   # Calculo de anomalia respecto a la media de la columna
   temp_anomaly = temp - np.mean(temp)
   print(f"Anomalias de temperatura: {temp_anomaly.round(2)}")

DataFrames con Pandas: Limpieza de Cruceros Oceanograficos
----------------------------------------------------------

Pandas es la herramienta estandar para el manejo de datos tabulares estructurados (archivos `.csv`, `.tsv` o bases de datos):

.. code-block:: python

   import pandas as pd

   # Simulacion de lectura de datos de crucero CTD
   data = {
       "station": ["B01", "B01", "B01", "B02", "B02", "B02"],
       "lat": [24.5, 24.5, 24.5, 24.8, 24.8, 24.8],
       "lon": [-111.2, -111.2, -111.2, -111.5, -111.5, -111.5],
       "depth_m": [5.0, 50.0, 150.0, 5.0, 50.0, 150.0],
       "temperature_C": [24.1, 18.2, 12.4, 23.8, 17.9, 11.8],
       "salinity_psu": [35.1, 34.9, 34.6, 35.0, 34.8, 34.5],
       "qc_flag": [1, 1, 1, 1, 1, 4]  # 1 = Bueno, 4 = Dato dudoso
   }
   df = pd.DataFrame(data)

   # Filtrado de calidad y calculo agrupado por estacion
   valid_data = df[df["qc_flag"] == 1]
   station_stats = valid_data.groupby("station")["temperature_C"].agg(["mean", "min", "max"])
   print("Estadisticas por estacion oceanografica:")
   print(station_stats)

Visualizacion de Perfiles Oceanograficos con Matplotlib
-------------------------------------------------------

En oceanografia fisica y quimica es una convencion estandar graficar la profundidad en el eje vertical invertido (con la superficie en 0 metros en la parte superior):

.. code-block:: python

   import matplotlib.pyplot as plt

   # Configuracion de figura cientifica de dos paneles
   fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6), sharey=True)

   # Panel 1: Temperatura
   ax1.plot(temp, depth, color="firebrick", marker="o", linewidth=2)
   ax1.set_xlabel("Temperatura (C)")
   ax1.set_ylabel("Profundidad (m)")
   ax1.set_title("Perfil Termico")
   ax1.grid(True, linestyle="--", alpha=0.6)
   ax1.invert_yaxis()  # Invertir eje: la superficie arriba

   # Panel 2: Salinidad
   ax2.plot(sal, depth, color="navy", marker="s", linewidth=2)
   ax2.set_xlabel("Salinidad (PSU)")
   ax2.set_title("Perfil Halino")
   ax2.grid(True, linestyle="--", alpha=0.6)

   plt.suptitle("Crucero Oceanografico - Estacion CTD Principal", fontsize=13)
   plt.tight_layout()
   plt.show()

Ejercicios de la Sesion
-----------------------

1. Cargue un archivo CSV de un crucero con datos de oxigeno disuelto y clorofila.
2. Genere una figura de publicacion con tres paneles que compare perfiles de temperatura, salinidad y oxigeno disuelto compartiendo el eje Y invertido.
