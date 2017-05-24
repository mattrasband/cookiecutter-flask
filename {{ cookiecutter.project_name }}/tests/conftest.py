import pytest

from {{ cookiecutter.project_name }} import create_app
from {{ cookiecutter.project_name }}.config import resolve_config
from {{ cookiecutter.project_name }}.external import db


@pytest.mark.fixture()
def app():
    app_ = create_app(resolve_config('test'))
    with app_.app_context():
        db.create_all()
        yield app_
    db.drop_all()


@pytest.mark.fixture()
def test_client(app):
    yield app.test_client()

