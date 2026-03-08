from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

@app.get("/")
def home():
    return {"mensaje": "IA Groq funcionando 🚀"}

@app.get("/chat")
def chat(msg: str):

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": msg}
        ]
    )

    return {
        "respuesta": completion.choices[0].message.content
