from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

class SignUpApp:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title('SIGN-UP')

        # Set window icon
        icon_image = Image.open(r"C:\Users\ASUS\Downloads\8044bae3-fa5c-4f27-997d-307d18c3f8e8.png")
        self.icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.iconphoto(False, self.icon_photo)  

        # Set background image
        bg_image = Image.open(r"C:\Users\ASUS\Downloads\Login (8).png")
        bg_image = bg_image.resize((1400, 800))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create entry fields and buttons
        self.create_widgets()

    def create_widgets(self):
        # Email Entry
        Label(self.root, text="Email*", font=("Arial", 14), bg='white').place(x=700, y=250)
        self.entry_email = Entry(self.root, font=("Arial", 12), fg='gray')
        self.entry_email.place(x=700, y=280, width=180)
        self.set_placeholder(self.entry_email, "Enter your email")

        # Password Entry
        Label(self.root, text="Password*", font=("Arial", 14), bg='white').place(x=700, y=320)
        self.entry_password = Entry(self.root, font=("Arial", 12), fg='gray')
        self.entry_password.place(x=700, y=350, width=180)
        self.set_placeholder(self.entry_password, "Enter your password")
        
        self.button_toggle_password = Button(self.root, text='👁‍🗨', command=lambda: self.toggle_password(self.entry_password,
        self.button_toggle_password))
        self.button_toggle_password.place(x=880, y=350)

        # Confirm Password Entry
        Label(self.root, text="Confirm Password*", font=("Arial", 14), bg='white').place(x=700, y=390)
        self.entry_confirm_password = Entry(self.root, font=("Arial", 12), fg='gray')
        self.entry_confirm_password.place(x=700, y=420, width=180)
        self.set_placeholder(self.entry_confirm_password, "Confirm your password")

        self.button_toggle_confirm_password = Button(self.root, text='👁‍🗨', command=lambda: 
        self.toggle_password(self.entry_confirm_password, self.button_toggle_confirm_password))
        self.button_toggle_confirm_password.place(x=880, y=420)

        # Buttons
        Button(self.root, text="NEXT", font=("Arial", 16, 'bold'), bg="red", fg='white').place(x=700, y=500)
        Button(self.root, text="SUBMIT", font=("Arial", 16, 'bold'), command=self.submit, bg="red", fg='white').place(x=700, y=660)
        Button(self.root, text="BACK", font=("Arial", 16, 'bold'), bg="red", fg='white').place(x=700, y=580)

    def set_placeholder(self, entry, placeholder):
        """Set placeholder text with gray color and add event bindings."""
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event: self.on_focus_in(entry, placeholder))
        entry.bind("<FocusOut>", lambda event: self.on_focus_out(entry, placeholder))

    def on_focus_in(self, entry, placeholder):
        """Remove placeholder text when the user clicks on the entry."""
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(fg='black')

    def on_focus_out(self, entry, placeholder):
        """Restore placeholder text if entry is empty."""
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg='gray')

    def toggle_password(self, entry, button):
        """Show/hide password when toggle button is clicked."""
        if entry.cget('show') == '*':
            entry.config(show='')
            button.config(text='👁')
        else:
            entry.config(show='*')
            button.config(text='👁‍🗨')

    def submit(self):
        """Handle form submission."""
        email = self.entry_email.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        if not email or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = sqlite3.connect('signup2.db')
        c = conn.cursor()
        c.execute(''' CREATE TABLE IF NOT EXISTS project(
             email TEXT,
             password TEXT, 
             confirm_password TEXT 
        )''')
        c.execute('INSERT INTO project VALUES(?, ?, ?)', (email, password, confirm_password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data saved successfully!")

if __name__ == "__main__":
    root = Tk()
    app = SignUpApp(root)
    root.mainloop()

 
