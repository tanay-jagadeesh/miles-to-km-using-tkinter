from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

window.minsize(height = 100, width = 300)

# Making the labels

equal_label = Label("is equal to", font = ("Arial", 24, "bold"))
equal_label.grid(column = 1, row = 2)

miles_label = Label("Miles", font = ("Arial", 24, "bold"))
miles_label.grid(column = 3, row = 1)

km_label = Label("Km", font = ("Arial", 24, "bold"))
km_label.grid(column = 3, row = 2)


