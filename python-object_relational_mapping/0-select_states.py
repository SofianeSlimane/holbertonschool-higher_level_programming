#!/usr/bin/python3
"""This module connects to MySQL database and lists all
all rows from a table"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    my_sql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost', user=my_sql_username,
                         passwd=mysql_password, db=database_name,
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
