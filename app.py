import json
from flask import Flask, render_template

app = Flask(__name__)

# ── Cargar datos ──────────────────────────────────────────────
with open("data.json", encoding="utf-8") as f:
    raw = json.load(f)

# ── Rutas ─────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
