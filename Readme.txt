#venv installation & activation
python -m venv venv
venv\Scripts\activate (windows)

#django installation:
pip install django
python -m django -- version

#admin overview:
django-admin
f.e. django-admin startproject <projectname>

#prjectstructure:
manage.py(runs command line commands, includes main method)
__init__.py (python package)
settings.py (settings and configurations, debugging, databases, security code)
urls.py (mapping for multiple urls)
wsgi.py (communication between webserver and app)

#force django to create auth tables
python manage.py migrate

#run the server (locally)
python manage.py runserver

#create a new app in the Python website/project
python manage.py startapp <name>

#create templates
appname -> templates -> appname -> template.html