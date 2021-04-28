import pymysql
db=pymysql.connect(host='localhost', user='root',password='',db='vishnu')
a=db.cursor()
ID=int(input("Enter ID:"))
b=input("Do you want to Delete (y/n)?:")
if b=="y":
    q="delete from databook where Id=%d"%ID
    a.execute(q)
    db.commit()
elif b=="n":
    print("exit")