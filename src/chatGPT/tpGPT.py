import requests  # Importa la librería para hacer solicitudes a la API

# API key de Groq - aca iria la clave real
API_KEY = "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"

# URL base para acceder al modelo LLaMA 3 a través de Groq
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Función principal que ejecuta el ciclo del asistente conversacional
def main():
    last_query = ""  # Guarda la última consulta del usuario (para reutilizar en caso de presionar Enter)

    # ciclo de interacción con el usuario
    while True:
        try:
            # pide una consulta al usuario
            user_input = input("Ingresá tu consulta (o 'salir'): ")

            # Si el usuario escribe "salir", termina el programa
            if user_input.lower() == "salir":
                break

            # Si no escribe nada, reutiliza la última pregunta hecha
            if user_input.strip() == "" and last_query:
                user_input = last_query
                print("Reusando consulta anterior:", user_input)
            elif user_input.strip() != "":
                last_query = user_input  # Actualiza la última consulta

            # Muestra lo que el usuario escribió
            print("You:", user_input)

            # Cabeceras HTTP necesarias para autenticar la solicitud
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }

            # Cuerpo de la solicitud: incluye modelo, historial de mensajes y configuración
            data = {
                "model": "llama3-8b-8192",  
                "messages": [
                    {"role": "system", "content": "Sos un asistente conversacional que responde preguntas de manera clara y breve."},
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.7  
            }

            # Envia la solicitud POST a la API y captura la respuesta
            response = requests.post(API_URL, headers=headers, json=data)
            response.raise_for_status()  # Lanza error si hubo problemas en la solicitud

            # Extrae la respuesta generada desde el JSON devuelto por la API
            respuesta = response.json()["choices"][0]["message"]["content"]

            # Muestra la respuesta del modelo
            print("chatGPT:", respuesta)

        except Exception as e:
            # Manejo de errores generales (conexión, formato, etc.)
            print("Ocurrió un error:", e)

# Punto de entrada al programa
if __name__ == "__main__":
    main()