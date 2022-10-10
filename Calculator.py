from tkinter import *

# Root Window
root = Tk()
root.title("Calculator")

entryBox = Entry(root, width=60, borderwidth=5)
entryBox.grid(row=0, column=0, columnspan=4, padx=0, pady=10)

# Functions


def buttonClick(number):
    current = entryBox.get()
    entryBox.delete(0, END)
    entryBox.insert(0, current + str(number))


def buttonClear():
    entryBox.delete(0, END)


def buttonOperation(operation):
    current = entryBox.get()
    if current[-1].isnumeric():
        entryBox.delete(0, END)
        entryBox.insert(0, f"{current} {operation} ")


def buttonEquals():
    equation = entryBox.get()
    if equation[-2] not in "+-x/":
        equation = equation.replace(" ", "")
        equation = equation.replace("x", "*")
        entryBox.delete(0, END)
        entryBox.insert(0, eval(equation))


# Define Buttons
button_0 = Button(root, text="0", padx=40, pady=20,
                  command=lambda: buttonClick(0))
button_1 = Button(root, text="1", padx=40, pady=20,
                  command=lambda: buttonClick(1))
button_2 = Button(root, text="2", padx=40, pady=20,
                  command=lambda: buttonClick(2))
button_3 = Button(root, text="3", padx=40, pady=20,
                  command=lambda: buttonClick(3))
button_4 = Button(root, text="4", padx=40, pady=20,
                  command=lambda: buttonClick(4))
button_5 = Button(root, text="5", padx=40, pady=20,
                  command=lambda: buttonClick(5))
button_6 = Button(root, text="6", padx=40, pady=20,
                  command=lambda: buttonClick(6))
button_7 = Button(root, text="7", padx=40, pady=20,
                  command=lambda: buttonClick(7))
button_8 = Button(root, text="8", padx=40, pady=20,
                  command=lambda: buttonClick(8))
button_9 = Button(root, text="9", padx=40, pady=20,
                  command=lambda: buttonClick(9))

button_clear = Button(root, text="Clear", padx=29,
                      pady=20, command=buttonClear)
button_equals = Button(root, text="=", padx=39, pady=20, command=buttonEquals)

button_add = Button(root, text="+", padx=39, pady=20,
                    command=lambda: buttonOperation("+"))
button_subtract = Button(root, text="-", padx=40,
                         pady=20, command=lambda: buttonOperation("-"))
button_multiply = Button(root, text="x", padx=40,
                         pady=20, command=lambda: buttonOperation("x"))
button_divide = Button(root, text="/", padx=40, pady=20,
                       command=lambda: buttonOperation("/"))

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

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

# Main Loop
root.mainloop()
