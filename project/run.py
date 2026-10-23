import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from flask import Flask

load_dotenv()

app = Flask(__name__)

url = URL.create(
    "mysql+pymysql",
    username="baseball_user",
    password=os.getenv("PASSWORD"),
    host="127.0.0.1",
    database="baseball",
)

engine = create_engine(url)

with engine.connect() as conn:
    print("Connected to MariaDB")

from . import routes
