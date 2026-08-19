from db_connection import *

def register(username, password, email):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
            INSERT INTO users (username, password, email) values
            ('{username}','{password}','{email}')
            ''')
            conn.commit()
            print('User Registred\n')
    except Exception as err:
        print('Registration error: ',err)

def get_user(username):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
            select * from users where username='{username}'
            ''')
            user = cursor.fetchone()
            return user
    except Exception as err:
        print('Get user error: ',err)

def login(username, password):
    user_exists = get_user(username)
    if user_exists:
        if password == user_exists[2]:
            return user_exists
        else:
            print('Incorrect password!\n')
    else:
        print('User not found\n')