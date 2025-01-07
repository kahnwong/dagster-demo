from typing import Any

from dagster import asset
from dagster import AssetDep
from dagster import AssetExecutionContext
from dagster import DailyPartitionsDefinition
from dagster import load_assets_from_current_module
from dagster import TimeWindowPartitionMapping

from dags.assets.bronze.foo.assets import b


daily_partitions_def = DailyPartitionsDefinition(
    start_date="2023-06-01", timezone="Asia/Bangkok"
)


@asset(
    partitions_def=daily_partitions_def,
    deps=[
        AssetDep(
            b,
            partition_mapping=TimeWindowPartitionMapping(),
        )
    ],
    key_prefix=["silver", "foo"],
    group_name="foo",
)
def e(context: AssetExecutionContext, b: Any):
    partition = context.partition_key
    context.log.info(f"partition: {partition}")
    context.log.info(f"b: {b}")

    return [1, 2, 3]


assets = load_assets_from_current_module()
