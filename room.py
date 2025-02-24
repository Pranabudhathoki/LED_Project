# from tkinter import *
# from tkinter.ttk import Combobox
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import sqlite3

# window=Tk()
# window.geometry('1366x768')
# window.title('ROOMBOOKING')
# bg_image = Image.open(r"C:\Users\ASUS\Downloads\Login (5).png")  
# bg_image = bg_image.resize((1400, 800))  
# new_width=bg_image.width
# new_height=bg_image.height
# bg_photo = ImageTk.PhotoImage(bg_image)
# bg_label = Label(window, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# def create_table():
#     conn = sqlite3.connect('hotel.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS room (
#         Contact INT PRIMARY KEY,
#         CheckIn INT,
#         CheckOut INT,
#         RoomType TEXT,
#         Cost FLOAT
#     )''')
#     conn.commit()
#     conn.close()

# def total():
#     Cost= 1500
#     if type_combobox == 'single':
#         Total_cost= Cost * 1
#         print(f"Total Cost: {Total_cost} ")
#     elif type_combobox == 'double':
#         Total_cost= Cost * 2
#         print(f"Total Cost: {Total_cost} ")
#     elif type_combobox == 'triple':
#         Total_cost= Cost * 3
#         print(f"Total Cost: {Total_cost} ")
#     else:
#         print("Invalid Room Type!")
     


# def save_data():
#     Contact = entry_contact.get()
#     CheckIn = entry_checkin.get()
#     CheckOut = entry_checkout.get()
#     RoomType = type_combobox.get()
#     Cost = entry_cost.get()

#     if Contact == "" or CheckIn == "" or CheckOut == "" or RoomType == "" or Cost == "":
#         messagebox.showerror("Error", "All fields are required!")
#         return

#     try:
#         conn = sqlite3.connect('hotel.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO room VALUES (?, ?, ?, ?, ?)", (Contact, CheckIn, CheckOut, RoomType, Cost))
#         conn.commit()
#         conn.close()
#         messagebox.showinfo("Success", "Data saved successfully!")
#     except sqlite3.IntegrityError:
#         messagebox.showerror("Error", "Contact number already exists!")
#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {e}")

# def fetch_data():
#     Contact = entry_contact.get()
#     if Contact == "":
#         messagebox.showerror("Error", "Please enter a Contact Number!")
#         return

#     conn = sqlite3.connect('hotel.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM room WHERE Contact=?", (Contact,))
#     row = c.fetchone()
#     conn.close()

#     if row:
#         entry_checkin.delete(0, END)
#         entry_checkout.delete(0, END)
#         type_combobox.set("")
#         entry_cost.delete(0, END)

#         entry_checkin.insert(0, row[1])
#         entry_checkout.insert(0, row[2])
#         type_combobox.set(row[3])
#         entry_cost.insert(0, row[4])
#         messagebox.showinfo("Success", "Data Retrieved Successfully!")
#     else:
#         messagebox.showerror("Error", "No record found!")



# label=Label(window, text="ROOMBOOKING", font=("Arial", 30),fg='black',bg='#f9f2ec')
# label.place(x=700, y=20)

# LabelFrameleft = LabelFrame(window, bd=2, relief=RIDGE, text="ROOMBOOKING Details",font=("arial",20,"bold"),bg="#f9f2ec", padx=2)
# LabelFrameleft.place(x=5,y=50,width=425,height=600)

# label_contact = Label(window, text="Customer Contact:", font=("Arial", 14),bg='#f9f2ec')
# label_contact.place(x=15, y=80)
# entry_contact = Entry(window, font=("Arial", 12))
# entry_contact.place(x=15, y=110)

# button = Button(window, text="Fetch Data",command=fetch_data,font=("Arial", 16, 'bold'), bg="black", fg='#ffe680')
# button.place(x=280, y=100)

# label_checkin = Label(window, text="Check-in Date:", font=("Arial", 14),bg='#f9f2ec')
# label_checkin.place(x=15, y=140)
# entry_checkin = Entry(window, font=("Arial", 12))
# entry_checkin.place(x=15, y=170)

# label_checkout = Label(window, text="Check-out Date:", font=("Arial", 14),bg='#f9f2ec')
# label_checkout.place(x=15, y=200)
# entry_checkout = Entry(window, font=("Arial", 12))
# entry_checkout.place(x=15, y=230)

# label_room = Label(window, text="Room-Type:", font=("Arial", 14),bg='#f9f2ec')
# label_room.place(x=15, y=260)
# type=["Single","Double","Triple"]
# type_combobox = Combobox(window, values=type, state="readonly", font=("Arial", 12))
# type_combobox.place(x=15, y=290)

# label_cost = Label(window, text="Total Cost:", font=("Arial", 14),bg='#f9f2ec')
# label_cost.place(x=15, y=320)
# entry_cost = Entry(window, font=("Arial", 12))
# entry_cost.place(x=15, y=350)

# button = Button(window, text="UPDATE",font=("Arial", 16, 'bold'), bg="black", fg='#ffe680')
# button.place(x=50, y=430)

# button = Button(window, text="RESET",font=("Arial", 16, 'bold'), bg="black", fg='#ffe680')
# button.place(x=155, y=480)

# button = Button(window, text="SUBMIT",command=total,font=("Arial", 16, 'bold'), bg="black", fg='#ffe680')
# button.place(x=260, y=530)


# window.mainloop() 







from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from datetime import datetime
from tkcalendar import DateEntry

window=Tk()
window.geometry('1366x768')
window.title('ROOMBOOKING')
bg_image = Image.open(r"C:\Users\ASUS\Downloads\Login (5).png")  
bg_image = bg_image.resize((1400, 800))  
new_width=bg_image.width
new_height=bg_image.height
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def create_table():
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS room (
        Contact TEXT PRIMARY KEY,
        CheckIn TEXT,
        CheckOut TEXT,
        RoomType TEXT,
        Cost FLOAT
    )''')
    conn.commit()
    conn.close()

def calculate_total():
    room_type = type_combobox.get()
    check_in = entry_checkin.get_date()
    check_out = entry_checkout.get_date()

    try:
        nights = (check_out - check_in).days

        if nights < 0:
            raise ValueError("Check-out date must be after check-in date")

        rates = {"Single": 1500, "Double": 2500, "Triple": 3500}
        if room_type not in rates:
            raise ValueError("Invalid room type")

        total_cost = rates[room_type] * nights
        entry_cost.delete(0, END)
        entry_cost.insert(0, f"{total_cost:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def save_data():
    Contact = entry_contact.get()
    CheckIn = entry_checkin.get_date().strftime("%Y-%m-%d")
    CheckOut = entry_checkout.get_date().strftime("%Y-%m-%d")
    RoomType = type_combobox.get()
    Cost = entry_cost.get()

    if Contact == "" or CheckIn == "" or CheckOut == "" or RoomType == "" or Cost == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        conn = sqlite3.connect('hotel.db')
        c = conn.cursor()
        c.execute("INSERT INTO room VALUES (?, ?, ?, ?, ?)", (Contact, CheckIn, CheckOut, RoomType, Cost))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data saved successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Contact number already exists!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def reset_form():
    entry_contact.delete(0, END)
    entry_checkin.set_date(datetime.now())
    entry_checkout.set_date(datetime.now())
    type_combobox.set("")
    entry_cost.delete(0, END)


label=Label(window, text="ROOMBOOKING", font=("Arial", 30),fg='black',bg='#f9f2ec')
label.place(x=700, y=20)

LabelFrameleft = LabelFrame(window, bd=2, relief=RIDGE, text="ROOMBOOKING Details",font=("arial",20,"bold"),bg="#f9f2ec", padx=2)
LabelFrameleft.place(x=5,y=50,width=425,height=600)

label_contact = Label(window, text="Customer Contact:", font=("Arial", 14),bg='#f9f2ec')
label_contact.place(x=15, y=80)
entry_contact = Entry(window, font=("Arial", 12))
entry_contact.place(x=15, y=110)

label_checkin = Label(window, text="Check-in Date:", font=("Arial", 14),bg='#f9f2ec')
label_checkin.place(x=15, y=140)
entry_checkin = DateEntry(window, font=("Arial", 12),bg='darkblue',fg='white',bd=2,date_pattern='yyyy-mm-dd')
entry_checkin.place(x=15, y=170)

label_checkout = Label(window, text="Check-out Date:", font=("Arial", 14),bg='#f9f2ec')
label_checkout.place(x=15, y=200)
entry_checkout = DateEntry(window, font=("Arial", 12),bg='darkblue',fg='white',bd=2,date_pattern='yyyy-mm-dd')
entry_checkout.place(x=15, y=230)

label_room = Label(window, text="Room-Type:", font=("Arial", 14),bg='#f9f2ec')
label_room.place(x=15, y=260)
type=["Single","Double","Triple"]
type_combobox = Combobox(window, values=type, state="readonly", font=("Arial", 12))
type_combobox.place(x=15, y=290)

label_cost = Label(window, text="Total Cost:", font=("Arial", 14),bg='#f9f2ec')
label_cost.place(x=15, y=320)
entry_cost = Entry(window, font=("Arial", 12))
entry_cost.place(x=15, y=350)

button = Button(window, text="UPDATE",font=("Arial", 16, 'bold'),command=calculate_total, bg="black", fg='#ffe680')
button.place(x=50, y=430)

button = Button(window, text="RESET",font=("Arial", 16, 'bold'),command=reset_form, bg="black", fg='#ffe680')
button.place(x=155, y=480)

button = Button(window, text="SUBMIT",font=("Arial", 16, 'bold'),command=save_data, bg="black", fg='#ffe680')
button.place(x=260, y=530)
window.mainloop() 







