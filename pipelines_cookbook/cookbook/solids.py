### Imports
from random import random
from time import sleep

from dagster import solid


def return_random_sleep():
    return sleep(10 * random())


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
    return output
