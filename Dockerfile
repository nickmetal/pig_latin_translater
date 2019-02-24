FROM python:3.7-alpine

LABEL Name=epl-translator Version=1.0.0
EXPOSE 8000

# TODO research multi stage build
RUN apk add --update make

COPY requirements.txt /opt/app/
COPY Makefile /opt/app/

WORKDIR /opt/app
RUN make install

ADD . /opt/app

RUN make tests
CMD make run_locally