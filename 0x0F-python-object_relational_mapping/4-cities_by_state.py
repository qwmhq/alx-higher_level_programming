#!/usr/bin/python3
"""4-cities_by_state
lists all cities from the given database
"""
import sys
import MySQLdb


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=user,
                         passwd=passwd,
                         db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                LEFT JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id ASC;")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
