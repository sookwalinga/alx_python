#!/usr/bin/python3
"""List all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
    
        # Create a cursor to interact with the database
        cursor = db.cursor()

        # Execute the SELECT query to list all cities
        query = ("SELECT cities.id, cities.name, states.name "
                 "FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "ORDER BY cities.id")
        cursor.execute(query)

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
