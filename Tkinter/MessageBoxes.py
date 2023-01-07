from tkinter import *
from tkinter import messagebox

root=Tk()
def info():
    messagebox.showinfo("This Is Information MassageBox","Information....")

def warning():
    messagebox.showwarning("This Is Warning MassageBox","Warning....")

def error():
    messagebox.showerror("This Is Error MassageBox","Error....")

def askquestion():
    messagebox.askquestion("This Is AskQuestion MassageBox","Question....")

def askokcancel():
    messagebox.askokcancel("This Is AskOkCancel MassageBox","Question....")

def askyesno():
    messagebox.askyesno("This Is AskYesNo MassageBox","Question....")

def askretrycancel():
    messagebox.askretrycancel("This Is AskRetryCancel MassageBox","Question....")


root.geometry("500x350")

label=Label(root,text="Massageboxes",fg="Orange",font=('arial',20))
Buttoninfo=Button(root,text="Info Box",command=info)
Buttonwarning=Button(root,text="Warning Box",command=warning)
Buttonerror=Button(root,text="Error Box",command=error)
ButtonAskQuestion=Button(root,text="Ask Question",command=askquestion)
ButtonAskOkCancel=Button(root,text="Ask OkCancel",command=askokcancel)
ButtonYesNO=Button(root,text="Ask YesNo",command=askyesno)
ButtonRetryCancel=Button(root,text="Ask RetryCancel",command=askretrycancel)

label.pack(pady=5)
Buttoninfo.pack(pady=5)
Buttonwarning.pack(pady=5)
Buttonerror.pack(pady=5)
ButtonAskQuestion.pack(pady=5)
ButtonAskOkCancel.pack(pady=5)
ButtonYesNO.pack(pady=5)
ButtonRetryCancel.pack(pady=5)

root.mainloop()