#!/usr/bin/python3
"""Script to display values in the states table where name matches the argument"""

import MySQLdb
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 5:
    print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
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

    # Execute the SELECT query with the user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

except MySQLdb.Error as e:
    print("MySQL Error: {}".format(e))
    sys.exit(1)
