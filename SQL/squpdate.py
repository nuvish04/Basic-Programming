import pymysql
db=pymysql.connect(host='localhost', user='root',password='',db='vishnu')
a=db.cursor()
ID=int(input("Enter ID:"))
b=input("Do you want to Update (y/n)?:")
if b=="y":
    name1=input("Enetr the new Name:")
    q="update databook set Name='%s' where Id=%d"%(name1,ID)
    a.execute(q)
    db.commit()
elif b=='n':
    print("Exit")