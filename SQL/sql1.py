import pymysql
db=pymysql.connect(host='localhost', user='root',password='',db='vishnu')
a=db.cursor()
q="insert into students(name,class,address,course,mark)values('Das','11','Kannur')"
q1="select from databook where Id=5"
a.execute(q)
db.commit()