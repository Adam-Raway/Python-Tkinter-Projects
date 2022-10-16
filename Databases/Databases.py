from logging import root
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Learning to use sqlite')
root.geometry("500x500")

# Create a database or connect to one
conn = sqlite3.connect('Databases/address_book.db')

# Creating a cursor instance
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)""")

# Commiting changes to a database
conn.commit()

# Close a connection
conn.close()

root.mainloop()
