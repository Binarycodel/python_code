from tkinter import *

root = Tk();


def myClick():
    label = Label(root , text="look! i clicked a button")
    label.pack()



##button = Button(root , text="Click me!" , state=DISABLED)
button = Button(root , text="Click me!" , padx=50 , pady=30 ,command=myClick , fg="blue")
button.pack()

root.mainloop()
