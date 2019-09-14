FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src