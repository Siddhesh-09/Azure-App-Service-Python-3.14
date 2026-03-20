import os
from flask import Flask, render_template, jsonify
import datetime
import random

# --- PATH CONFIGURATION ---
# This ensures Azure finds your folders correctly
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, 
            template_folder=template_dir, 
            static_folder=static_dir)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        # If the file is still missing, this will tell us exactly where it's looking
        return f"Template Error: Flask is looking in {template_dir}. Error: {str(e)}", 500

@app.route('/api/telemetry')
def telemetry():
    return jsonify({
        "cpu": f"{random.randint(12, 28)}%",
        "ram": f"{random.randint(310, 480)}MB",
        "status": "OPERATIONAL",
        "node": "AZ-PRIMARY-CORE"
    })

if __name__ == '__main__':
    # Use 8080 for Azure compatibility
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
