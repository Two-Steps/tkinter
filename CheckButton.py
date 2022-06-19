from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry('200x300')

def button_apple():
    print('This is an apple')

def button_orange():
    print('This is an orange')

Button(master=app, text='Apple', command=button_apple).grid(padx=10, pady=10)
Button(master=app, text='Orange', command=button_orange).grid(padx=10, pady=10)

app.mainloop()