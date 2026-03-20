import os
import random
from flask import Flask, render_template, jsonify

# template_folder='.' tells Flask to look in the root for index.html
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/telemetry')
def telemetry():
    return jsonify({
        "cpu": f"{random.randint(10, 30)}%",
        "ram": f"{random.randint(200, 500)}MB",
        "status": "OPERATIONAL",
        "node": "AZ-PRIMARY-3.14"
    })

if __name__ == '__main__':
    # Azure uses port 8080 or the PORT environment variable
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
