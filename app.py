import json
import os

from flask import Flask, render_template

app = Flask(__name__)

DATA_FILE = os.environ.get("STATUS_FILE", "mock_dc_status.json")


def load_status():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if not isinstance(data, list):
        data = []
    online = sum(1 for dc in data if str(dc.get("status", "")).lower() == "online")
    return {
        "datacenters": data,
        "total": len(data),
        "online": online,
        "status": "OPERATIONAL" if online == len(data) and data else "DEGRADED",
    }


@app.route("/")
def dashboard():
    return render_template("dashboard.html", **load_status())


@app.route("/public")
def public():
    return render_template("public.html", **load_status())


@app.route("/api/status")
def api_status():
    from flask import jsonify
    return jsonify(load_status())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
