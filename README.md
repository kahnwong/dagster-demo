# dagster-demo

## Setup
Note: On Big Sur, run `export SYSTEM_VERSION_COMPAT=1` before running `pipenv install`.

```
# local test
$ pipenv install
$ dagit -h 0.0.0.0 -p 3000

# docker
docker-compose -f docker-compose-dagster.yml up
```

## Guides
### General

* plain python first
* path: workspace.yml → [repos.py](http://repos.py) → pipelines
* then use docker with db for [schedule, backfill and sensor]

### Pipelines

* botch solid / pipelines config → reload [to see config validation error before executing pipelines]
* botched code → re-execute to see errors in console
* re-run from [point of failure]
* retry
* prod/dev config
  * edit config in playground, does NOT modify the code

### Partition set

* backfill
  * also check data for given backfill run

### Sensor

* add new file and see sensor picking it up
