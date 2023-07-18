FROM python:alpine
WORKDIR /app
COPY /requirements.txt  /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY .  .

CMD gunicorn -b 0.0.0.0:5000 run:app