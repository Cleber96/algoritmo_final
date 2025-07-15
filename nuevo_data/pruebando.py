import os
import json
from config import model
history_file_path = "historial_conversacion.json"
def cargar_historial():
    if os.path.exists(history_file_path):
        with open(history_file_path, "r", encoding="utf-8") as file:
            try:
                history_data = json.load(file)
                return history_data
            except json.JSONDecodeError:
                # Si hay un error al decodificar JSON (ej. archivo vacío o corrupto),
                # se devuelve un historial vacío para empezar de nuevo.
                print(f"Advertencia: El archivo de historial '{history_file_path}' está corrupto o vacío. Se iniciará un nuevo historial.")
                return []
    return []
def guardar_historial(chat_history_obj):
    serializable_history = []
    for content in chat_history_obj:
        content_dict = {
            "role": content.role,
            "parts": []
        }
        for part in content.parts:
            if hasattr(part, 'text'):
                content_dict["parts"].append({"text": part.text})
        serializable_history.append(content_dict)

    with open(history_file_path, "w", encoding="utf-8") as file:
        json.dump(serializable_history, file, ensure_ascii=False, indent=4)
historial_cargado = cargar_historial()
chat = model.start_chat(history=historial_cargado)
mensaje = """
Hola, ¿cómo estás?
"""
response = chat.send_message(mensaje)
guardar_historial(chat.history)
output_file_path = "RIDME.md"
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(response.text)

print(f"{output_file_path}")
print(f"  File /home/cleber/Escritorio/Nueva carpeta 4/venv/lib/python3.12/site-packages/proto/message.py, line 877, in __getattr__   {history_file_path}" )