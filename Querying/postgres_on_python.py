# Using PostgreSQL on Python

import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
cur = conn.cursor()

########################### do sth ###########################

cur.execute("""CREATE TABLE IF NOT EXISTS person (
    id INT PRIMARY KEY, 
    name VARCHAR(255), 
    age INT, 
    gender CHAR
    );
""")

cur.execute("""INSERT INTO person 
    (id, name, age, gender) VALUES
    (1, 'Adam', 28, 'm'),
    (2, 'Bob', 50, 'm'),
    (3, 'Charlotte', 22, 'f'),
    (4, 'Daniel', 35, 'm'),
    (5, 'Erika', 33, 'f')
""")

cur.execute("""
SELECT * FROM person WHERE name = 'Bob';
""")

print(cur.fetchone())

cur.execute("""
SELECT * FROM person WHERE age < 50;
""")

##############################################################


conn.commit()
cur.close()
conn.close()