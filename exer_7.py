import psycopg2

conn = psycopg2.connect(database='employeedb',user='asad',password='1234')
cr = conn.cursor()
cr.execute("select * from product")
rows = cr.fetchall()
for i in rows:
	print(i)
conn.commit()
cr.close()
conn.close()
