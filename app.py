from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def mock_data():
    return [
        {"name": "DC-01", "status": "Healthy"},
        {"name": "DC-02", "status": "Warning"},
        {"name": "DC-03", "status": "Critical"}
    ]

@app.route("/")
def dashboard():
    return render_template("dashboard.html", dcs=mock_data(), time=datetime.now())

@app.route("/public")
def public():
    return render_template("public.html", dcs=mock_data(), time=datetime.now())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)