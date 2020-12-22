import psycopg2

conn = psycopg2.connect(database='employeedb',user='asad',password='1234')
cr = conn.cursor()
cr.execute('alter table product add column cat_id int')
cr.execute('alter table product add constraint f_key foreign key(cat_id) references category(id)')
conn.commit()
cr.close()
conn.close()
