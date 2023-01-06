from tkinter import *

def _from_rgb(rgb):
         return "#%02x%02x%02x" % rgb

def change(event):
    r=int(red.get())
    y=int(green.get())
    b=int(blue.get())
    lable.config(text="RGB Value :("+str(r)+","+str(y)+","+str(b)+")")
    root.configure(bg=_from_rgb((r,y,b)))
    
root=Tk()
root.geometry("500x350")

red=StringVar()
green=StringVar()
blue=StringVar()

lablered=Label(root,text="Red",fg="Red",font=('arial 12 bold'))
lableGreen=Label(root,text="Green",fg="Green",font=('arial 12 bold'))
lableblue=Label(root,text="Blue",fg="Blue",font=('arial 12 bold'))

scalered=Scale(root,orient=HORIZONTAL,to=225,length=225,command=change,variable=red)
scalegreen=Scale(root,orient=HORIZONTAL,to=225,length=225,command=change,variable=green)
scaleblue=Scale(root,orient=HORIZONTAL,to=225,length=225,command=change,variable=blue)

lable=Label(root,text="",font=('arial 12 bold'))

lablered.pack()
scalered.pack()

lableGreen.pack(pady=10)
scalegreen.pack()

lableblue.pack(pady=10)
scaleblue.pack()

lable.pack(pady=40)
mainloop()