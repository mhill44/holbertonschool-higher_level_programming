#!/usr/bin/python3
'''takes an argument and displays all values
in states table of hbtn_0e_0_usa
where NAME matches argument'''
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

    with db.cursor() as cur:
        cur.execute(""" SELECT * FROM states
                    WHERE states.name = %s""", (A_STATE,))
        query_rows = cur.fetchall()
        for row in query_rows:
            if row[1] == sys.argv[4]:
                print(row)

        cur.close()
        db.close()

