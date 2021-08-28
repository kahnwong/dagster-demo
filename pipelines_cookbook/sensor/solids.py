### Imports
from dagster import solid


### SOLIDS
@solid(config_schema={"filename": str})
def process_file(context):
    filename = context.solid_config["filename"]
    context.log.info(filename)
