#!/usr/bin/python3
"""5-filter_cities
lists all cities from a state from the given database
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
    cur.execute("SELECT cities.name\
                FROM states\
                LEFT JOIN cities\
                ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;",
                (state,))

    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(', '.join(cities))

    cur.close()
    db.close()
