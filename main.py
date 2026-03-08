from fastapi import FastAPI
import requests
import os

app = FastAPI()

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

@app.get("/")
def home():
    return {"mensaje": "Servidor funcionando 🚀"}

@app.get("/chat")
def chat(msg: str):
    try:
        payload = {"inputs": msg}

        response = requests.post(API_URL, headers=headers, json=payload)

        return {
            "status_code": response.status_code,
            "respuesta": response.json()
        }

    except Exception as e:
        return {"error": str(e)}
