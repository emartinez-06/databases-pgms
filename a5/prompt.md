# Assignment 5
## Write a python program using sqlalchemy to access the baseball database. Use a configuration file named csi3335,py with a dictionary called mysql which contains 4 keys - location, user, password and database. For example, the dictionary may look like:

mysql = {'host':'localhost','user':'web','password':'mypass','database':'baseball'}. Do not include your file. We will use our own.

### The program must update the baseball database to accomodate teams moving from one city to another. Specifically:
- A class must conform to the franchises table
- A class must conform to the teams table
- For each active franchise (franchise.active = 'Y'), update the teams table with a new team for 2026.
- The teamID, lgID, divID, franchID and team_name will be the same for each team in 2026 as in 2025.
- The other fields may be NULL.
- The new teams should be successfully inserted into the teams table.
- SQL injection attacks should be prevented.
- Your assignment should be a python file meeting the following criteria

It must be named ***yourlastname.py***
- It must contain your name on the first line (commented out)
- It must contain the assignment name (Assignment 5) on the second line (commented out)
- It must be well designed and be well documented. See the python style guide for details.
