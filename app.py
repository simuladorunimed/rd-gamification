mport os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

RD_CRM_TOKEN = os.environ.get("RD_CRM_TOKEN")
RD_CRM_BASE_URL = "https://crm.rdstation.com/api/v1"


def rd_headers():
    return {
        "accept": "application/json",
        "content-type": "application/json",
    }


def ensure_token():
    if not RD_CRM_TOKEN:
        raise RuntimeError("RD_CRM_TOKEN não configurado")


def check_rd_token():
    ensure_token()
    url = f"{RD_CRM_BASE_URL}/token/check"
    params = {"token": RD_CRM_TOKEN}
    r = requests.get(url, headers=rd_headers(), params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def criar_negociacao(payload):
    ensure_token()
    url = f"{RD_CRM_BASE_URL}/deals"
    params = {"token": RD_CRM_TOKEN}
    r = requests.post(url, headers=rd_headers(), params=params, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()


@app.route("/")
def home():
    return "App rodando"


@app.route("/test-rd")
def test_rd():
    try:
        result = check_rd_token()
        return jsonify({"ok": True, "rd_response": result})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500
