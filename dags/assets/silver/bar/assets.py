from dagster import graph_asset
from dagster import load_assets_from_current_module
from dagster import op

from dags.utils.db import write_to_db


@op()
def sailfish():
    return "gs://silver/bar/sailfish"


@graph_asset()
def eagle():
    return write_to_db(sailfish())


assets = load_assets_from_current_module()
