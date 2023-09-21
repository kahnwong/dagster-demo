from dagster import asset
from dagster import DailyPartitionsDefinition
from dagster import load_assets_from_current_module

daily_partitions_def = DailyPartitionsDefinition(
    start_date="2023-06-01", timezone="Asia/Bangkok"
)


@asset(
    key_prefix=["bronze", "bar"],
    group_name="bar",
)
def c():
    return [1, 2, 3]


@asset(
    key_prefix=["bronze", "bar"], group_name="bar", partitions_def=daily_partitions_def
)
def d(context):
    context.log.info(f"bar: {context.asset_partition_key_for_output()}")

    return [1, 2, 3]


assets = load_assets_from_current_module()
