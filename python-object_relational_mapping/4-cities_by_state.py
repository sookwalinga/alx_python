#!/usr/bin/python3
"""List all cities of a state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 5:
    print("Usage: {} <username> <password> <database> <state_name>"
          .format(sys.argv[0]))
    sys.exit(1)

# Retrieve command line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

try:
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor to interact with the database
    cursor = db.cursor()

    # Execute the SELECT query to list cities of the given state
    query = ("SELECT cities.name, states.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id")
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print("{}, {}".format(row[0], row[1]))

    # Close the cursor and the database connection
    cursor.close()
    db.close()

except MySQLdb.Error as e:
    print("MySQL Error: {}".format(e))
    sys.exit(1)
