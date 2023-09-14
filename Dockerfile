FROM python:3.8.7

ENV PYTHONUNBUFFERED 1

RUN apt install libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

EXPOSE 9000
STOPSIGNAL SIGINT
