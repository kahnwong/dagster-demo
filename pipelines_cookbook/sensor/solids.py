### Imports
from dagster import solid

from utils.sleep_utils import return_random_sleep


### SOLIDS
@solid(config_schema={"filename": str})
def process_file(context):
    filename = context.solid_config["filename"]
    context.log.info(filename)

    return_random_sleep()
