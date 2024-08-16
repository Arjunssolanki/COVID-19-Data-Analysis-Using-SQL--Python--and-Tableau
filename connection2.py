import psycopg2
from config import HOST, USER, PASSWORD, DATABASE, PORT
import pandas as pd

class PostgreSQLConnection:
    def __enter__(self):
        
        self.connection = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            port=PORT
        )
        return self.connection
# closing the connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        
        if hasattr(self, 'connection'):
            self.connection.close()
            print("Connection closed")


def fetch_data(query):
    with PostgreSQLConnection() as connection:
        df = pd.read_sql(query, connection)
    return df
