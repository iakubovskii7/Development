import sqlite3


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