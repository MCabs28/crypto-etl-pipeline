import psycopg2
from config.config import DB_CONFIG
from logs.logger import logger


def get_connection():
    logger.info("Connecting to PostgreSQL...")
    return psycopg2.connect(**DB_CONFIG)
