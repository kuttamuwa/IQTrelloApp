#FROM ubuntu:16.04
#FROM mongo:latest

# install python 3
#RUN apt-get update && apt-get install
#RUN apt-get install python3.8

FROM python:3
#RUN ec "Basliyoruz..."
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

#RUN python manage.py makemigrations
#RUN python manage.py migrate
#RUN echo "Makemigrations ve migrate tamamlandi"

#RUN python manage.py createsuperuser
#
#RUN python manage.py runserver