# blog-post-django

## docker commands
docker volume inspect media

docker exec -it blogpost_backend bash > 

#### to open postgres terminal

psql -h database -U postgres -d blogpost

#### to open django terminal

python manage.py shell



## create the Default User
first make the first migration and then to migrate, add default user as a
default value. before the second migration create default user with below commands:

python manage.py shell

from django.contrib.auth.models import User

User.objects.create_user(username="default_user", password="default_password")


## delete existing migrations

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

find . -path "*/migrations/*.pyc" -delete

### drop database tables

docker-compose down -v

docker-compose up --build
