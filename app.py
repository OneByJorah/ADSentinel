import json
from flask import Flask, render_template

app = Flask(__name__)

# Load mock data
with open('mock_dc_status.json', 'r') as f:
    data = json.load(f)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', dc_data=data)

@app.route('/public')
def public():
    return "🟢 All systems operational"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
