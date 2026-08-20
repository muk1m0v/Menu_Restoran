import db_connection
import register
import admin
import user_menu

db_connection.init_db()

while True:
    if not db_connection.current_user:
        print("\n[1] Login")
        print("[2] Register")
        print("[0] Exit")
        ok = input("Выберите действие: ")
        
        match ok:
            case "1":
                register.login()
            case "2":
                register.register()
            case "0":
                break
            case _:
                print("Неверный ввод!")
    else:
        is_admin = db_connection.current_user[5]
        
        if is_admin:
            admin.admin_menu()
        else:
            user_menu.user_menu()