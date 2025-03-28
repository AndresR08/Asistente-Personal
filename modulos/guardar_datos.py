import json
import os
from scripts.config import CONFIGURACION

def guardar(producto):
    ruta = CONFIGURACION["ruta_datos"]
    if os.path.exists(ruta):
        with open(ruta, "r") as archivo:
            datos = json.load(archivo)
    else:
        datos = []

    datos.append(producto)

    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)
    print("Producto guardado correctamente.")
