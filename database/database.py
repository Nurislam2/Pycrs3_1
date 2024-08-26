import sqlite3
from database.queries import Queries


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(Queries.CREATE_SURVEY_RESULTS_TABLE)
            conn.execute(Queries.DROP_CATEGORIES_TABLE)
            conn.execute(Queries.CREATE_CATEGORIES_TABLE)
            conn.execute(Queries.POPULATE_CATEGORIES)
            conn.execute(Queries.DROP_DISHES_TABLE)
            conn.execute(Queries.CREATE_DISHES_TABLE)
            conn.execute(Queries.POPULATE_DISHES)

            conn.commit()

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)

            conn.commit()

    def fetch(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute(query, params)

            return result.fetchall()



