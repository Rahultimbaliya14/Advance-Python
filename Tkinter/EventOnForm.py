from tkinter import *

def singleleft(event):
    lable.config(text="You Click Single Time")
def rightclick(event):
    lable.config(text="You Right Click Single  Time")
def middleclick(event):
    lable.config(text="You Middle Click Single  Time")
def motionleft(event):
    lable.config(text="Motion Of The LEft")
def motionright(event):
    lable.config(text="Motion Of The Right")
def mousewheel(event):
    lable.config(text="Click The ScrollWheel")
def aclick(event):
    lable.config(text="You Click a Key")
def doubleclickleft(event):
    lable.config(text="Double Click Left Button")
def doubleclickright(event):
    lable.config(text="Double Click Right Button")
def enter(event):
    lable.config(text="Mouse On The Window")
def leave(event):
    lable.config(text="Mouse Is Not On The Window")
def motion(event):
    lable.config(text="You Move The Cursor On The Windows")
def Keypress(event):
    lable.config(text="Press Key")
def Keyrelease(event):
    lable.config(text="Release Key")
def right(event):
    lable.config(text="Press Right Arrow Key")
def left(event):
    lable.config(text="Press Left Arrow Key")
def up(event):
    lable.config(text="Press Up Arrow Key")
def down(event):
    lable.config(text="Press Down Arrow Key")





root=Tk()
root.geometry("500x350")
lable=Label(root,text="Try All The Click On The This Button",fg="Orange")
lable.configure(font=('arial 15 bold'))

lable.pack()

root.bind('<Button-1>',singleleft)
root.bind('<Button-3>',rightclick)
root.bind('<Button-2>',middleclick)
root.bind('<B1-Motion>',motionleft)
root.bind('<B3-Motion>',motionright)
root.bind('<MouseWheel>',mousewheel)
root.bind('<Double-Button-1>',doubleclickleft)
root.bind('<Double-Button-3>',doubleclickright)
root.bind('<Enter>',enter)
root.bind('<Leave>',leave)
root.bind('<Motion>',motion)
root.bind('<a>',aclick) 
root.bind("<KeyPress>",Keypress)
root.bind("<KeyRelease>",Keyrelease)
root.bind('<Right>',right)
root.bind('<Left>',left)
root.bind('<Up>',up)
root.bind('<Down>',down)

mainloop()