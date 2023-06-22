ARG MODE_ENV

FROM python:3.11.2-slim AS base

FROM base AS branch-dev
ENV REQUIREMENTS_FILE=requirements/dev.txt

FROM base AS branch-prod
ENV REQUIREMENTS_FILE=./requirements/base.txt

FROM branch-${MODE_ENV:-prod} as final

RUN echo $REQUIREMENTS_FILE
RUN echo .
COPY $REQUIREMENTS_FILE /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /usr/src/app/
WORKDIR /usr/src/app/

CMD uvicorn main:app --host 0.0.0.0 --port 7000 --reload
