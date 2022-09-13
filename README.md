# Export snowflake data

## Requirements

Exports data from snowflake to csv files.
Generate archives and uploads it to SFTP or external S3 location

### Input

Process reads export_config.json file

### Schedule



### Output

Archive or csv file.

### Volume of data

Depends of data stores in snowflake.

## Parameters

All parameters are stores in export_config.json file. You have to define export_name as a parameter for the main process.

### Logging levels

| Level | Numeric value |
|-- | -- |
| CRITICAL | 50 |
| ERROR | 40 |
| WARNING | 30 |
| INFO | 20 |
| DEBUG | 10 |
| NOTSET | 0 |
