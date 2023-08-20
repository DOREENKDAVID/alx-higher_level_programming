#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa:
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State, City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query_rows = session.query(City, State).filter(City.state_id == State.id)
    .order_by(City.id).all()
    for city, state in query_rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
