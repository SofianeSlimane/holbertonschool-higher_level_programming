#!/usr/bin/python3
"""This module connects to MySQL database and lists all
specific rows from a table, safe from SQL injection"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(sys.argv) > 4 or ";" in sys.argv[3]:
        raise ValueError
    else:
        my_sql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=my_sql_username,
                         passwd=mysql_password, db=database_name,
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities,
                 states WHERE states.id = cities.state_id
                 ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # print(sys.argv)
    # print(len(sys.argv))
    cur.close()
    db.close()
