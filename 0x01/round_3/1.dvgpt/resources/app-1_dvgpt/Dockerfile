FROM python:3.11-bullseye

RUN [ "mkdir", "-p", "/wsgi", "/frontend"]

COPY "wsgi/" "/wsgi"
COPY "frontend/" "/frontend"

RUN ["pip3", "install", "-r", "/wsgi/requirements.txt"]

WORKDIR "/wsgi"
CMD [ "bash", "start.sh"]
