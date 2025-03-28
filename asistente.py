from modulos import entrada_voz, entrada_texto, guardar_datos, calculos

class Asistente:
    def __init__(self):
        print("Iniciando Asistente Personal...")

    def ingresar_por_voz(self):
        print("Procesando entrada por voz...")
        datos = entrada_voz.capturar_entrada()
        self.procesar_y_guardar(datos)

    def ingresar_por_texto(self):
        print("Procesando entrada por texto...")
        datos = entrada_texto.capturar_entrada()
        self.procesar_y_guardar(datos)

    def procesar_y_guardar(self, datos):
        # Procesar datos
        producto = calculos.procesar_producto(datos)
        guardar_datos.guardar(producto)
        print("Datos procesados y guardados con éxito.")
