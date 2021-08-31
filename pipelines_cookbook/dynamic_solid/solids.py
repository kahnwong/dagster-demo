### Imports
from typing import List

from dagster import DynamicOutput
from dagster import DynamicOutputDefinition
from dagster import Field
from dagster import solid

from utils.sleep_utils import return_random_sleep


### SOLIDS
@solid(
    config_schema={"total_prtns": Field(int, is_required=False)},
    output_defs=[DynamicOutputDefinition(List[str])],
)
def return_partitions(context):
    total_prtns = context.solid_config.get("total_prtns")
    context.log.info(f"total partitions: {total_prtns}")

    prtns = list(range(total_prtns))
    prtns = [f"set_{str(i)}" for i in prtns]

    # split into chunks
    n = 20
    prtns_chunk = [prtns[x : x + n] for x in range(0, len(prtns), n)]

    return_random_sleep()

    for index, prtns in enumerate(prtns_chunk):
        yield DynamicOutput(value=prtns, mapping_key=f"prtn_set_{index}")


@solid
def count_prtns(context, prtns: List[str]) -> int:
    total_prtns = len(prtns)
    context.log.info(f"total partitions: {total_prtns}")

    return_random_sleep()

    return total_prtns


@solid
def sum_total_prtns(context, prtn_counts: List[int]) -> int:
    total_prtns = sum(prtn_counts)
    context.log.info(f"total partitions: {total_prtns}")

    return_random_sleep()

    return total_prtns
