from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()
client = OpenAI()

@app.get("/")
def home():
    return {"mensaje": "🚀 Mi agente de IA está vivo"}

@app.get("/chat")
def chat(msg: str):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=msg
    )
    return {"respuesta": response.output_text}
