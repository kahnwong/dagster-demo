import os

from dagster import default_executors
from dagster import ModeDefinition
from dagster import pipeline
from dagster import PresetDefinition
from dagster import ScheduleDefinition

from .solids import step_five
from .solids import step_four
from .solids import step_one
from .solids import step_seven
from .solids import step_six
from .solids import step_three
from .solids import step_two

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
        ("pipelines_cookbook.cookbook.environments", "prod.yaml"),
    ],
)

dev_preset = PresetDefinition.from_pkg_resources(
    name="dev",
    mode="local",
    pkg_resource_defs=[
        ("pipelines_cookbook.cookbook.environments", "dev.yaml"),
    ],
)


### PIPELINES
@pipeline(mode_defs=[local_mode], preset_defs=[dev_preset, prod_preset])
def cookbook():
    one = step_one()
    two = step_two()
    three = step_three(one, two)

    four = step_four()
    five = step_five()
    six = step_six(four, five)

    step_seven(three, six)


### REPOSITORY
pipelines = [cookbook]

schedules = [
    ScheduleDefinition(
        name="cookbook",
        cron_schedule="* * * * *",
        pipeline_name="cookbook",
        run_config=prod_preset.run_config,
        environment_vars=dict(os.environ),
        execution_timezone="Asia/Bangkok",
        mode="local",
    )
]

repo = pipelines + schedules
