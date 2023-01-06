from tkinter import *

def change():
    top=Toplevel()
    top.geometry("200x150")
    lable=Label(top,text="This Top Level Window")
    lable.pack()
root=Tk()
root.geometry("500x350")

button=Button(root,text="Click Me",command=change)
button.pack()
mainloop()