from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Canvas Example")
root.geometry("500x350")

can=Canvas(root,width=400,height=300)

can.create_arc(180, 150, 80,210, start=0,extent=220,fill="red")
can.create_oval(80, 30, 140,150,fill="blue")
can.create_line(108, 120,320, 40,fill="green")
can.create_polygon(50,50, 100, 80, 120, 120, 100, 190,fill="aqua")
# can.create_rectangle(50, 110,300,280, fill= "blue")
# img=ImageTk.PhotoImage(Image.open("canvas.jpg"))
# can.create_image(10,10,anchor=NW,image=img)


can.pack()
mainloop()
