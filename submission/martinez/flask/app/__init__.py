"""Erick Martinez: Flask application for the 2025 baseball playoffs."""

from flask import Flask
from sqlalchemy import URL, create_engine
from csi3335 import mysql

app = Flask(__name__)

# URL.create safely handles special characters in the supplied password.
url = URL.create(
    "mariadb+mariadbconnector",
    host=mysql["host"],
    username=mysql["user"],
    password=mysql["password"],
    database=mysql["database"],
)
engine = create_engine(url)

# Register routes after app and engine exist, since routes imports both.
from app import routes  # noqa: E402, F401
