# Crypto ETL Pipeline

An end-to-end Data Engineering project that extracts real-time cryptocurrency market data from the CoinGecko API, validates the data, loads it into PostgreSQL, and transforms it into analytics-ready models using dbt.

This project demonstrates modern data engineering practices including ETL development, SQL analytics, dbt modeling, data quality testing, source freshness monitoring, incremental models, reusable macros, and project organization.

---

# Overview

The pipeline automates the process of collecting cryptocurrency market data and preparing it for analytics.

The workflow consists of:

1. Extract cryptocurrency data from the CoinGecko API.
2. Validate incoming data before loading.
3. Load clean data into PostgreSQL.
4. Build staging and analytics models using dbt.
5. Test data quality using dbt generic and custom tests.
6. Monitor source freshness.
7. Create reusable SQL logic with dbt macros.
8. Optimize processing using incremental models.

---

# Features

- Extract cryptocurrency market data from the CoinGecko API
- Validate incoming data before loading
- Load clean data into PostgreSQL
- Build staging and mart models using dbt
- SQL analytics for reporting
- Generic dbt tests
- Custom dbt tests
- Source testing
- Source freshness monitoring
- Seed files for reference data
- Reusable dbt macros
- Incremental models for efficient processing
- Logging and exception handling
- Retry logic for API requests
- Clean project architecture

---

# Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Database | PostgreSQL |
| Query Language | SQL |
| Transformation | dbt |
| API | CoinGecko API |
| Version Control | Git & GitHub |

---

# Architecture

```
                CoinGecko API
                      │
                      ▼
             Python ETL Pipeline
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
  Validation      Logging        Retry Logic
                      │
                      ▼
                PostgreSQL
                      │
                      ▼
                    dbt
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
   Sources        Staging Models    Mart Models
                      │
                      ▼
          Tests • Seeds • Macros
                      │
                      ▼
             Analytics-ready Data
```

---

#  Project Structure

```text
crypto-etl-pipeline/
│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
│   ├── config.py
│   └── constants.py
│
├── extract/
│   └── crypto_api.py
│
├── load/
│   ├── db_connection.py
│   └── load_db.py
│
├── validation/
│   └── validator.py
│
├── tests/
│
└── dbt/
    └── crypto_analytics/
        ├── models/
        ├── macros/
        ├── seeds/
        ├── tests/
        ├── analyses/
        ├── snapshots/
        ├── dbt_project.yml
        └── README.md
```

---

# Data Flow

```
CoinGecko API
      │
      ▼
Extract Data
      │
      ▼
Validate Data
      │
      ▼
Load into PostgreSQL
      │
      ▼
dbt Sources
      │
      ▼
Staging Models
      │
      ▼
Mart Models
      │
      ▼
Analytics & Reporting
```

---

# Setup Instructions

## Clone the repository

```bash
git clone <repository-url>
cd crypto-etl-pipeline
```

## Create a virtual environment

```bash
python -m venv venv
```

## Activate the environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment variables

Create a `.env` file containing your PostgreSQL credentials.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=crypto_db
DB_USER=postgres
DB_PASSWORD=your_password
```

---

# Running the ETL Pipeline

Execute the ETL pipeline:

```bash
python app.py
```

---

# Running dbt

Navigate to the dbt project:

```bash
cd dbt/crypto_analytics
```

Build models:

```bash
dbt run
```

Run tests:

```bash
dbt test
```

Load seed files:

```bash
dbt seed
```

Check source freshness:

```bash
dbt source freshness
```

Generate documentation:

```bash
dbt docs generate
```

Launch documentation:

```bash
dbt docs serve
```

---

# Skills Demonstrated

- Python ETL Development
- REST API Integration
- Data Validation
- Logging
- Exception Handling
- Retry Logic
- PostgreSQL
- SQL Analytics
- dbt Modeling
- Generic Tests
- Custom Tests
- Source Testing
- Source Freshness
- Seed Files
- Incremental Models
- Macros
- Git Version Control
- Project Organization

---

# Future Improvements

- Orchestrate the pipeline using Apache Airflow
- Containerize the project with Docker
- Deploy to AWS
- Process large-scale datasets using Apache Spark
- Add CI/CD with GitHub Actions
- Implement automated monitoring and alerting

---

# Learning Goals

This project was built to strengthen practical skills in modern Data Engineering by applying industry-standard tools and workflows in an end-to-end ETL pipeline.

---

##  Author

**Mark Cabael**

Data Engineering Portfolio Project