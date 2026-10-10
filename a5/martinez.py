# Erick Martinez
# Assignment 5

from sqlalchemy import create_engine, text, URL
from config import Config

url = URL.create(
    "mariadb+mariadbconnector",
    username=Config.DB_USER,
    password=Config.DB_PASSWORD,
    host=Config.DB_HOST,
    database=Config.DB_NAME,
)

engine = create_engine(url)

with engine.connect() as connection:
    result = connection.execute(text("SELECT DATABASE(), VERSION()"))
    print(result.one())

engine.dispose()
