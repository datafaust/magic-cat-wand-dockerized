#!/bin/bash
FROM python:3


RUN apt-get update \
    && apt-get install -y \
        build-essential \
        git \
        make \
        wget

COPY requirements.txt ./
RUN pip install -r requirements.txt
WORKDIR /

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]