# 🚀 Crypto ETL Pipeline

A production-inspired **ETL (Extract, Transform, Load)** project built with **Python**, **PostgreSQL**, and **SQL**. The pipeline extracts real-time cryptocurrency market data from the CoinGecko API, validates the data, stores it in PostgreSQL, and performs analytical SQL queries on the collected historical data.

This project is part of my Data Engineering portfolio and focuses on applying software engineering best practices such as modular architecture, logging, exception handling, transaction management, and data validation.

---

## 📌 Project Overview

The pipeline performs the following workflow:

```text
CoinGecko API
      │
      ▼
Extract Data
      │
      ▼
Automatic Retry
      │
      ▼
Data Validation
      │
      ▼
Load into PostgreSQL
      │
      ▼
Logging
      │
      ▼
SQL Analytics
```

---

## 🛠️ Tech Stack

* Python 3
* PostgreSQL
* SQL
* psycopg2
* Requests
* Tenacity
* Python-dotenv
* Logging
* DBeaver
* Git & GitHub

---

## 📂 Project Structure

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
└── README.md
```

---

## ✨ Features

* Fetch real-time cryptocurrency data from the CoinGecko API
* Automatic retry for temporary API failures
* Data validation before database insertion
* PostgreSQL transaction management (`COMMIT` / `ROLLBACK`)
* Structured logging to both console and log file
* Environment variable configuration using `.env`
* Modular and maintainable project architecture
* Historical data collection for trend analysis
* SQL analytics using aggregate functions and time-based queries

---

## 🗄️ Database Schema

**Table:** `crypto_prices`

| Column       | Description                       |
| ------------ | --------------------------------- |
| coin_name    | Cryptocurrency name               |
| symbol       | Coin symbol (BTC, ETH)            |
| price_usd    | Current price in USD              |
| market_cap   | Market capitalization             |
| total_volume | 24-hour trading volume            |
| fetched_at   | Timestamp when data was collected |

---

## 📊 SQL Analytics

The project includes analytical SQL queries such as:

* Count total records
* Retrieve latest cryptocurrency prices
* Filter records using `WHERE`
* Sort data using `ORDER BY`
* Limit query results using `LIMIT`
* Calculate averages with `AVG()`
* Find highest and lowest values using `MAX()` and `MIN()`
* Group data using `GROUP BY`
* Round values using `ROUND()`
* Perform daily time-based analysis using `DATE()`

---

## ▶️ Running the Project

### Activate the virtual environment

```bash
source venv/bin/activate
```

### Run the ETL pipeline

```bash
python app.py
```

---

## 📈 Current Progress

### ✅ Completed

* Project setup
* PostgreSQL integration
* CoinGecko API integration
* ETL pipeline
* Logging
* Exception handling
* Automatic retry mechanism
* Data validation
* SQL Analytics

### 🚧 Coming Next

* dbt Transformations
* Pipeline Scheduling
* Unit Testing with pytest
* Docker
* GitHub Documentation Improvements

---

## 📚 What I Learned

Through this project, I gained practical experience with:

### Python

* Project structure
* Functions
* Dictionaries
* Loops
* Exception handling
* Logging
* Environment variables
* Modular programming

### SQL

* SELECT
* WHERE
* ORDER BY
* LIMIT
* COUNT()
* AVG()
* MAX()
* MIN()
* ROUND()
* GROUP BY
* DATE()

### Data Engineering

* ETL pipeline development
* REST API integration
* Data validation
* Retry mechanisms
* PostgreSQL transactions
* Historical data collection
* SQL-based analytics
* Production-inspired project organization

---

## 🎯 Future Improvements

* Build data transformations using dbt
* Schedule the pipeline with Apache Airflow
* Add automated testing using pytest
* Dockerize the application
* Create architecture diagrams
* Deploy the project

---

## 👨‍💻 Author

**Mark Cabael**

Aspiring Data Engineer building production-inspired data pipelines using **Python**, **SQL**, **PostgreSQL**, **dbt**, **Apache Airflow**, **PySpark**, and **Databricks**.
