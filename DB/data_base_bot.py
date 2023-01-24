import sqlite3
from pathlib import Path


def init():
    """
    Создание файла sqlite3
    """
    DB_NAME = 'db.sqlite3'
    DB_PATH = Path(__file__).parent.parent
    global db, cur
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cur = db.cursor()


def create_table():
    """
    создания таблиц
    """
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER,
            photo TEXT)
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            username TEXT,
            adress TEXT,
            age INTEGER,
            day TEXT,
            product_id INTEGER,
            FOREIGN KEY (product_id)
                REFERENCES products (product_id)
                ON DELETE CASCADE)
        """
    )
    db.commit()


def make_full_products():
    """
     таблица products
    """
    cur.execute("""INSERT INTO products(
    name,
    price,
    photo
    ) VALUES
    ('Магнит Души', 1, 'images/dusha_cheloveka.jpg'),
    ('Магнит Человечина', 1, 'images/uS4qWjJwSUw.jpg'),
    ('Магнит', 1, 'images/article_horseshoe-magnet_www.kepfeltoltes.hu_-1200x1005'),
    ('Статуэтка Джозефа', 1, 'assortiments/2604061696_w700_h500_kollektsionnaya-statuetka-veronese.webp'),
    ('Плакат с Джо Джо', 1, 'images/people_2_smock_front_black_500'),
    ('Свитшот с Джостарами', 1, 'imagde/_J4cLtxDOmo.jpg'),
    ('Свитшот с Дио', 1, 'images/people_24_child_sweatshirt_front_black_500.jpg'),
    ('Свитшот с Спид вагоном', 1, 'images/')
    """)
    db.commit()


def get_products():
    """
    Достаём данные из products
    """
    cur.execute("""
    SELECT * FROM products
    """)
    return cur.fetchall()


def make_full_order(data):
    """
        Заполняем таблицу order
    """
    data = data.as_dict()
    cur.execute("""INSERT INTO orders(
        username,
        adress,
        age,
        day,
        product_id
    ) VALUES (:user_name,:adress,:age,:day,:product_id)""",
                {'user_name': data['name'],
                'adress': data['adress'],
                 'age': data['age'],
                 'day': data['day'],
                 'product_id': data['product_id']})
    db.commit()
