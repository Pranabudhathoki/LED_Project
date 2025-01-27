# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from tkinter.ttk import Combobox

# def resize_bg(event):
#     """Resize the background image to fit the window size."""
#     new_width = event.width
#     new_height = event.height
#     resized_image = bg_image.resize((new_width, new_height), Image.ANTIALIAS)
#     bg_photo = ImageTk.PhotoImage(resized_image)
#     bg_label.config(image=bg_photo)
#     bg_label.image = bg_photo

# def submit():
#     """Handle form submission."""
#     full_name = entry_name.get()
#     dob = entry_dob.get()
#     phone = entry_phone.get()
#     country = country_combobox.get()

#     if not full_name or not dob or not phone or not country:
#         messagebox.showerror("Error", "Please input all the details.")
#     else:
#         messagebox.showinfo("Success", "Form submitted!")

# # Main window
# window = Tk()
# window.geometry('1366x768')
# window.minsize(800, 600)
# window.resizable(True, True)

# # Load background image
# bg_image = Image.open(r"C:\Users\sarji\Downloads\Login (1).png")  # Ensure the path is correct
# bg_photo = ImageTk.PhotoImage(bg_image)

# # Canvas for background
# bg_label = Label(window, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # Resize the background dynamically
# window.bind("<Configure>", resize_bg)

# # Header text
# lbl = Label(window, text='Sign up', font=('Arial', 30, 'bold'), fg='red', bg='white')
# lbl.place(relx=0.5, rely=0.1, anchor="left")

# slogan = Label(window, text='Enter your details to sign up', font=('Arial', 14), fg='black', bg='white')
# slogan.place(relx=0.5, rely=0.17, anchor="left")

# # Labels and input fields
# label_name = Label(window, text="Full name*", font=("Arial", 14), bg='white')
# label_name.place(relx=0.5, rely=0.3, anchor="left")
# entry_name = Entry(window, font=("Arial", 12))
# entry_name.place(relx=0.5, rely=0.35, anchor="left", relwidth=0.4)

# label_dob = Label(window, text="Date of birth (DD/MM/YYYY)*", font=("Arial", 14), bg='white')
# label_dob.place(relx=0.5, rely=0.4, anchor="left")
# entry_dob = Entry(window, font=("Arial", 12))
# entry_dob.place(relx=0.5, rely=0.45, anchor="left", relwidth=0.4)

# label_phone = Label(window, text="Phone Number*", font=("Arial", 14), bg='white')
# label_phone.place(relx=0.5, rely=0.5, anchor="left")
# entry_phone = Entry(window, font=("Arial", 12))
# entry_phone.place(relx=0.5, rely=0.55, anchor="left", relwidth=0.4)

# label_country = Label(window, text="Country*", font=("Arial", 14), bg='white')
# label_country.place(relx=0.5, rely=0.6, anchor="left")
# countries = ["Nepal", "United States", "United Kingdom", "India", "Australia", "Germany", "France", "China", "Japan"]
# country_combobox = Combobox(window, values=countries, state="readonly", font=("Arial", 12))
# country_combobox.place(relx=0.5, rely=0.65, anchor="left", relwidth=0.4)

# # Submit button
# button = Button(window, text="SUBMIT", command=submit, font=("Arial", 16, 'bold'), bg="red", fg='white')
# button.place(relx=0.5, rely=0.75, anchor="left")

# window.mainloop()


# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from tkinter.ttk import Combobox

# def resize_bg(event):
#     """Resize the background image to fit the window size."""
#     new_width = event.width
#     new_height = event.height
#     resized_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(resized_image)
#     bg_label.config(image=bg_photo)
#     bg_label.image = bg_photo

# def submit():
#     """Handle form submission."""
#     username = entry_name.get()
#     password = entry_pass.get()
#     # phone = entry_phone.get()
#     # country = country_combobox.get()

#     if not username or not password:
#         messagebox.showerror("Error", "Please input all the details.")
#     else:
#         messagebox.showinfo("Success", "Form submitted!")

# # Main window
# window = Tk()
# window.geometry('1366x768')
# window.minsize(800, 600)
# window.resizable(True, True)

# # Load background image
# bg_image = Image.open(r"C:\\Users\\sarji\\Downloads\\Login (1).png")  # Ensure the path is correct
# bg_photo = ImageTk.PhotoImage(bg_image)

# # Canvas for background
# bg_label = Label(window, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # Resize the background dynamically
# window.bind("<Configure>", resize_bg)

# # # Header text
# # lbl = Label(window, text='Sign up', font=('Arial', 30, 'bold'), fg='red', bg='white')
# # lbl.place(relx=0.5, rely=0.1, anchor="n")

# # slogan = Label(window, text='Enter your details to sign up', font=('Arial', 14), fg='black', bg='white')
# # slogan.place(relx=0.5, rely=0.17, anchor="n")

# # Labels and input fields
# label_name = Label(window, text="Username*", font=("Arial", 14,'bold'), bg='white')
# label_name.place(relx=0.5, rely=0.3, anchor="nw")
# entry_name = Entry(window,font=("Arial", 12))
# entry_name.insert(0, "Enter your Username")
# entry_name.place(relx=0.5, rely=0.35, anchor="nw", relwidth=0.4)

# label_pass = Label(window, text="Password*", font=("Arial", 14,'bold'), bg='white')
# label_pass.place(relx=0.5, rely=0.4, anchor="nw")
# entry_pass = Entry(window,font=("Arial", 12))
# entry_pass.insert(0, "Enter your Password")
# entry_pass.place(relx=0.5, rely=0.45, anchor="nw", relwidth=0.4)

# # label_phone = Label(window, text="Phone Number*", font=("Arial", 14), bg='white')
# # label_phone.place(relx=0.5, rely=0.5, anchor="nw")
# # entry_phone = Entry(window, font=("Arial", 12))
# # entry_phone.place(relx=0.5, rely=0.55, anchor="nw", relwidth=0.4)

# # label_country = Label(window, text="Country*", font=("Arial", 14), bg='white')
# # label_country.place(relx=0.5, rely=0.6, anchor="nw")
# # countries = ["Nepal", "United States", "United Kingdom", "India", "Australia", "Germany", "France", "China", "Japan"]
# # country_combobox = Combobox(window, values=countries, state="readonly", font=("Arial", 12))
# # country_combobox.place(relx=0.5, rely=0.65, anchor="nw", relwidth=0.4)

# # Submit button
# button = Button(window, text="SUBMIT", command=submit, font=("Arial", 16, 'bold'), bg="red", fg='white')
# button.place(relx=0.5, rely=0.75, anchor="nw")

# window.mainloop()


# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from tkinter.ttk import Combobox

# def resize_bg(event):
#     """Resize the background image to fit the window size."""
#     new_width = event.width
#     new_height = event.height
#     resized_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(resized_image)
#     bg_label.config(image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to the image

# def submit():
#     """Handle form submission."""
#     username = entry_name.get()
#     password = entry_pass.get()

#     if not username or not password:
#         messagebox.showerror("Error", "Please input all the details.")
#     else:
#         messagebox.showinfo("Success", "Form submitted!")

# # Main window
# window = Tk()
# window.geometry('1366x768')
# window.minsize(800, 600)
# window.resizable(True, True)

# # Load background image
# bg_image = Image.open(r"C:\\Users\\sarji\\Downloads\\Login (1).png")  # Ensure the path is correct
# bg_photo = ImageTk.PhotoImage(bg_image)

# # Canvas for background
# bg_label = Label(window, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # Resize the background dynamically
# window.bind("<Configure>", resize_bg)

# # Labels and input fields
# label_name = Label(window, text="Username*", font=("Arial", 14,'bold'), bg='white')
# label_name.place(relx=0.5, rely=0.3, anchor="nw")
# entry_name = Entry(window, font=("Arial", 12))
# entry_name.insert(0, "Enter your Username")
# entry_name.place(relx=0.5, rely=0.35, anchor="nw", relwidth=0.4)

# label_pass = Label(window, text="Password*", font=("Arial", 14,'bold'), bg='white')
# label_pass.place(relx=0.5, rely=0.4, anchor="nw")
# entry_pass = Entry(window, font=("Arial", 12), show="*")
# entry_pass.insert(0, "Enter your Password")
# entry_pass.place(relx=0.5, rely=0.45, anchor="nw", relwidth=0.4)

# # Submit button
# button = Button(window, text="SUBMIT", command=submit, font=("Arial", 16, 'bold'), bg="red", fg='white')
# button.place(relx=0.5, rely=0.75, anchor="nw")

# window.mainloop()


from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox

def resize_bg(event):
    # """Resize the background image to fit the window size."""
    new_width = event.width
    new_height = event.height
    resized_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(resized_image)
    bg_label.config(image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference to the image

def toggle_password():
    # """Toggle password visibility."""
    if show_password_var.get():
        entry_pass.config(show="")  # Show the password
    else:
        entry_pass.config(show="*")  # Hide the password

def submit():
    # """Handle form submission."""
    username = entry_name.get()
    password = entry_pass.get()

    if not username or not password:
        messagebox.showerror("Error", "Please input all the details.")
    else:
        messagebox.showinfo("Success", "Form submitted!")

# Main window
window = Tk()
window.geometry('1366x768')
window.minsize(800, 600)
window.resizable(True, True)

# Load background image
bg_image = Image.open(r"C:\\Users\\sarji\\Downloads\\Login (1).png")  # Ensure the path is correct
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas for background
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Resize the background dynamically
window.bind("<Configure>", resize_bg)

# Labels and input fields
label_name = Label(window, text="Username*", font=("Arial", 14,'bold'), bg='white')
label_name.place(relx=0.5, rely=0.3, anchor="nw")
entry_name = Entry(window, font=("Arial", 12))
entry_name.insert(0, "Enter your Username")
entry_name.place(relx=0.5, rely=0.35, anchor="nw", relwidth=0.4)

label_pass = Label(window, text="Password*", font=("Arial", 14,'bold'), bg='white')
label_pass.place(relx=0.5, rely=0.4, anchor="nw")
entry_pass = Entry(window, font=("Arial", 12), show="*")
entry_pass.insert(0, "Enter your Password")
entry_pass.place(relx=0.5, rely=0.45, anchor="nw", relwidth=0.4)

# Show Password Checkbutton
show_password_var = BooleanVar()
show_password_checkbox = Checkbutton(window, text="Show Password", variable=show_password_var, command=toggle_password, bg='white')
show_password_checkbox.place(relx=0.5, rely=0.5, anchor="nw")

# Submit button
button = Button(window, text="SUBMIT", command=submit, font=("Arial", 16, 'bold'), bg="red", fg='white')
button.place(relx=0.5, rely=0.75, anchor="nw")

window.mainloop()
