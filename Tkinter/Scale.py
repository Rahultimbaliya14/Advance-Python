from tkinter import *
def change(event):
    p=int(size.get())
    lable.config(font=('Helvetica bold',p))
root=Tk()
root.geometry("500x350")
size=DoubleVar()
scale=Scale(root,orient=HORIZONTAL,length=100,command=change,variable=size)
lable=Label(root,text="This IS The lable")
labl1=Label(root,text="Scroll The Scale")

lable.pack()
scale.pack(pady=50)
labl1.pack()
mainloop()