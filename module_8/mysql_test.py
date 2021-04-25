# Andrew Niemann, 4/25/21, Module 8.2
# connects to MySQL database

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

  print(f"Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")
  input("\n\tPress any key to continue...")

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("The supplied username or password is invalid")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("The specified database does not exist")
  else:
    print(err)
  
finally:
  db.close()
