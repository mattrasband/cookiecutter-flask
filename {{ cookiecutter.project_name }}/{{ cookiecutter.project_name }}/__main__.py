import os

from {{ cookiecutter.project_name }} import create_app, models
from {{ cookiecutter.project_name }}.config import resolve_config
from {{ cookiecutter.project_name }}.external import db



app = create_app(resolve_config(os.getenv('PY_ENV')))


@app.cli.command()
def routes():
    """List application routes"""
    routings = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        routings.append('{:30s} {:30s} {}'.format(rule.endpoint, methods,
                                                  rule))
    print(*sorted(routings))


def make_shell_context():
    """
    Factory to generate the shell context for the
    `flask shell` command.
    """
    ctx = dict(app=app, db=db)
    # Add all the models to the shell context
    for name, cls in models.__dict__.items():
        if isinstance(cls, db.Model):
            ctx[name] = cls
    return ctx


app.make_shell_context = make_shell_context


if __name__ == '__main__':
    app.run()

