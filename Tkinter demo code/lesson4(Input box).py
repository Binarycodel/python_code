from tkinter import *


root = Tk()

def clickMe():
    lb = Label(root , text=entry.get())
    lb.pack()

entry = Entry(root , width=50 , fg="red" , borderwidth=6)
entry.pack()
entry.insert(0 , "Please Enter Name")


button = Button(root, text="Click Me!" , command=clickMe)
button.pack()


root.mainloop()
