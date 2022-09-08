#!/usr/bin/env python3
"""Basic Babel setup"""
from flask_babel import Babel
from pytz import timezone, UTC
from datetime import datetime, timezone
from typing import Union
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
    current_time = datetime.now(timezone.utc)
    return render_template('index.html', current_time)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    locale = request.args.get('locale')
    if g.user.get("locale") is not None:
        return (locale)
    if locale in app.config['LANGUAGES']:
        return (locale)
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Infer appropriate time zone"""
    timezone = request.args.get("timezone")
    try:
        if g.user.get("timezone") is not None:
            return (timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"
    return (app.config['BABEL_DEFAULT_TIMEZONE'])


def get_user() -> Union[dict, None]:
    """returns a user dictionary"""
    try:
        login_as = request.args.get('login_as', None)
        user = users[int(login_as)]
    except Exception:
        user = None


@app.before_request
def before_request():
    """Define a before_request"""
    g.user = get_user()
