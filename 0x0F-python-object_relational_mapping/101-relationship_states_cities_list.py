#!/usr/bin/python3
"""101-relationship_states_cities_list
list all State objects, and corresponding City objects
from the database hbtn_0e_101_usa
"""
import sys
from relationship_city import City
from relationship_state import Base, State
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
    query = session.query(State).order_by(State.id)
    for state in query.all():
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))
    session.close()
