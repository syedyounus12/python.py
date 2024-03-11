import mysql.connector

con = mysql.connector.connect(host='localhost', database='cat', user='root', password='8919398624')
print("Created Completed")

cursor = con.cursor()

create = 'create table empolyee(emo int, ename varchar(40), age int, ecity varchar(40), ecountry varchar(40))'

cursor.execute(create)

cursor.close()