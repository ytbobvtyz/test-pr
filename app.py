
def get_user(user_id):
    return db.query(f"SELECT * FROM users WHERE id={user_id}")

def delete_user(user_id):
    db.execute(f"DELETE FROM users WHERE id={user_id})

def i_am_robot(robot):
	print(f'i am {robot}')
