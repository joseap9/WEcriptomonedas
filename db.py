import psycopg2

conn = psycopg2.connect(host = '127.0.0.1',
database = 'coins',
user = 'postgres' ,
password = 'Japa1998',
connect_timeout=3)

cursor = conn.cursor()

sql = "insert into coin(name,valor,volumen) values ('coin3',5,3);"

cursor.execute(sql)

sql = "select * from coin;"

cursor.execute(sql)

response = cursor.fetchall()

conn.commit()

print(response)
