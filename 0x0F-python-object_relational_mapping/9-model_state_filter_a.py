#!/usr/bin/python3
"""9-model_state_filter_a
list all State objects that contain the letter a
from the database
"""
import sys
from model_state import Base, State

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
    query = (session.query(State)
                    .filter(State.name.like('%a%'))
                    .order_by(State.id))
    for state in query.all():
        print('{}: {}'.format(state.id, state.name))
    session.close()
