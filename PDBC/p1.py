import mysql.connector

con = None
try:

    con = mysql.connector.connect(host='localhost', database='cat', user='root', password='8919398624')

    print("connection tested")

except BaseException as e:

    print("Exceptions is:", e)

finally:
    con.close()
