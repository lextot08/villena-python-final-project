from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk,Image

#Database Function
def createTable(): #table for finance
    
    conn = sqlite3.connect('db_sbms.db')
    
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS tb_sbms (
              id INTEGER PRIMARY KEY,
              budget INTEGER NOT NULL,
              date INTEGER NOT NULL
              )''')

    conn.commit()
    conn.close()

def createTable1(): #table for inventory
    
    conn = sqlite3.connect('db_sbms.db')
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS tb_sbms1 (
              id INTEGER PRIMARY KEY,
              product_name TEXT NOT NULL,
              stock INTEGER NOT NULL,
              cost INTEGER NOT NULL
              )''')

    conn.commit()
    conn.close()

def addFinanceData(): #add data into finance table
    budget_value1 = f_entry.get()
    budget_value2 = f2_entry.get()
    conn = sqlite3.connect('db_sbms.db')
    c = conn.cursor()

    c.execute("INSERT INTO tb_sbms (budget, date) VALUES (?, ?)", (budget_value1, budget_value2))

    conn.commit()
    conn.close()

    display_data()

def addInventoryData(): #for inventory
    inv_value1 = i_entry.get()
    inv_value2 = i2_entry.get()
    inv_value3 = i3_entry.get()

    conn = sqlite3.connect('db_sbms.db')
    c = conn.cursor()

    c.execute("INSERT INTO tb_sbms1 (product_name, stock, cost) VALUES (?, ?, ?)", (inv_value1, inv_value2, inv_value3))

    conn.commit()
    conn.close()

    display_data()

def addData(): #its like if else, checking kung aling table and active
    if f_frame.winfo_ismapped(): 
        addFinanceData()
        
    elif inv_frame.winfo_ismapped():
        addInventoryData()

#for displaying data, maalin kung anong table ang naka open
def display_data():
    for row in treeview.get_children():
        treeview.delete(row) #treeview is for finance

    for row in treeview1.get_children():
        treeview1.delete(row) #may number 1 is for inventory
    
    conn = sqlite3.connect('db_sbms.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tb_sbms")
    rows = c.fetchall()

    c.execute("SELECT * FROM tb_sbms1")
    rows1 = c.fetchall()

    conn.close()

    for row in rows:
        treeview.insert('', 'end', values=(row[0], row[1], row[2]))

    for row in rows1:
        treeview1.insert('', 'end', values=(row[0], row[1], row[2], row[3]))


def deleteData():
    selected_item = treeview.selection() or treeview1.selection()  # Get selected item from either treeview
    if selected_item:
        item = selected_item[0]
        
        # Check if the selected item is from the Finance treeview
        if treeview.selection():
            record_id = treeview.item(item, "values")[0]
            conn = sqlite3.connect('db_sbms.db')
            c = conn.cursor()
            c.execute("DELETE FROM tb_sbms WHERE id = ?", (record_id,))
            conn.commit()
            conn.close()
            treeview.delete(item)

        # Check if the selected item is from the Inventory treeview
        elif treeview1.selection():
            record_id = treeview1.item(item, "values")[0]
            conn = sqlite3.connect('db_sbms.db')
            c = conn.cursor()
            c.execute("DELETE FROM tb_sbms1 WHERE id = ?", (record_id,))
            conn.commit()
            conn.close()
            treeview1.delete(item)

#Main Tkinter code
root = Tk()
root.title('Small Business Management System')
root.geometry("1550x830")

createTable()
createTable1()

#background
bg = Image.open("techbg.jpg")
resized = bg.resize((1550,790))
re_img=ImageTk.PhotoImage(resized)

my_bg = Label(root, image=re_img)
my_bg.place(x=0, y=0)

#logo
logo = Image.open("Newlogo.png")
resizedlogo = logo.resize((200, 150))
re_logo=ImageTk.PhotoImage(resizedlogo)

my_logo = Label(root, image=re_logo, bg="#041414")
my_logo.place(relx=0.01, rely=0.01)


#frame1 = buttons ung frame ay nasa root
frame1 = LabelFrame(root, bg="#50818f", bd=5, padx=20, pady=8)
frame1.place(relwidth=0.30, relheight=0.20, relx=0.10, rely=0.55)

#template for displaying database records
display_frame = LabelFrame(root, bg="#50818f", bd = 10, font='Times 12 bold')
display_frame.place(relwidth=0.45, relheight=0.6, relx=0.43, rely=0.15)

#template for entry button
Entry_frame = LabelFrame(root, bd=5, padx=30, pady=20, bg="#50818f")
Entry_frame.place(relx=0.03, rely=0.30, relwidth=0.37, relheight=0.20,)

#entry and display for finance table
f_frame = LabelFrame(root, bd=5, padx=30, pady=20, bg="#50818f")
frame3 = LabelFrame(root, bg="#50818f", bd = 10, font='Times 12 bold')
#finance frame
budget_lb = Label(f_frame, bg="#50818f", text="Set Budget:", font=('Arial', 10))
date_lb = Label(f_frame, bg="#50818f", text="Set Days:", font=('Arial', 10))
f_entry = Entry(f_frame)
f2_entry = Entry(f_frame)

#entry and display for inventory table
inv_frame = LabelFrame(root, bd=5, padx=30, pady=20, bg="#50818f")
frame4 = LabelFrame(root, bg="#50818f", bd = 10, font='Times 12 bold')
#inventory frame
product_name_lb = Label(inv_frame, bg="#50818f", text="Product Name:", font=('Arial', 10))
stock_lb = Label(inv_frame, bg="#50818f", text="Stocks:", font=('Arial', 10))
total_price_lb = Label(inv_frame, bg="#50818f", text="Total Cost:", font=('Arial', 10))
i_entry = Entry(inv_frame, width=20)
i2_entry = Entry(inv_frame)
i3_entry = Entry(inv_frame)

#Buttons function
def close_all_frame():
    f_frame.place_forget()
    inv_frame.place_forget()
    frame3.place_forget()
    frame4.place_forget()

def show_f_frame():
    f_frame.place(relx=0.03, rely=0.30, relwidth=0.37, relheight=0.20,)
    frame3.place(relwidth=0.45, relheight=0.6, relx=0.43, rely=0.15)
    budget_lb.grid(row=0, column=0)
    date_lb.grid(row=0, column=1)
    #entry
    f_entry.grid(row=1, column=0, pady=5, padx=20)
    f2_entry.grid(row=1, column=1, pady=5, padx=20)
    
def show_inv_frame():
    inv_frame.place(relx=0.03, rely=0.30, relwidth=0.37, relheight=0.20,)
    frame4.place(relwidth=0.45, relheight=0.6, relx=0.43, rely=0.15)
    product_name_lb.grid(row=0, column=0)
    stock_lb.grid(row=0, column=1)
    total_price_lb.grid(row=0, column=2)
    #entry
    i_entry.grid(row=1, column=0, pady=5, padx=20)
    i2_entry.grid(row=1, column=1, pady=5, padx=20)
    i3_entry.grid(row=1, column=2, pady=5, padx=20)

def clear_frame():
    for widget in f_frame.winfo_children():
        if isinstance(widget, Entry):
            widget.delete(0, END)
    for widget in inv_frame.winfo_children():
        if isinstance(widget, Entry):
            widget.delete(0, END)    

#frame1 start
my_button1 = Button(frame1, padx=20, pady=10, text="FINANCE", command=show_f_frame)
my_button1.grid(row=0, column=0, padx=10, pady=10)

my_button2 = Button(frame1, padx=20, pady=10, text="INVENTORY", command=show_inv_frame)
my_button2.grid(row=0, column=1, padx=10, pady=10)

my_button3 = Button(frame1, padx=28, pady=10, text="CHANGE", command=close_all_frame)
my_button3.grid(row=0, column=2, padx=10, pady=10)

my_button4 = Button(frame1, padx=33, pady=10, text="ADD", command=addData)
my_button4.grid(row=1, column=0, padx=10, pady=10)

my_button5 = Button(frame1, padx=33, pady=10, text="CLEAR", command=clear_frame)
my_button5.grid(row=1, column=1, padx=10, pady=10)

my_button6 = Button(frame1, padx=33, pady=10, text="DELETE", command=deleteData)
my_button6.grid(row=1, column=2, padx=10, pady=10)
#frame1 end

#for treeview or displaying data
columns = ('ID', 'Budget', 'Date')
treeview = ttk.Treeview(frame3, columns=columns, show='headings')

treeview.heading('ID', text='ID')
treeview.heading('Budget', text='Budget')
treeview.heading('Date', text='Date')
#column
treeview.column('ID', width=70)
treeview.column('Budget', width=270)
treeview.column('Date', width=270)

treeview.pack()

#treeview for inevntory
columns1 = ('ID', 'product_name', 'stock', 'cost')
treeview1 = ttk.Treeview(frame4, columns=columns1, show='headings')

treeview1.heading('ID', text='ID')
treeview1.heading('product_name', text='Product Name')
treeview1.heading('stock', text='Stock')
treeview1.heading('cost', text='Cost')
#column
treeview1.column('ID', width=50)
treeview1.column('product_name', width=200)
treeview1.column('stock', width=200)
treeview1.column('cost', width=200)

treeview1.pack()

display_data()
root.mainloop()