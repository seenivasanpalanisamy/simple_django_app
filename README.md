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