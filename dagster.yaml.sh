#!/bin/bash
echo "scheduler:
  module: dagster.core.scheduler
  class: DagsterDaemonScheduler
"

if [ ! -z "$RUN_COORDINATOR" ]; then
  echo "run_coordinator:
  module: dagster.core.run_coordinator
  class: DefaultRunCoordinator
"
else
  echo "run_coordinator:
  module: dagster.core.run_coordinator
  class: QueuedRunCoordinator
  config:
    max_concurrent_runs: 1
"
fi

if [ ! -z "$DAGSTER_PG_USERNAME"  ] || [ ! -z "$DAGSTER_PG_PASSWORD"  ] || [ ! -z "$DAGSTER_PG_HOST"  ] || [ ! -z "$DAGSTER_PG_DB"  ]; then
  echo "run_storage:
  module: dagster_postgres.run_storage
  class: PostgresRunStorage
  config:
    postgres_db:
      username:
        env: DAGSTER_PG_USERNAME
      password:
        env: DAGSTER_PG_PASSWORD
      hostname:
        env: DAGSTER_PG_HOST
      db_name:
        env: DAGSTER_PG_DB
      port: 5432

event_log_storage:
  module: dagster_postgres.event_log
  class: PostgresEventLogStorage
  config:
    postgres_db:
      username:
        env: DAGSTER_PG_USERNAME
      password:
        env: DAGSTER_PG_PASSWORD
      hostname:
        env: DAGSTER_PG_HOST
      db_name:
        env: DAGSTER_PG_DB
      port: 5432

schedule_storage:
  module: dagster_postgres.schedule_storage
  class: PostgresScheduleStorage
  config:
    postgres_db:
      username:
        env: DAGSTER_PG_USERNAME
      password:
        env: DAGSTER_PG_PASSWORD
      hostname:
        env: DAGSTER_PG_HOST
      db_name:
        env: DAGSTER_PG_DB
      port: 5432
"
fi
