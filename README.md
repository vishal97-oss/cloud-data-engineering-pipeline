# cloud-data-engineering-pipeline
End-to-end cloud data engineering and analytics pipeline using Python, REST APIs, SQL, Azure, dimensional modeling, and Power BI.
#
# Real-Time NYC Citi Bike Data Engineering & Analytics Pipeline

This project is a hands-on data engineering project where I am building an end-to-end pipeline using live NYC Citi Bike data.

Right now, the project pulls live station data from the Citi Bike REST API using Python and saves the raw JSON data locally. I am building the project step by step so I can understand how each part of a real data pipeline works.

The final goal is to connect the full flow from API ingestion all the way to SQL, a data warehouse, cloud storage, and Power BI.

## Current Architecture

```text
Citi Bike REST API
        ↓
      Python
        ↓
 Raw JSON Files
   data/raw/
```

## Current Status

Completed:

* REST API connection
* Python data extraction
* Timestamped raw JSON storage
* Basic error handling

Planned next:

* Data cleaning and transformation
* SQL database
* Data warehouse
* Star schema
* Fact and dimension tables
* Microsoft Azure
* Power BI dashboard

## Tech Stack

Currently used:

* Python
* REST API
* JSON
* requests
* Git
* GitHub

Planned:

* Pandas
* SQL
* PostgreSQL / Azure SQL
* Azure Blob Storage
* ETL
* Data Pipelines
* Data Warehousing
* Dimensional Modeling
* Power BI

## Project Steps

### Step 1 — Extract ✅

The first step is to connect Python to the live Citi Bike API and pull current station data.

The API gives information such as:

* Station ID
* Bikes available
* E-bikes available
* Docks available
* Station status
* Last reported time

### Step 2 — Raw Storage ✅

After pulling the data, I save the original API response as a JSON file inside:

```text
data/raw/
```

I add a timestamp to every file so each API pull can be stored separately.

Example:

```text
station_status_20260815_210801.json
```

I keep the raw data unchanged first so I always have the original source before doing any cleaning or transformation.

### Step 3 — Transform 🚧 Planned

Next, I will use Python and Pandas to clean and organize the raw data.

This will include things like:

* Handling missing values
* Fixing data types
* Selecting useful columns
* Restructuring the JSON data
* Preparing the data for SQL

### Step 4 — Load into SQL 🚧 Planned

After transformation, the cleaned data will be loaded into a SQL database.

This is where I will start working with SQL tables and queries instead of only JSON files.

### Step 5 — Data Warehouse & Modeling 🚧 Planned

The next stage will be to organize the SQL data into a proper warehouse structure.

I plan to create a Star Schema with tables such as:

```text
fact_station_snapshots
dim_stations
dim_date_time
```

The fact table will store changing station measurements, while the dimension tables will store descriptive information such as station and date/time details.

### Step 6 — Microsoft Azure 🚧 Planned

After the local pipeline is working, I plan to move the project into Microsoft Azure.

The cloud part of the project is planned to use:

* Azure Blob Storage
* Azure SQL Database

This will help me understand how the same pipeline works in a cloud environment.

### Step 7 — Power BI 🚧 Planned

The final step will be to connect the processed warehouse data to Power BI.

The dashboard will be used to look at things like:

* Bike availability
* E-bike availability
* Empty stations
* Full stations
* Busy time periods
* Station usage patterns

## Repository Structure

```text
cloud-data-engineering-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   └── extract.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

This structure will grow as I add transformation, SQL, cloud, data warehouse, and Power BI parts.

## Final Project Goal

The full project will eventually look like this:

```text
REST API
   ↓
Python
   ↓
ETL
   ↓
Cloud Storage
   ↓
SQL
   ↓
Data Warehouse
   ↓
Star Schema
   ↓
Power BI
```

This project is currently **in progress**.

The API ingestion and raw storage stages are completed, and I will continue building the remaining stages step by step.

