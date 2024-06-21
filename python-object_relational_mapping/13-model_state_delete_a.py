#!/usr/bin/python3
"""This script allows us to connect to a MySQL database,
thanks to create_engine, sessionmaker creates an interface
that allows us to interacte with the database and do
operations like retrieving rows from a table, thanks
to Session's query method"""
if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    for arguments in sys.argv:
        if ";" in arguments:
            raise ValueError
        my_sql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            my_sql_username, mysql_password,
                            database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session_object = Session()
    session_object.query(State).filter(State.name.contains('a')).delete()
    session_object.commit()
