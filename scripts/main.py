import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from asistente import Asistente

def main():
    print("Bienvenido al Asistente Personal")
    print("1. Ingresar datos por voz")
    print("2. Ingresar datos por texto")
    opcion = input("Elige una opción (1/2): ")

    # Crear instancia del asistente
    asistente = Asistente()

    if opcion == "1":
        asistente.ingresar_por_voz()
    elif opcion == "2":
        asistente.ingresar_por_texto()
    else:
        print("Opción no válida")
        return

if __name__ == "__main__":
    main()
