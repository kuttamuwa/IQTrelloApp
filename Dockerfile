# base image
FROM python:3.8
RUN pip install --upgrade pip

ENV PYTHONBUFFERED=1
WORKDIR /app
COPY requirements.txt /app
COPY ctest.py /app
COPY . /app

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

#RUN python manage.py makemigrations
#RUN python manage.py migrate

#RUN python manage.py createsuperuser
#
#RUN python manage.py runserver