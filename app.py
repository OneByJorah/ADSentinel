
import json, os
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def load_dc_status():
    path = os.path.join(os.path.dirname(__file__), "mock_dc_status.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []

@app.route("/")
def dashboard():
    dcs = load_dc_status()
    return render_template("dashboard.html", dcs=dcs, time=datetime.now())

@app.route("/public")
def public():
    dcs = load_dc_status()
    return render_template("public.html", dcs=dcs, time=datetime.now())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
