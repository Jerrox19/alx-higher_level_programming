#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute SELECT query to retrieve all states
    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    # Display results
    for state in cursor.fetchall():
        print(state)

    # Close cursor and database
    cursor.close()
    db.close()
