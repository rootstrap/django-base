
# django-base

  

This project includes the basic boilerplate for a basic rest-api made in django.

  

## Create django project from django-base.

You can follow this steps to create a django project, using this one as a base.

  

1. Clone this repo:

`$ git clone git@github.com:rootstrap/django-base.git` and change the folder name (django-base) to your new project name.

2. Move into the renamed folder and delete the track from git:

`$ sudo rm -r git`

3. Change the main app name (django_base) to your new main app name.

4. Change all ocurrencies of django-base to your project name, and all ocurrencies of django_base to your main app name. You can use for example:

`$ grep iRl "django-base" ./` in the project folder to search all ocurrencies.

5. Generate a unique secret key for your project:

+ `$ python manage.py shell` to open a Django bash.

+ `$ from django.core.management.utils import get_random_secret_key`

+ `$ get_random_secret_key()`. After this command, you get a secret key. Set the value in a virtual environment variable called `DJANGO_SECRET_KEY` (this will be used in settings).

6. If you want to corroborate, run:

`$ python manage.py runserver` and check the correct start.

  

If everything went ok, you have now your project created with this one as a base.

You can follow the installation instructions to start working.

  

## Installation instructions.

- Create a virtual environment with:

`$ mkvirtualenv <env_name>`

- Switch to the virtualenv with:

`$ workon <env_name>`

- Install the dependencies:

`$ pip install -r requirements.txt`

- Set general configuration in `<main_app_name>/settings/base.py` file. Then split the configuration for each environment you use, in different files under `<main_app_name>/settings/<env_name>.py`. After that, set on each environment you use, the `<env_name>` in a environment variable called `ENV_ROLE`. Default environment name is `development`.

- Run the initial migrations:

`$ python manage.py migrate`

- To add apps to the project you have to run:

`$ python manage.py startapp <appname>`

- Edit the models.py as desired, and add the urls to api/urls.py

  

## Deploy to Heroku.

Rename the desired procfile from one of the examples.

Gunicorn is the standard for simple web apps wich rely on wsgi only.

If you need to use websockets and channels you'll need to use daphne to suport both asgi and wsgi.

  

## Running on docker

  

Install Docker official mac app https://hub.docker.com/editions/community/docker-ce-desktop-mac .

Start Docker, login on docker (with `docker login`) and run the following commands:

1. `$ docker-compose build` to create the image.

2. `$ docker-compose run web python manage.py migrate` to run migrations.

3. `$ docker-compose run web` to start the backend on port 8000 (you can change this in the docker-compose.yml).

  

## Suggested project scaffolding

  

This is the suggested scaffolding for a django project. You can take a look at:

https://github.com/rootstrap/tech-guides

```

project_name

|

|__project_name(Here you should put all the settings for the app)

| |__ __init__.py

| |__settings

| |__ __init__.py

| |__ base.py

| |__ development.py

| |__ staging.py

| |__ production.py

| ...

| |__wsgi.py(optional)

| |__asgi.py(optional)

| |__urls.py

| ...

|

|__templates "Here are general templates, will be loaded last in the application"

|

|__api

| |__ __init__.py

| ...

| |__ urls.py (Use this file in order to route the apps located under the applications folder)

|

|__applications

| |__ __init__.py

| |__app1

| ... |__models.py(Split to folder and import models in __init__ if neccesary)

| |__views.py

| |__serializers.py

| |__urls.py

| |__test

| | |__requests

| | |__model_name_1

| | ... |__test_create

| | |__test_update

| | |__test_retrieve

| | |__test_delete

| | |__test_custom_functionality(optional)

| | ...

| |

| |__templates(Optional and not present if the project is api only)

| |

| |__api.py(Optional and not present if project is api only)

| ... (if needed add more files)

|

|__utils

| |__util_1.py

| |__util_2.py

...

```

## Libraries

| **Library** | **Description**
|----------|-------
|  [Django](https://github.com/django/django)  |   The Web framework for perfectionists with deadlines|
|  [Django all auth](https://github.com/pennersr/django-allauth)  |   Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication|
|  [Django rest framework](https://github.com/encode/django-rest-framework)  |   Web APIs for Django. 🎸|
|  [Django rest framework JWT](https://github.com/jpadilla/django-rest-framework-jwt)  |   JSON Web Token Authentication support for Django REST Framework|
|  [Django rest auth](https://github.com/Tivix/django-rest-auth)  |   This app makes it extremely easy to build Django powered SPA's (Single Page App) or Mobile apps exposing all registration and authentication related functionality as CBV's (Class Base View) and REST (JSON)|
|  [Django Heroku](https://github.com/heroku/django-heroku)  | A Django library for Heroku apps|
|  [django cors headers](https://github.com/adamchainz/django-cors-headers)  | Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS)|
|  [dj-database-url](https://github.com/jacobian/dj-database-url)  | Use Database URLs in your Django Application|
|  [defusedxml](https://github.com/tiran/defusedxml)  | Defusing XML bombs and other exploits|
|  [certifi](https://pypi.org/project/certifi/)  | Certifi is a carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. It has been extracted from the Requests project|
|  [chardet](https://pypi.org/project/chardet/)  | The Universal Character Encoding Detector|
|  [idna](https://pypi.org/project/idna/)  | Support for the Internationalised Domain Names in Applications|
|  [oauthlib](https://github.com/oauthlib/oauthlib)  | A generic, spec-compliant, thorough implementation of the OAuth request-signing logic|
|  [psycopg2](https://pypi.org/project/psycopg2/)  | Most popular PostgreSQL database adapter for the Python programming language|
|  [PyJWT](https://pypi.org/project/PyJWT/)  | A Python implementation of RFC 7519|
|  [python3-openid](https://pypi.org/project/python3-openid/)  | A set of Python packages to support use of the OpenID decentralized identity system|
|  [pytz](https://pypi.org/project/pytz/2005k/)  | World modern and historical timezone definitions|
|  [requests](https://pypi.org/project/requests/)  | Requests is the only Non-GMO HTTP library for Python, safe for human consumption|
|  [requests-oauthlib](https://github.com/requests/requests-oauthlib)  | OAuthlib support for Python-Requests!|
|  [six](https://pypi.org/project/six/)  | Six is a Python 2 and 3 compatibility library|
|  [sqlparse](https://pypi.org/project/sqlparse/)  | A non-validating SQL parser module. It provides support for parsing, splitting and formatting SQL statements|
|  [urllib3](https://pypi.org/project/urllib3/)  | A powerful, sanity-friendly HTTP client for Python|
|  [whitenoise](https://pypi.org/project/whitenoise/)  | Radically simplified static file serving for Python web apps|



## License

React Redux Base is available under the MIT license. See the LICENSE file for more info.

## Credits

**React Redux Base** is maintained by [Rootstrap](http://www.rootstrap.com) with the help of our [contributors](https://github.com/rootstrap/react-redux-base/contributors).

[<img src="https://s3-us-west-1.amazonaws.com/rootstrap.com/img/rs.png" width="100"/>](http://www.rootstrap.com)
