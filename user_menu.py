import datetime
import db_connection
import register

def user_menu():
    print("\n--- USER MENU ---")
    print("[1] Menu")
    print("[2] Order table")
    print("[3] Order item")
    print("[4] Cancel order")
    print("[5] Logout")
    choice = input("Выберите пункт: ")

    with db_connection.conn.cursor() as cur:
        match choice:
            case "1":
                cur.execute("SELECT id, food_name, price FROM Foods")
                foods = cur.fetchall()
                print("\n--- МЕНЮ ---")
                for f in foods:
                    print(f"[{f[0]}] {f[1]} — {f[2]} сомони")

            case "2":
                table_num = int(input("Номер столика: "))
                customer_id = db_connection.current_user[0]
                cur.execute(f"INSERT INTO Orders (customer_id, table_number) VALUES ({customer_id}, {table_num})")

                cur.execute(f"SELECT MAX(id) FROM Orders WHERE customer_id = {customer_id}")
                order_id = cur.fetchone()[0]

                print(f"Заказ успешно создан! Ваш Order ID: {order_id}")

            case "3":
                order_id = int(input("Order ID: "))
                food_id = int(input("Food ID: "))
                qty = int(input("Количество: "))
            
                cur.execute(f"""
                    INSERT INTO Order_Items (order_id, food_id, quantity) 
                    VALUES ({order_id}, {food_id}, {qty})
                """)
            
                cur.execute(f"""
                    UPDATE Orders SET total_price = (
                        SELECT SUM(f.price * oi.quantity)
                        FROM Order_Items oi
                        JOIN Foods f ON oi.food_id = f.id
                        WHERE oi.order_id = {order_id}
                    ) WHERE id = {order_id}
                """)
                print("Блюдо добавлено, общая сумма заказа пересчитана!")

            case "4":
                order_id = int(input("Order ID: "))
                customer_id = db_connection.current_user[0]

                cur.execute(f"SELECT order_date FROM Orders WHERE id={order_id} AND customer_id={customer_id}")
                order = cur.fetchone()

                if order:
                    order_date = order[0].date()
                    today = datetime.date.today()

                    if order_date == today:
                        cur.execute(f"UPDATE Orders SET status='Cancelled' WHERE id={order_id}")
                        print("Заказ успешно отменён!")
                    else:
                        print("Отмена невозможна: заказ был сделан не сегодня.")
                else:
                    print("Заказ не найден или принадлежит не вам.")

            case "5":
                register.logout()

            case _:
                print("Неверный пункт меню!")