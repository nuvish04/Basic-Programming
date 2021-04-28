import tkinter
from tkinter import *
def abc():
    sel="value ="+str(b.get())
    l.config(text=sel)
a=tkinter.Tk()
a.title("Scale")
a.minsize(400,600)
b=DoubleVar()
c=Scale(a,variable=b,orient=HORIZONTAL,bg="yellow")
c.pack()
d=tkinter.Button(a,text="Click",fg="white",bg="Black",activebackground="red",activeforeground="yellow",padx=10,pady=10,command=abc)
d.pack(anchor=CENTER)
l=tkinter.Label(a,bg="pink",font="Helvetica 13 bold")
a.config(bg="pink")
l.pack()
a.mainloop()