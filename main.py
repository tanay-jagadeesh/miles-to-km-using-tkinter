from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

window.minsize(height = 100, width = 300)

# Making the labels

my_label = Label("is equal to", font = ("Arial", 24, "bold"))
my_label.grid(column = 1, row = 2)

my_label = Label("Miles", font = ("Arial", 24, "bold"))
my_label.grid(column = 3, row = 1)


