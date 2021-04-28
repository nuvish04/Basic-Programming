import tkinter
from tkinter import *
from tkinter import messagebox
def msg():
    messagebox.askyesnocancel("Hello","Vishnu")

def ms():
        messagebox.showinfo("Info","Info Display")
def m():
    messagebox.showerror("Error","Error404")
a=tkinter.Tk()
a.title("MessageBox")
a.minsize(400,400)
b=tkinter.Button(a,text="Click",activebackground="green",activeforeground="yellow",bg="black",fg="pink",pady=10,command=msg)
b.pack()
c=tkinter.Button(a,text="Click",activebackground="green",activeforeground="yellow",bg="black",fg="pink",pady=10,command=ms)
c.pack()
d=tkinter.Button(a,text="Click",activebackground="green",activeforeground="yellow",bg="black",fg="pink",pady=10,command=m)
d.pack()
a.mainloop()