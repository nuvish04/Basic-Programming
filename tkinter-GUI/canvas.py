import tkinter
from tkinter import *
a=tkinter.Tk()
a.title("Canvas")
a.minsize(400,600)
b=tkinter.Canvas(a,bg="pink",height=300,width=300)
b.create_line(0,100,300,100,fill="green")
b.create_line(150,0,150,200,fill="red")
b.create_rectangle(50,150,250,0,fill="yellow")
b.create_oval(50,150,250,0,fill="red")
b.pack()
a.mainloop()