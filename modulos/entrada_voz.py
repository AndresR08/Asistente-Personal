import speech_recognition as sr

def capturar_entrada():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Habla ahora...")
        try:
            audio = recognizer.listen(source)
            texto = recognizer.recognize_google(audio, language="es-ES")
            print(f"Texto capturado: {texto}")
            return texto
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        except sr.RequestError:
            print("Error en el servicio de reconocimiento de voz.")
