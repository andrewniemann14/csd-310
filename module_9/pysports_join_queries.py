# Andrew Niemann, 5/1/21, Module 9.2
# queries and prints player record and team name per player

import mysql.connector
from mysql.connector import errorcode

config = {
  "user": "pysports_user",
  "password": "MySQL8IsGreat!",
  "host": "127.0.0.1",
  "database": "pysports",
  "raise_on_warnings": True
}

try:
  db = mysql.connector.connect(**config)
  print(f"Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}\n")

  print("\n-- DISPLAYING PLAYER RECORDS --")
  cursor = db.cursor()
  cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
  players = cursor.fetchall()
  for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team Name: {player[3]}\n")

  input("\nPress any key to continue...")

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("The supplied username or password is invalid")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("The specified database does not exist")
  else:
    print(err)
  
finally:
  db.close()