from flask import Flask, request, jsonify
import os

TARGET_PIPELINE = "Campanha A Grande Jogada"

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"ok": True, "service": "rd-gamification"})

@app.post("/webhook")
def webhook():
    data = request.get_json(silent=True) or {}
    pipeline = data.get("pipeline")
    matched = pipeline == TARGET_PIPELINE
    return jsonify({
        "received": True,
        "matched": matched,
        "target_pipeline": TARGET_PIPELINE,
        "data": data
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
