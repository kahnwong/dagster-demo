from dagster import build_schedule_from_partitioned_job
from dagster import define_asset_job

from .assets import assets
from .assets import daily_partitions_def


job = define_asset_job(
    name="bronze_bar",
    selection=assets,
    partitions_def=daily_partitions_def,
)

schedule = build_schedule_from_partitioned_job(job, minute_of_hour=15, hour_of_day=15)
