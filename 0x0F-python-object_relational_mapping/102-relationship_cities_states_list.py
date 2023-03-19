#!/usr/bin/python3
"""102-relationship_cities_states_list
list all City objects from the database hbtn_0e_101_usa
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
    query = session.query(City).order_by(City.id)
    for city in query.all():
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
    session.close()
