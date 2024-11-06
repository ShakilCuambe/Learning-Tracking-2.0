from tkinter import *

window = Tk()
window.title("Miles to kilometers convertor")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=8)
entry.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2
           )
equality = Label(text="is equal to")
equality.grid(row=1, column=0)


def convert():
    km_conversion.config(text=str(round(float(entry.get()) * 1.609)))

km_conversion = Label(text="0")
km_conversion.grid(row=1, column=1)

kilometers = Label(text="km")
kilometers.grid(row=1, column=2)

calculate = Button(text="Calculate", command=convert)
calculate.grid(row=2, column=1)

window.mainloop()
