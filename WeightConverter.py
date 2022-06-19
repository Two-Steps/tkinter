from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry('550x200')

def clear_data():
    gram_value.delete(1.0, END)
    pounds_value.delete(1.0, END)
    ounce_value.delete(1.0, END)
def convert_data():
    if input_text.get() != '':
        kg = float(input_text.get())
        clear_data()
        g = str(kg * 1000)
        p = str(kg * 2.20462)
        o = str(kg * 35.274)
        gram_value.insert(END,g)
        pounds_value.insert(END,p)
        ounce_value.insert(END,o)
        a.set('test')
    

Label(master=app, text='Enter the weight in Kg',font='arial 12').grid(row=0, column=0, pady=10)
input_text = Entry(master=app, font='arial 12',width=20)
input_text.grid(row=0, column=1, padx=10, pady=10)
Button(master=app, text='Convert', font='arial 12', command=convert_data).grid(row=0, column=2, pady=10)

Label(master=app, text='Gram', font='arial 12').grid(row=1, column=0)
Label(master=app, text='Pounds', font='arial 12').grid(row=1, column=1)
Label(master=app, text='Ounce', font='arial 12').grid(row=1, column=2)

gram_value = Text(master=app, font='arial 12', width=15, height=3)
gram_value.grid(row=2, column=0)
pounds_value = Text(master=app, font='arial 12', width=15, height=3)
pounds_value.grid(row=2, column=1)
ounce_value = Text(master=app, font='arial 12', width=15, height=3)
ounce_value.grid(row=2, column=2)

app.mainloop()