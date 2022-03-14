#!/bin/bash
FROM python:3


RUN apt-get update \
    && apt-get install -y \
        build-essential \
        git \
        make \
        wget

COPY flask_app/requirements.txt ./
RUN pip install -r requirements.txt
#ADD . /flask_app
#WORKDIR /flask_app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]