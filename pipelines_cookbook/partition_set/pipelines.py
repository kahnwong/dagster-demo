import os
from datetime import datetime
from datetime import time
from datetime import timedelta

from dagster import daily_schedule
from dagster import default_executors
from dagster import ModeDefinition
from dagster import pipeline
from dagster import PresetDefinition

from .solids import prtn_set
from utils.yaml_utils import yaml_to_dict

### MODE
local_mode = ModeDefinition(
    name="local",
    executor_defs=default_executors,
)

### PRESETS
prod_preset = PresetDefinition.from_pkg_resources(
    name="prod",
    mode="local",
    pkg_resource_defs=[
        ("pipelines_cookbook.partition_set.environments", "prod.yaml"),
    ],
)

dev_preset = PresetDefinition.from_pkg_resources(
    name="dev",
    mode="local",
    pkg_resource_defs=[
        ("pipelines_cookbook.partition_set.environments", "dev.yaml"),
    ],
)


### PIPELINES
@pipeline(mode_defs=[local_mode], preset_defs=[prod_preset, dev_preset])
def cookbook_partition_set():
    prtn_set()


### PARTITION SCHEDULES
@daily_schedule(
    pipeline_name="cookbook_partition_set",
    start_date=datetime.now() - timedelta(days=30 * 2),  # T-2 months
    execution_time=time(15, 15),
    environment_vars=dict(os.environ),
    execution_timezone="Asia/Bangkok",
    mode="local",
)
def cookbook_partition_set_schedule(day):
    run_config = yaml_to_dict("pipelines_cookbook/partition_set/environments/prod.yaml")
    run_config["solids"]["prtn_set"]["config"]["day"] = str(day.date())

    return run_config


### REPOSITORY
pipelines = [cookbook_partition_set]
schedules = [cookbook_partition_set_schedule]

repo = pipelines + schedules
