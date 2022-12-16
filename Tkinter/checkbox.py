from tkinter import *
root=Tk()
root.geometry("400x400")
def janki():
    if i.get()=="janki" and b.get()=="aman" and u.get()=="aman":
       lable.configure(font=('arial 10 italic'))
    if i.get()=="janki" and b.get()=="janki" and u.get()=="aman":
       lable.configure(font=('arial 10 bold italic'))
    if i.get()=="janki" and b.get()=="janki" and u.get()=="janki":
       lable.configure(font=('arial 10 bold italic underline'))
    if i.get()=="aman" and b.get()=="aman" and u.get()=="janki":
       lable.configure(font=('arial 10 underline'))
    if i.get()=="aman" and b.get()=="janki" and u.get()=="aman":
       lable.configure(font=('arial 10 bold'))
    if i.get()=="aman" and b.get()=="janki" and u.get()=="janki":
       lable.configure(font=('arial 10 bold underline'))
    if i.get()=="aman" and b.get()=="aman" and u.get()=="aman":
       lable.configure(font=('arial 10 '))
    if i.get()=="janki" and b.get()=="aman" and u.get()=="janki":
       lable.configure(font=('arial 10 italic underline'))
   
    
b=StringVar()
i=StringVar()
u=StringVar()
lable=Label(root,text="This is the text")
lable.place(x=20,y=50)

bold=Checkbutton(root,text="bold",variable=b,onvalue="janki",offvalue="aman",command=janki)
italic=Checkbutton(root,text="ITALIC",onvalue="janki",offvalue="aman",variable=i,command=janki)
underline=Checkbutton(root,text="UNDERLINE",variable=u,onvalue="janki",offvalue="aman",command=janki)
bold.pack(pady=20,padx=40)
italic.pack(pady=20,padx=40)
underline.pack(pady=20,padx=40)

root.mainloop()