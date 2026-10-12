import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")


"""
mysql = {
    "host": "localhost",
    "user": "web",
    "password": "mypass",
    "database": "baseball",
}
"""


class Config:
    DB_HOST = "127.0.0.1"
    DB_USER = "baseball_user"
    DB_NAME = "baseball"
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
