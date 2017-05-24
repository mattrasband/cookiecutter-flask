from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def init_app(app):
    """
    Initialize the external application dependencies

    :param app: Flask application instance
    """
    for extension in [db, login_manager]:
        extension.init_app(app)
    Migrate(db, app)

