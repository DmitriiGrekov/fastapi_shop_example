FROM python:3.12.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /usr/src/app

COPY . .

RUN pip3 install --upgrade pip && pip3 install poetry
RUN poetry install
