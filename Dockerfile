FROM python:3.8-buster

WORKDIR /opt/bin
COPY wait-for-it.sh .

RUN pip install pipenv

WORKDIR /usr/src/app
COPY Pipfile* ./

ARG PIPENV_DEV
ENV PIPENV_DEV=${PIPENV_DEV}

RUN pipenv install --ignore-pipfile --deploy

ENV PYTHONPATH=${PYTHONPATH}:/usr/src/app/src

EXPOSE 5000

CMD [ "pipenv", "run", "serve" ]
