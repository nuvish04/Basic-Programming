import tkinter
from tkinter import *
a=tkinter.Tk()
def start():
    #hello username
    l = tkinter.Label(a, text="Hello "+c.get(), font="Helvetica 13 bold", pady=15, bg="pink")
    l.grid(row=6,column=2)
a.title("Register")
a.config(bg="pink")
a.minsize(550,550)
#username and pass
b=tkinter.Label(a,text="REGISTRATION FORM", font="Helvetica 17 bold",pady=15,bg="pink")
b.grid(row=0,column=2)
b=tkinter.Label(a,text="User Name", font="Helvetica 13 bold",pady=10,bg="pink")
b.grid(row=1,column=1)
c=tkinter.Entry(a,bg="lightblue")
c.grid(row=1,column=2)
b=tkinter.Label(a,text="Password", font="Helvetica 13 bold",pady=10,bg="pink")
b.grid(row=2,column=1)
d=tkinter.Entry(a,bg="lightblue")
d.grid(row=2,column=2)
#language
var1=IntVar()
var2=IntVar()
var3=IntVar()
b=tkinter.Label(a,text="Select Your Language", font="Helvetica 13 bold",bg="pink" ,pady=10)
b.grid(row=3,column=1)
f=tkinter.Checkbutton(a,text="English", font="Helvetica 13 bold",bg="pink",pady=10,variable=var1)
f.grid(row=3,column=2)
f=tkinter.Checkbutton(a,text="Malayalam", font="Helvetica 13 bold",bg="pink",pady=10,variable=var2)
f.grid(row=3,column=3)
f=tkinter.Checkbutton(a,text="Hindi", font="Helvetica 13 bold",bg="pink",pady=10,variable=var3)
f.grid(row=3,column=4)
#Gender
b=tkinter.Label(a,text="Gender", font="Helvetica 13 bold",bg="pink" ,pady=10)
b.grid(row=4,column=1)
var=IntVar()
g=tkinter.Radiobutton(a,text="Male", font="Helvetica 13 bold",bg="pink",pady=10,variable=var,value=1)
g.grid(row=4,column=2)
g=tkinter.Radiobutton(a,text="Female", font="Helvetica 13 bold",bg="pink",pady=10,variable=var,value=2)
g.grid(row=4,column=3)
g=tkinter.Radiobutton(a,text="Others", font="Helvetica 13 bold",bg="pink",pady=10,variable=var,value=3)
g.grid(row=4,column=4)
#login
e=tkinter.Button(a,text="Login",activebackground="green",activeforeground="yellow",bg="black",fg="pink",pady=10,command=start)
e.grid(row=5,column=2)
a.mainloop()