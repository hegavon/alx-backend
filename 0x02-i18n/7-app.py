#!/usr/bin/env python3
"""
Basic Flask app with Babel setup locale & timezone selection & user login mock
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_timezone
import pytz


class Config:
    """
    Config class for setting up Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieve user from the request.
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    Set up user before handling the request.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Get the best match language from the request URL parameters / user settings
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Get the timezone from the request or user settings.
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except pytz.UnknownTimeZoneError:
            pass
    if g.user:
        user_timezone = g.user.get('timezone')
        try:
            return pytz.timezone(user_timezone)
        except pytz.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """
    Index route.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
