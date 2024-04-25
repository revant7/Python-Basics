import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="students"
)

cur = mydb.cursor()
cur.execute("select * from student")
r = cur.fetchone()
print(type(r))

