import db_connection
from hashing import hash_password, verify_password

def register():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    phone = input("Phone: ")
    
    hashed_pwd = hash_password(password)
    
    try:
        with db_connection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO Customers (username, password, email, phone_number, is_admin)
                    VALUES (%s, %s, %s, %s, FALSE)
                """, (username, hashed_pwd, email, phone))
                conn.commit()
                print("Успешная регистрация!")
    except Exception as e:
        print("Ошибка регистрации:", e)

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    try:
        with db_connection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, username, password, email, phone_number, is_admin FROM Customers WHERE username=%s", (username,))
                user = cur.fetchone()
                
                if user and verify_password(password, user[2]):
                    db_connection.current_user = user
                    print(f"\nДобро пожаловать, {user[1]}!")
                else:
                    print("Неверный логин или пароль!")
    except Exception as e:
        print("Ошибка входа:", e)

def logout():
    db_connection.current_user = None
    print("Вы вышли из системы.")