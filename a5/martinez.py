# Erick Martinez
# Assignment 5

from sqlalchemy import create_engine, text, URL, MetaData, Table, select
from sqlalchemy.orm import DeclarativeBase
from config import Config

url = URL.create(
    "mariadb+mariadbconnector",
    username=Config.DB_USER,
    password=Config.DB_PASSWORD,
    host=Config.DB_HOST,
    database=Config.DB_NAME,
)

# The program will update a team moving from one city to another

# The teams tables is connected with the franchID, every year
# a team gets a new table, however the franchise table is static
# and is consistent throughout years. The franchID is a primary
# key so it is unique.
#
# The teams franchID is a MUL so many team rows (new year and or new team)
# can be under a single franchise, the default behavior for a teams franchID
# is to be NULL.
#
engine = create_engine(url)


class Base(DeclarativeBase):
    pass


metadata = MetaData()


class Franchise(Base):
    __table__ = Table("franchises", metadata, autoload_with=engine)


class Team(Base):
    __table__ = Table("teams", metadata, autoload_with=engine)

# autolaod = reflection
#
activeFranchise = select(Franchise).where(Franchise.active == "Y")


with engine.connect() as connection:
    result = connection.execute(activeFranchise)
    for row in result:


engine.dispose()
