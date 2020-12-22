import psycopg2

conn = psycopg2.connect(database='employeedb',user='asad',password='1234')
cr = conn.cursor()
cr.execute("create table product (id int primary key default nextval('inc'), name varchar(50), cost_price int ,sell_price int check(sell_price > cost_price))")
conn.commit()
cr.close()
conn.close()
