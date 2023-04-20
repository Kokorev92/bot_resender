import sqlite3
import sqlite3 as sl
import logging

logging.basicConfig(level=logging.DEBUG)

db = sl.connect('bot.db')
user = (1234567, 'User1', 'pass1')
try:
    db.execute('INSERT INTO users (id,login, pass) VALUES(?,?, ?);', user)
    db.commit()
except sqlite3.Error as err:
    print('ERROR DB:', err)

data = db.execute('SELECT * FROM users;')

# print(data.fetchall())

for row in data:
    print(row)