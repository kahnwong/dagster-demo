from dagster import repository

from pipelines_cookbook.cookbook import pipelines as cookbook

# from pipelines_cookbook.asset_materialization import pipelines as asset_materialization

# from pipelines_cookbook.partition_set import pipelines as partition_set


@repository
def dagster_repository():
    return (
        # + asset_materialization.repo
        cookbook.repo
        # + partition_set.repo
    )
