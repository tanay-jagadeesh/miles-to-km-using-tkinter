from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

window.minsize(height = 100, width = 300)

# Making the labels

equal_label = Label(text = "is equal to", font = ("Arial", 24, "bold"))
equal_label.grid(column = 0, row = 1)

miles_label = Label(text = "Miles", font = ("Arial", 24, "bold"))
miles_label.grid(column = 2, row = 0)

km_label = Label(text = "Km", font = ("Arial", 24, "bold"))
km_label.grid(column = 2, row = 1)


          