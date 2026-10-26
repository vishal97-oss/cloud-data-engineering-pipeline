import json
from datetime import datetime
from pathlib import Path

import requests


# Live Citi Bike API endpoint that gives us current station availability data.
API_URL = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"


# Step 1: Extract live station data from the REST API.
def fetch_station_status():
    try:
        response = requests.get(API_URL, timeout=30)

        # Stop the pipeline if the API returns an error status.
        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print(f"API request failed: {error}")
        raise


# Step 2: Save the original API response as raw JSON before changing anything.
# Keeping raw data gives us a clean source that we can transform later.
def save_raw_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Find the project folder and point Python to our raw data directory.
    project_root = Path(__file__).resolve().parent.parent
    raw_folder = project_root / "data" / "raw"
    raw_folder.mkdir(parents=True, exist_ok=True)

    # Add a timestamp so every API pull can be stored separately.
    file_path = raw_folder / f"station_status_{timestamp}.json"

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

        return file_path

    except OSError as error:
        print(f"Failed to save raw data: {error}")
        raise


# Run the ingestion process and confirm whether it completed successfully.

#EXCUTION BLOCK


#if __name__ == "__main__":
def main():
    print("Starting Citi Bike API ingestion...")

    try:
        station_data = fetch_station_status()
        saved_file = save_raw_data(station_data)

        print("API request successful.")
        print(f"Raw data saved to: {saved_file}")

    except Exception:
        print("Ingestion pipeline failed.")

if __name__ == "__main__":
    main()

