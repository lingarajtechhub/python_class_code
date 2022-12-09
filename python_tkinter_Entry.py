from tkinter import*
from tkinter import messagebox

top = Tk()

top.geometry("400x250") 

e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()

def submit():
    #messagebox.showinfo("Data","Show Info")
    top2 = Tk()
    top2.geometry("200x200")
    nm = str(e1).get()
    eml = e2.get()
    pwd = e3.get()
    ph = e4.get()
    info1 = Label(top2, text="Name= %s" % nm).place(x=30,y=50)
    info2 = Label(top2, text="email= %s" % eml).place(x=30,y=90)
    info3 = Label(top2, text="Password= %s" % pwd).place(x=30,y=130)
    info4 = Label(top2, text="= %s" % nm).place(x=30,y=170)
    
name = Label(top, text="Name").place(x=30,y=50)
email = Label(top, text="Email").place(x=30,y=90)
password = Label(top, text="Password").place(x=30,y=130)
phone = Label(top, text="PhoneNumber").place(x=30,y=170)
b = Button(top, command=submit, text="Submit", activebackground="pink", activeforeground="blue").place(x=120, y=210)

e1 = Entry(top).place(x=120, y=50)
e2 = Entry(top).place(x=120, y=90)
e3 = Entry(top).place(x=120, y=130)
e4 = Entry(top).place(x=120, y=170)

top.mainloop()