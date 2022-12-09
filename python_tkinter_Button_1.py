from tkinter import*
from tkinter import messagebox
#creating the application main window
top = Tk()

top.title("Button Info")

def fun():
    #print("Welcome To Tkinter.")
    messagebox.showinfo("Hello","Welcome To Python.")
    
def fun2():
    messagebox.showwarning("Warning","Big Trouble.")

def fun3():
    messagebox.showerror("Error","Danger! Quick To Recover Required.")

def fun4():
    messagebox.askquestion("Confirm","Are U Sure!")
    #messagebox.askyesno("Confirm","Are U Sure!")


top.geometry("400x200")

b = Button(top,text="Show Info", command=fun)
b2 = Button(top,text="Show Warning", command=fun2)
b3 = Button(top,text="Show Error", command=fun3)
b4 = Button(top,text="Ask Question", command=fun4)

b.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)

#enter the event mainloop
top.mainloop()

