import os

import requests
from dagster import DagsterRunStatus
from dagster import run_failure_sensor
from dagster import run_status_sensor
from dagster import RunFailureSensorContext
from dagster import RunStatusSensorContext


DISCORD_WEBHOOK_URL_PASS = os.getenv("DISCORD_WEBHOOK_URL_PASS")
DISCORD_WEBHOOK_URL_FAIL = os.getenv("DISCORD_WEBHOOK_URL_FAIL")

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}


@run_failure_sensor(monitor_all_repositories=True)
def alert_failure(context: RunFailureSensorContext):
    message = f"""
    Job "{context.dagster_run.job_name}" failed.
    Error: {context.failure_event.message}
    Run ID: {context.dagster_run.run_id}
    """

    requests.post(DISCORD_WEBHOOK_URL_FAIL, json={"content": message})


@run_status_sensor(
    monitor_all_repositories=True,
    run_status=DagsterRunStatus.SUCCESS,
)
def alert_success(context: RunStatusSensorContext):
    message = f'Job "{context.dagster_run.job_name}" succeeded.'

    requests.post(DISCORD_WEBHOOK_URL_PASS, json={"content": message})


sensors = [
    alert_failure,
    alert_success,
]
