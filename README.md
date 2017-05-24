# cookiecutter-flask

Cookiecutter template for how I write flask projects, usually kept up to date.

It includes the following:

* Basic flask app setup, using the application factory pattern
* Config is set up via classes, use `PY_ENV=<dev|test|prod>` to select, if ommitted an error is emitted.
* `Dockerfile` and `docker-compose.yml` to run local dependencies easily
* Flask, Flask-Login, Flask-SQLAlchemy, and postgres assumed

## Usage

If you don't have [cookiecutter](https://github.com/audreyr/cookiecutter) installed:

    pip install cookiecutter

Then generate the project, you will be prompted for configuration options:

    cookiecutter gh:mrasband/cookiecutter-flask

Notes:

* If no `docker_org` is provided, the docker files won't be included.
