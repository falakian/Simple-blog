FROM python:alpine

RUN mkdir /app

ADD .  /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install flask gunicorn
RUN pip install flask_sqlalchemy
RUN pip install flask_bcrypt
RUN pip install flask_login
RUN pip install flask_wtf
RUN pip install wtforms
RUN pip install email_validator


CMD gunicorn -b 0.0.0.0:5000 run:app