from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

window.minsize(height = 100, width = 300)

# Making the labels

equal_label = Label(text = "is equal to", font = ("Arial", 15))
equal_label.grid(column = 0, row = 1)

miles_label = Label(text = "Miles", font = ("Arial", 15))
miles_label.grid(column = 2, row = 0)

km_label = Label(text = "Km", font = ("Arial", 15))
km_label.grid(column = 2, row = 1)

miles_label = Label(text = "", font = ("Arial", 15))
miles_label.grid(column = 1, row = 1)

button = Button(text="Calculate", command= button_clicked)
button.grid(column =1, row = 2)

entry = Entry(width=30)
entry.grid(column = 1, row = 1)


def button_clicked():
    miles_calc = float(entry.get() * 1.609)
    result_label.config(text = miles_calc)

window.mainloop()
          