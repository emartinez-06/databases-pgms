# Assignment 6 — Erick Martinez

This Flask application displays the 2025 baseball playoff results. Each
series appears once, with the round, winning and losing team names, and
the number of games won by each team.

## Setup and run

1. Open a terminal in the included `flask` directory.
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv .venv
   . .venv/bin/activate
   ```
3. Install dependencies with `python -m pip install -r requirements.txt`.
   The MariaDB Python driver may require MariaDB Connector/C and development
   tools installed on the host system.
4. Place the instructor-provided `csi3335.py` in the `flask` directory.
   It must define `mysql`, a dictionary containing `host`, `user`,
   `password`, and `database`. This configuration file is intentionally
   excluded from the submission.
5. Run `python -m flask run` and visit http://127.0.0.1:5000/home.
   The included `.flaskenv` selects the `app` application automatically.

## Design

- `flask/app/__init__.py` creates the Flask app and database engine using
  only the instructor-provided `csi3335.mysql` configuration.
- `flask/app/routes.py` reflects the `teams` and `seriespost` tables into
  ORM classes. It filters series to 2025 and joins two aliases of `Team`
  on both team ID and year to obtain the correct season's names.
- `flask/app/templates/playoffs.html` renders the query results. Jinja
  escapes displayed values and shows a message when there are no results.

The database must contain the `teams` and `seriespost` tables and their
2025 records. `seriespost.wins` is the winner's games won; `losses` is the
loser's games won. The application reads data and does not change it.

No credentials, database dumps, or virtual environment are included.
