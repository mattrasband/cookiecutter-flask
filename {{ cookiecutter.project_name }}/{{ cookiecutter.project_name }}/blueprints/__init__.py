import importlib
import os

from flask import Blueprint


def init_app(app):
    """Initialize the blueprints, this will automatically
    scan the current directory, find any blueprints, and
    auto register them. Note this will only work for files
    in this directory and currently does not traverse."""
    # TODO: walk nested modules
    for file_name in os.listdir(os.path.dirname(__file__)):
        if not file_name.startswith('_') and file_name.endswith('.py'):
            import_name = '.{}'.format(os.path.splitext(file_name)[0])
            bp_mod = importlib.import_module(import_name,
                                             package=__name__)
            for _, v in bp_mod.__dict__.items():
                if isinstance(v, Blueprint):
                    app.register_blueprint(v)
