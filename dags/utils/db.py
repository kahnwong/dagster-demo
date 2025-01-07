from dagster import op


@op()
def write_to_db(context, gcs_path):
    context.log.info(f"gcs_path: {gcs_path}")
    context.log.info("Writing to db...")

    # implement write logic here

    return 200
