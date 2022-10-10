from tkinter import *

root = Tk();

label1 = Label(root , text="this is coll")
label2 = Label(root , text="i am impressed")

label1.grid(row=0 , column=0)
label2.grid(row=1 , column=5)


root.mainloop()
