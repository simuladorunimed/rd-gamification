import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"ok": True, "service": "rd-gamification"})

@app.route("/test-rd")
def test_rd():
    return "rota test-rd funcionando"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
