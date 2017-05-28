import os
import sys
import warnings
from pathlib import Path


PROJECT_ROOT = Path(__name__).parent.parent


class BaseConfig:
    """Basic config"""
    SECRET_KEY = None

    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def lazy_init(cls):
        """If any variables need to be configured or
        loaded from something unique, set them on the
        class with this method"""
        return cls


class Development(BaseConfig):
    SECRET_KEY = '{{ cookiecutter.project_name | upper }}_DEVELOPMENT'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:@localhost/{{ cookiecutter.project_name }}'  # noqa
    DEBUG = 1

    @classmethod
    def lazy_init(cls):
        if os.getenv('DATABASE_URL'):
            cls.SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
        return cls


class Testing(BaseConfig):
    SECRET_KEY = '{{ cookiecutter.project_name | upper }}_TESTING'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = 1


class Production(BaseConfig):
    """Production values should be from the environment
    and not hard coded in your config. These are simply
    placeholders for the values you know you need to set."""
    SECRET_KEY = None
    SQLALCHEMY_DATABASE_URI = None
    TESTING = 0
    DEBUG = 0

    @classmethod
    def lazy_init(cls):
        cls.SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        cls.SECRET_KEY = os.environ['SECRET_KEY']
        return cls


def resolve_config(env=''):
    if env in ['dev', 'development']:
        cls = Development
    elif env in ['uat', 'test', 'testing']:
        cls = Testing
    elif env in ['prod', 'production']:
        cls = Production
    else:
        warnings.warn('No environment was set with PY_ENV, you are '
                      'getting "prod" by default to be safe!')
        cls = Production

    return cls.lazy_init()

