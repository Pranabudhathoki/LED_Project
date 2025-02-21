

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1550x800+0+0')
        self.root.title('Sunset Hotel Management System')

        # Create Frames for Home and Login pages
        self.home_frame = Frame(self.root)
        self.login_frame = Frame(self.root)

        self.create_home_page()
        self.create_login_page()

        # Show Home Page by default
        self.show_frame(self.home_frame)

    def create_home_page(self):
        # Background image for Home Page
        home_image = Image.open(r"C:\Users\sarji\Downloads\Login (2).png")
        bg_homeimage = ImageTk.PhotoImage(home_image)
        bg_label_homepage = Label(self.home_frame, image=bg_homeimage)
        bg_label_homepage.image = bg_homeimage
        bg_label_homepage.pack()

        # Navigation Buttons
        Button(self.home_frame, text="HOME", command=self.home, font=("Arial", 16, 'bold'), bg="white", fg='black').place(relx=0.65, rely=0.1, anchor="ne")
        Button(self.home_frame, text="ROOMS", command=self.room, font=("Arial", 16, 'bold'), bg="white", fg='black').place(relx=0.73, rely=0.1, anchor="ne")
        Button(self.home_frame, text="BOOK", command=self.book, font=("Arial", 16, 'bold'), bg="white", fg='black').place(relx=0.85, rely=0.1, anchor="ne")
        Button(self.home_frame, text="LOGIN", command=lambda: self.show_frame(self.login_frame), font=("Arial", 16, 'bold'), bg="white", fg='black').place(relx=0.93, rely=0.1, anchor="ne")

    def create_login_page(self):
        # Database setup
        conn = sqlite3.connect(r"D:\Semester1\Programming&Algorithms\PRJCTS\SignIn.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS sign_in(
                      f_name text,
                      password text)''')
        conn.commit()
        conn.close()

        # Background image for Login Page
        bg_image = Image.open(r"C:\\Users\\sarji\\Downloads\\Login (1).png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.login_frame, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.pack()

        # Username Entry
        label_name = Label(self.login_frame, text="Username*", font=("Arial", 14, 'bold'), bg='white')
        label_name.place(relx=0.5, rely=0.3, anchor="nw")
        self.entry_name = Entry(self.login_frame, font=("Arial", 12))
        self.entry_name.insert(0, "Enter your Username")
        self.entry_name.place(relx=0.5, rely=0.35, anchor="nw", relwidth=0.3)

        # Password Entry
        label_pass = Label(self.login_frame, text="Password*", font=("Arial", 14, 'bold'), bg='white')
        label_pass.place(relx=0.5, rely=0.4, anchor="nw")
        self.entry_pass = Entry(self.login_frame, font=("Arial", 12), show="*")
        self.entry_pass.insert(0, "Enter your Password")
        self.entry_pass.place(relx=0.5, rely=0.45, anchor="nw", relwidth=0.3)

        # Show Password Checkbox
        self.show_password_var = BooleanVar()
        show_password_checkbox = Checkbutton(self.login_frame, text="Show Password", variable=self.show_password_var, command=self.toggle_password, bg='white')
        show_password_checkbox.place(relx=0.5, rely=0.5, anchor="nw")

        # Forgot Password Button
        forgot_button = Button(self.login_frame, text="Forgot Password?", fg="blue", cursor="hand2", font=("Arial", 10, "underline"), bd=0, command=self.forgot_password)
        forgot_button.place(relx=0.5, rely=0.7, anchor="nw")

        # Signup
        signup_button = Button(self.login_frame, text='Dont have an account?',fg="blue", cursor="hand2", font=("Arial", 10, "underline"), bd=0, command=self.signup)
        signup_button.place(relx=0.5,rely=0.8, anchor="nw")

        # Submit Button
        button = Button(self.login_frame, text="SUBMIT", command=self.submit, font=("Arial", 16, 'bold'), bg="red", fg='white')
        button.place(relx=0.5, rely=0.75, anchor="nw")

        # Back Button
        back_button = Button(self.login_frame, text="BACK TO HOME", command=lambda: self.show_frame(self.home_frame), font=("Arial", 12, 'bold'))
        back_button.place(relx=0.5, rely=0.9, anchor="nw")

    def toggle_password(self):
        if self.show_password_var.get():
            self.entry_pass.config(show="")
        else:
            self.entry_pass.config(show="*")

    def forgot_password(self):
        messagebox.showinfo("Password Reset", "Redirecting to password reset...")

    def signup():
        messagebox.showinfo("Opening signup page pls wait...")

    def submit(self):
        username = self.entry_name.get()
        password = self.entry_pass.get()

        if not username or not password:
            messagebox.showerror("Error", "Please input all the details.")
        else:
            conn = sqlite3.connect(r"D:\Semester1\Programming&Algorithms\PRJCTS\SignIn.db")
            c = conn.cursor()
            c.execute('INSERT INTO sign_in (f_name, password) VALUES (?, ?)', (username, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Form submitted!")
            self.entry_name.delete(0, END)
            self.entry_pass.delete(0, END)

    def show_frame(self, frame):
        self.home_frame.pack_forget()
        self.login_frame.pack_forget()
        frame.pack()

    def home(self):
        print("Welcome to Home Page...")

    def room(self):
        print("Welcome to Rooms...")

    def book(self):
        print("Welcome to Booking...")

# Run the App
root = Tk()
app = HotelApp(root)
root.mainloop()

