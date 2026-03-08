from fastapi import FastAPI
import requests
import os

app = FastAPI()

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/blenderbot-400M-distill"

headers = {
    "Authorization": f"Bearer {os.getenv("HF_TOKEN")}",
    "Content-Type": "application/json"
}

@app.get("/")
def home():
    return {"mensaje": "IA funcionando 🚀"}

@app.get("/chat")
def chat(msg: str):

    payload = {"inputs": msg}

    response = requests.post(API_URL, headers=headers, json=payload)

    return {"respuesta": response.json()}
