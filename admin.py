import db_connection
import register

def admin_menu():
    print("\n--- ADMIN MENU ---")
    print("[1] Add food")
    print("[2] Get food")
    print("[3] Change food")
    print("[4] Delete food")
    print("[5] Get customers")
    print("[6] Delete customer")
    print("[7] Get orders")
    print("[8] Delete order")
    print("[9] Logout")
    choice = input("Выберите пункт: ")

    with db_connection.conn.cursor() as cur:
        match choice:
            case "1":
                name = input("Название блюда: ")
                price = int(input("Цена: "))
                cur.execute(f"INSERT INTO Foods (food_name, price) VALUES ('{name}', {price})")
                print("Блюдо добавлено!")
                
            case "2":
                cur.execute("SELECT id, food_name, price FROM Foods")
                foods = cur.fetchall()
                print("\nСписок блюд:")
                for f in foods:
                    print(f"ID: {f[0]} | Название: {f[1]} | Цена: {f[2]}")
                    
            case "3":
                fid = int(input("ID блюда: "))
                price = int(input("Новая цена: "))
                cur.execute(f"UPDATE Foods SET price={price} WHERE id={fid}")
                print("Цена обновлена!")
                
            case "4":
                fid = int(input("ID блюда для удаления: "))
                cur.execute(f"DELETE FROM Foods WHERE id={fid}")
                print("Блюдо удалено!")
                
            case "5":
                cur.execute("SELECT id, username, email, phone_number, is_admin FROM Customers")
                customers = cur.fetchall()
                print("\nСписок пользователей:")
                for c in customers:
                    print(f"ID: {c[0]} | Пользователь: {c[1]} | Email: {c[2]} | Телефон: {c[3]} | Admin: {c[4]}")
                    
            case "6":
                cid = int(input("ID пользователя для удаления: "))
                cur.execute(f"DELETE FROM Customers WHERE id={cid}")
                print("Пользователь удалён!")
                
            case "7":
                cur.execute("SELECT id, customer_id, total_price, table_number, order_date, status FROM Orders")
                orders = cur.fetchall()
                print("\nСписок заказов:")
                for o in orders:
                    print(f"Заказ ID: {o[0]} | Customer ID: {o[1]} | Сумма: {o[2]} | Стол: {o[3]} | Дата: {o[4]} | Статус: {o[5]}")
                    
            case "8":
                oid = int(input("ID заказа для удаления: "))
                cur.execute(f"DELETE FROM Orders WHERE id={oid}")
                print("Заказ удалён!")

            case "9":
                register.logout()

            case _:
                print("Неверный пункт меню!")