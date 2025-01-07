from dagster import define_asset_job

from .assets import assets


job = define_asset_job(
    name="silver_bar_downstream_ops",
    selection=assets,
)
