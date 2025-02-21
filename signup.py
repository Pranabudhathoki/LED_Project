from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import sqlite3

window=Tk()
window.geometry('1366x768')
window.title('SUNSET')
bg_image = Image.open(r"C:\Users\ASUS\Downloads\Login (4).png")  
bg_image = bg_image.resize((1400, 800))  
new_width=bg_image.width
new_height=bg_image.height
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def submit():
    fullname = entry_name.get()
    dob = entry_dob.get()
    phone = entry_phone.get()
    country = country_combobox.get()

    if not fullname or not dob or not phone or not country:
        messagebox.showerror("Error", "All fields are required!")
        return

    else:
        conn=sqlite3.connect('signup.db')
        c=conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS proj(
         fullname TEXT,
         dob INT, 
         phone INT, 
         country TEXT)''')
        c.execute('INSERT INTO proj VALUES(?, ?, ?, ?)',(fullname, dob, phone, country))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data saved successfully!")

button = Button(window, text="SUBMIT",command=submit,font=("Arial", 16, 'bold'), bg="red", fg='white')
button.place(x=1050, y=650)

label_name = Label(window, text="Full name*", font=("Arial", 14),bg='white')
label_name.place(x=850, y=250)
entry_name = Entry(window, font=("Arial", 12))
entry_name.place(x=850, y=280)

label_dob = Label(window, text="Date of birth (DD/MM/YYYY)*", font=("Arial", 14),bg='white')
label_dob.place(x=850, y=330)
entry_dob = Entry(window, font=("Arial", 12))
entry_dob.place(x=850, y=360)

label_phone = Label(window, text="Phone Number*", font=("Arial", 14),bg='white')
label_phone.place(x=850, y=410)
entry_phone = Entry(window, font=("Arial", 12))

# x=entry_phone
# if x >= '10':
#     messagebox.showerror("Invalid number!")
# else:
#     messagebox.showinfo("Success", "Valid number!")

entry_phone.place(x=850, y=440)

label_country = Label(window, text="Country*", font=("Arial", 14),bg='white')
label_country.place(x=850, y=490)
countries = ["Nepal","United States", "United Kingdom", "India", "Australia", "Germany", "France", "China", "Japan"]
country_combobox = Combobox(window, values=countries, state="readonly", font=("Arial", 12))
country_combobox.place(x=850, y=520)

window.mainloop()




