#!/bin/bash
if [ "$RUN_MODE" == "dagster" ]; then
  # Generate Dagster Config
  ${DAGSTER_HOME}/dagster.yaml.sh > ${DAGSTER_HOME}/dagster.yaml

  dagster instance migrate
  dagit -h 0.0.0.0 -p 3000
elif [ "$RUN_MODE" == "dagster-daemon" ]; then
  # Generate Dagster Config
  ${DAGSTER_HOME}/dagster.yaml.sh > ${DAGSTER_HOME}/dagster.yaml

  dagster-daemon run
else
  echo "RUN_MODE not recognized (should be dagster or dagster-daemon): $RUN_MODE"
fi
