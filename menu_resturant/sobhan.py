import tkinter as tk
from  tkinter import *
root=tk.Tk()
root.geometry("300x220")
root.resizable(False,False)
def clicked():
    lblWelcome.configure(text="Hello " + strName.get())
lblName=Label(root, text="What is your name?")
lblName.place(height=20,width=150,x=0,y=40)
lblWelcome=Label(root, text="Hello World")
lblWelcome.place(height=50,width=100,x=100,y=140)
btn=Button(root, text="Click Me!", command=clicked)
btn.place(height=40,width=100,x=100,y=100)
strName=tk.StringVar()
txtName=tk.Entry(root,textvariable=strName)
txtName.place(height=20,width=80,x=150,y=40)
root.mainloop()