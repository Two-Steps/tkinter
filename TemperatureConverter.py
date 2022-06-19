from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Temperature Converter')
#window.resizable(width=False, height=False)
window.geometry('400x250')
# GUI C to F
frm_entry_celsius = Frame(master=window)
ent_temperature_celsius = Entry(master=frm_entry_celsius, width=10)
lbl_temp_celsius = Label(master=frm_entry_celsius, text='\N{DEGREE CELSIUS}')
lbl_result_fahrenheit = Label(master=window, text='\N{DEGREE FAHRENHEIT}')

ent_temperature_celsius.grid(row=0, column=0, sticky='e')
lbl_temp_celsius.grid(row=0, column=1, sticky='w')
lbl_result_fahrenheit.grid(row=0, column=2, sticky='w')

# funtion to convert C to F
def celsius_to_fahrenheit():
    celsius = ent_temperature_celsius.get()
    if celsius != '':
        fahrenheit = 9/5 * float(celsius) + 32
        lbl_result_fahrenheit['text'] = f'{round(fahrenheit,2)} \N{DEGREE FAHRENHEIT}'
# button
btn_convert_celsius = Button(
    master=window,
    text='\N{RIGHTWARDS BLACK ARROW}',
    command=celsius_to_fahrenheit
)
# order widget father
frm_entry_celsius.grid(row=1, column=0, padx=10, pady=10)
btn_convert_celsius.grid(row=1, column=1, padx=10, pady=10)
lbl_result_fahrenheit.grid(row=1, column=2, padx=10, pady= 10)
## try work for F to C
def fahrenheit_to_celsius():
    fahrenheit = ent_temperature_fahrenheit.get()
    if fahrenheit != '':
        celsius = 5/9 * (float(fahrenheit) - 32)
        lbl_result_celsius['text'] = f'{round(celsius,2)} \N{DEGREE CELSIUS}'
frm_entry_fahrenheit = Frame(master=window)
ent_temperature_fahrenheit = Entry(master=frm_entry_fahrenheit, width=10)
lbl_temp_fahrenheit = Label(master=frm_entry_fahrenheit, text='\N{DEGREE FAHRENHEIT}')
lbl_result_celsius = Label(master=window,text= '\N{DEGREE CELSIUS}')

btn_convert_fahrenheit = Button(
    master=window,
    text='\N{RIGHTWARDS BLACK ARROW}',
    command=fahrenheit_to_celsius
)

ent_temperature_fahrenheit.grid(row=0, column=0,sticky='e')
lbl_temp_fahrenheit.grid(row=0, column=1, sticky='w')

frm_entry_fahrenheit.grid(row=0, column=0, padx=10, pady=10)
btn_convert_fahrenheit.grid(row=0, column=1, padx= 10, pady=10)
lbl_result_celsius.grid(row=0, column=2, padx=10, pady=10)

window.mainloop()
