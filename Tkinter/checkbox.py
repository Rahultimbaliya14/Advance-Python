from tkinter import *
root=Tk()
root.geometry("400x400")
def ok():
    if i.get()=="ok" and b.get()=="no" and u.get()=="no":
       lable.configure(font=('arial 10 italic'))
    if i.get()=="ok" and b.get()=="ok" and u.get()=="no":
       lable.configure(font=('arial 10 bold italic'))
    if i.get()=="ok" and b.get()=="ok" and u.get()=="ok":
       lable.configure(font=('arial 10 bold italic underline'))
    if i.get()=="no" and b.get()=="no" and u.get()=="ok":
       lable.configure(font=('arial 10 underline'))
    if i.get()=="no" and b.get()=="ok" and u.get()=="no":
       lable.configure(font=('arial 10 bold'))
    if i.get()=="no" and b.get()=="ok" and u.get()=="ok":
       lable.configure(font=('arial 10 bold underline'))
    if i.get()=="no" and b.get()=="no" and u.get()=="no":
       lable.configure(font=('arial 10 '))
    if i.get()=="ok" and b.get()=="no" and u.get()=="ok":
       lable.configure(font=('arial 10 italic underline'))
   
    
b=StringVar()
i=StringVar()
u=StringVar()
lable=Label(root,text="This is the text")
lable.place(x=20,y=50)

bold=Checkbutton(root,text="bold",variable=b,onvalue="ok",offvalue="no",command=ok)
italic=Checkbutton(root,text="ITALIC",onvalue="ok",offvalue="no",variable=i,command=ok)
underline=Checkbutton(root,text="UNDERLINE",variable=u,onvalue="ok",offvalue="no",command=ok)
bold.pack(pady=20,padx=40)
italic.pack(pady=20,padx=40)
underline.pack(pady=20,padx=40)

root.mainloop()