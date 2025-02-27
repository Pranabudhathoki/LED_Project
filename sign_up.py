from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
import sqlite3

class HotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1366x768')
        self.root.title('SUNSET Hotel Management System')
        self.root.state('zoomed')
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.setup_ui()
        icon_image = Image.open(r"d:\downloadIMAGES\Adobe Express - file.png")
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.iconphoto(False, icon_photo)

    def setup_ui(self):
        try:
            bg_image = Image.open(r"c:\\Users\\sarji\\Downloads\\Login (3).png")
            self.bg_photo = ImageTk.PhotoImage(bg_image)

            bg_label = Label(self.root, image=self.bg_photo)
            bg_label.place(relwidth=1, relheight=1)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image!\n{e}")

        self.create_database()
        self.create_widgets()

    def create_database(self):
        conn = sqlite3.connect(r'signup.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS proj (
                    fullname TEXT,
                    dob TEXT, 
                    phone TEXT, 
                    country TEXT)''')
        conn.commit()
        conn.close()

    def add_placeholder(self, entry, text):
        def on_entry_click(event):
            if entry.get() == text:
                entry.delete(0, END)
                entry.config(fg='black')

        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, text)
                entry.config(fg='gray')

        entry.insert(0, text)
        entry.config(fg='gray')
        entry.bind("<FocusIn>", on_entry_click)
        entry.bind("<FocusOut>", on_focus_out)

    def create_widgets(self):
        Label(self.root, text="Full name*", font=("Arial", 14), bg='white').place(relx=0.62, rely=0.32, anchor="nw")
        self.entry_name = Entry(self.root, font=("Arial", 12))
        self.entry_name.place(relx=0.62, rely=0.36, anchor="nw", relwidth=0.25)
        self.add_placeholder(self.entry_name, "Enter your full name")

        Label(self.root, text="Date of birth (DD/MM/YYYY)*", font=("Arial", 14), bg='white').place(relx=0.62, rely=0.42, anchor="nw")
        self.entry_dob = Entry(self.root, font=("Arial", 12))
        self.entry_dob.place(relx=0.62, rely=0.46, anchor="nw", relwidth=0.25)
        self.add_placeholder(self.entry_dob, "DD/MM/YYYY")

        Label(self.root, text="Phone Number*", font=("Arial", 14), bg='white').place(relx=0.62, rely=0.52, anchor="nw")
        self.entry_phone = Entry(self.root, font=("Arial", 12))
        self.entry_phone.place(relx=0.62, rely=0.56, anchor="nw", relwidth=0.25)
        self.add_placeholder(self.entry_phone, "Enter phone number")

        Label(self.root, text="Country*", font=("Arial", 14), bg='white').place(relx=0.62, rely=0.62, anchor="nw")
        countries = ["Nepal", "United States", "United Kingdom", "India", "Australia", "Germany", "France", "China", "Japan"]
        self.country_combobox = Combobox(self.root, values=countries, state="readonly", font=("Arial", 12))
        self.country_combobox.place(relx=0.62, rely=0.66, anchor="nw", relwidth=0.25)

        Button(self.root, text="SUBMIT", command=self.submit, font=("Arial", 16, 'bold'), bg="red", fg='white').place(relx=0.72, rely=0.75, anchor="nw")
        Button(self.root, text='NEXT', command=self.next_page, font=("Arial", 16, 'bold'), bg="red", fg='white').place(relx=0.72, rely=0.80, anchor="nw")    
        
        # BACK button
        self.home_button = Button(self.root, text='BACK', command=self.go_back, font=("Arial", 16, 'bold'), bg="red", fg='white')
        self.home_button.place(relx=0.72, rely=0.85, anchor="nw")

    def submit(self):
        fullname = self.entry_name.get().strip()
        dob = self.entry_dob.get().strip()
        phone = self.entry_phone.get().strip()
        country = self.country_combobox.get().strip()

        if fullname == "Enter your full name" or dob == "DD/MM/YYYY" or phone == "Enter phone number" or not country:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Phone number must be 10 digits!")
            return

        try:
            conn = sqlite3.connect(r'signup.db')
            c = conn.cursor()
            c.execute('INSERT INTO proj (fullname, dob, phone, country) VALUES (?, ?, ?, ?)', (fullname, dob, phone, country))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Data saved successfully!")
            self.entry_name.delete(0, END)
            self.entry_dob.delete(0, END)
            self.entry_phone.delete(0, END)
            self.country_combobox.set("")
            self.add_placeholder(self.entry_name, "Enter your full name")
            self.add_placeholder(self.entry_dob, "DD/MM/YYYY")
            self.add_placeholder(self.entry_phone, "Enter phone number")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to save data!\n{e}")

    def next_page(self):
        messagebox.showinfo("Loading next page...", "Forgot password page.")

    def go_back(self):
        messagebox.showinfo("Home", "Returning to previous page...")

    def on_closing(self):
        if messagebox.askyesno("Exit", "Are you sure you want to close the window?"):
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = HotelManagement(root)
    root.mainloop()
