# If you use oh-my-zsh:
# https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/autoenv
autostash FLASK_APP={{ cookiecutter.project_name }}/__main__.py
autostash FLASK_DEBUG=1
autostash PY_ENV=dev
