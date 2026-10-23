CSI 3335 — Fall 2026 Project
Due: December 6, 2026, at 11:59 PM

Course: https://cs.baylor.edu/~speegle/3335/index.php

Specification: Version 1.0 · January 21, 2026 · Original specifications
1. Project overview
Build an individual web-database application for the class baseball
database. Follow the Flask tutorial covered in class during Asynchronous
Monday. The application must support website registration and login, and
securely store user information.
2. Registration and login
- [ ] On the first visit, present the option to log in or register.
- [ ] Require a unique username and a password for registration.
- [ ] Securely store user information in a table named users.
- [ ] Include SQL to create this table and populate it with an original user.
3. Franchise selection
After login:
- [ ] Populate a dropdown with franchise names.
- [ ] Let the user select a franchise.
- [ ] Randomly select a player or manager who played or managed at least
  one game for that franchise.
- [ ] Make all eligible players and managers equally likely to be selected.
- [ ] Remember all franchises selected by each user in the database.
4. Required reports
Player report
For the selected player, display:
- [ ] Number of seasons played for the selected franchise.
- [ ] Number of games played for the selected franchise.
- [ ] List of different positions played for the selected franchise.
- [ ] Total number of seasons played in baseball.
- [ ] List of any awards or accomplishments, such as All-Star game
  appearances and Hall of Fame votes.
Manager report
For the selected manager, display:
- [ ] Number of seasons managed for the selected franchise.
- [ ] Number of games managed for the selected franchise.
- [ ] Total number of seasons managed in baseball.
- [ ] List of postseason series appearances the team enjoyed under that
  manager.
Any manager receives credit for any postseason games for the team in
that year.

5. Required buttons
Cheat
- [ ] Show players who played in an All-Star game for the selected franchise.
- [ ] Make each player a link to that player's report described above.
- [ ] Account for franchises that have no All-Star players.
List
- [ ] Show 20 random players for the selected franchise.
- [ ] Make each player a link to that player's report described above.
Managers
- [ ] Show managers for the selected franchise WHO WERE NEVER PLAYERS.
- [ ] Make each manager a link to that manager's report described above.
History
- [ ] Show the last five franchises selected by the logged-in user.
- [ ] Make each franchise selectable.
- [ ] When a history entry is selected, set it as the default franchise.
- [ ] Randomly generate a player report from that franchise.
- [ ] Use that franchise for all future selections until changed.
6. Technical requirements
1. Use the class MariaDB baseball database.
2. Provide yourlastname.sql to create the user table in the database.
3. Use Flask as the backend.
4. Set the project name in .flaskenv.
5. Do not touch any database other than baseball.
6. You may change baseball as needed. Include all such commands in
   yourlastname.sql.
7. Use only the listed Python libraries, with the versions below.
Python version
Python 3.13.9
Allowed libraries
alembic==1.17.1
blinker==1.9.0
click==8.3.0
colorama==0.4.6
dnspython==2.8.0
email-validator==2.3.0
flask==3.1.2
flask-login==0.6.3
flask-sqlalchemy==3.1.1
flask-wtf==1.2.2
greenlet==3.2.4
idna==3.11
itsdangerous==2.2.0
jinja2==3.1.6
mako==1.3.10
markupsafe==3.0.3
numpy==2.3.4
pandas==2.3.3
pymysql==1.1.2
python-dateutil==2.9.0.post0
python-dotenv==1.2.1
pytz==2025.2
six==1.17.0
sqlalchemy==2.0.44
typing-extensions==4.15.0
tzdata==2025.2
werkzeug==3.1.3
wtforms==3.2.1
7. Submission checklist
Submit everything in one ZIP file.
- [ ] yourlastname.sql — SQL to alter the baseball database as needed,
  including creation of users and an original user.
- [ ] All Python code needed to create the Flask website.
- [ ] csi3335f2025.py — database connection dictionary described below.
- [ ] Exclude your virtual environment.
Database dictionary file
The file csi3335f2025.py must contain a dictionary:
1. Named mysql.
2. With four keys: host, user, password, and database.
3. Similar to the assignment's example:
mysql = {
    'host': 'localhost',
    'user': 'web',
    'password': 'mypass',
    'database': 'yourteamname',
}
The instructor will change this file as needed for grading.
Specification details retained: The required filename includes f2025
even though this is the Fall 2026 project. The supplied example uses
yourteamname, but the requirements mandate the baseball database.

8. Grading rubric
Automatic-zero conditions
Failure to use the class MariaDB baseball database, failure to use
Flask and the required dictionary file, or use of any library outside
the approved list results in an automatic zero.

Points
Requirement	Points
Suggested directory structure; server launches	10
Required user table with the correct name	10
Successful user login	10
Franchise names load in dropdown	10
Random player data displays	10
Manager data displays	10
Cheat button works	10
List button works	10
Managers button works	10
Inline code documentation	10
Total	100
