# base image
FROM python:3.8

ENV PORT=8000

ENV PYTHONBUFFERED=1
WORKDIR /app
COPY requirements.txt /app
COPY ctest.py /app
COPY runforme.sh /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN bash runforme.sh

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000