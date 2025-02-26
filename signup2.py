from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

window=Tk()
window.geometry('1366x768')
window.title('SUNSET')
bg_image = Image.open(r"C:\Users\ASUS\Downloads\Login (8).png")  
bg_image = bg_image.resize((1400, 800))  
new_width=bg_image.width
new_height=bg_image.height
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def toggle_password(entry, button):
    if entry.cget('show') == '*':
        entry.config(show='')
        button.config(text='👁')
    else:
        entry.config(show='*')
        button.config(text='👁‍🗨')


def submit():
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    
    if not email or not password or not confirm_password :
        messagebox.showerror("Error", "All fields are required!")
        return

    else:
        conn=sqlite3.connect('signup2.db')
        c=conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS project(
         email TEXT,
         password TEXT, 
         confirm_password TEXT 
         )''')
        c.execute('INSERT INTO project VALUES(?, ?, ?)',(email, password, confirm_password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data saved successfully!")

label_email = Label(window, text="Email*", font=("Arial", 14),bg='white')
label_email.place(x=700, y=250)
entry_email = Entry(window, font=("Arial", 12))
entry_email.place(x=700, y=280)


label_password = Label(window, text="Password*", font=("Arial", 14),bg='white')
label_password.place(x=700, y=320)
entry_password = Entry(window, font=("Arial", 12))
entry_password.place(x=700, y=350)
button_toggle_password = Button(window, text='👁‍🗨', command=lambda: toggle_password(entry_password, button_toggle_password))
button_toggle_password.place(x=880, y=350)

label_confirm_password = Label(window, text="Confirm Password*", font=("Arial", 14),bg='white')
label_confirm_password.place(x=700, y=390)
entry_confirm_password = Entry(window, font=("Arial", 12))
entry_confirm_password.place(x=700, y=420)
button_toggle_confirm_password = Button(window, text='👁‍🗨', command=lambda: toggle_password(entry_confirm_password, button_toggle_confirm_password))
button_toggle_confirm_password.place(x=880, y=420)


button = Button(window, text="NEXT",font=("Arial", 16, 'bold'), bg="red", fg='white')
button.place(x=700, y=500)

button = Button(window, text="SUBMIT",font=("Arial", 16, 'bold'),command=submit, bg="red", fg='white')
button.place(x=700, y=580)

window.mainloop()



