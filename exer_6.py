import psycopg2

conn = psycopg2.connect(database='employeedb',user='asad',password='1234')
cr = conn.cursor()


"""
category_records =[ (1,101,'mobiles'),
	(2,102,'mobile accessories'),
	(3,103,'laptops'),
	(4,104,'earphons'),
	(5,105,'shoes'),
	(6,106,'shocks'),
	(7,107,'television'),
	(8,108,'air conditioner'),
	(9,109,'washing machine'),
	(10,110,'refrigerators'),
	(11,111,'watches'),
	(12,112,'winter wear'),
	(13,113,'clothing'),
	(14,114,'toys'),
	(15,115,'cycles'),
	(16,116,'kids clothing '),
	(17,117,'furniture'),
	(18,118,'books'),
	(19,119,'decorations'),
	(20,120,'groceries')
]



for i in category_records:
	a = (f"insert into category (id,code,name) values ({i[0]},{i[1]},'{i[2]}')")
	cr.execute(a)
	conn.commit()

"""


product_records = [
    (1,'realmec15', 8999, 9499, 1),
    (2,'poco m2', 8000, 10000 ,1),
    (3,'iphone ', 8000, 10000 ,1),
    (4,'realme narzo 20', 9499, 10499, 1),
    (5,'Mi 4A pro 80 cm smart TV', 12999, 13999, 4),
    (6,'Nokia 80 cm smart TV', 11999, 14499, 4),
    (7,'alessa Running', 499, 661, 3),
    (8,'snekers for women', 299, 348, 3),
    (9,'Full sleeve solid men Sweatshirt', 599, 759, 5),
    (10,'slim men light blue', 399, 498, 5),
    (11,'printed women round neck', 199, 319, 6),
    (12,'solid women round neck blue', 99, 169, 6),
    (13,'Decorum 160 TC polycotton', 199, 259, 8),
    (14,'Decor home 140 TC microfiber', 199, 248, 8),
    (15,'Remote control helicopter', 299, 439, 7),
    (16,'Remote control car', 199, 397, 7),
    (17,'Shrimad bhagabvad gita', 99, 183, 10),
    (19,'smanay', 99, 156, 10),
    (20,'hot water bag', 99, 186, 11),
    (21,'hot water bag electric', 99, 256, 11),
    (22,'gaming keyboard', 899, 1256, 13),
    (23,'gaming mouse', 999, 1356, 13), 
]

for i in product_records:
	a = (f"insert into product (id,name,cost_price,sell_price,cat_id) values ({i[0]},'{i[1]}',{i[2]},{i[3]},{i[4]})")
	cr.execute(a)
	conn.commit()



cr.close()
conn.close()






