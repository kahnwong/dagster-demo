### Imports
from dagster import Field
from dagster import OutputDefinition
from dagster import solid

from utils.day_utils import get_day
from utils.sleep_utils import return_random_sleep


### SOLIDS
@solid(
    config_schema={"day": Field(str, is_required=True)},
    output_defs=[OutputDefinition(name="s3path", dagster_type=str)],
)
def prtn_set(context) -> str:
    log = context.log
    day = get_day(context.solid_config["day"], log)
    log.info(f"day: {day}")

    return_random_sleep()

    return "s3path"
