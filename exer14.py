import psycopg2

conn = psycopg2.connect(database='employeedb',user='asad',password='1234')
cr = conn.cursor()

cr.execute("select product.id,product.name,product.cost_price,product.sell_price,category.code,category.name from product inner join category on product.id = category.id")
rows = cr.fetchall()
for i in  rows:
	print(i)
conn.commit()
cr.close()
conn.close()
