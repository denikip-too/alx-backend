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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', methods=['GET'])
def home():
    """return simple outputs"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Get locale from request"""
    locale = request.args.get('locale')
    if users["locale"] is not None:
        return (users["locale"])
    if locale in app.config['LANGUAGES']:
        return (locale)
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Infer appropriate time zone"""
    timezone = pytz.timezone('users["timezone"]')
    try:
        if users["timezone"] is not None:
            return (users["timezone"])
    except pytz.exceptions.UnknownTimeZoneError:
        return ("validation fail")
    return (app.config['BABEL_DEFAULT_TIMEZONE'])


def get_user():
    """returns a user dictionary"""


@app.before_request
def before_request():
    """Define a before_request"""
    flask.g.user = get_user()
