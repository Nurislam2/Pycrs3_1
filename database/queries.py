class Queries:
    CREATE_SURVEY_RESULTS_TABLE = """
        CREATE TABLE IF NOT EXISTS survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone_number TEXT,
            visit_date DATE,
            food_rating INTEGER,
            cleanliness_rating INTEGER,
            extra_comments TEXT
        )
    """

    DROP_CATEGORIES_TABLE = """
        DROP TABLE IF EXISTS categories
    """

    CREATE_CATEGORIES_TABLE = """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """

    POPULATE_CATEGORIES = """
        INSERT INTO categories(name) VALUES 
            ("Первые блюда"),
            ("Детское блюда"),
            ("Салаты")
    """

    DROP_DISHES_TABLE = "DROP TABLE IF EXISTS dishes"

    CREATE_DISHES_TABLE = """
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            cover TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """

    POPULATE_DISHES = """
    INSERT INTO dishes(name, price, cover, category_id) VALUES 
    ('Борщ зеленый с щавелем', 390, 'pictures/First/1.png', 1),
    ('Домашний борщ', 320, 'pictures/First/2.png', 1),
    ('Сырники с изюмом и вареньем', 275, 'pictures/Kids/1.png', 2),
    ('Блинчики со сгущенкой', 130, 'pictures/Kids/2.png', 2),
    ('Цезарь', 590, 'pictures/Salad/1.png', 3),
    ('Бархат', 410, 'pictures/Salad/2.png', 3)
    """
