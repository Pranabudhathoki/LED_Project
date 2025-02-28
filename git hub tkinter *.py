
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


window = Tk()
window.state('zoomed')
window.title('Forgot Password')

bg_image = Image.open(r"c:\Users\sarji\Downloads\Login (5).png")
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(window, image=bg_photo)
bg_label.image = bg_photo
bg_label.pack(fill="both", expand=True)  


def setup_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS security_questions (
            username TEXT PRIMARY KEY,
            question1 TEXT,
            answer1 TEXT,
            question2 TEXT,
            answer2 TEXT,
            question3 TEXT,
            answer3 TEXT
        )
    """)
    conn.commit()
    conn.close()

setup_database()


frame = Frame(window, bg="white", padx=50, pady=50)
frame.place(relx=0.5, rely=0.5, anchor="center")  


label_username = Label(frame, text="Enter Username:", font=("Arial", 12), bg='white')
label_username.pack(pady=5)
entry_username = Entry(frame, font=("Arial", 12), justify="center")
entry_username.pack(pady=5)

def fetch_questions():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT question1, question2, question3 FROM security_questions WHERE username = ?", (entry_username.get(),))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        entry_q1.delete(0, "end")
        entry_q2.delete(0, "end")
        entry_q3.delete(0, "end")
        entry_q1.insert(0, result[0])
        entry_q2.insert(0, result[1])
        entry_q3.insert(0, result[2])
    else:
        messagebox.showerror("Error", "Username not found!")

def validate_entries():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM security_questions WHERE username=? AND answer1=? AND answer2=? AND answer3=?", 
                   (entry_username.get(), entry_a1.get(), entry_a2.get(), entry_a3.get()))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        messagebox.showinfo("Success", "Answers verified successfully! Proceed to reset your password.")
    else:
        messagebox.showwarning("Error", "Incorrect answers. Please try again!")


def on_enter(e):
    if e.widget.get() in ["Answer 1", "Answer 2", "Answer 3"]:
        e.widget.delete(0, "end")

def on_leave(e):
    if e.widget.get() == "":
        if e.widget == entry_a1:
            e.widget.insert(0, "Answer 1")
        elif e.widget == entry_a2:
            e.widget.insert(0, "Answer 2")
        elif e.widget == entry_a3:
            e.widget.insert(0, "Answer 3")


button_fetch = Button(frame, text="FETCH QUESTIONS", font=("Arial", 12, 'bold'), bg="orange", fg='white', command=fetch_questions)
button_fetch.pack(pady=10)


entry_q1 = Entry(frame, font=("Arial", 12), justify="center")
entry_q1.pack(fill="x", pady=5)
entry_a1 = Entry(frame, font=("Arial", 12), justify="center")
entry_a1.insert(0, "Answer 1")
entry_a1.pack(fill="x", pady=5)
entry_a1.bind('<FocusIn>', on_enter)
entry_a1.bind('<FocusOut>', on_leave)


entry_q2 = Entry(frame, font=("Arial", 12), justify="center")
entry_q2.pack(fill="x", pady=5)
entry_a2 = Entry(frame, font=("Arial", 12), justify="center")
entry_a2.insert(0, "Answer 2")
entry_a2.pack(fill="x", pady=5)
entry_a2.bind('<FocusIn>', on_enter)
entry_a2.bind('<FocusOut>', on_leave)


entry_q3 = Entry(frame, font=("Arial", 12), justify="center")
entry_q3.pack(fill="x", pady=5)
entry_a3 = Entry(frame, font=("Arial", 12), justify="center")
entry_a3.insert(0, "Answer 3")
entry_a3.pack(fill="x", pady=5)
entry_a3.bind('<FocusIn>', on_enter)
entry_a3.bind('<FocusOut>', on_leave)


button_submit = Button(frame, text="SUBMIT", font=("Arial", 14, 'bold'), bg="red", fg='white', command=validate_entries)
button_submit.pack(pady=15)


window.mainloop()
 