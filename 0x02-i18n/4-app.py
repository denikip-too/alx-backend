#!/usr/bin/env python3
"""Basic Babel setup"""
from flask_babel import Babel
from pytz import timezone, UTC
from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """configure available languages in our app"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'])
def home() -> str:
    """return simple outputs"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    locale = 'fr'
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return (locale)
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
