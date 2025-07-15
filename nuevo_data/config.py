# config.py
import google.generativeai as genai

# Aquí puedes cargar la clave API de una manera más segura, como desde una variable de entorno.
API_KEY_GEMINI = 'AIzaSyAupffvXcdU2kS6oOd2YekGUIHJVdER0bk'
genai.configure(api_key=API_KEY_GEMINI)

# Inicializa el modelo para reutilizarlo más tarde.
model = genai.GenerativeModel('gemini-2.5-flash')
