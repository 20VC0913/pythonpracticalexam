import mysql.connector as sql
connect=sql.connect(host='localhost',user="root",passwd="root", database="studentdb")
cur=connect.cursor()
cur.execute("select * from student")
for x in cur:
    print(x)