from dagster import repository

from pipelines_cookbook.cookbook import pipelines as cookbook
from pipelines_cookbook.dynamic_solid import pipelines as dynamic_solid
from pipelines_cookbook.partition_set import pipelines as partition_set
from pipelines_cookbook.sensor import pipelines as sensor


@repository
def dagster_repository():
    return cookbook.repo + partition_set.repo + sensor.repo + dynamic_solid.repo
