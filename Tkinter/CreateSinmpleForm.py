from tkinter import *
from random import *

i=0
root=Tk()
root.geometry("300x300")

root.config(bg="BLUE")

def changetext():
    global i
    if i==0 :
        root.config(bg="RED")
        i=1
    elif i==1:
        root.config(bg="YEllow")
        i=2
    elif i==2:
         root.config(bg="BLACK")
         i=3
    elif i==3:
        root.config(bg="CYAN")
        i=4
    elif i==4:
        root.config(bg="GREEN")
        i=5
    elif i==5:
        root.config(bg="PURPLE")
        i=6
    elif i==6:
        root.config(bg="AQUA")
        i=0
        changetext()



#Insert The Lable Into The Form
lable=Label(root,text="This My First Tkinter Program",fg='red')
lable.pack()

def leftclick(event):
    lable.config(text="You Click Mouse Left Button")

def rightclick(event):
    lable.config(text="You Click Mouse Right But")
def motion(event):
    lable.config(text="You In The Button")
def dubbleone():
    lable.config(text="You Click Mouse Left Button Two Time")


#Insert The Button In The Form
btnchange=Button(root,text="Change Color",command=changetext)
btnchange.bind('<Button-1>',leftclick)
btnchange.bind('<Button-3>',rightclick)
btnchange.bind('<Motion>',motion)
btnchange.bind('<Double-1',dubbleone)
btnchange.place(x=100,y=150)


root.mainloop()
