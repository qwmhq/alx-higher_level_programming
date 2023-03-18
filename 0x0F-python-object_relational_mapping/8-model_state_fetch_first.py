#!/usr/bin/python3
"""8-model_state_fetch_first
fetch the first state in the states table
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
    query = session.query(State).order_by(State.id)
    state = query.first()
    if state is None:
        print('Nothing')
    else:
        print('{}: {}'.format(state.id, state.name))
    session.close()
