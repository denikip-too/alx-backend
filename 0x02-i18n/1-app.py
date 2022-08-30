#!/usr/bin/env python3
"""Basic Babel setup"""
from flask_babel import Babel
from pytz import timezone, UTC
from babel import Locale
app = Flask(__name__)


babel = Babel(app)


class config(object):
    """configure available languages in our app"""

    LANGUAGES = ['en', 'fr']

    def __init__(self, default_locale='en', default_timezone='UTC'):
        """set Babel’s default locale ("en") and timezone ("UTC")"""
        self._default_locale = default_locale
        self._default_timezone = default_timezone
        self.app = app

    @property
    def default_timezone(self):
        """The default timezone from the configuration as instance of a
        `pytz.timezone` object.
        """
        return timezone(self.app.config['BABEL_DEFAULT_TIMEZONE'])

    @property
    def default_locale(self):
        """The default locale from the configuration as instance of a
        `babel.Locale` object.
        """
        return Locale.parse(self.app.config['BABEL_DEFAULT_LOCALE'])

    @app.route('/')
    def local_time():
        """display local time"""
        return (render_template(
            '1-index.html', utc_dt=self.default_timezone()))
