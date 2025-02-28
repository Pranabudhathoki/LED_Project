from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


window = Tk()
window.state('zoomed')
window.title('Forgot Password setup')


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
            id INTEGER PRIMARY KEY,
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


label_name = Label(frame, text="Please answer the following questions CORRECTLY",
                   font=("Arial", 14, 'bold'), bg='white')
label_name.pack(pady=10)

def on_enter(e):
    if e.widget.get() in ["Question 1", "Question 2", "Question 3", "Answer 1", "Answer 2", "Answer 3"]:
        e.widget.delete(0, "end")

def on_leave(e):
    if e.widget.get() == "":
        if e.widget == entry_q1:
            e.widget.insert(0, "Question 1")
        elif e.widget == entry_q2:
            e.widget.insert(0, "Question 2")
        elif e.widget == entry_q3:
            e.widget.insert(0, "Question 3")
        elif e.widget == entry_a1:
            e.widget.insert(0, "Answer 1")
        elif e.widget == entry_a2:
            e.widget.insert(0, "Answer 2")
        elif e.widget == entry_a3:
            e.widget.insert(0, "Answer 3")

def save_entries():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO security_questions (question1, answer1, question2, answer2, question3, answer3) VALUES (?, ?, ?, ?, ?, ?)",
                   (entry_q1.get(), entry_a1.get(), entry_q2.get(), entry_a2.get(), entry_q3.get(), entry_a3.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Security questions saved successfully!")

def validate_entries():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM security_questions WHERE question1=? AND answer1=? AND question2=? AND answer2=? AND question3=? AND answer3=?", 
                   (entry_q1.get(), entry_a1.get(), entry_q2.get(), entry_a2.get(), entry_q3.get(), entry_a3.get()))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        messagebox.showinfo("Success", "Answers verified successfully! Proceed to reset your password.")
    else:
        messagebox.showwarning("Error", "Incorrect answers. Please try again!")


q1_frame = Frame(frame, bg="white")
q1_frame.pack(fill="x", pady=5)

entry_q1 = Entry(q1_frame, font=("Arial", 12), justify="center")
entry_q1.insert(0, "Question 1")
entry_q1.pack(side="left", fill="x", expand=True, padx=10)
entry_q1.bind('<FocusIn>', on_enter)
entry_q1.bind('<FocusOut>', on_leave)

entry_a1 = Entry(q1_frame, font=("Arial", 12), justify="center")
entry_a1.insert(0, "Answer 1")
entry_a1.pack(side="right", fill="x", expand=True, padx=10)
entry_a1.bind('<FocusIn>', on_enter)
entry_a1.bind('<FocusOut>', on_leave)


q2_frame = Frame(frame, bg="white")
q2_frame.pack(fill="x", pady=5)

entry_q2 = Entry(q2_frame, font=("Arial", 12), justify="center")
entry_q2.insert(0, "Question 2")
entry_q2.pack(side="left", fill="x", expand=True, padx=10)
entry_q2.bind('<FocusIn>', on_enter)
entry_q2.bind('<FocusOut>', on_leave)

entry_a2 = Entry(q2_frame, font=("Arial", 12), justify="center")
entry_a2.insert(0, "Answer 2")
entry_a2.pack(side="right", fill="x", expand=True, padx=10)
entry_a2.bind('<FocusIn>', on_enter)
entry_a2.bind('<FocusOut>', on_leave)


q3_frame = Frame(frame, bg="white")
q3_frame.pack(fill="x", pady=5)

entry_q3 = Entry(q3_frame, font=("Arial", 12), justify="center")
entry_q3.insert(0, "Question 3")
entry_q3.pack(side="left", fill="x", expand=True, padx=10)
entry_q3.bind('<FocusIn>', on_enter)
entry_q3.bind('<FocusOut>', on_leave)

entry_a3 = Entry(q3_frame, font=("Arial", 12), justify="center")
entry_a3.insert(0, "Answer 3")
entry_a3.pack(side="right", fill="x", expand=True, padx=10)
entry_a3.bind('<FocusIn>', on_enter)
entry_a3.bind('<FocusOut>', on_leave)


button_save = Button(frame, text="SAVE", font=("Arial", 14, 'bold'), bg="green", fg='white', command=save_entries)
button_save.pack(pady=10)


button_submit = Button(frame, text="SUBMIT", font=("Arial", 14, 'bold'), bg="red", fg='white', command=validate_entries)
button_submit.pack(pady=15)


button_next = Button(frame, text="NEXT", font=("Arial", 14, 'bold'), bg="blue", fg='white')
button_next.pack(pady=10)


window.mainloop()


