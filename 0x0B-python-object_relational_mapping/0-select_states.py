#!/usr/bin/python3
"""
Wll select all from table states from the DB hbtn_0e_0_usa
mapped to port 3306 on localhost
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
