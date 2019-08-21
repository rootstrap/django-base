# django-base

This project includes the basic boilerplate for a basic rest-api made in django.

## Installation instructions.
- Clone the Repo: `$ git clone git@github.com:rootstrap/django-base.git`
- Create a virtual environment with `mkvirtualenv <env_name>`
- Switch to the virtualenv with `workon <env_name>`
- Install the dependencies: `$ pip install -r requirements.txt`
- Run the initial migrations: `$ python manage.py migrate`
- To add apps to the project you have to run: `$ python manage.py startapp <appname>`
- Edit the models.py as desired, and add the urls to api/urls.py

## Deploy to Heroku.

Rename the desired procfile from one of the examples.
Gunicorn is the standard for simple web apps wich rely on wsgi only.
If you need to use websockets and channels you'll need to use daphne to suport both asgi and wsgi.

## Running on docker

Install Docker official mac app https://hub.docker.com/editions/community/docker-ce-desktop-mac .  
Start Docker, login on docker (with `docker login`) and run the following commands:
1. `docker-compose build` to create the image.
2. `docker-compose run web python manage.py migrate` to run migrations.
3. `docker-compose run web` to start the backend on port 8000 (you can change this in the docker-compose.yml).
