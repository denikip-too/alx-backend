#!/usr/bin/env python3
"""Basic Babel setup"""
from flask_babel import Babel
from pytz import timezone, UTC
from flask import Flask, render_template
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """configure available languages in our app"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('Config')


@app.route('/', methods=['GET'])
def home():
    """return simple outputs"""
    return render_template('1-index.html')
