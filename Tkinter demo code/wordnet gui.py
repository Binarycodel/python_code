import tkinter as tk

root = tk.Tk()
root.title("WordNet")
sv = tk.StringVar()

frame1 = tk.LabelFrame(root , text="" , padx=5 ,pady=2)
##frame1.grid(row=0, column=0)

frame2 = tk.LabelFrame(root , text="" , padx=0 ,pady=0)
##frame2.grid(row=1, column=0)


def show(event=None):
    print(f"hello {user_entry.get()}")
   

## the first frame data...... 
user_entry = tk.Entry(frame1, width=50 , borderwidth=4)
user_entry.bind('<Return>' , show )
search_button = tk.Button(frame1 , text="Search" , padx=10, pady=5 , command=show)
label = tk.Label(frame1 , text ="Search Word : ")
display = tk.Text(frame2)


label.grid(row=0 , column=0)
user_entry.grid(row=0 , column=1, columnspan=3 , pady=10 , padx=10)
search_button.grid(row=0, column=4)


# createing scrollbar
scroll = tk.Scrollbar(root)
scroll.pack(side=tk.RIGHT , fill = tk.Y)
##scroll.grid(row=0 , column=1 , rowspan=5)
scroll.config(command=display.yview)


# the second frame data.....
display.insert(tk.END , "hellow word........")
display.config(yscrollcommand=scroll.set)
display.pack()
##display.grid( row=0 , column=0 , columnspan=4)


frame1.pack()
frame2.pack()


root.mainloop()
