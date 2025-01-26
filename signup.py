from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox

window=Tk()
window.geometry('1366x768')

bg_image = Image.open(r"D:\Project\class project\Login (2).png")  
bg_image = bg_image.resize((1366, 768))  
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl=Label(window, text='Sign up', font=('Arial', 30,'bold'),fg='red',bg='white').place(x=750,y=90)
slogan=Label(window, text='Enter your details to sign up', font=('Arial', 14),fg='black',bg='white').place(x=750,y=140)

def submit():
    full_name = entry_name.get()
    dob = entry_dob.get()
    phone = entry_phone.get()
    country = country_combobox.get()

    if not full_name or not dob or not phone or not country:
        messagebox.showerror("Please input all the details.")
    else:
        messagebox.showinfo("Success,  form submited")

button = Button(window, text="SUBMIT",command=submit,font=("Arial", 16, 'bold'), bg="red", fg='white').place(x=1050, y=650)

label_name = Label(window, text="Full name*", font=("Arial", 14),bg='white').place(x=850, y=250)
entry_name = Entry(window, font=("Arial", 12)).place(x=850, y=280)

label_dob = Label(window, text="Date of birth (DD/MM/YYYY)*", font=("Arial", 14),bg='white').place(x=850, y=330)
entry_dob = Entry(window, font=("Arial", 12)).place(x=850, y=360)

label_phone = Label(window, text="Phone Number*", font=("Arial", 14),bg='white').place(x=850, y=410)
entry_phone = Entry(window, font=("Arial", 12)).place(x=850, y=440)

label_country = Label(window, text="Country*", font=("Arial", 14),bg='white').place(x=850, y=490)
countries = ["Nepal","United States", "United Kingdom", "India", "Australia", "Germany", "France", "China", "Japan"]
country_combobox = Combobox(window, values=countries, state="readonly", font=("Arial", 12)).place(x=850, y=520)

window.mainloop()


