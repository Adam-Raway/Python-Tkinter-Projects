from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Radio Buttons Practice")

r = IntVar()
r.set("2")


def clicked(value):
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    respone = messagebox.askokcancel("This is not my popup!", value)
    print(respone)


Radiobutton(root, text="Option 1", variable=r, value=1,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 3", variable=r, value=3,
            command=lambda: clicked(r.get())).pack()

root.mainloop()
