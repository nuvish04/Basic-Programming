import tkinter
from tkinter import *
a=tkinter.Tk()
a.title("Menu")
a.minsize(550,550)
men=Menu()
men.add_command(label="File",font="Helvetica 13 bold")
men.add_command(label="Edit",font="Helvetica 13 bold")
men.add_command(label="Quit",font="Helvetica 13 bold")
var=Listbox(a,bg="lightpink",font="Helvetica 13 bold")
var.insert(1,"Sl.No")
var.insert(2,"Name")
var.insert(3,"Age")
var.pack()
d=tkinter.Button(a,text="Click",fg="white",bg="Black",activebackground="red",activeforeground="yellow",padx=10,pady=10,command=lambda var=var:var.delete(ANCHOR))
d.pack()
a.config(bg="pink",menu=men)
a.mainloop()