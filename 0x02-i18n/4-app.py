#!/usr/bin/env python3
"""
A basic Flask app with Babel setup locale selection & template parameterization
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale():
    """
    Get the best match language from the request or URL parameters.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Index route.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
