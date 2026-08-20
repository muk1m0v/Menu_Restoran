import db_connection
<<<<<<< HEAD
from hashing import hash_password, verify_password
=======
>>>>>>> c8f6537813e323f84729d4dfb8fd17e18d252657

def register():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    phone = input("Phone: ")
    
<<<<<<< HEAD
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
=======
    with db_connection.conn.cursor() as cur:
        try:
            cur.execute(f"""
                INSERT INTO Customers (username, password, email, phone_number, is_admin)
                VALUES ('{username}', '{password}', '{email}', '{phone}', FALSE)
            """)
            db_connection.conn.commit()
            print("Успешная регистрация!")
        except Exception as e:
            print("Ошибка регистрации:", e)
>>>>>>> c8f6537813e323f84729d4dfb8fd17e18d252657

def login():
    username = input("Username: ")
    password = input("Password: ")
    
<<<<<<< HEAD
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
=======
    with db_connection.conn.cursor() as cur:
        cur.execute(f"SELECT id, username, password, email, phone_number, is_admin FROM Customers WHERE username='{username}' AND password='{password}'")
        user = cur.fetchone()
        
        if user:
            db_connection.current_user = user
            print(f"\nДобро пожаловать, {user[1]}!")
        else:
            print("Неверный логин или пароль!")
>>>>>>> c8f6537813e323f84729d4dfb8fd17e18d252657

def logout():
    db_connection.current_user = None
    print("Вы вышли из системы.")