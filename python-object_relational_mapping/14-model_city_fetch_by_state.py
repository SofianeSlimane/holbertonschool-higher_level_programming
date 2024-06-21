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
    from model_city import City

    my_sql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            my_sql_username, mysql_password,
                            database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session_object = Session()
    joined_rows = session_object.query(
        City, State).join(State).order_by(City.id.asc())
    for instance, instance2 in joined_rows:
        print(f"{instance2.name}:  ({instance.id}) {instance.name}")
