import os
from flask import Flask, render_template, jsonify
import datetime
import random

# This finds the exact folder where app.py lives
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

# Explicitly tell Flask where to look
app = Flask(__name__, 
            template_folder=template_dir, 
            static_folder=static_dir)

@app.route('/')
def index():
    return render_template('index.html')

# ... the rest of your routes ...
