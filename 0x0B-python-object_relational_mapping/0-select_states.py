#!/usr/bin/python3
""" Wll select states from a database """
import MySQLdb
import sys

if __name__ == "__main__":

    """ The Connection Variables """
    DB_HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    DB_PORT = '3306'

    """ This connects to the DB """
    db = MySQLdb.connect(host=DB_HOST, port=int(DB_PORT),
                         user=DB_USER, passwd=DB_PASS,
                         db=DB_NAME, charset='utf8')

    with db.cursor() as cur:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        cur.close()
        db.close()
