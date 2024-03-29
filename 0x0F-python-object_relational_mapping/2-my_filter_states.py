#!/usr/bin/python3
"""2-my_filter_states
lists all states with a name matching the given string
from the given database
"""
import sys
import MySQLdb


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=user,
                         passwd=passwd,
                         db=database,
                         charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT *\
                FROM states\
                WHERE BINARY name='{:s}'\
                ORDER BY states.id ASC;".format(state))
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
