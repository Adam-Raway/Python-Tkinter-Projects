from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Learning how to use Matplotlib")
root.geometry('400x400')


def graph():
    housePrices = np.random.normal(200000, 25000, 5000)
    plt.hist(housePrices, 50)
    plt.show()


myButton = Button(root, text='Graph It!', command=graph)
myButton.pack()

root.mainloop()
