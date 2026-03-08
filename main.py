from fastapi import FastAPI
import requests
import os

app = FastAPI()

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}

@app.get("/")
def home():
    return {"mensaje": "Mi IA funciona gratis 🚀"}

@app.get("/chat")
def chat(msg: str):
    payload = {"inputs": msg}

    response = requests.post(API_URL, headers=headers, json=payload)

    return {"respuesta": response.json()}
