import time
from openai import OpenAI
from dotenv import load_dotenv
from agent import Agent

load_dotenv()

print("😊 Bienvenido a byte.beta (version de prueba), sera un placer ayudarte 😉")

client = OpenAI()
agent = Agent()

# ----------------------------
# Efecto escribir letra por letra
# ----------------------------
def type_writer(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# ----------------------------
# Obtener respuesta IA
# ----------------------------
def get_response(agent, client):
    try:
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=agent.messages
        )

        if response and response.choices:
            reply = response.choices[0].message.content

            # Guardar en memoria
            agent.messages.append({
                "role": "assistant",
                "content": reply
            })

            return reply

        return ""

    except Exception as e:
        return f"Error IA: {e}"

# ----------------------------
# Loop principal
# ----------------------------
while True:
    user_input = input("Tú: ").strip()

    if not user_input:
        continue

    if user_input.lower() in ("salir", "exit", "bye"):
        print("👋 Hasta luego!")
        break

    # Guardar mensaje usuario
    agent.messages.append({
        "role": "user",
        "content": user_input
    })

    # Obtener respuesta
    reply = get_response(agent, client)

    # Mostrar letra por letra
    if reply:
        type_writer("IA: " + reply, delay=0.02)
