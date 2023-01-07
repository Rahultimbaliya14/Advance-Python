from tkinter import *
root=Tk()

def printdata():
    top=Toplevel()
    top.geometry("500x350")
    
    mr1=int(m1.get())
    mr2=int(m2.get())
    mr3=int(m3.get())

    total=mr1+mr2+mr3
    pr=total/3
    grade=StringVar()

    if pr<35:
        grade="You Are Failed"
    elif pr>35 and pr<45:
        grade="You Got D Grade "
    elif pr>45 and pr<65:
        grade="You Got C Grade"
    elif pr>65 and pr<75:
        grade="You Got B Grade"
    elif pr>75 and pr<90:
        grade="You Got A Grade"
    elif pr>90 and pr<100:
        grade="You Got B Grade"
    else:
        grade="Enter Right Mark Pllzz"
    
    lablemr1=Label(top,text="Subject First Mark: "+str(mr1),anchor=CENTER)
    lablemr2=Label(top,text="Subject Second Mark: "+str(mr2),anchor=CENTER)
    lablemr3=Label(top,text="Subject Third Mark: "+str(mr3)     ,anchor=CENTER)
    labletotal=Label(top,text="Total :"+str(total),anchor=CENTER)
    lablepr=Label(top,text="Persentage :"+str(int(pr))   ,anchor=CENTER)
    lablegrade=Label(top,text="Grade :"+grade,anchor=CENTER)
    button=Button(top,text="Close",command=top.quit)

    lablemr1.grid(row=1,pady=10,padx=40)
    lablemr2.grid(row=2,pady=10,padx=40)
    lablemr3.grid(row=3,pady=10,padx=40)
    labletotal.grid(row=4,pady=10,padx=40)
    lablepr.grid(row=5,pady=10,padx=40)
    lablegrade.grid(row=6,pady=10,padx=40)
    button.grid(row=7,pady=20,padx=40)
    
    top.mainloop()

root.geometry("500x350")
lablem1=Label(root,text="Enter Frist Subject Mark :")
lablem2=Label(root,text="Enter Second Subject Mark :")
lablem3=Label(root,text="Enter Third Subject Mark :")
m1=StringVar()
m2=StringVar()
m3=StringVar()
entrym1=Entry(root,textvariable=m1)
entrym2=Entry(root,textvariable=m2)
entrym3=Entry(root,textvariable=m3)
Button=pButton(root,text="Submit",command=printdata)
lablem1.grid(row=1,column=1,pady=20,padx=20)
entrym1.grid(row=1,column=2,pady=20,padx=20)
lablem2.grid(row=2,column=1,pady=20,padx=20)
entrym2.grid(row=2,column=2,pady=20,padx=20)
lablem3.grid(row=3,column=1,pady=20,padx=20)
entrym3.grid(row=3,column=2,pady=20,padx=20)
Button.grid(row=4,column=2,pady=20,padx=20)
mainloop()