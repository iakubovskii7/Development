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


create_table5 = """
DROP TABLE IF EXISTS product_segment, product;

CREATE TABLE IF NOT EXISTS product_segment (
    ID SERIAL PRIMARY KEY,
    segment VARCHAR NOT NULL,
    discount NUMERIC (4, 2)
);
 
 
INSERT INTO product_segment (segment, discount)
VALUES
    ('Grand Luxury', 0.05),
    ('Luxury', 0.06),
    ('Mass', 0.1);
    
CREATE TABLE IF NOT EXISTS product(
    id serial primary key,
    name varchar not null,
    price numeric(10,2),
    net_price numeric(10,2),
    segment_id int not null,
    foreign key(segment_id) references product_segment(id)
);
 
 
INSERT INTO product (name, price, segment_id) 
VALUES ('diam', 804.89, 1),
    ('vestibulum aliquet', 228.55, 3),
    ('lacinia erat', 366.45, 2),
    ('scelerisque quam turpis', 145.33, 3),
    ('justo lacinia', 551.77, 2),
    ('ultrices mattis odio', 261.58, 3),
    ('hendrerit', 519.62, 2),
    ('in hac habitasse', 843.31, 1),
    ('orci eget orci', 254.18, 3),
    ('pellentesque', 427.78, 2),
    ('sit amet nunc', 936.29, 1),
    ('sed vestibulum', 910.34, 1),
    ('turpis eget', 208.33, 3),
    ('cursus vestibulum', 985.45, 1),
    ('orci nullam', 841.26, 1),
    ('est quam pharetra', 896.38, 1),
    ('posuere', 575.74, 2),
    ('ligula', 530.64, 2),
    ('convallis', 892.43, 1),
    ('nulla elit ac', 161.71, 3);
"""
