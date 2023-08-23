#!/usr/bin/python3
"""List states with names starting with 'N' from db: hbtn_0e_0_usa"""

import MySQLdb
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 4:
    print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    sys.exit(1)

# Retrieve command line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

try:
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor to interact with the database
    cursor = db.cursor()

    # Execute the SELECT query for states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

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
