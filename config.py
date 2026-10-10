import os


class Config:
    DB_HOST = "127.0.0.1"
    DB_USER = "baseball_user"
    DB_NAME = "baseball"
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
