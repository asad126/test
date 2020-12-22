import psycopg2

conn = psycopg2.connect(database='employeedb',user='asad',password='1234')
cr = conn.cursor()
cr.execute('create table category (id serial primary key, code int unique, name varchar(50) not null)')
conn.commit()
cr.close()
conn.close()
