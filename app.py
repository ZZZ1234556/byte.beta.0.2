from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
from agent import Agent

load_dotenv()

app = Flask(__name__)
client = OpenAI()
agent = Agent()

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Guardar mensaje del usuario
    agent.messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=agent.messages
        )

        # Obtener respuesta del asistente
        reply = response.choices[0].message.content

        # Guardar en historial
        agent.messages.append({"role": "assistant", "content": reply})

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=PORT)
