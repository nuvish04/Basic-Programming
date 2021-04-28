import time
import datetime
print("second :",time.time())
print("Local time :",time.localtime())
time.sleep(1)
print("Asctime :",time.asctime())
a=time.localtime()
print("Year:",a.tm_year)
print("Current Time :",datetime.datetime.now())
b=datetime.datetime.now()
print(b.year)
print(b.strftime('%H'))
print(b.strftime('%A'))
print(b.strftime('%B'))
