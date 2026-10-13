# Erick Martinez
# Assignment 5

from sqlalchemy import create_engine, text, URL, MetaData, Table, select
from sqlalchemy.orm import DeclarativeBase, Session
from csi3335 import mysql

url = URL.create(
    "mariadb+mariadbconnector",
    username=mysql["user"],
    password=mysql["password"],
    host=mysql["location"] if "location" in mysql else mysql["host"],
    database=mysql["database"],
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


# autoload = reflection

with Session(engine) as session:
    franchQuery = select(Franchise.franchID).where(Franchise.active == "Y")
    resultFranch = session.execute(franchQuery).all()

    for franchise in resultFranch:
        teamQuery = select(Team).where(
            Team.franchID == franchise.franchID,
            Team.yearID == 2025,
        )
        resultTeams = session.scalars(teamQuery).all()

        for team in resultTeams:
            newTeam = Team(
                yearID=2026,
                teamID=team.teamID,
                lgID=team.lgID,
                divID=team.divID,
                franchID=team.franchID,
                team_name=team.team_name,
            )
            session.add(newTeam)

    session.commit()
