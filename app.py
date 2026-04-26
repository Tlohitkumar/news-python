from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# 😊 Sentiment + Trust + Summary
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

    summary = text[:120] + "..." if len(text) > 120 else text

    trust = 80
    if "fake" in text.lower() or "rumor" in text.lower():
        trust = 45

    return jsonify({
        "sentiment": result,
        "trust": trust,
        "summary": summary
    })


# ⚖️ Bias Detection
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


# 🚨 Fake News Detector
@app.route('/fakecheck', methods=['POST'])
def fakecheck():
    data = request.get_json()
    text = data.get("text", "").lower()

    suspicious_words = [
        "shocking",
        "viral",
        "secret",
        "exposed",
        "breaking",
        "rumor",
        "fake",
        "miracle"
    ]

    score = sum(word in text for word in suspicious_words)

    if score >= 3:
        result = "🚨 Possible Fake"
    elif score >= 1:
        result = "⚠️ Suspicious"
    else:
        result = "✅ Likely Real"

    return jsonify({
        "fakeStatus": result
    })


if __name__ == "__main__":
    app.run(port=5000)