from dagster import asset
from dagster import AutoMaterializePolicy
from dagster import DailyPartitionsDefinition
from dagster import load_assets_from_current_module

daily_partitions_def = DailyPartitionsDefinition(
    start_date="2023-06-01", timezone="Asia/Bangkok"
)


@asset(
    auto_materialize_policy=AutoMaterializePolicy.eager(),
    key_prefix=["bronze", "baz"],
    group_name="baz",
)
def f():
    return [1, 2, 3]


assets = load_assets_from_current_module()
