#!/usr/bin/python3
"""3-my_safe_filter_states
lists all states with a name matching the given string
from the given database safely
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
                         db=database)
    cur = db.cursor()
    cur.execute("SELECT *\
                FROM states\
                WHERE name=%s\
                ORDER BY id ASC;",
                (state,))
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
