import os

from dagster import default_executors
from dagster import ModeDefinition
from dagster import pipeline
from dagster import PresetDefinition
from dagster import RunRequest
from dagster import sensor

from .solids import process_file
from utils.yaml_utils import yaml_to_dict


### MODE
local_mode = ModeDefinition(
    name="local",
    executor_defs=default_executors,
    resource_defs={},
)

### PRESETS
prod_preset = PresetDefinition.from_pkg_resources(
    name="prod",
    mode="local",
    pkg_resource_defs=[
        ("pipelines_cookbook.sensor.environments", "prod.yaml"),
    ],
)

dev_preset = PresetDefinition.from_pkg_resources(
    name="dev",
    mode="local",
    pkg_resource_defs=[
        ("pipelines_cookbook.sensor.environments", "dev.yaml"),
    ],
)


### SENSOR
@sensor(
    pipeline_name="cookbook_sensor",
    # minimum_interval_seconds=60*60, # 1 hr
    mode="local",
)
def cookbook_sensor_def(_context):
    MY_DIRECTORY = "data/for_sensor"

    for filename in os.listdir(MY_DIRECTORY):
        filepath = os.path.join(MY_DIRECTORY, filename)
        if os.path.isfile(filepath):
            run_config = yaml_to_dict(
                "pipelines_cookbook/sensor/environments/prod.yaml"
            )
            run_config["solids"]["process_file"]["config"]["filename"] = filename

            yield RunRequest(
                run_key=filename,
                run_config=run_config,
            )


### PIPELINES
@pipeline(mode_defs=[local_mode], preset_defs=[dev_preset, prod_preset])
def cookbook_sensor():
    process_file()


### REPOSITORY
pipelines = [cookbook_sensor]

sensors = [
    cookbook_sensor_def,  # local filesystem
    # cookbook_s3_sensor_def, # s3
]

repo = pipelines + sensors
