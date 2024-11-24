import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_database():
    db = {
        "database": os.getenv("DATABASE"),
        "host": os.getenv("HOST"),
        "user": os.getenv("USER"),
        "password": os.getenv("PASSWORD"),
        "port": os.getenv("PORT"),
    }
    return db


def db_conn() -> psycopg2.extensions.connection:
    conn = psycopg2.connect(**get_database())
    return conn


def get_secret_key():
    secret_key = os.getenv("SECRET_KEY")
    return secret_key


def get_version():
    version = os.getenv("VERSION")
    return version
