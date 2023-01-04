from tkinter import *

def sel():
    lable.config(text="Your Gender :"+var.get())

root=Tk()
root.geometry("500x350")
var=StringVar()
r1=Radiobutton(root,text="Male",variable=var,value="Male",command=sel)
r2=Radiobutton(root,text="Female",variable=var,value="Female",command=sel)
r3=Radiobutton(root,text="Other",variable=var,value="Other",command=sel)
lable=Label(root,text="")
r1.pack()
r2.pack()
r3.pack()
lable.pack(pady=40)

mainloop()