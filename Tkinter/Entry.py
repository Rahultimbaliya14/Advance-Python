from tkinter import *

def sel():
    lable.config(text=var.get())

root=Tk()
root.geometry("500x350")

var=StringVar()
entry=Entry(root,textvariable=var)
button=pButton(root,text="OK",command=sel)
lable=Label(root,text="")

entry.pack(pady=20)
button.pack()
lable.pack(pady=50)

mainloop()