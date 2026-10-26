# Real-Time NYC Citi Bike Data Engineering & Analytics Pipeline

An end-to-end data engineering project using Python, REST APIs, Pandas, MySQL, SQLAlchemy, and a structured ETL workflow.

This project uses live NYC Citi Bike station data to demonstrate how data moves through a real data engineering pipeline.

The pipeline currently extracts live data from the Citi Bike REST API, stores the raw JSON response, transforms the data into a clean tabular format, and loads the processed data into a MySQL database.

Future stages will expand the project into dimensional modeling, a data warehouse, Microsoft Azure, and Power BI.

---

## Current Architecture

```text
Citi Bike REST API
        ↓
      Python
        ↓
   Raw JSON Files
     data/raw/
        ↓
      Pandas
        ↓
 Transformed Data
  data/processed/
        ↓
      MySQL
```

---

## Current Status

### Completed

- REST API connection
- Live Citi Bike data extraction
- Timestamped raw JSON storage
- Basic error handling
- Data transformation with Pandas
- Processed data storage
- MySQL database connection
- Loading transformed data into MySQL
- Environment-variable based database credentials
- Git protection for sensitive `.env` credentials

### Planned Next

- Data warehouse design
- Star schema
- Fact and dimension tables
- Microsoft Azure
- Azure Blob Storage
- Azure SQL Database
- Power BI dashboard

---

## Tech Stack

### Currently Used

- Python
- REST API
- JSON
- Pandas
- MySQL
- SQL
- SQLAlchemy
- python-dotenv
- requests
- Git
- GitHub

### Planned

- Data Warehousing
- Dimensional Modeling
- Star Schema
- Microsoft Azure
- Azure Blob Storage
- Azure SQL Database
- Power BI

---

## Project Steps

### Step 1 — Extract ✅

The pipeline connects to the live Citi Bike REST API and retrieves current station-status data.

The API provides information such as:

- Station ID
- Bikes available
- E-bikes available
- Docks available
- Station status
- Last reported time

The extraction logic is handled in:

```text
src/extract.py
```

---

### Step 2 — Raw Storage ✅

The original API response is saved as a timestamped JSON file inside:

```text
data/raw/
```

Example:

```text
station_status_20260815_210801.json
```

Keeping the raw data unchanged preserves the original source before any transformation takes place.

---

### Step 3 — Transform ✅

The raw Citi Bike JSON data is transformed using Python and Pandas.

The transformation process includes:

- Reading the raw API data
- Selecting useful fields
- Restructuring nested JSON data
- Cleaning the dataset
- Preparing the data for SQL
- Saving processed output

The transformation logic is handled in:

```text
src/transform.py
```

Processed data is stored inside:

```text
data/processed/
```

---

### Step 4 — Load into MySQL ✅

The transformed Citi Bike data is loaded into a MySQL database using SQLAlchemy.

The loading logic is handled in:

```text
src/load.py
```

The local database used by this project is:

```text
citibike_etl
```

Before running the load script, create the database in MySQL:

```sql
CREATE DATABASE citibike_etl;
```

Database credentials are not hard-coded in the Python source code.

Instead, the project reads them from a local `.env` file.

---

## Environment Setup

The repository includes:

```text
.env.example
```

Use it as a template to create your own local `.env` file.

Example:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=citibike_etl
```

The real `.env` file is included in `.gitignore` and should never be committed to GitHub.

Your local `.env` file should contain your own MySQL credentials.

---

## Installation

Clone the repository and install the required Python dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the Python libraries required to run the project.

---

## Running the Pipeline

### 1. Extract data

```bash
python src/extract.py
```

### 2. Transform data

```bash
python src/transform.py
```

### 3. Load data into MySQL

Make sure MySQL is running and the `citibike_etl` database has been created.

Then run:

```bash
python src/load.py
```

---

## Repository Structure

```text
cloud-data-engineering-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

The local `.env` file is intentionally excluded from GitHub.

---

## Next Stage — Data Warehouse & Dimensional Modeling 🚧

The next phase will organize the SQL data into a dimensional model.

The planned Star Schema will include tables such as:

```text
fact_station_snapshots
dim_stations
dim_date_time
```

The fact table will store changing station measurements, while the dimension tables will contain descriptive station and date/time information.

---

## Future Cloud Architecture 🚧

After the local ETL pipeline and dimensional model are complete, the project will be extended into Microsoft Azure.

Planned cloud technologies include:

- Azure Blob Storage
- Azure SQL Database

The goal is to move the same ETL workflow from a local environment into a cloud-based data engineering architecture.

---

## Power BI 🚧

The final analytics layer will connect the processed warehouse data to Power BI.

The dashboard is planned to analyze metrics such as:

- Bike availability
- E-bike availability
- Empty stations
- Full stations
- Busy time periods
- Station usage patterns

---

## Final Project Goal

The complete project architecture is planned to become:

```text
REST API
   ↓
Python Extraction
   ↓
Raw Storage
   ↓
Transformation
   ↓
MySQL / SQL
   ↓
Data Warehouse
   ↓
Star Schema
   ↓
Microsoft Azure
   ↓
Power BI
```

---

## Project Status

This project is currently **in progress**.

The Extract, Transform, and MySQL Load stages are complete.

The next stages will focus on dimensional modeling, data warehousing, cloud deployment with Microsoft Azure, and Power BI analytics.