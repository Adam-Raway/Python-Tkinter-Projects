from audioop import add
from logging import root
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

from pyparsing import col

root = Tk()
root.title('Learning to use sqlite')
root.geometry("361x400")


def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('Databases/address_book.db')
    # Creating a cursor instance
    c = conn.cursor()

    '''
    # Create table
    c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        province text,
        zipcode integer
    )""")
    '''

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :province, :zipcode)",
              {
                  "f_name": f_name.get(),
                  "l_name": l_name.get(),
                  "address": address.get(),
                  "city": city.get(),
                  "province": province.get(),
                  "zipcode": zipcode.get()
              })

    # Commiting changes to a database
    conn.commit()
    # Close a connection
    conn.close()

    # Clear textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    province.delete(0, END)
    zipcode.delete(0, END)


def query():
    # Create a database or connect to one
    conn = sqlite3.connect('Databases/address_book.db')
    # Creating a cursor instance
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    print_records = ""
    for record in records:
        print_records += f"{record[0]} {record[1]}: {record[2]} \t {record[6]}\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)

    # Commiting changes to a database
    conn.commit()
    # Close a connection
    conn.close()


def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('Databases/address_book.db')
    # Creating a cursor instance
    c = conn.cursor()

    c.execute(f"DELETE from addresses WHERE oid={select_oid.get()}")

    # Commiting changes to a database
    conn.commit()
    # Close a connection
    conn.close()


def save():
    # Create a database or connect to one
    conn = sqlite3.connect('Databases/address_book.db')
    # Creating a cursor instance
    c = conn.cursor()

    record_id = select_oid.get()
    c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    province = :province,
    zipcode = :zipcode

    WHERE oid = :oid""",
              {
                  "first": f_name_updateWindow.get(),
                  "last": l_name_updateWindow.get(),
                  "address": address_updateWindow.get(),
                  "city": city_updateWindow.get(),
                  "province": province_updateWindow.get(),
                  "zipcode": zipcode_updateWindow.get(),
                  "oid": record_id
              })

    # Commiting changes to a database
    conn.commit()
    # Close a connection
    conn.close()

    updateWindow.destroy()


def update():
    global updateWindow
    updateWindow = Tk()
    updateWindow.title('Update a Record')
    updateWindow.geometry("361x300")

    # Create a database or connect to one
    conn = sqlite3.connect('Databases/address_book.db')
    # Creating a cursor instance
    c = conn.cursor()

    record_id = select_oid.get()
    # Query the database
    c.execute(f"SELECT * from addresses WHERE oid={record_id}")
    records = c.fetchall()

    # Create global variables for text box names
    global f_name_updateWindow
    global l_name_updateWindow
    global address_updateWindow
    global city_updateWindow
    global province_updateWindow
    global zipcode_updateWindow

    # Create Text Boxes
    f_name_updateWindow = Entry(updateWindow, width=30)
    f_name_updateWindow.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_updateWindow = Entry(updateWindow, width=30)
    l_name_updateWindow.grid(row=1, column=1, padx=20)
    address_updateWindow = Entry(updateWindow, width=30)
    address_updateWindow.grid(row=2, column=1, padx=20)
    city_updateWindow = Entry(updateWindow, width=30)
    city_updateWindow.grid(row=3, column=1, padx=20)
    province_updateWindow = Entry(updateWindow, width=30)
    province_updateWindow.grid(row=4, column=1, padx=20)
    zipcode_updateWindow = Entry(updateWindow, width=30)
    zipcode_updateWindow.grid(row=5, column=1, padx=20)

    # Create Text Box Labels
    f_name_label_updateWindow = Label(updateWindow, text="First Name")
    f_name_label_updateWindow.grid(row=0, column=0, pady=(10, 0))
    l_name_label_updateWindow = Label(updateWindow, text="Last Name")
    l_name_label_updateWindow.grid(row=1, column=0)
    address_label_updateWindow = Label(updateWindow, text="Address")
    address_label_updateWindow.grid(row=2, column=0)
    city_label_updateWindow = Label(updateWindow, text="City")
    city_label_updateWindow.grid(row=3, column=0)
    province_label_updateWindow = Label(updateWindow, text="Province")
    province_label_updateWindow.grid(row=4, column=0)
    zipcode_label_updateWindow = Label(updateWindow, text="Zipcode")
    zipcode_label_updateWindow.grid(row=5, column=0)

    for record in records:
        f_name_updateWindow.insert(0, record[0])
        l_name_updateWindow.insert(0, record[1])
        address_updateWindow.insert(0, record[2])
        city_updateWindow.insert(0, record[3])
        province_updateWindow.insert(0, record[4])
        zipcode_updateWindow.insert(0, record[5])

    # Create a save button
    save_btn = Button(
        updateWindow, text="Save Updated Records", command=save)
    save_btn.grid(row=6, column=0, columnspan=2,
                  pady=10, padx=10, ipadx=100, sticky=W)

    # Commiting changes to a database
    conn.commit()
    # Close a connection
    conn.close()


# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

province = Entry(root, width=30)
province.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)


# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

province_label = Label(root, text="Province")
province_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)


# Create submit button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=126)

# Create a delete button
delete_btn = Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=8, column=0, columnspan=2,
                pady=10, padx=10, ipadx=70, sticky=W)

# Create an upadate button
update_btn = Button(root, text="Update Records", command=update)
update_btn.grid(row=9, column=0, columnspan=2,
                pady=10, padx=10, ipadx=67, sticky=W)

# Create a selection entry box
select_oid = Entry(root, width=10)
select_oid.grid(row=8, column=1, ipady=30, ipadx=15, rowspan=2,
                padx=(0, 10), pady=10, sticky=E)

root.mainloop()
