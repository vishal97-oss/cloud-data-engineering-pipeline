import json
import pandas as pd
from pathlib import Path

with open("data/raw/station_status_20261011_185135.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["data"]["stations"])

df["last_reported"] = pd.to_datetime(
    df["last_reported"],
    unit="s",
    utc=True
)

Path("data/processed").mkdir(parents=True, exist_ok=True)

df.to_csv(
    "data/processed/station_status_clean.csv",
    index=False
)

print("Transform complete!")
print(df.head())