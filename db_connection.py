import psycopg2

current_user = None

def get_connection():
    return psycopg2.connect(
        dbname="menu", 
        user="postgres", 
        password="MUKIMO707", 
        host="localhost", 
        port="5432"
    )

def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Foods (
                    id SERIAL PRIMARY KEY,
                    food_name VARCHAR(100) NOT NULL,
                    price SMALLINT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS Customers (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    email VARCHAR(100),
                    phone_number VARCHAR(20),
                    is_admin BOOLEAN DEFAULT FALSE
                );
                CREATE TABLE IF NOT EXISTS Orders (
                    id SERIAL PRIMARY KEY,
                    customer_id INT REFERENCES Customers(id) ON DELETE CASCADE,
                    total_price SMALLINT DEFAULT 0,
                    table_number SMALLINT,
                    order_date TIMESTAMP DEFAULT NOW(),
                    status VARCHAR(20) DEFAULT 'Pending'
                );
                CREATE TABLE IF NOT EXISTS Order_Items (
                    id SERIAL PRIMARY KEY,
                    order_id INT REFERENCES Orders(id) ON DELETE CASCADE,
                    food_id INT REFERENCES Foods(id) ON DELETE CASCADE,
                    quantity INT NOT NULL
                );
            """)
            conn.commit()