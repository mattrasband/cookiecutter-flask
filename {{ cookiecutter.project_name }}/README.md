# {{ cookiecutter.project_name }}

My awesome project does things.

## Development

Install the dependencies, this is often a one time task (but run it whenever they are updated):

    pip install -r requirements.txt

Set the application environment variables:

    export FLASK_APP={{ cookiecutter.project_name }}/__main__.py
    export FLASK_DEBUG=1
    export PY_ENV=dev

Initialize the database migrations (one time):

    flask db init

Run the app in development mode:

    flask run

{% if cookiecutter.docker_org != '' -%}
## Using Docker for local dev

    docker-compose up psql{%- endif %}

## Testing

    python -m pytest

## Style

    flake8

## Commands to be aware of:

    flask --help

    # Database
    flask db migrate -m "Auto create a new migration with this as a message"
    flask db upgrade

    # Info
    flask routes

