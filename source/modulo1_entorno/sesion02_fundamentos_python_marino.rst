Sesion 2: Fundamentos de Python Aplicados a Datos Marinos
=========================================================

.. note::
   **Duracion:** 2 horas.
   **Objetivo central:** Dominar tipos de datos, estructuras y funciones en Python a traves de ejemplos oceanograficos reales.

Tipos de Datos Primarios y Variables
------------------------------------

En oceanografia, trabajamos constantemente con numeros enteros (conteo de muestras), flotantes (temperatura, salinidad, profundidad), cadenas de texto (identificadores de estaciones) y booleanos (control de calidad):

.. code-block:: python

   station_id = "CTD-B01"      # Cadena (str)
   latitude = 24.1425           # Flotante (float)
   longitude = -110.3128        # Flotante (float)
   depth_m = 450.5              # Profundidad en metros (float)
   qc_passed = True             # Bandera de calidad (bool)
   sample_count = 12            # Conteo de botellas Niskin (int)

Estructuras de Datos: Listas y Diccionarios
-------------------------------------------

Las **listas** almacenan secuencias ordenadas de valores (ej. profundidades de muestreo), mientras que los **diccionarios** vinculan claves y atributos (ej. metadatos de una estacion):

.. code-block:: python

   # Lista de profundidades estandar (metros)
   sampling_depths = [0, 10, 25, 50, 75, 100, 200, 500]

   # Diccionario con metadatos de estacion oceanografica
   station_metadata = {
       "cruise": "GOLFO-2026-I",
       "station": "E04",
       "lat_dms": (25, 30, 15.2),  # Grados, Minutos, Segundos
       "lon_dms": (-111, 12, 45.8),
       "bottom_depth_m": 820.0,
   }

Control de Flujo: Condicionales y Bucles
---------------------------------------

Iterar sobre perfiles oceanograficos y filtrar segun criterios fisicos:

.. code-block:: python

   temperatures = [24.5, 22.1, 18.3, 14.2, 11.0, 8.5]

   for temp in temperatures:
       if temp > 20.0:
           layer = "Capa superficial calida"
       elif temp >= 12.0:
           layer = "Termoclina"
       else:
           layer = "Agua profunda"
       print(f"Temperatura: {temp:4.1f} C -> {layer}")

Funciones Reutilizables: Conversion de Coordenadas
--------------------------------------------------

En bitacoras y cartas nauticas es habitual registrar coordenadas en formato sexagesimal (Grados, Minutos y Segundos). La libreria espacial requiere **Grados Decimales (DD)**:

.. math::

   \text{DD} = \text{Grados} + \frac{\text{Minutos}}{60} + \frac{\text{Segundos}}{3600}

.. code-block:: python

   def dms_to_dd(degrees: float, minutes: float, seconds: float, hemisphere: str = "N") -> float:
       """
       Convierte coordenadas de Grados, Minutos y Segundos (DMS) a Grados Decimales (DD).
       
       Parametros:
           degrees (float): Grados absolutos.
           minutes (float): Minutos sexagesimales.
           seconds (float): Segundos sexagesimales.
           hemisphere (str): Orientacion cardinal ('N', 'S', 'E', 'W').
       
       Retorna:
           float: Coordenada en grados decimales con signo apropiado.
       """
       dd = degrees + (minutes / 60.0) + (seconds / 3600.0)
       if hemisphere.upper() in ["S", "W"]:
           dd = -dd
       return round(dd, 6)

   # Ejemplo de aplicacion practica
   lat_estacion = dms_to_dd(24, 15, 30.5, "N")
   lon_estacion = dms_to_dd(110, 20, 15.0, "W")
   print(f"Coordenadas en Grados Decimales: ({lat_estacion}, {lon_estacion})")

Ejercicios de la Sesion
-----------------------

1. Escriba una funcion que reciba una lista de temperaturas registradas por un CTD y devuelva el gradiente termico vertical entre la superficie y la maxima profundidad.
2. Cree una lista de diccionarios representando tres estaciones oceanograficas con coordenadas en DMS y conviertalas a grados decimales mediante un bucle ``for``.
