import sqlite3
import os

class Database:

    def __init__(self, database_path):


        os.makedirs(os.path.dirname(database_path), exist_ok=True)
        self.connection = sqlite3.connect(
                "database/test_bench.db"
        )

        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inspections(
                id INTEGER PRIMARY KEY,
                result TEXT
            )
        """)

        self.connection.commit()

    def save(self, result):

        self.cursor.execute(
                "INSERT INTO inspections(result) VALUES(?)",
                (result,)
        )

        self.connection.commit()
