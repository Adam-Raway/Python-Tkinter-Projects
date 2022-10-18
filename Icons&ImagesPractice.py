from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Icons and Images Practice')
root.iconbitmap('Images/Python.ico')

buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

myImg = ImageTk.PhotoImage(Image.open('Images/Example Swan.jpg'))
myLabel = Label(image=myImg)
myLabel.pack()

root.mainloop()
