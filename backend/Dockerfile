ARG MODE_ENV

FROM python:3.11.2-slim AS base

FROM base AS branch-dev
ENV REQUIREMENTS_FILE=requirements/dev.txt

FROM base AS branch-prod
ENV REQUIREMENTS_FILE=requirements/base.txt

FROM branch-${MODE_ENV:-prod} as final

RUN echo $REQUIREMENTS_FILE
COPY $REQUIREMENTS_FILE /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /usr/src/app/
WORKDIR /usr/src/app/

ARG BACKEND_HOST
ENV ENV_BACKEND_HOST $BACKEND_HOST

ARG BACKEND_PORT
ENV ENV_BACKEND_PORT $BACKEND_PORT

CMD uvicorn main:app --host ${ENV_BACKEND_HOST} --port ${ENV_BACKEND_PORT} --reload

