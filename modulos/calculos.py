def procesar_producto(texto):
    # Simulación de procesamiento (puedes adaptarlo)
    if "kg" in texto.lower():
        datos = texto.split()
        peso = float(datos[0])
        descripcion = " ".join(datos[2:-2])
        precio_total = int(datos[-1])
        precio_libra = round(precio_total / (peso * 2.20462), 2)  # Convierte kg a libras
        return {
            "descripcion": descripcion,
            "peso_kg": peso,
            "precio_total": precio_total,
            "precio_por_libra": precio_libra
        }
    else:
        return {"descripcion": texto, "detalle": "Sin cálculo especial"}
