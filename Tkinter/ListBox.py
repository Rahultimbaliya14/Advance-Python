from tkinter import *
root=Tk()
root.geometry("500x400")
def onetotwosingle():
    item=listbox1.get(ANCHOR)
    listbox1.delete(ANCHOR)
    listbox2.insert(END,item)

def onetotwoall():
    listbox1.select_set(0,END)
    listbox1item=listbox1.get(0,END)
    for item in listbox1item:
        listbox2.insert(END,item)
        listbox1.delete(0,END)

def twotooneall():
    listbox2.select_set(0,END)
    listbox1item=listbox2.get(0,END)
    for item in listbox1item:
        listbox1.insert(END,item)
        listbox2.delete(0,END)

def twotoonesingle():
    item=listbox2.get(ANCHOR)
    listbox2.delete(ANCHOR)
    listbox1.insert(END,item)

listbox1=Listbox(root)
listbox2=Listbox(root)

my_list1=['C','C++','Java','Python']
for item in my_list1:
    listbox1.insert(END,item)


button1=Button(root,text=">>",command=onetotwoall)
button2=Button(root,text=">",command=onetotwosingle)   
button3=Button(root,text="<<",command=twotooneall)
button4=Button(root,text="<",command=twotoonesingle)

listbox1.place(x=20,y=20)
listbox2.place(x=200,y=20)

button1.place(x=150,y=20)
button2.place(x=150,y=60)
button3.place(x=150,y=100)
button4.place(x=150,y=140)

root.mainloop()