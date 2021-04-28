import pymysql
db=pymysql.connect(host='localhost', user='root',password='',db='vishnu')
a=db.cursor()
q="select * from databook"
a.execute(q)
b=a.fetchall()
for i in b:
    id=i[0]
    name=i[1]
    add=i[2]
    sal=i[3]
    print("Employee ID :",id,"\tName :",name,"\tAddress :",add,"\tSalary :",sal)
ID=int(input("Enter ID:"))
q1="select * from databook where Id=%d"%ID
a.execute(q1)
c=a.fetchone()
name1 = c[1]
add1 = c[2]
sal1 = c[3]
print("Employee ID :",ID,"\tName :",name1,"\tAddress :",add1,"\tSalary :",sal1)
db.commit()