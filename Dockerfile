FROM python:3.8
LABEL version="1.0.0"

ENV LC_ALL = C.UTF-8
ENV LANG = C.UTF-8
EXPOSE 80

COPY slit/requirements.txt /slit/requirements.txt

WORKDIR /slit/

RUN umask 002

RUN python -V
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN mkdir images

ADD . /slit

ENTRYPOINT [ "/bin/bash","slit/setup_env.sh" ]