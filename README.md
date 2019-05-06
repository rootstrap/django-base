# django-base

This project includes the basic boilerplate for a basic rest-api made in django.

## Installation instructions.
- Clone the Repo: `$ git clone git@github.com:rootstrap/django-base.git`
- Create a virtual environment with `mkvirtualenv <env_name>`
- Install the dependencies: `$ pip install -r requirements.txt``
- Run the initial migrations: `$ python manage.py migrate``
- To add apps to the project you have to run: `$ python manage.py startapp <appname>``
- Edit the models.py as desired, and add the urls to api/urls.py
