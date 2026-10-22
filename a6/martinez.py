# Erick Martinez
# Assignment 6

from flask import Flask
from sqlalchemy import create_engine, URL
from config import Config

app = Flask(__name__)

url = URL.create(
    "mariadb+mariadbconnector",
    username=Config.DB_USER,
    password=Config.DB_PASSWORD,
    host=Config.DB_HOST,
    database=Config.DB_NAME,
)

engine = create_engine(url)
from a6 import routes
