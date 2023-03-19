#!/usr/bin/python3
"""100-relationship_states_cities
create the State 'California with the city 'San Fransisco'
from the database hbtn_0e_100_usa
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_city = City(name='San Fransisco')
    new_state = State(name='California', cities=[new_city])
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()
