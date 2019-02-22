FROM python:3.7-alpine

LABEL Name=epl-translator Version=1.0.0
EXPOSE 8000

# TODO research multi stage build
RUN apk add --update make

WORKDIR /opt/app
ADD . /opt/app

RUN make install
RUN make tests

CMD make run_locally

