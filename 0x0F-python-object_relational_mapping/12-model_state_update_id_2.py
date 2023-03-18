#!/usr/bin/python3
"""12-model_state_update_id_2
change the name of a State object from the database
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
    query = session.query(State).filter(State.id == 2)
    state = query.first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
