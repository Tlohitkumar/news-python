from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/bias', methods=['POST'])
def bias():
    data = request.get_json()
    text = data.get("text", "").lower()

    left_words = ["welfare", "rights", "equality", "climate", "workers"]
    right_words = ["tax", "security", "military", "border", "business"]

    left_score = sum(word in text for word in left_words)
    right_score = sum(word in text for word in right_words)

    if left_score > right_score:
        result = "Left Leaning 🔵"
    elif right_score > left_score:
        result = "Right Leaning 🔴"
    else:
        result = "Neutral ⚪"

    return jsonify({"bias": result})

if __name__ == "__main__":
    app.run(port=5000)