import speech_recognition as sr

def procesar_datos(datos):
    """Procesa los datos ingresados por texto o voz, calculando precio por libra si es necesario."""
    print("\nProcesando los datos...")
    # Intentar extraer cantidades, productos y precios del texto
    try:
        # Buscar patrón: 'X kg de PRODUCTO por Y'
        import re
        match = re.search(r"(\d+(?:\.\d+)?)\s*kg\s*de\s*(\w+)\s*por\s*(\d+)", datos, re.IGNORECASE)
        if match:
            cantidad_kg = float(match.group(1))  # Cantidad en kg
            producto = match.group(2)  # Producto
            precio_total = int(match.group(3))  # Precio total

            # Calcular precio por libra (1 kg = 2.20462 libras)
            precio_por_libra = precio_total / (cantidad_kg * 2.20462)

            # Mostrar los resultados
            print(f"\nProducto: {producto.capitalize()}")
            print(f"Cantidad: {cantidad_kg} kg")
            print(f"Precio total: ${precio_total}")
            print(f"Precio por libra: ${precio_por_libra:.2f}")
        else:
            print("No se pudo interpretar la entrada. Por favor, usa un formato como '5 kg de banano por 5000'.")
    except Exception as e:
        print(f"Error procesando los datos: {e}")

def ingresar_por_texto():
    """Permite ingresar los datos manualmente por texto."""
    print("\nModo: Ingreso por texto")
    datos = input("Escribe los datos de tus compras (ej. '5 kg de banano por 5000'): ")
    procesar_datos(datos)

def ingresar_por_voz():
    """Permite ingresar los datos por voz utilizando reconocimiento de habla."""
    print("\nModo: Ingreso por voz")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Habla ahora...")
        try:
            audio = recognizer.listen(source)
            datos = recognizer.recognize_google(audio, language="es-ES")
            print(f"Has dicho: {datos}")
            procesar_datos(datos)
        except sr.UnknownValueError:
            print("No se pudo entender lo que dijiste. Por favor, intenta de nuevo.")
        except sr.RequestError:
            print("Error con el servicio de reconocimiento de voz. Revisa tu conexión a internet.")

def menu_principal():
    """Muestra el menú principal para elegir el método de ingreso."""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ingresar datos por texto")
        print("2. Ingresar datos por voz")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            ingresar_por_texto()
        elif opcion == "2":
            ingresar_por_voz()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
