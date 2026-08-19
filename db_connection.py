import psycopg2


def get_connection():
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            database='task_meneger_db',
            port=5432,
            password='MUKIMO707'
        )
        return conn
    except Exception as err:
        print(f'Connection Error: {err}')



def init_tables():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (
                id SERIAL PRIMARY KEY,
                username varchar(50) not null unique,
                password varchar(50) not null,
                email varchar(100) not null unique
            );
            CREATE TABLE IF NOT EXISTS tasks
            (
                id serial primary key,
                title varchar(150) not null,
                user_id int references users(id) on delete cascade,
                due_date timestamp default now(),
                is_completed boolean default false,
                created_at timestamp default now()
            )
            ''')
            conn.commit()
    except Exception as err:
        print('Cretion tables error: ',err)