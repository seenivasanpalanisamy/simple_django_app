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

NGINX CONFIG:

Add the following to nginx.conf file

```
server {
    # the port your site will be served on
    listen      80;
    server_name host_name;   # substitute by your FQDN and machine's IP address
    charset     utf-8;

    #Max upload size
    client_max_body_size 75M;   # adjust to taste

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
``` 

RUN:

```
python manage.py runserver
```

EXAMPLE:

This is an sample user commenting application with little features for create,update,delete operation.

Some apis as follwed
```
http://localhost:8000/details/
http://localhost:8000/home/
http://localhost:8000/create/?name=test1&comment=My1stdjangoapp&title=test
http://localhost:8000/update/?name=test1&comment=My1stdjangoapp&title=test&new_comment=My2ndjangoapp
http://localhost:8000/delete/?name=test1&comment=My1stdjangoapp&title=test
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

1.Create an cloud instance with python,mysql installed <br />
2.Clone the repo with git commands <br />
3.Install nginx and uwsgi and config them to run multiple workers. <br />
4.Run the django server with the help of uWSGI. <br />

TASK COMPLETED:

1.Cloud setup <br />
2.django application <br />
3.Hosted the server in cloud <br />
4.Git Repository <br />
5.Rest api's <br />
