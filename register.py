import db_connection

def register():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    phone = input("Phone: ")
    
    with db_connection.conn.cursor() as cur:
        try:
            cur.execute(f"""
                INSERT INTO Customers (username, password, email, phone_number, is_admin)
                VALUES ({username}, {password}, {email}, {phone}, FALSE)
            """)
            print("Успешная регистрация!")
        except Exception as e:
            print("Ошибка регистрации:", e)

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    with db_connection.conn.cursor() as cur:
        cur.execute(f"SELECT id, username, password, email, phone_number, is_admin FROM Customers WHERE username={username} AND password={password}")
        user = cur.fetchone()
        
        if user:
            db_connection.current_user = user
            print(f"\nДобро пожаловать, {user[1]}!")
        else:
            print("Неверный логин или пароль!")

def logout():
    db_connection.current_user = None
    print("Вы вышли из системы.")