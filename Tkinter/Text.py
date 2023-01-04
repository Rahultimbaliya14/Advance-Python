from tkinter import *
root=Tk()
root.geometry("500x350")

txt = Text( root, fg = 'orange' ,bd=10,bg="black" ,relief=RAISED )
txt.insert(INSERT,"This Is The First Line \n")
txt.insert(INSERT,"This Is The Second Line \n")
txt.insert(INSERT,"This Is The Third Line")
txt.pack()
mainloop()