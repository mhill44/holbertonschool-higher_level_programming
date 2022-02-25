#!/usr/bin/python3
'''
a script that lists all states with a name starting
with uppercase N from the DB hbtn_0e_0_usa
'''

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute(SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
        cursor.close()
        db.close()
