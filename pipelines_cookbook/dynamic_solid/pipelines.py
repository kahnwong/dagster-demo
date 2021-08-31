from dagster import default_executors
from dagster import ModeDefinition
from dagster import pipeline
from dagster import PresetDefinition

from .solids import count_prtns
from .solids import return_partitions
from .solids import sum_total_prtns


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
        ("pipelines_cookbook.dynamic_solid.environments", "prod.yaml"),
    ],
)

dev_preset = PresetDefinition.from_pkg_resources(
    name="dev",
    mode="local",
    pkg_resource_defs=[
        ("pipelines_cookbook.dynamic_solid.environments", "dev.yaml"),
    ],
)


### PIPELINES
@pipeline(mode_defs=[local_mode], preset_defs=[dev_preset, prod_preset])
def cookbook_dynamic_solid():
    chunk_partition_count = return_partitions().map(count_prtns)
    sum_total_prtns(chunk_partition_count.collect())


### REPOSITORY
pipelines = [cookbook_dynamic_solid]
schedules = []

repo = pipelines + schedules
