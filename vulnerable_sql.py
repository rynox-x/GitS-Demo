import sqlite3

conn = sqlite3.connect("db.sqlite")

username = input()

query = (
    "SELECT * FROM users "
    "WHERE username = '" + username + "'"
)

conn.execute(query)
