from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def get_strength_score(password: str) -> int:
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    return score

def score_to_label(score: int) -> str:
    if score == 0:
        return "Please enter a password"
    elif score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/check", methods=["POST"])
def api_check():
    data = request.get_json(force=True)
    password = data.get("password", "")
    score = get_strength_score(password)
    return jsonify({
        "score": score,
        "label": score_to_label(score)
    })

if __name__ == "__main__":
    app.run(debug=True)
