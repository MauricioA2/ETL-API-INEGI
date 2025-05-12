import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path='data/precios_combustible.db'):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path

    def save_dataframe(self, df, table_name='precios'):
        with sqlite3.connect(self.db_path) as conn:
            df.to_sql(table_name, conn, if_exists='append', index=False)