# https://github.com/vo0x
import sqlite3

def init_db():
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, last_name TEXT)''')
    conn.commit()
    conn.close()

def register_user(user_id, username, first_name, last_name):
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT OR IGNORE INTO users (user_id, username, first_name, last_name)
                      VALUES (?, ?, ?, ?)''', (user_id, username, first_name, last_name))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT user_id FROM users''')
    users = cursor.fetchall()
    conn.close()
    return [user[0] for user in users]

def get_user_count():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT COUNT(*) FROM users''')
    count = cursor.fetchone()[0]
    conn.close()
    return count