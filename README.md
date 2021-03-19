# IQ Vizyon Trello Application
Sample Trello application for IQ Vizyon with DRF/ORM and MongoDB
Web socket is provided by Django
API is provided by DRF (Django Rest Framework)

Djongo is used to manage models and controllers with MongoDB.

yagmail is used to send mails.

# Installation
Python >= 3.6

We recommend you to use pip
pip install -r requirements.txt 


# 2. Step
Do not forget to activate your env via source / activate.bat

python manage.py makemigrations
python manage.py migrate

# 3. Step
You should create your super user in Django before run server
python manage.py createsuperuser

Then you can run server.
* python manage.py runserver

# ! Note ! :
You should set DEBUG=False if you want to create some init data.
Do not set True before you migrate and createsuperuser.

# API Endpoints
/cards
/comments
/boards

# Docker
I couldn't fully handle with docker and docker-compose. Yet, there is Dockerfile and docker-compose.yml
You can solve if you will.