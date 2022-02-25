#!/usr/bin/python3
"""takes the name of a state as an arg and
lists * cities of that state,
using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":

    """ Connection Variables """
    DB_HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    DB_PORT = '3306'
    A_STATE = sys.argv[4]

    ''' Connect to the database '''
    db = MySQLdb.connect(host=DB_HOST, port=int(DB_PORT),
                         user=DB_USER, passwd=DB_PASS,
                         db=DB_NAME, charset='utf8')

    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            WHERE states.name=%s", (A_STATE, ))

    query_rows = cur.fetchall()
    out = []
    for row in query_rows:
        out.append(row[0])

    print(', '.join(out))

    cur.close()
    db.close()
