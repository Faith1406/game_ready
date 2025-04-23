import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

app = Flask(__name__)


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Missing 'prompt' in request"}), 400
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash-8b",
            contents=prompt,
        )

        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
