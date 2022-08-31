#!/usr/bin/env python3
"""Get locale from request"""
from flask_babel import Babel
from flask import Flask, render_template
app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    supported_languages = ["en", "fr"]
    return request.accept_languages.best_match(supported_languages)
