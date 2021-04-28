#!"C:\Users\php 3\AppData\Local\Programs\Python\Python37-32\python.exe"
import cgi,cgitb
form1=cgi.FieldStorage()
#name
name1=form1.getvalue("fname")
name2=form1.getvalue("lname")
#phone
ph=form1.getvalue("phone")
#email
email=form1.getvalue("em")
#pass
ps=form1.getvalue("pass")
#checkbox
if form1.getvalue("abc"):
    eng="ON"
else :
    eng="OFF"
if form1.getvalue("xyz"):
    mal="ON"
else:
    mal="OFF"
#radio
if form1.getvalue("gen"):
    gend=form1.getvalue("gen")
else:
    gend="NOT SET"
#textarea
if form1.getvalue("add"):
    ad=form1.getvalue("add")
else:
    ad="NOT SET"
#selectbox
if form1.getvalue("state"):
    st=form1.getvalue("state")
else:
    st="NOT SET"
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Registration CGI</title>')
print('</head>')
print('<body>')
print('<hr>')
print("First Name : %s" %(name1))
print('<br>')
print("Last Name : %s" %(name2))
print('<hr>')
print("Phone: %s " %(ph))
print('<hr>')
print("Email: %s" %(email))
print('<hr>')
print("English : %s" %(eng))
print('<br>')
print("Malayalam : %s" %(mal))
print('<hr>')
print("Gender : %s" %(gend))
print('<hr>')
print("Address : %s" %(ad))
print('<hr>')
print("State : %s" %(st))
print('<hr>')
print("Password: %s" %(ps))
print('<hr>')
print('</body>')
print('</html>')