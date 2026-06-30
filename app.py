import json
import logging
import os
from pathlib import Path
from flask import Flask, jsonify, render_template

app = Flask(__name__)
logger = logging.getLogger(__name__)

# Checkpoint: preserve original expected contract globally so existing templates keep working
DATA: list = []

DATA_PATH = Path(__file__).with_name('mock_dc_status.json')


def _load_mock_data() -> list:
    try:
        with DATA_PATH.open('r', encoding='utf-8') as f:
            loaded = json.load(f)
        if isinstance(loaded, list):
            return loaded
        logger.warning('Unexpected mock data type in %s; defaulting to []', DATA_PATH)
        return []
    except FileNotFoundError:
        logger.warning('Mock data file not found at %s; defaulting to []', DATA_PATH)
        return []
    except json.JSONDecodeError as exc:
        logger.warning('Invalid JSON in %s (%s); defaulting to []', DATA_PATH, exc)
        return []


DATA = _load_mock_data()


@app.route('/')
def dashboard():
    return render_template('dashboard.html', dc_data=DATA)


@app.route('/public')
def public():
    return "🟢 All systems operational"


@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'mock_dc_count': len(DATA)}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
