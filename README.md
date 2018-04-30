# simple_django_app

SETUP:

Installing dependencies, initialization:
```
pip install --upgrade -r requirements.txt   # install python dependencies 
python manage.py migrate    # initialize the django mysql database
```
CONFIG:

Set all environment variables needed
```
eg. DEBUG_LEVEL,DB configurations,HOST etc..
```

RUN:

```
python manage.py runserver
```

EXAMPLE:

This is an sample user commenting application with little features for create,update,delete operation.

Some urls as follwed
```
http://localhost:8000/details/
http://localhost:8000/home/
http://localhost:8000/create/?name=test1&comment=My1stdjangoapp&title=test
``` 

USED HOSTED MYSQL:

Temporarily used freemysqlhosting site for db.
```
'ENGINE': 'django.db.backends.mysql',
'NAME': 'sql12234563'
'USER': 'sql12234563',
'PASSWORD': 'V58C8ZFlFr',
'HOST': 'sql12.freemysqlhosting.net',
'PORT': '3360'
```

CLOUD SETUP:

Permanent setup as aws EC-2 instance.

1.Create an cloud instance with python,mysql installed
2.Clone the repo with git commands
3.Install nginx and uwsgi and config them to run multiple workers.
4.Run the django server with the help of uWSGI.

TASK COMPLETED:

1.Cloud setup
2.django application
3.Hosted the server in cloud
4.Git Repository
5.Rest api's
