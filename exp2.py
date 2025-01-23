import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
import re
from datetime import datetime

class HotelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Sunset Hotel Management System")
        self.geometry("1200x800")
        self.configure(bg='#F8F9FA')
        
        self.colors = {
            'primary': '#D4AF37',
            'secondary': '#1E3D59',
            'bg': '#F8F9FA',
            'text': '#333333',
            'white': '#FFFFFF'
        }
        
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.configure_styles()
        
        self.main_container = ttk.Frame(self, style='Main.TFrame')
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        self.nav_history = []
        self.current_user = None
        
        self.create_header()
        self.show_home_page()

    def configure_styles(self):
        self.style.configure('TFrame', background=self.colors['bg'])
        self.style.configure('Main.TFrame', background=self.colors['bg'])
        self.style.configure('TLabel', background=self.colors['bg'], foreground=self.colors['text'])
        self.style.configure('Header.TFrame', background=self.colors['white'])
        self.style.configure('Header.TLabel', background=self.colors['white'], foreground=self.colors['secondary'], font=('Helvetica', 24, 'bold'))
        self.style.configure('Title.TLabel', font=('Helvetica', 32, 'bold'), foreground=self.colors['secondary'], background=self.colors['bg'])
        self.style.configure('Custom.TButton', font=('Helvetica', 12), background=self.colors['primary'], foreground=self.colors['white'])
        self.style.map('Custom.TButton', background=[('active', self.colors['secondary'])])

    def create_header(self):
        self.header = ttk.Frame(self, style='Header.TFrame')
        self.header.pack(fill=tk.X)
        
        logo = ttk.Label(self.header, text="SUNSET", style='Header.TLabel')
        logo.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.nav_frame = ttk.Frame(self.header, style='Header.TFrame')
        self.nav_frame.pack(side=tk.RIGHT, padx=20)
        
        self.update_navigation()

    def update_navigation(self):
        for widget in self.nav_frame.winfo_children():
            widget.destroy()
        
        nav_items = [
            ("Home", self.show_home_page),
            ("Rooms", self.show_rooms_page),
            ("Book", self.show_booking_page),
        ]
        
        if self.current_user:
            nav_items.append(("Logout", self.logout))
        else:
            nav_items.append(("Login", self.show_login_page))
        
        for text, command in nav_items:
            btn = ttk.Button(self.nav_frame, text=text, command=command, style='Custom.TButton')
            btn.pack(side=tk.LEFT, padx=5)

    def show_home_page(self):
        self.clear_page()
        
        content = ttk.Frame(self.main_container)
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        hero = ttk.Frame(content)
        hero.pack(fill=tk.X, pady=50)
        
        hero_title = ttk.Label(hero, text="SUNSET HOTEL", font=('Helvetica', 48, 'bold'), foreground=self.colors['secondary'])
        hero_title.pack()
        
        hero_subtitle = ttk.Label(hero, text="Where comfort meets elegance", font=('Helvetica', 24))
        hero_subtitle.pack(pady=10)
        
        btn_frame = ttk.Frame(content)
        btn_frame.pack(pady=30)
        
        book_btn = ttk.Button(btn_frame, text="Book Now", style='Custom.TButton', command=self.show_booking_page)
        book_btn.pack(side=tk.LEFT, padx=10)
        
        explore_btn = ttk.Button(btn_frame, text="Explore Rooms", style='Custom.TButton', command=self.show_rooms_page)
        explore_btn.pack(side=tk.LEFT, padx=10)
        
        features = ttk.Frame(content)
        features.pack(fill=tk.X, pady=50)
        
        features_title = ttk.Label(features, text="Our Features", style='Title.TLabel')
        features_title.pack(pady=20)
        
        feature_items = ttk.Frame(features)
        feature_items.pack()
        
        self.create_feature(feature_items, "Luxury Rooms", "Experience ultimate comfort")
        self.create_feature(feature_items, "Fine Dining", "World-class cuisine")
        self.create_feature(feature_items, "Spa & Wellness", "Rejuvenate your senses")

    def show_login_page(self):
        self.clear_page()
        
        container = ttk.Frame(self.main_container)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        logo = ttk.Label(container, text="SUNSET", font=('Helvetica', 36, 'bold'), foreground=self.colors['secondary'])
        logo.pack(pady=20)
        
        welcome = ttk.Label(container, text="Welcome Back", font=('Helvetica', 24))
        welcome.pack(pady=10)
        
        form = ttk.Frame(container)
        form.pack(pady=20)
        
        ttk.Label(form, text="Username", font=('Helvetica', 12)).pack(anchor="w")
        username_entry = ttk.Entry(form, width=40)
        username_entry.pack(pady=5)
        
        ttk.Label(form, text="Password", font=('Helvetica', 12)).pack(anchor="w")
        password_entry = ttk.Entry(form, width=40, show="•")
        password_entry.pack(pady=5)
        
        login_btn = ttk.Button(form, text="Login", style='Custom.TButton', command=lambda: self.handle_login(username_entry.get(), password_entry.get()))
        login_btn.pack(pady=20)
        
        links = ttk.Frame(form)
        links.pack()
        
        signup_link = ttk.Label(links, text="Create Account", font=('Helvetica', 10), foreground="blue", cursor="hand2")
        signup_link.pack(side=tk.LEFT, padx=10)
        signup_link.bind("<Button-1>", lambda e: self.show_signup_page())
        
        forgot_link = ttk.Label(links, text="Forgot Password?", font=('Helvetica', 10), foreground="blue", cursor="hand2")
        forgot_link.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(container, text="Back to Home", command=self.show_home_page)
        back_btn.pack(pady=20)

    def show_booking_page(self):
        self.clear_page()
        
        content = ttk.Frame(self.main_container)
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        title = ttk.Label(content, text="Book Your Stay", style='Title.TLabel')
        title.pack(pady=20)
        
        form = ttk.Frame(content, style='TFrame')
        form.pack(fill=tk.X)
        
        dates_frame = ttk.Frame(form)
        dates_frame.pack(fill=tk.X, pady=10)
        
        checkin_frame = ttk.Frame(dates_frame)
        checkin_frame.pack(side=tk.LEFT, padx=10)
        
        ttk.Label(checkin_frame, text="Check-in Date", font=('Helvetica', 12)).pack(anchor="w")
        self.checkin_cal = Calendar(checkin_frame, selectmode='day')
        self.checkin_cal.pack()
        
        checkout_frame = ttk.Frame(dates_frame)
        checkout_frame.pack(side=tk.LEFT, padx=10)
        
        ttk.Label(checkout_frame, text="Check-out Date", font=('Helvetica', 12)).pack(anchor="w")
        self.checkout_cal = Calendar(checkout_frame, selectmode='day')
        self.checkout_cal.pack()
        
        details_frame = ttk.Frame(form)
        details_frame.pack(fill=tk.X, pady=20)
        
        ttk.Label(details_frame, text="Number of Guests", font=('Helvetica', 12)).pack(anchor="w")
        
        guests_frame = ttk.Frame(details_frame)
        guests_frame.pack(fill=tk.X)
        
        self.adults_var = tk.StringVar(value="2")
        self.children_var = tk.StringVar(value="0")
        
        ttk.Spinbox(guests_frame, from_=1, to=4, width=10, textvariable=self.adults_var).pack(side=tk.LEFT, padx=5)
        ttk.Label(guests_frame, text="Adults").pack(side=tk.LEFT, padx=5)
        
        ttk.Spinbox(guests_frame, from_=0, to=4, width=10, textvariable=self.children_var).pack(side=tk.LEFT, padx=5)
        ttk.Label(guests_frame, text="Children").pack(side=tk.LEFT, padx=5)
        
        ttk.Label(details_frame, text="Room Type", font=('Helvetica', 12)).pack(anchor="w", pady=(20,5))
        
        self.room_var = tk.StringVar(value="Deluxe")
        room_types = ["Standard", "Deluxe", "Suite", "Presidential Suite"]
        
        for room in room_types:
            ttk.Radiobutton(details_frame, text=room, value=room, variable=self.room_var).pack(anchor="w")
        
        submit_btn = ttk.Button(form, text="Proceed to Payment", style='Custom.TButton', command=self.handle_booking)
        submit_btn.pack(pady=20)

    def show_rooms_page(self):
        self.clear_page()
        
        content = ttk.Frame(self.main_container)
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        title = ttk.Label(content, text="Our Rooms", style='Title.TLabel')
        title.pack(pady=20)
        
        rooms_frame = ttk.Frame(content)
        rooms_frame.pack(fill=tk.X)
        
        self.create_room_card(rooms_frame, "Standard Room", "Perfect for solo travelers or couples", "From $99/night")
        self.create_room_card(rooms_frame, "Deluxe Room", "Spacious room with city view", "From $149/night")
        self.create_room_card(rooms_frame, "Suite", "Luxury suite with separate living area", "From $249/night")
        self.create_room_card(rooms_frame, "Presidential Suite", "Ultimate luxury with panoramic views", "From $499/night")

    def create_feature(self, parent, title, description):
        feature = ttk.Frame(parent, style='TFrame')
        feature.pack(side=tk.LEFT, padx=10)
        
        ttk.Label(feature, text=title, font=('Helvetica', 16, 'bold'), foreground=self.colors['secondary']).pack()
        ttk.Label(feature, text=description).pack()

    def create_room_card(self, parent, title, description, price):
        card = ttk.Frame(parent, style='TFrame')
        card.pack(fill=tk.X, pady=10)
        
        ttk.Label(card, text=title, font=('Helvetica', 18, 'bold'), foreground=self.colors['secondary']).pack(anchor="w")
        ttk.Label(card, text=description).pack(anchor="w", pady=5)
        ttk.Label(card, text=price, font=('Helvetica', 14, 'bold'), foreground=self.colors['primary']).pack(anchor="w")
        
        book_btn = ttk.Button(card, text="Book Now", style='Custom.TButton', command=self.show_booking_page)
        book_btn.pack(anchor="e")

    def clear_page(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def handle_login(self, username, password):
        # This is a mock login. In a real application, you would verify against a database.
        if username == "admin" and password == "password":
            self.current_user = username
            self.update_navigation()
            self.show_home_page()
            messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def logout(self):
        self.current_user = None
        self.update_navigation()
        self.show_home_page()
        messagebox.showinfo("Logout", "You have been logged out successfully")

    def handle_booking(self):
        if not self.current_user:
            messagebox.showwarning("Login Required", "Please login to make a booking")
            self.show_login_page()
            return
        
        checkin = self.checkin_cal.get_date()
        checkout = self.checkout_cal.get_date()
        adults = self.adults_var.get()
        children = self.children_var.get()
        room_type = self.room_var.get()
        
        booking_details = f"""
        Booking Details:
        Check-in: {checkin}
        Check-out: {checkout}
        Adults: {adults}
        Children: {children}
        Room Type: {room_type}
        """
        
        messagebox.showinfo("Booking Confirmation", booking_details)

if __name__ == "__main__":
    app = HotelApp()
    app.mainloop()