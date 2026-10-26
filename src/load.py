import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
load_dotenv()

df = pd.read_csv("data/processed/station_status_clean.csv")

connection_url = URL.create(
    "mysql+mysqlconnector",
    username="root",
    password=os.getenv("DB_PASSWORD"),
    host="localhost",
    database="citibike_etl"
)

engine = create_engine(connection_url)

with engine.connect():
    print("MySQL connection successful!")

df.to_sql(
    "station_status",
    con=engine,
    if_exists="replace",
    index=False
)

print("Load complete!")
print(f"{len(df)} rows loaded into MySQL.")