""" Programmer: Walter Reeves """
from tkinter import *
from tkinter import ttk


def get_entry():
    """ Gets the entry from the entry box. """

    miles = float(entry.get())
    kilometers = miles * 1.60934
    ttk.Label(frame, text=kilometers).grid(column=2, row=2)


window = Tk()
window.title("Miles to Kilometers Converter")

frame = ttk.Frame(window, padding=10)
frame.grid()

to_convert = StringVar()
entry = ttk.Entry(frame, textvariable=to_convert, width=10, justify="right")
entry.grid(column=2, row=1)

ttk.Label(frame, text="miles").grid(column=3, row=1)
ttk.Label(frame, text="is").grid(column=1, row=2)
ttk.Label(frame, text="kilometers").grid(column=3, row=2)
ttk.Button(frame, text="Calculate", command=get_entry).grid(column=4, row=2)

window.mainloop()
