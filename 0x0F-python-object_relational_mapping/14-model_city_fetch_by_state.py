#!/usr/bin/python3
"""14-model_fetch_by_state.py
print all City objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, passwd, database)
    engine = create_engine(conn_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = (session.query(City, State)
                    .filter(City.state_id == State.id)
                    .order_by(City.id))
    for city, state in query.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
