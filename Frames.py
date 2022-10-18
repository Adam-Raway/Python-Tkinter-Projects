import imp
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.dates import FR
from pyparsing import col

root = Tk()
root.title("Frames Lesson")

frame = LabelFrame(root, text="This is my frame... ",
                   padx=50, pady=50, fg="#aaaaaa", bg="#111111")
frame.pack(padx=10, pady=10)

button1 = Button(frame, text="Click here!")
button2 = Button(frame, text="or here!")
button1.grid(row=0, column=0)
button2.grid(row=1, column=1)

root.mainloop()
