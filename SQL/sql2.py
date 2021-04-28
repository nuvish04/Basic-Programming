import pymysql
def insertfn():
    name=input("Enter your Name :")
    cls=input("Enter your Class :")
    add=input("Enter your Address :")
    course=input("Enter your Course :")
    mark=int(input("Enter Marks :"))
    q="insert into student(name,class,address,course,mark)values('%s','%s','%s','%s',%d)"%(name,cls,add,course,mark)
    a.execute(q)
    db.commit()
    n = input("Do you want to continue?(y/n):")
    if n == 'y':
        insertfn()
    elif n == 'n':
        print("Exit")
        exit()
db=pymysql.connect(host='localhost', user='root',password='',db='vishnu')
a=db.cursor()
n=input("Do you want to Insert?(y/n):")
if n=='y':
    insertfn()
elif n=='n':
    b = input("Do you want to Delete (y/n)?:")
    if b == "y":
        q = "delete from student where mark<=50"
        a.execute(q)
        db.commit()
    elif b == "n":
        b = input("Do you want to Update (y/n)?:")
        if b == "y":
            ID = int(input("Enter rollno:"))
            name1 = input("Enter the new Address:")
            q = "update student set address='%s' where rollno=%d" % (name1, ID)
            a.execute(q)
            db.commit()
        elif b == 'n':
            print("Exit")
            quit()