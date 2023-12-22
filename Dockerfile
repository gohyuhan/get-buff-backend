FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN apt-get update && \
    apt-get install -y postgresql-client

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
