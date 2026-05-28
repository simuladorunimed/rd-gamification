from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"ok": True, "service": "rd-gamification"})

@app.post("/webhook")
def webhook():
    data = request.get_json(silent=True) or {}
    return jsonify({"received": True, "data": data})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)