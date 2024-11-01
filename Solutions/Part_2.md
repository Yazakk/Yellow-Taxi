# Data Pipeline Design

## 1. Ingestion

Download the data from NYC Yellow Taxi Trip Records on a monthly basis.

### Tools
Use a python script to fetch the data using `requests` library. The function has been scripted to perform the task [*download_data*](../functions.py) 

Monthly scheduling of the download can be handled using `airflow`. Setup a DAG to trigger the download on the first of each month. We need to take into consideration that data is available in m-2 manner. So, a logic to pass the previous 2 months needs to be implemented.

### Error Handling
Ensure that retries is setup in `airflow`. Add manual intervention where user will get a notification by email if the process keeps failing.

## 2. Transformation

Filter the trip fares over $10 and rename certain columns.

### Tools
`Pandas` can be used to data transformation in python. After ingesting the data, read the parquet file into a pandas data frame and filter the records where the fare is higher than $10. Use the rename function to align with the schema.

### Data Governance
Validate data types like *pickup_time* and *dropoff_time* to make sure that they are in datetime format. Ensure the uniqueness of any key data such as trip_id. Create a log for any missing or inconsistencies in the data. 

## 3. Loading

Insert the data to PostgreSQL

### Tools
Use `SQLAlchemy` to connect to the PostgreSQL database and `psycopg2` as the underlying driver. `Airflow` can also be used to manage dependencies and handling the loading process. The function [*push_to_db*](../functions.py) takes care of pushing the data in to the db.

### Error Handling 

Implement error handling logic in case of database connection error and handle conflict scenarios while inserting the data. 

In case of insertion failure, retry the insertion, and then skip and log the failed entry to revisit it again.

### Data Quality and Data Governance
Ensure data completeness by tracking the count of data ingested, transformed, and loaded. Ensure db schema constrains where fields such as trip_id, pickup_time, dropoff_time are non-nullable. `Airflow` can be used to monitor the pipeline health and add alerts for any pipeline failures. Make sure that log is set in place to monitor and trace data lineage.