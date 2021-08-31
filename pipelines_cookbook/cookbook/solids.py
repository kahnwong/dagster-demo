### Imports
from random import choices

from dagster import RetryRequested
from dagster import solid

from utils.sleep_utils import return_random_sleep


### SOLIDS
@solid
def step_one(context) -> int:
    context.log.info("Hello 1")
    return_random_sleep()
    return 1


@solid
def step_two(context) -> int:
    context.log.info("Hello 2")
    return_random_sleep()
    return 2


@solid
def step_three(context, a: int, b: int) -> int:
    output = a + b
    context.log.info(f"output: {output}")
    return_random_sleep()
    return output


@solid
def step_four(context) -> int:
    context.log.info("Hello 4")
    return_random_sleep()
    return 4


@solid
def step_five(context) -> int:
    context.log.info("Hello 5")
    return_random_sleep()
    return 5


@solid
def step_six(context, a: int, b: int) -> int:
    output = a + b
    context.log.info(f"output: {output}")
    return_random_sleep()
    return output


@solid
def step_seven(context, a: int, b: int) -> int:
    output = a + b
    context.log.info(f"output: {output}")

    return_random_sleep()

    ### trigger retry
    try:
        d = {1: 40, 0: 60}
        num = choices(*zip(*d.items()), k=1)[0]

        context.log.info(f"num: {num}")

        3 / num
    except ZeroDivisionError:
        raise RetryRequested(max_retries=5)

    return output
