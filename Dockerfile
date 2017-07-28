############################################################
# Spooncover app base Dockerfile
############################################################

FROM python:3.5

MAINTAINER Evgeny Shakhmaev

RUN apt-get update

RUN apt-get install -y tar git curl nano wget net-tools build-essential

RUN mkdir /project
COPY requirements.txt /project

RUN pip install --upgrade pip
RUN pip install -r /project/requirements.txt

COPY /. /project/sportrotter

WORKDIR /project

ENTRYPOINT ["python", "manage.py", "runserver"]