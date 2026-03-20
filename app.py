from flask import Flask, render_template, jsonify
import datetime
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/telemetry')
def telemetry():
    # Real-time simulated data for the dashboard
    return jsonify({
        "cpu": f"{random.randint(10, 30)}%",
        "ram": f"{random.randint(200, 500)}MB",
        "load": random.uniform(0.1, 0.9),
        "node": "AZ-PRIMARY-3.14"
    })

if __name__ == '__main__':
    app.run(debug=True)