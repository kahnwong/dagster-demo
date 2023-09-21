from dagster import Definitions
from dagster import load_assets_from_package_module

from . import assets
from .assets.bronze.bar import job as bronze_bar_job
from .assets.bronze.bar import schedule as bronze_bar_schedule
from .assets.bronze.foo import job as bronze_foo_job
from .assets.bronze.foo import schedule as bronze_foo_schedule
from .assets.silver.foo import job as silver_foo_job
from .assets.silver.foo import schedule as silver_foo_schedule
from .sensors.alerts import sensors as maintenance_sensors


defs = Definitions(
    assets=load_assets_from_package_module(assets),
    jobs=[bronze_foo_job, bronze_bar_job, silver_foo_job],
    schedules=[bronze_foo_schedule, bronze_bar_schedule, silver_foo_schedule],
    sensors=[*maintenance_sensors],
    # resources=cookbook_all_resources,
)
