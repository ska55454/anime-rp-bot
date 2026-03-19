from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]

    response = client.responses.create(
        model="gpt-5.2",
        instructions="""
Tu incarnes Aiko, une fille anime.

- Toujours en roleplay
- Ajoute des actions entre *...*
- Sois douce, taquine et naturelle
""",
        input=message
    )

    return jsonify({"reply": response.output_text})

app.run(host="0.0.0.0", port=3000)
