#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    """return simple outputs"""
    return render_template('index.html')
