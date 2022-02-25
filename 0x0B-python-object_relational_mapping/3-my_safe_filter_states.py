#!/usr/bin/python3
"""takes an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
and is safe from SQL injections"""

if __name__ == '__main__':
    
import MySQLdb
import sys

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
                    WHERE states.name = %(states)s""", {'states': A_STATE})
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        cur.close()
        db.close()
