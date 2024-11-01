import os
import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta


def download_data(year: int, month: int):
    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02d}.parquet"
    local_path = f"../data/yellow_tripdata_{year}-{month:02d}.parquet"

    if not os.path.exists(local_path):  # Avoid re-downloading
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(response.content)
        else:
            raise Exception("Failed to download file")
    return local_path


def push_to_db(path: str, table_name: str):
    # database connection parameters
    username = 'data_engineer'
    password = '123456!'
    host = 'localhost'
    port = '5432'
    database = 'yellow_taxi'

    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

    df = pd.read_parquet(path)

    # Push DataFrame to PostgreSQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print("Data pushed to PostgreSQL!")


def postgres_engine():
    # database connection parameters
    username = 'data_engineer'
    password = '123456!'
    host = 'localhost'
    port = '5432'
    database = 'yellow_taxi'

    # Create the database engine
    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
    
    return engine

def get_data(engine, query):
    try:
        with engine.connect() as connection:
            df = pd.read_sql_query(query, connection)
        print("Query executed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    return df

def get_month_start_end(year: int, month: int):
    start_of_month = datetime(year, month, 1)

    if month == 12: 
        end_of_month = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_of_month = datetime(year, month + 1, 1) - timedelta(days=1)

    return start_of_month, end_of_month