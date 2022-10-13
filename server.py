import psycopg2

conn = psycopg2.connect(
    database='test',
    host='localhost',
    user='admin',
    password='admin',
    port='5432'
    )

cursor = conn.cursor()
cursor.execute('SELECT * FROM people')
colnames = [desc[0] for desc in cursor.description]
print('colnames', colnames)