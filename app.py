from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json()
    text = data.get("text", "")

    score = TextBlob(text).sentiment.polarity

    if score > 0:
        result = "Positive 😊"
    elif score < 0:
        result = "Negative 😡"
    else:
        result = "Neutral 😐"

    return jsonify({"sentiment": result})

if __name__ == "__main__":
    app.run(port=5000)