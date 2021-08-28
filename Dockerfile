FROM python:3.9-slim-buster

## install dependencies
RUN apt update && apt install jq -y
COPY ./Pipfile.lock ./Pipfile.lock
RUN jq -r '.default | to_entries[] | .key + .value.version ' Pipfile.lock > requirements.txt
RUN pip install -r requirements.txt


## Dagster
ENV DAGSTER_HOME=/opt/dagster/home
ENV DAGSTER_APP=/opt/dagster/app
ENV DAGSTER_DAGS=/opt/dagster/dags

RUN mkdir -p ${DAGSTER_HOME} ${DAGSTER_APP}


# Dagster Config
COPY dagster.yaml.sh ${DAGSTER_HOME}/dagster.yaml.sh
RUN chmod +x ${DAGSTER_HOME}/dagster.yaml.sh


## Entrypoint
WORKDIR ${DAGSTER_DAGS}
VOLUME ${DAGSTER_DAGS}

COPY entrypoint.sh ${DAGSTER_APP}/entrypoint.sh
RUN chmod +x ${DAGSTER_APP}/entrypoint.sh

ENTRYPOINT ["/opt/dagster/app/entrypoint.sh"]
