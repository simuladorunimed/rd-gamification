from flask import Flask, request, jsonify
import os

TARGET_PIPELINE = "Campanha A Grande Jogada"
TARGET_STAGE = "Novo Lead"

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"ok": True, "service": "rd-gamification"})

@app.post("/webhook")
def webhook():
    data = request.get_json(silent=True) or {}
    pipeline = data.get("pipeline")
    stage = data.get("stage")

    matched = pipeline == TARGET_PIPELINE and stage == TARGET_STAGE
    action = "create_task" if matched else "ignore"

    return jsonify({
        "received": True,
        "matched": matched,
        "action": action,
        "target_pipeline": TARGET_PIPELINE,
        "target_stage": TARGET_STAGE,
        "data": data
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
