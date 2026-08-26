from tkinter import *
from datetime import date

root = Tk()
root.title("Welcome App")
root.geometry("500x400")

lbl = Label( text="Hey There!", fg="white", bg="blue", height=2, width=30)

name_lbl = Label( text="Enter your full name:")
name_entry = Entry()

def display():
    name = name_entry.get()
    global Message
    message = "Welcome to my Application! \nToday's date is-"
    greet = "Hello"+name+"\n"
    text_box(END, greet)
    text_box(END, message)
    text_box(END,date.today)
text_box = Text(height=3)

btn = Button(text="Begin", command=display, height=1, bg="#1299A0")

lbl.pack()
name_lbl.pack()
btn.pack()
text_box.pack()

root.mainloop()