from datetime import datetime
from utils.sf import run_snowflake_query
import json
import logging
import os

config_file = os.environ["CONFIG_FILE"]  #'export_config.json'
sf_export_area = os.environ["SF_EXPORT_AREA"]  #'OUTRA_DATA_ETL_S3_EXPORT'

def export_data(config):
    csv_run = False
    CURRENT_DATE_YYYYMMDD = datetime.today().strftime('%Y%m%d')

    print(f"Started export of {config['TABLE']}")
    parquet_query = f'copy into @{sf_export_area}/{CURRENT_DATE_YYYYMMDD}/{config["TABLE"]} from "{config["SCHEMA"]}"."{config["TABLE"]}" FILE_FORMAT = (type=parquet) OVERWRITE=TRUE HEADER=TRUE;'
    csv_query = f'copy into @{sf_export_area}/{CURRENT_DATE_YYYYMMDD}/{config["TABLE"]}.csv.gz from "{config["SCHEMA"]}"."{config["TABLE"]}" FILE_FORMAT = (type=csv) OVERWRITE = TRUE HEADER=TRUE;'
    try:
        run_snowflake_query(parquet_query)
    except BaseException as err:
        logging.error(f"Error: Snowflake execution command failed! Query: {parquet_query}")
        logging.error(f"Error message: {err}")
        csv_run = True
    finally:
        try:
            if csv_run:
                run_snowflake_query(csv_query)
        except BaseException as err:
            logging.error(f"Error: Snowflake execution command failed! Query: {csv_query}")
            logging.error(f"Error message: {err}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(level=int(os.environ.get("LOGLEVEL")))

    data = json.load(open(config_file))
    for config in data["exports"]:
        try:
            export_data(config)
        except BaseException as err:
            logging.error(f"Error: {err=}, {type(err)=}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
