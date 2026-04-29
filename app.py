def get_user(user_id):
    import sqlite3
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def delete_user(user_id):
    import sqlite3
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
