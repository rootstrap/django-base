# django-base

This project includes the basic boilerplate for a basic rest-api made in django.

## Create django project from django-base.
You can follow this steps to create a django project, using this one as a base.

1. Clone this repo: `$ git clone git@github.com:rootstrap/django-base.git` and change the folder name (django-base) to your new project name.
2. Move into the renamed folder and delete the track from git: `$ sudo rm -r ./git`
3. Change the main app name (django_base) to your new main app name.
4. Change all ocurrencies of django-base to your project name, and all ocurrencies of django_base to your main app name. You can use for example: `$ grep iRl "django-base" ./` in the project folder to search all ocurrencies.
5. Run `$ python manage.py runserver` and check the correct start, if you want to corroborate.
6. Create your project repo in github.
7. Run this commands to start track of git and push the project:
    * `$ git init`
    * `$ git add .`
    * `$ git commit -m "initial commit"`
    * `$ git remote add origin <url_from_your_repo>`
    * `$ git push -u origin master`

If everything went ok, you have now your project created with this one as a base.
You can follow the installation instructions to start working.

## Installation instructions.
- Create a virtual environment with: `mkvirtualenv <env_name>`
- Switch to the virtualenv with: `workon <env_name>`
- Install the dependencies: `$ pip install -r requirements.txt`
- Create a local_settings.py file (you can use the local_settings_template)
- Run the initial migrations: `$ python manage.py migrate`
- To add apps to the project you have to run: `$ python manage.py startapp <appname>`
- Edit the models.py as desired, and add the urls to api/urls.py

## Deploy to Heroku.
Rename the desired procfile from one of the examples.
Gunicorn is the standard for simple web apps wich rely on wsgi only.
If you need to use websockets and channels you'll need to use daphne to suport both asgi and wsgi.
