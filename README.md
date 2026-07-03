# Crypto ETL Pipeline

A beginner-friendly Data Engineering project built with **Python** and **PostgreSQL** that extracts real-time cryptocurrency data from the CoinGecko API, validates it, and stores it in a PostgreSQL database.

This project is part of my journey to becoming a Data Engineer and focuses on writing clean, modular, and production-inspired ETL code.

## Project Overview

The pipeline performs the following steps:

1. Extract cryptocurrency data from the CoinGecko API
2. Retry failed API requests automatically
3. Validate the incoming data
4. Load validated data into PostgreSQL
5. Log every step of the pipeline


## Tech Stack

* Python 3
* PostgreSQL
* psycopg2
* Requests
* Tenacity
* Python-dotenv
* Logging
* DBeaver


## Project Structure

```text
crypto-etl-pipeline/
│
├── app.py
├── config.py
├── constants.py
├── requirements.txt
├── .env
│
├── extract/
│   └── crypto_api.py
│
├── validation/
│   └── validator.py
│
├── load/
│   ├── db_connection.py
│   └── load_db.py
│
├── logs/
│   ├── logger.py
│   └── pipeline.log
│
└── venv/
```

---

## Features

* Fetch cryptocurrency prices from CoinGecko API
* Automatic retry for temporary API failures
* Data validation before database insertion
* PostgreSQL transaction handling (`commit` / `rollback`)
* Structured logging
* Environment variable configuration
* Modular project architecture

---

## Database

Table: `crypto_prices`

Columns:

* coin_name
* symbol
* price_usd
* market_cap
* total_volume
* fetched_at

---

##  Running the Project

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run the pipeline:

```bash
python app.py
```

---

## Current Progress

### Completed

* Project setup
* PostgreSQL integration
* CoinGecko API integration
* ETL pipeline
* Logging
* Exception handling
* Automatic retry
* Data validation

### Coming Next

* SQL Analytics
* dbt Transformations
* Pipeline Scheduling
* Unit Testing
* Docker
* Documentation Improvements

---

## What I Learned

Through this project, I practiced:

* Python modules and packages
* REST API integration
* PostgreSQL connectivity
* SQL INSERT operations
* Transaction management
* Exception handling
* Logging best practices
* Data validation
* Writing modular and maintainable code

---

## Future Improvements

* Build analytics queries using SQL
* Transform data using dbt
* Automate pipeline execution
* Dockerize the application
* Add unit tests with pytest
* Deploy the project

---

##  Author

**Mark Cabael**

Aspiring Data Engineer focused on building production-inspired data pipelines using Python, SQL, PostgreSQL, dbt, Airflow, and Databricks.
