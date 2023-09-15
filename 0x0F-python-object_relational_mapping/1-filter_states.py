#!/usr/bin/python3
""" Script that lists all 'states' with a 'name' starting with 'N' from the
    database 'hbtn_0e_usa' """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Scrip that list all states with a name starting with 'N' """
    db = MySQLdb.connect(host="localhost",  # your host
                         user=argv[1],       # username
                         passwd=argv[2],     # password
                         db=argv[3],
                         port=3306)   # name of the database
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states
                WHERE name like BINARY 'N%'
                ORDER BY id ASC;""")
    for row in cur.fetchall():
        print(row)

    cursor.close()
    db.close()
