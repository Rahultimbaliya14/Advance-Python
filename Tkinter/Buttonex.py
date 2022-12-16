from tkinter import *
root=Tk()
root.geometry("400x400")


def bold1():
    lable.configure(font=("arial 10 bold"))

def italic1():
    lable.configure(font=("arial 10 italic"))

def underline1():
    lable.configure(font=("arial 10 underline"))


bold=Button(root,text="Bold" ,command=bold1)
italic=Button(root,text="Italic",command=italic1 )
Underline=Button(root,text="Underline",command=underline1)
bold.pack(pady=20)
italic.pack(pady=20)
Underline.pack(pady=20 )
lable=Label(root,text="This Is Text")
lable.pack(pady=30)





root.mainloop()

