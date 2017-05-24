import os
import sys
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
    SQLALCHEMY_DATABASE_URI = 'postgres://localhost/{{ cookiecutter.project_name }}'  # noqa
    DEBUG = 1

    @classmethod
    def lazy_init(cls):
        if os.getenv('DATABASE_URL'):
            cls.SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
        return cls


class Testing(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = 1


class Production(BaseConfig):
    SECRET_KEY = None
    SQLALCHEMY_DATABASE_URI = None

    @classmethod
    def lazy_init(cls):
        cls.SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        cls.SECRET_KEY = os.environ['SECRET_KEY']


def resolve_config(env=''):
    cls = None
    if env in ['dev', 'development']:
        cls = Development
    elif env in ['uat', 'test', 'testing']:
        cls = Testing
    elif env in ['prod', 'production']:
        cls = Production
    else:
        print('\n\n\tERROR: Invalid environment provided, set with '
              'PY_ENV=<env>\n\n', file=sys.stderr)
        raise SystemExit('Invalid environment provided.')

    return cls.lazy_init()

