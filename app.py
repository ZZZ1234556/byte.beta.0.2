import os
import gradio as gr
from pathlib import Path
from gpt4all import GPT4All

# -------------------------------
# 1️⃣ Configuración del modelo
# -------------------------------

# Carpeta donde se descargará el modelo
model_dir = Path("models")
model_dir.mkdir(exist_ok=True)

# Descargar el modelo si no existe
model_path = model_dir / "gpt4all-lora-quantized.bin"
if not model_path.exists():
    print("Descargando modelo GPT4All...")
    # Nota: Debes colocar aquí la descarga del modelo o subirlo a tu repo
    # model_path = "ruta_al_modelo.bin"

# Cargar el modelo
model = GPT4All("ggml-gpt4all-j-v1.3-groovy")

# -------------------------------
# 2️⃣ Función del chat
# -------------------------------

def chat(user_input, chat_history=[]):
    """
    user_input: texto que envía el usuario
    chat_history: historial de conversación
    """
    # Concatenar historial + nuevo input
    prompt = "\n".join(chat_history + [f"Usuario: {user_input}", "IA:"])
    
    # Generar respuesta
    response = model.generate(prompt)
    
    # Agregar al historial
    chat_history.append(f"Usuario: {user_input}")
    chat_history.append(f"IA: {response}")
    
    # Retornar historial para mostrar en la interfaz
    return "\n".join(chat_history), chat_history

# -------------------------------
# 3️⃣ Interfaz Gradio
# -------------------------------

PORT = int(os.environ.get("PORT", 8080))

iface = gr.Interface(
    fn=chat,
    inputs=["text", "state"],
    outputs=["text", "state"],
    title="Byte.beta Gratis IA",
    description="Chat con modelo local GPT4All (gratis, sin OpenAI)"
)

# -------------------------------
# 4️⃣ Lanzar servidor
# -------------------------------

iface.launch(
    server_name="0.0.0.0",
    server_port=PORT
)
