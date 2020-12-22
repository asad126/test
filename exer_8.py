import psycopg2

conn = psycopg2.connect(database='employeedb',user='asad',password='1234')
cr = conn.cursor()
cr.execute("select * from product")  # limit 1 can be possible
rows = cr.fetchone()
print(rows)
conn.commit()
cr.close()
conn.close()
