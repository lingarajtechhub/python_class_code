from tkinter import*

top = Tk()

def login_fun():
    top.destroy()
    top2 = Tk()

    top2.title("Database Window")

    top2.mainloop()




top.title("Login Window")

#top.geometry("400x200")

screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

b = Button(top, text="Login", command=login_fun)

#e = Entry(top, Text="")

b.pack()

top.mainloop()

