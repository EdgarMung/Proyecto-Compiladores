import tkinter as tk
from tkinter import *

def clearFrame():
    # destroy all widgets from frame
    for widget in frame.winfo_children():
       widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    frame.pack_forget()


root = tk.Tk()

frame = Frame(root)
frame.pack(side="top", expand=True, fill="both")

lab = Label(frame, text="hiiii")
lab.grid(row=0, column=0, padx=10, pady=5)

frame.but = Button(frame, text="clear frame", command=clearFrame)
frame.but.grid(row=0, column=1, padx=10, pady=5)


# then whenever you add data in frame then you can show that frame
lab2 = Label(frame, text="hiiii")
lab2.grid(row=1, column=0, padx=10, pady=5)
frame.pack()

root.mainloop()