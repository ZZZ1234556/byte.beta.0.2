import gradio as gr
from openai import OpenAI
import os

# Cliente OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def chat(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error IA: {str(e)}"

# Puerto Render
PORT = int(os.environ.get("PORT", 8080))

# Interface Gradio
iface = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text"
)

# Launch server
iface.launch(
    server_name="0.0.0.0",
    server_port=PORT
)
