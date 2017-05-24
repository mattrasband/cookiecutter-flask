from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from {{ cookiecutter.project_name }} import external


def create_app(config):
    """
    Flask application factory: generate a configured flask
    application.
    :param config: Configuration object or dictionary
    """
    app = Flask('{{ cookiecutter.project_name }}')

    app.config.from_object(config)

    external.init_app(app)

    # http://werkzeug.pocoo.org/docs/0.12/contrib/fixers/#werkzeug.contrib.fixers.ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    return app

