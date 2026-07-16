from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

@app.route("/")
def home():
    return "API Online!"

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    pergunta = data["message"]

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": pergunta
            }
        ]
    )

    return jsonify({
        "answer": resposta.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
