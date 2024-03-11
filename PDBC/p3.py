import mysql.connector
con = mysql.connector.connect(host='localhost', database='cat', user='root', password='8919398624')
cursor = con.cursor()
insert = 'insert into empolyee(emo, ename, age, ecity, ecountry) values(%s, %s, %s, %s, %s)'
values = (101, "Youns", 22, "adoni", "india")
values = (102, "Talha", 23, "adoni", "india")
print("inserted data")
cursor.execute(insert, values)
con.commit()
cursor.close()
con.close()