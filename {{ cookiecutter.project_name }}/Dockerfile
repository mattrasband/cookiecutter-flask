FROM python:3.6
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn --workers 4 --bind 0.0.0.0:5000 {{ cookiecutter.project_name }}.__main__:app
