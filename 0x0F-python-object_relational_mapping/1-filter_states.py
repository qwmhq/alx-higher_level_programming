#!/usr/bin/python3
"""1-filter_states
lists all states with a name starting with N
from the given database
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT *\
                 FROM states\
                 WHERE name LIKE BINARY 'N%'\
                 ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
