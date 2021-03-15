# IQ Vizyon Trello Application
Sample Trello application for IQ Vizyon with DRF and MongoDB
Web socket is provided by Django
API is provided by DRF (Django Rest Framework)
Djongo is used to manage models and controllers with MongoDB.


# Installation
Python >= 3.6

You can use environment.yml if you wish to use conda.
However, some libraries may not be installed properly such as Djongo and Yagmail which are required libraries
to create collections into MongoDB while protecting Django ORM with Djongo.
Yagmail is also useful library to send mails on SMTP protocols.

So that, we recommend you to use to install libs
pip install -r requirements.txt 


# 2. Step
Do not forget to activate your env via source / activate.bat

python manage.py makemigrations
python manage.py migrate
* python manage.py runserver

# 3. Step
You should create your super user in Django before run server
python manage.py createsuperuser

Then you can run server.

# API Endpoints
/cards
/comments
/boards

