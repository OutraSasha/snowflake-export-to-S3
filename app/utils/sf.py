import os

import snowflake.connector

# Snowflake connection
sf_username = os.environ["SF_USERNAME"]
sf_password = os.environ["SF_PASSWORD"]
sf_account = os.environ["SF_ACCOUNT"]
sf_warehouse = os.environ["SF_WAREHOUSE"]
sf_database = os.environ["SF_DATABASE"]
sf_schema = os.environ["SF_SCHEMA"]

# load to snowflake
def run_snowflake_query(query):
    conn = snowflake.connector.connect(
        user=sf_username,
        password=sf_password,
        account=sf_account,
        warehouse=sf_warehouse,
        database=sf_database,
        schema=sf_schema,
        region="eu-west-1",
    )

    cur = conn.cursor()
    cur.execute(query)
    query_id = cur.sfqid
    cur.get_results_from_sfqid(query_id)
    results = cur.fetchall()
    return results[0]
