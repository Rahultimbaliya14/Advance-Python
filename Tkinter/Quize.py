from tkinter import *
root=Tk()
root.geometry('600x600')

lable1=Label(root,text="")
i=0
def draw():
    if i==0:
        lable1=Label(root,text="Who Is Funder Of The C++ Language",fg='RED')
        lable1.place(x=20,y=100)
        radion1=Radiobutton(root,text="Lusmus Loadorf",value=1)
        radion1.place(x=20,y=150)
        radion2=Radiobutton(root,text="Dinial Ritchi",value="right")
        radion2.place(x=20,y=200)
        radion3=Radiobutton(root,text="jeff Bejoj",value=2)
        radion3.place(x=20,y=250)
        radion3=Radiobutton(root,text="mark Finland",value=3)
        radion3.place(x=20,y=300)
    
btn=Button(root,text="Start" ,command=draw)
btn.place(x=20,y=00)
root.mainloop()



