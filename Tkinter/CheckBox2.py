from tkinter import *

def sel():
    text=""
    if s.get()=="ok":
        text=text+" Singing"
    if d.get()=="ok":
        text=text+" Dancing"
    if c.get()=="ok":
        text=text+" Codding"
    if r.get()=="ok":
        text=text+" Running"
    lable.config(text="You Are Hobies Are:"+text)

root=Tk()
root.geometry("500x350")
lable=Label(root,text="You Are Hobies Are: ",fg="orange")
lable.configure(font=("arial",12))
s=StringVar()
d=StringVar()
c=StringVar()
r=StringVar()

singing=Checkbutton(root,text="Singing",variable=s,offvalue="no",onvalue="ok",command=sel)
Codding=Checkbutton(root, text="Codding",variable=c,offvalue="no",onvalue="ok",command=sel)
Dancing=Checkbutton(root,text="Dancing",variable=d,offvalue="no",onvalue='ok',command=sel)
Running=Checkbutton(root,text="Running",variable=r,offvalue="no",onvalue="ok",command=sel)
lable.pack()
singing.pack(pady=10)
Codding.pack(pady=10)
Dancing.pack(pady=10)
Running.pack(pady=10)
mainloop()
