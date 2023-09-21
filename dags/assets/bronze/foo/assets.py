from dagster import asset
from dagster import DailyPartitionsDefinition
from dagster import load_assets_from_current_module

daily_partitions_def = DailyPartitionsDefinition(
    start_date="2023-06-01", timezone="Asia/Bangkok"
)


@asset(
    key_prefix=["bronze", "foo"],
    group_name="foo",
)
def a(context):
    return ["a"]


@asset(
    key_prefix=["bronze", "foo"], group_name="foo", partitions_def=daily_partitions_def
)
def b(context):
    context.log.info(f"foo: {context.asset_partition_key_for_output()}")

    return [1, 2, 3]


assets = load_assets_from_current_module()
