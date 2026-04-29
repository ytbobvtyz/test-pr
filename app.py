def get_user(user_id):
    return db.query(f"SELECT * FROM users WHERE id={user_id}")
