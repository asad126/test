import psycopg2

conn = psycopg2.connect(database='employeedb',user='asad',password='1234')
cr = conn.cursor()
cr.execute("select max(sell_price) as Maximum from product")
rows = cr.fetchall()
print(rows)
conn.commit()
cr.close()
conn.close()
