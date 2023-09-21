from dagster import asset
from dagster import AssetIn
from dagster import load_assets_from_current_module
from dagster import TimeWindowPartitionMapping
from dagster import WeeklyPartitionsDefinition

weekly_partitions_def = WeeklyPartitionsDefinition(
    start_date="2023-06-01", timezone="Asia/Bangkok"
)


@asset(
    partitions_def=weekly_partitions_def,
    ins={
        "a": AssetIn(
            key=["bronze", "foo", "b"],
            partition_mapping=TimeWindowPartitionMapping(),
        )
    },
    key_prefix=["silver", "foo"],
    group_name="foo",
)
def e(a):
    return [1, 2, 3]


assets = load_assets_from_current_module()
