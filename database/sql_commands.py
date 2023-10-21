import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("db.sqlite3")
        self.cursor = self.conn.cursor()

    def sql_create_tables(self):
        if self.conn:
            print("Database connected successfully")

        self.conn.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.conn.commit()

    def sql_insert_user_query(self, telegram_id, useername, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, useername, first_name, last_name)
        )
        self.conn.commit()
