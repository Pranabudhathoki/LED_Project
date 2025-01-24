

from tkinter import *
from PIL import Image, ImageTk


window = Tk()
window.geometry("1366x768")
window.title("Hotel Sunset")
window.resizable(True, True)

bg_image = Image.open(r"C:\Users\ASUS\Downloads\Login (1).png")  
bg_image = bg_image.resize((1366, 768))  
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

slogan = Label( window,
    text='"Where comfort meets elegance, and every stay feels like home."',
    font=("Arial", 22)
)

slogan.place(x=200, y=400)

def login():
    login_window = Toplevel()
    login_window.geometry("400x300")
    login_window.title("Login")
    Label(login_window, text="Welcome to the Login Page", font=("Arial", 16)).pack(pady=20)
    login_window.mainloop()

login_button = Button(
    window,
    text="Login",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="black",
    command=login,
    width=10,
    height=1,
    relief="solid",
    borderwidth=2
)
login_button.place(x=1200, y=50)  

window.mainloop()


