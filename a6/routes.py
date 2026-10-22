from flask import render_template
from sqlalchemy import MetaData, Table, select
from sqlalchemy.orm import DeclarativeBase, Session, aliased
from a6.martinez import app, engine

metadata = MetaData()


class Base(DeclarativeBase):
    pass


class Team(Base):
    __table__ = Table("teams", metadata, autoload_with=engine)


class PostSeries(Base):
    __table__ = Table("seriespost", metadata, autoload_with=engine)


@app.route("/")
@app.route("/home")
def playoffs():
    winner = aliased(Team, name="winner")
    loser = aliased(Team, name="loser")
    playoff_query = (
        select(
            PostSeries.round,
            winner.team_name.label("winner"),
            loser.team_name.label("loser"),
            PostSeries.wins.label("winner_wins"),
            PostSeries.losses.label("loser_wins"),
        )
        .select_from(PostSeries)
        .join(
            winner,
            (winner.teamID == PostSeries.teamIDwinner)
            & (winner.yearID == PostSeries.yearID),
        )
        .join(
            loser,
            (loser.teamID == PostSeries.teamIDloser)
            & (loser.yearID == PostSeries.yearID),
        )
        .where(PostSeries.yearID == 2025)
        .order_by(PostSeries.round, PostSeries.seriespost_ID)
    )

    with Session(engine) as session:
        results = session.execute(playoff_query).mappings().all()

    return render_template("playoffs.html", results=results)
