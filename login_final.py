from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

class SunsetHotelLogin:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title('Sunset Hotel Management System')
        
        try:
            icon_image = Image.open(r"d:\downloadIMAGES\Adobe Express - file.png")
            icon_photo = ImageTk.PhotoImage(icon_image)
            self.root.iconphoto(False, icon_photo)
        except:
            messagebox.showerror("Error", "Icon image not found")
        
        self.setup_database()
        self.setup_ui()
    
    def setup_database(self):
        conn = sqlite3.connect("signup.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sign (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
        conn.commit()
        conn.close()
    
    def setup_ui(self):
        self.login_frame = Frame(self.root)
        self.login_frame.pack(fill='both', expand=True)
        
        try:
            bg_image = Image.open(r"C:\\Users\\sarji\\Downloads\\Login (1).png")
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = Label(self.login_frame, image=self.bg_photo)
            bg_label.pack()
        except:
            messagebox.showerror("Error", "Background image not found")
        
        self.create_login_fields()
    
    def add_placeholder(self, entry, text, is_password=False):
        def on_entry_click(event):
            if entry.get() == text:
                entry.delete(0, END)
                entry.config(fg='black', show="*" if is_password else "")

        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, text)
                entry.config(fg='gray', show="" if not is_password else "*")
        
        entry.insert(0, text)
        entry.config(fg='gray', show="" if not is_password else "*")
        entry.bind("<FocusIn>", on_entry_click)
        entry.bind("<FocusOut>", on_focus_out)
    
    def create_login_fields(self):
        Label(self.login_frame, text="Email*", font=("Arial", 14, 'bold'), bg='white').place(relx=0.5, rely=0.3, anchor="nw")
        self.user = Entry(self.login_frame, font=("Arial", 12))
        self.user.place(relx=0.5, rely=0.35, anchor="nw", relwidth=0.3)
        self.add_placeholder(self.user, "Enter your email")
        
        Label(self.login_frame, text="Password*", font=("Arial", 14, 'bold'), bg='white').place(relx=0.5, rely=0.4, anchor="nw")
        self.code = Entry(self.login_frame, font=("Arial", 12))
        self.code.place(relx=0.5, rely=0.45, anchor="nw", relwidth=0.3)
        self.add_placeholder(self.code, "Enter your password", is_password=True)
        
        self.show_password_var = BooleanVar(value=False)
        show_password_checkbox = Checkbutton(self.login_frame, text="Show Password", variable=self.show_password_var, command=self.toggle_password, bg='white')
        show_password_checkbox.place(relx=0.5, rely=0.5, anchor="nw")
        
        Button(self.login_frame, text="Forgot Password?", fg="blue", cursor="hand2", font=("Arial", 10, "underline"), bd=0, command=self.forgot_password).place(relx=0.5, rely=0.7, anchor="nw")
        Button(self.login_frame, text="Don't have an account?", fg="blue", cursor="hand2", font=("Arial", 10, "underline"), bd=0, command=self.signup).place(relx=0.5, rely=0.75, anchor="nw")
        Button(self.login_frame, text="SUBMIT", command=self.signin, font=("Arial", 16, 'bold'), bg="red", fg='white').place(relx=0.5, rely=0.80, anchor="nw")
    
    def toggle_password(self):
        if self.show_password_var.get():
            self.code.config(show="")
        else:
            self.code.config(show="*")
    
    def forgot_password(self):
        messagebox.showinfo("Password Reset", "Redirecting to password reset...")
    
    def signup(self):
        messagebox.showinfo("Signup", "Opening signup page, please wait...")
    
    def signin(self):
        username = self.user.get().strip()
        password = self.code.get().strip()

        if username in ["", "Enter your email"] or password in ["", "Enter your password"]:
            messagebox.showerror("Error", "Please input all the details.")
            return
        
        # Authentication logic here (Database query can be added)
        messagebox.showinfo("Success", "Login successful!")
    
    def on_closing(self):
        if messagebox.askyesno("Exit", "Are you sure you want to close the window?"):
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = SunsetHotelLogin(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
