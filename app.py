@app.route("/")
def home():
    return "App rodando"

@app.route("/test-rd")
def test_rd():
    return "VERSAO NOVA 12345"
