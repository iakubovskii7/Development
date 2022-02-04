import sqlite3
from sqlalchemy import create_engine
import pandas as pd

def create_connection_sqlite():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    return conn


def sql_query(query,
              dbname='dvdrental', user='postgres', password='postgres',
              host='localhost', port=5432):
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")
    df = pd.read_sql(query, engine)
    return df


def exec_sql(sql, connection):
    try:
        cur = connection.cursor()
        cur.execute(sql)
        connection.commit()
    except Exception as e:
        print(e)
        connection.rollback()
    return


