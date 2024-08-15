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