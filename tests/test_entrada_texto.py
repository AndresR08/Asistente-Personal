from modulos import entrada_texto

def test_captura_texto():
    texto = "5 kg de banano por 5000"
    assert entrada_texto.capturar_entrada() == texto  # Esto es un ejemplo
