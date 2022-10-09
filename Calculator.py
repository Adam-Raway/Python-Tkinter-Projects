from tkinter import *
from tkinter.tix import ButtonBox

# Root Window
root = Tk()
root.title("Calculator")

entryBox = Entry(root, width=40, borderwidth=5)
entryBox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Functions


def buttonAdd():
    return


# Define Buttons
button_0 = Button(root, text="0", padx=40, pady=20, command=buttonAdd)
button_1 = Button(root, text="1", padx=40, pady=20, command=buttonAdd)
button_2 = Button(root, text="2", padx=40, pady=20, command=buttonAdd)
button_3 = Button(root, text="3", padx=40, pady=20, command=buttonAdd)
button_4 = Button(root, text="4", padx=40, pady=20, command=buttonAdd)
button_5 = Button(root, text="5", padx=40, pady=20, command=buttonAdd)
button_6 = Button(root, text="6", padx=40, pady=20, command=buttonAdd)
button_7 = Button(root, text="7", padx=40, pady=20, command=buttonAdd)
button_8 = Button(root, text="8", padx=40, pady=20, command=buttonAdd)
button_9 = Button(root, text="9", padx=40, pady=20, command=buttonAdd)

button_clear = Button(root, text="Clear", padx=29, pady=20, command=buttonAdd)
button_equals = Button(root, text="=", padx=39, pady=20, command=buttonAdd)
button_add = Button(root, text="+", padx=40, pady=20, command=buttonAdd)

# Add buttons to root window
button_0.grid(row=4, column=0)
button_equals.grid(row=4, column=1)
button_clear.grid(row=4, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

# Main Loop
root.mainloop()
