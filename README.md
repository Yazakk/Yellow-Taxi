# Yellow Taxi

Before going through the tasks, I skimed through the [*data dictionary*](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf) available to better understand the data. I formulated the following reasoning and data definitions:
1. Revenue:
   revenue was calculated as the following: fare_amount + extra + improvement_surcharge + congestion_surcharge + airport_fee. Amounts such as MTA_tax, Tip_amount, and Tolls_amount should not be considered as part of the revenue.
2. Payment Type:
    Only Cash, Credit Card, and Unknow payments where considered in the analysis. No Charge, Void trip, and dispute where filtered out from the records.

 ## Prerequists
 1. Docker needs to be installed on your machine
 2. Python 3.9.9 was used for this project
 3. VSCode
 
 ## Setup
  ### Step 1: Set Up the PostgreSQL Docker Container
  1. Open terminal in VSCode
  2. Create a Docker Network
  `docker network create my_network`
  3. Run Docker Compose
  `docker-compose up -d`
  
  ### Step 2: Set Up the PostgreSQL Docker Container
  1. Create python environment
  2. Activate the environment
  3. Install python packages in requirements file
 
 ## Solutions
  ### Part 1:
   1. Run step_0 notebook [*step_0*](Solutions/step_0.ipynb).
   2. open terminal in VScode and run the follwoing command:
   `docker exec -it yellow_taxi_container psql -U data_engineer -d yellow_taxi`
   This will let you query the database through vscode once the data has been pushed
   3. Run the scripts in [*Part_1*](Solutions/Part_1.sql).

   NOTE: Task 3 (Frequent Riders ) could not be comleted because RiderID was not provided in the data.
  
  ### Part 2:
   [*Part_2*](Solutions/Part_2.md) explains how a Data Pipeline can be designed for ingesting, transforming, and loading NYC Yellow taxi data taking into account the tools to be used, how to handle errors, and how to ensure data quality and data governance.
   
  ### Part 3 and 4:
  Run the [*python_notebook*](Solutions/Part_3_4.ipynb) to generate the solution for Part 3 and Part 4.


   
