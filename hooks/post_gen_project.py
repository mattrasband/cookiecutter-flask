#!/usr/bin/env python
import os


PROJECT_DIRECTORY = os.path.relpath(os.path.curdir)


def _rm(*files):
    for file_ in files:
        os.remove(os.path.join(PROJECT_DIRECTORY, file_))


if __name__ == '__main__':
    # delete out docker stuff if there is no org set
    if '{{ cookiecutter.docker_org }}' == '':
        _rm('Dockerfile', 'docker-compose.yml')

    if '{{ cookiecutter.autoenv }}' != 'y':
        _rm('.autoenv.zsh')
